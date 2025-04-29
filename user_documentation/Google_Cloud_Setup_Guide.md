☁️ Google Cloud Setup Guide – Course Access Bot

1. Create a Google Cloud Project
	•	Visit Google Cloud Console.
	•	Click Create Project and name it, e.g., Telegram Access Bot.

⸻

2. Enable Required APIs

Go to APIs & Services > Library, then enable:
	•	Google Sheets API
	•	Google Drive API

⸻

3. Create a Service Account
	1.	Navigate to IAM & Admin > Service Accounts.
	2.	Click Create Service Account.
	3.	Name it (e.g., telegram-access-bot).
	4.	Grant the role: Editor.
	5.	Proceed and create the account.

⸻

4. Generate and Secure the Credentials
	1.	After creating the service account, go to the Keys tab.
	2.	Click Add Key > Create New Key → Choose JSON format.
	3.	Download the google_credentials.json file.

Convert to Base64 (for Railway deployment)
	•	Run this command to encode the file:

base64 google_credentials.json


	•	Copy the entire Base64 string.
	•	Paste it into Railway as the value for the variable: GOOGLE_CREDENTIALS_B64.

❄️ This eliminates the need to upload files to Railway — credentials are decoded and used in memory.

⸻

5. Share the Google Sheet
	1.	Open your Google Sheet.
	2.	Click Share.
	3.	Paste your Service Account email (found inside the JSON file).
	4.	Set permission to Editor.
	5.	Click Done.

⸻

📂 Sheet Structure Requirements (Critical)

Column A (Emails)	Column B (Telegram User IDs)
customer1@gmail.com	(Leave empty)
customer2@example.com	(Leave empty)

Rules:
	•	No header row required (start from Row 1).
	•	Column A = course purchase emails (manually added or imported).
	•	Column B = filled by bot after successful verification.
	•	Do not reorder or insert extra columns.
	•	Avoid formulas or formatting in data cells.

Example:

A	B
jack@gmail.com	
andrew@gmail.com	
emily@yahoo.com	



⸻

⚠️ Best Practices
	•	Always keep the Sheet clean: no merged cells, no styling.
	•	Never upload your google_credentials.json to GitHub.
	•	Use .env or Railway Variables to manage secrets.
	•	Protect your Google Cloud account with 2FA.

⸻

✅ Once configured, your bot will authenticate securely and manage access automatically.