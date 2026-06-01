import os
import json
import requests

print("Testing secrets...")

print("CLARITY_API_TOKEN exists:", bool(os.environ.get("CLARITY_API_TOKEN")))
print("GOOGLE_SHEET_ID exists:", bool(os.environ.get("GOOGLE_SHEET_ID")))
print("GOOGLE_SERVICE_ACCOUNT_JSON exists:", bool(os.environ.get("GOOGLE_SERVICE_ACCOUNT_JSON")))

print("Success")
