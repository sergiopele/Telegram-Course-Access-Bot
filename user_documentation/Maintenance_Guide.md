🛠 Maintenance Guide - Course Access Bot

1. Add New Verified Customers
	•	Open the linked Google Sheet.
	•	Insert new customer emails into Column A (starting from Row 1).
	•	Leave Column B empty — the bot will automatically populate it after a user verifies.

2. Google Sheet Permissions
	•	The linked Google Service Account must have Editor access to the Google Sheet.
	•	Share the Sheet with your Service Account email address.

3. Controlling Access Behavior
	•	ALLOW_MULTIPLE_USERS_PER_EMAIL=true: Allow multiple users per email (Telegram IDs will be comma-separated).
	•	ALLOW_MULTIPLE_USERS_PER_EMAIL=false: Only the first verified Telegram ID will be allowed per email. Others will be rejected.

4. Limit Number of Verification Attempts (Anti-Abuse)
	•	MAX_VERIFICATION_ATTEMPTS=3 (or any number):
Set the maximum number of email verification attempts per user session.
	•	After exceeding this limit, users will receive a message prompting them to contact support.
	•	This prevents overuse of the Google Sheets API and abuse.

5. Update Invite Link, Support Email, or Other Configs
	•	Modify any of the following in Railway > Environment Variables (no code changes needed):
	•	PRIVATE_GROUP_INVITE_LINK
	•	SUPPORT_EMAIL
	•	GOOGLE_SHEET_NAME
	•	ADMIN_TELEGRAM_ID

6. Rotate Google Credentials
	•	In Google Cloud Console:
	•	Create a new Service Account key.
	•	Download the .json key file.
	•	Encode it to Base64 using base64 google_credentials.json (Mac/Linux) or PowerShell.
	•	Paste the string into Railway under the variable: GOOGLE_CREDENTIALS_B64.

7. Monitoring Activity
	•	Bot logs all interactions, including successful and failed verifications, into bot_actions.log.
	•	You can access logs from:
	•	Railway logs panel (live),
	•	Local log file when testing locally.

8. Security Best Practices
	•	Never commit sensitive files (like google_credentials.json) to GitHub.
	•	Use .env or Railway ENV variables to store secrets.
	•	Protect your Railway and Google accounts with 2FA.
	•	Grant least privilege access to your Google Service Account.