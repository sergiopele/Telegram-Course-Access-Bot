# ☁️ Google Cloud Setup Guide - Course Access Bot

## 1. Create a Project
- Go to [Google Cloud Console](https://console.cloud.google.com/).
- Create a new project (e.g., "Telegram Access Bot").

## 2. Enable APIs
- Enable:
  - Google Sheets API
  - Google Drive API

## 3. Create a Service Account
- Go to IAM & Admin → Service Accounts → Create Service Account.
- Grant access → Basic → Editor (for Sheet editing).

## 4. Create and Download Key
- Create JSON key.
- Download and save as `google_credentials.json`.

## 5. Share Google Sheet
- Open your Google Sheet.
- Share it with your Service Account email.
- Grant "Editor" permissions.

---

# 🗂️ Sheet Structure Requirements (Very Important)

Your Google Sheet must be structured exactly like this:

| Column A (Emails)     | Column B (Telegram User IDs) |
|:----------------------|:-----------------------------|
| customer1@gmail.com   | (Leave empty)                |
| customer2@example.com | (Leave empty)                |
| ...                   | ...                          |

## Rules:
- Column A must contain **one email per row**.
- Column B must be **initially empty**.  
  ➔ The bot will automatically fill it after users verify.
- No header row is required.  
  ➔ Start entering data from **Row 1** directly.
- Do **not insert extra columns**.
- Do **not change order** of columns.

## Example:

| A                 | B |
|-------------------|---|
| jack@gmail.com    |   |
| andrew@gmail.com  |   |
| emily@yahoo.com   |   |

✅ Emails entered manually or imported automatically.

✅ Telegram User IDs are written by the bot automatically after successful verification.

---

# 📢 Important
- Keep the Sheet **simple and clean**.
- Avoid formulas, merged cells, or formatting tricks.
- Always give the Service Account "Editor" access to this sheet.

✅ Now your bot will work correctly without errors!