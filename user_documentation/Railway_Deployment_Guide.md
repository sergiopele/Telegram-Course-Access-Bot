🚀 Railway Deployment Guide - Course Access Bot

1. Project Preparation
	•       Push your code to a private GitHub repository.
	•       Do not include google_credentials.json in your repo — it should never be committed.
	•       Remove or comment out any load_dotenv() calls in main.py if present (not needed in Railway).
	•       Ensure .gitignore includes .env, google_credentials.json, and bot_actions.log.

⸻

2. Environment Variables

        Set these inside Railway → Variables:

| Key                                   | Example Value         |
|:--------------------------------------|:----------------------|
| BOT_TOKEN                             | Telegram bot token    |
| SUPPORT_EMAIL                         | support@example.com   |
| PRIVATE_GROUP_INVITE_LINK             | Telegram invite link  |
| GOOGLE_SHEET_NAME                     | Telegram_Bot_Sheet    |
| ADMIN_TELEGRAM_ID                     | 1234567890            |
| ALLOW_MULTIPLE_USERS_PER_EMAIL        | true / false          |
| GOOGLE_CREDENTIALS_B64                |(Base64 string of your .json) |
| MAX_VERIFICATION_ATTEMPTS             | number (set 2-3)      |


3. Google Credentials Setup
	•       Convert google_credentials.json into a Base64 string.
	•       Paste the Base64 string into a new environment variable called GOOGLE_CREDENTIALS_B64.
	•       This allows the bot to authenticate with Google Sheets without uploading any files.

✅ This replaces the old “Upload File” or volume mounting step (not needed anymore).

4. Deploy the Bot
	•	Connect your Railway project to the GitHub repo.
	•	Railway will automatically build and deploy using the Dockerfile.
	•	If deploying manually, use the Railway CLI or drag-and-drop ZIP upload.

✅ Bot will start automatically once build completes.

⸻

5. Logs and Verification
	•	Use the Railway Logs tab to monitor startup.
	•	You should see messages like:

✅ Google Sheet connection successful: 'Telegram_Bot'
🟢 Starting Course Access Bot...

