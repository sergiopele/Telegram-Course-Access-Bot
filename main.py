import os
import json
import base64
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import (
    ApplicationBuilder, CommandHandler, MessageHandler,
    ConversationHandler, ContextTypes, filters
)
from datetime import datetime

# --- Load environment variables ---
BOT_TOKEN = os.getenv("BOT_TOKEN")
SUPPORT_EMAIL = os.getenv("SUPPORT_EMAIL", "support@example.com")
PRIVATE_GROUP_INVITE_LINK = os.getenv("PRIVATE_GROUP_INVITE_LINK", "https://t.me/exampleinvite")
GOOGLE_SHEET_NAME = os.getenv("GOOGLE_SHEET_NAME", "Telegram_Bot")
ADMIN_TELEGRAM_ID = int(os.getenv("ADMIN_TELEGRAM_ID", "0"))
ALLOW_MULTIPLE_USERS_PER_EMAIL = os.getenv("ALLOW_MULTIPLE_USERS_PER_EMAIL", "false").lower() == "true"
MAX_VERIFICATION_ATTEMPTS = int(os.getenv("MAX_VERIFICATION_ATTEMPTS", "3"))

if not BOT_TOKEN:
    raise RuntimeError("❌ BOT_TOKEN is missing!")
if not GOOGLE_SHEET_NAME:
    raise RuntimeError("❌ GOOGLE_SHEET_NAME is missing!")

# --- Google Sheets Setup ---
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
credentials_b64 = os.getenv("GOOGLE_CREDENTIALS_B64")
if not credentials_b64:
    raise RuntimeError("❌ GOOGLE_CREDENTIALS_B64 is missing!")
credentials_json = base64.b64decode(credentials_b64).decode("utf-8")
credentials_dict = json.loads(credentials_json)
creds = ServiceAccountCredentials.from_json_keyfile_dict(credentials_dict, scope)
client = gspread.authorize(creds)

# --- Logging ---
LOG_FILE = "bot_actions.log"
def log_action(action: str):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = f"[{timestamp}] {action}"
    print(log_entry)
    with open(LOG_FILE, "a") as log:
        log.write(log_entry + "\n")

# --- Health Check ---
def check_google_sheet_connection(sheet_name: str):
    try:
        sheet = client.open(sheet_name).sheet1
        sample_emails = sheet.col_values(1)[:5]
        print(f"✅ Google Sheet connection successful: '{sheet_name}'")
        if sample_emails:
            print("Sample emails loaded:", sample_emails)
        else:
            print("⚠️ Sheet is empty or no emails found yet.")
    except Exception as e:
        print(f"❌ Google Sheet connection failed: {e}")
        raise RuntimeError("Google Sheet connection test failed. Check credentials and sharing permissions.")

check_google_sheet_connection(GOOGLE_SHEET_NAME)

# --- Bot States and UI ---
CHOOSING, VERIFY_EMAIL = range(2)
MAIN_MENU = ReplyKeyboardMarkup(
    [["Verify Course Purchase"]],
    resize_keyboard=True
)

# --- Handlers ---
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data["attempts"] = 0
    await update.message.reply_text(
        "Welcome to the Course Access Bot!\n\nPlease select an option below:",
        reply_markup=MAIN_MENU
    )
    return CHOOSING

async def choose_action(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    if text == "Verify Course Purchase":
        await update.message.reply_text("Please enter the email address you used to purchase the course:")
        return VERIFY_EMAIL
    else:
        await update.message.reply_text("Please use the menu to select a valid action.", reply_markup=MAIN_MENU)
    return CHOOSING

async def verify_email(update: Update, context: ContextTypes.DEFAULT_TYPE):
    attempts = context.user_data.get("attempts", 0)
    if attempts >= MAX_VERIFICATION_ATTEMPTS:
        await update.message.reply_text(
            f"❌ You have exceeded the maximum number of verification attempts.\nPlease contact our support team at {SUPPORT_EMAIL}."
        )
        log_action(f"User {update.effective_user.id} exceeded max attempts.")
        return CHOOSING

    context.user_data["attempts"] = attempts + 1
    email_input = update.message.text.strip().lower()
    user = update.effective_user
    sheet = client.open(GOOGLE_SHEET_NAME).sheet1
    raw_emails = sheet.col_values(1)
    emails = [email.lower() for email in raw_emails]

    try:
        if email_input in emails:
            email_row = emails.index(email_input) + 1
            existing_telegram_ids = sheet.cell(email_row, 2).value

            if existing_telegram_ids:
                if not ALLOW_MULTIPLE_USERS_PER_EMAIL:
                    await update.message.reply_text(
                        f"❌ This email has already been used to verify access.\nIf you believe this is a mistake, contact {SUPPORT_EMAIL}."
                    )
                    log_action(f"FAILED verification - reused email: {email_input} by {user.id}")
                    return CHOOSING
                updated_ids = f"{existing_telegram_ids}, {user.id}"
            else:
                updated_ids = str(user.id)

            sheet.update_cell(email_row, 2, updated_ids)
            await update.message.reply_text(
                f"✅ Verification successful!\n\nJoin here: {PRIVATE_GROUP_INVITE_LINK}"
            )
            log_action(f"SUCCESS - email {email_input} linked to {user.id}")

            if ADMIN_TELEGRAM_ID:
                admin_msg = f"✅ Access granted:\n@{user.username or 'No username'}\nID: {user.id}\nEmail: {email_input}"
                try:
                    await context.bot.send_message(chat_id=ADMIN_TELEGRAM_ID, text=admin_msg)
                except Exception as e:
                    log_action(f"WARNING - Admin notify failed: {e}")
        else:
            await update.message.reply_text(
                f"❌ Email not found.\nIf this is an error, contact {SUPPORT_EMAIL}."
            )
            log_action(f"FAILED - unknown email: {email_input} by {user.id}")

    except Exception as e:
        log_action(f"ERROR - verification exception: {e}")
        await update.message.reply_text("❌ An internal error occurred. Please try again later.")

    await update.message.reply_text("Would you like to verify another email?", reply_markup=MAIN_MENU)
    return CHOOSING

async def cancel(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Operation cancelled.", reply_markup=MAIN_MENU)
    return CHOOSING

# --- Bot Startup ---
app = ApplicationBuilder().token(BOT_TOKEN).build()

conv_handler = ConversationHandler(
    entry_points=[CommandHandler("start", start)],
    states={
        CHOOSING: [MessageHandler(filters.TEXT & ~filters.COMMAND, choose_action)],
        VERIFY_EMAIL: [MessageHandler(filters.TEXT & ~filters.COMMAND, verify_email)],
    },
    fallbacks=[CommandHandler("cancel", cancel)],
)

app.add_handler(conv_handler)

if __name__ == "__main__":
    print("🟢 Starting Course Access Bot...")
    app.run_polling()
