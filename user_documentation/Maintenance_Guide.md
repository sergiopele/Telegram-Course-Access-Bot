# 🛠 Maintenance Guide - Course Access Bot

## 1. Add New Verified Customers
- Open the linked Google Sheet.
- Insert new customer emails into Column A.
- Leave Column B empty (bot fills it automatically after user verification).

## 2. Google Sheet Permissions
- Ensure the Service Account has "Editor" access, not "Viewer".

## 3. Controlling Access Settings
- `ALLOW_MULTIPLE_USERS_PER_EMAIL=true`: Allow multiple users per email (IDs will be appended).
- `ALLOW_MULTIPLE_USERS_PER_EMAIL=false`: Restrict to one user per email.

## 4. Update Invite Link or Support Email
- Change values in Railway Environment Variables (no redeployment needed).

## 5. Rotate Google Credentials
- In Google Cloud Console:
  - Create new Service Account key.
  - Upload new `google_credentials.json` to Railway.

## 6. Monitoring Activity
- Review deployment logs in Railway.
- All bot interactions are logged in `bot_actions.log` file.

## 7. Important
- Never upload `google_credentials.json` to GitHub or public places.
- Protect Railway account with 2FA.