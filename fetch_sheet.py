import gspread
import pandas as pd
from oauth2client.service_account import ServiceAccountCredentials

# Setup credentials
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json", scope)
client = gspread.authorize(creds)

# Open the Google Sheet
sheet = client.open("Your Sheet Name").worksheet("Sheet1")  # Adjust the name if needed

# Convert to DataFrame
data = sheet.get_all_records()
df = pd.DataFrame(data)

# Save to CSV
df.to_csv("synced_sheet_data.csv", index=False)
print("✅ Synced Google Sheet to CSV")

