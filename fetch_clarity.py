import os
import json
import gspread
from google.oauth2.service_account import Credentials

# Read service account from GitHub secret
service_account_info = json.loads(
    os.environ["GOOGLE_SERVICE_ACCOUNT_JSON"]
)

scopes = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive"
]

creds = Credentials.from_service_account_info(
    service_account_info,
    scopes=scopes
)

gc = gspread.authorize(creds)

sheet = gc.open_by_key(
    os.environ["GOOGLE_SHEET_ID"]
)

worksheet = sheet.worksheet("daily_metrics")

worksheet.append_row([
    "TEST",
    "GitHub Action",
    "Success"
])

print("Row written successfully")
