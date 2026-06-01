import os
import json
import requests
import gspread
from datetime import datetime
from google.oauth2.service_account import Credentials

# Google auth
service_account_info = json.loads(
    os.environ["GOOGLE_SERVICE_ACCOUNT_JSON"]
)

creds = Credentials.from_service_account_info(
    service_account_info,
    scopes=[
        "https://www.googleapis.com/auth/spreadsheets",
        "https://www.googleapis.com/auth/drive"
    ]
)

gc = gspread.authorize(creds)

sheet = gc.open_by_key(
    os.environ["GOOGLE_SHEET_ID"]
)

worksheet = sheet.worksheet("daily_metrics")

# Clarity API
headers = {
    "Authorization": f"Bearer {os.environ['CLARITY_API_TOKEN']}",
    "Content-Type": "application/json"
}

url = (
    "https://www.clarity.ms/export-data/api/v1/"
    "project-live-insights"
)

params = {
    "numOfDays": "1",
    "dimension1": "Device"
}

response = requests.get(
    url,
    headers=headers,
    params=params
)

data = response.json()

traffic = next(
    x for x in data
    if x["metricName"] == "Traffic"
)

mobile = 0
desktop = 0
tablet = 0
total = 0

for row in traffic["information"]:
    device = row.get("Device")
    sessions = int(row.get("totalSessionCount", 0))

    total += sessions

    if device == "Mobile":
        mobile = sessions
    elif device == "PC":
        desktop = sessions
    elif device == "Tablet":
        tablet = sessions

worksheet.append_row([
    datetime.utcnow().strftime("%Y-%m-%d"),
    total,
    mobile,
    desktop,
    tablet
])

print("Clarity data written successfully")
