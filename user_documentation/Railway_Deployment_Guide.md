# 🚀 Railway Deployment Guide - Course Access Bot

## 1. Project Preparation
- Push your code to a private GitHub repository (without google_credentials.json).
- Remove or comment out `load_dotenv()` in main.py.

## 2. Environment Variables
Set these inside Railway → Variables:

| Key                                   | Example Value         |
|:--------------------------------------|:----------------------|
| BOT_TOKEN                             | Telegram bot token    |
| SUPPORT_EMAIL                         | support@example.com   |
| PRIVATE_GROUP_INVITE_LINK             | Telegram invite link  |
| GOOGLE_SHEET_NAME                     | Telegram_Bot_Sheet    |
| ADMIN_TELEGRAM_ID                     | 1234567890            |
| ALLOW_MULTIPLE_USERS_PER_EMAIL        | true / false          |

## 3. Upload google_credentials.json
- Use Railway’s file upload (file storage) and place it in `/app/`.

## 4. Deployment
- Connect Railway to your GitHub repo or upload manually.
- Build will auto-run using Dockerfile.
- Railway will start your bot automatically.

## 5. Logs
- View live deployment logs.
- Confirm Google Sheet connection and bot startup.

✅ Now your bot is live!