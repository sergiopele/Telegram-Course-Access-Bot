🚀 Telegram Course Access Bot

Automated Telegram bot for verifying online course buyers and granting private community access.

⸻

📚 Project Summary

This Telegram bot automates access control for private communities based on course purchases.

Key Features
	•	Email verification via live Google Sheets lookup
	•	Secure Google API integration (read/write)
	•	Admin notifications on successful verifications
	•	Action logging for tracking
	•	Configurable environment (invite link, support contact, multiple/single access per email)
	•	Verification attempt limit to prevent abuse (ENV-configurable)

Technology Stack
	•	Python
	•	Telegram Bot API
	•	Google Sheets API
	•	Docker (for deployment)
	•	Railway (cloud hosting)

Security Best Practices
	•	Sensitive credentials are excluded from version control
	•	Credentials are passed securely using Base64-encoded environment variables
	•	Service Accounts follow least-privilege principle

Deployment
	•	Fully dockerized and deployable to Railway.app with zero config drift
	•	Base64 strategy enables deployment even on Railway free tier (no file uploads required)

⸻

📄 Documentation
	•	User Guide
	•	Maintenance Guide
	•	Deployment Guide
	•	Google Cloud Setup Guide
	•	Telegram Bot Creation Guide

⸻

📬 Support

For questions or assistance, please contact sergiypelework@gmail.com.