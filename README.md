# 🚀 Telegram Course Access Bot

Automated Telegram bot for verifying online course buyers and granting private community access.

---

## 📚 Project Summary

This Telegram bot automates access control for private communities based on course purchases.

### Key Features
- Email verification via live Google Sheets lookup
- Secure Google API integration (read/write)
- Admin notifications on successful verifications
- Action logging for tracking
- Configurable environment (invite link, support contact, multiple/single access per email)

### Technology Stack
- Python
- Telegram Bot API
- Google Sheets API
- Docker (for deployment)
- Railway (cloud hosting)

### Security Best Practices
- Sensitive credentials are excluded from version control.
- Uses secure environment variables.
- Service Accounts have least privilege access.

### Deployment
- Fully dockerized and deployable to Railway.app with zero config drift.

---

## 📄 Documentation
- [User Guide](user_documentation/User_Guide.md)
- [Maintenance Guide](user_documentation/Maintenance_Guide.md)
- [Deployment Guide](user_documentation/Railway_Deployment_Guide.md)
- [Google Cloud Setup Guide](user_documentation/Google_Cloud_Setup_Guide.md)
- [Telegram Bot Creation Guide](user_documentation/Telegram_Bot_Creation_Guide.md)

---

## 📬 Support

For questions or assistance, please contact **sergiypelework@gmail.com**.