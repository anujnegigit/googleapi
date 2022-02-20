import gspread
from oauth2client.service_account import ServiceAccountCredentials

emails = ["themillibit@gmail.com", "hello@gmail.com", "testing@gmail.com"]
names = ["the Millibit", "hello", "testing"]

scope=["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("credentials.json", scope)
client = gspread.authorize(creds)

spreadsheet = client.open("try")
worksheet = spreadsheet.add_worksheet("try1", 50, 50)

for i in range (1 , len(emails)):
    worksheet.update_cell(i, 1, names[i])
    worksheet.update_cell(i, 2, emails[i])
#
# #Open by URl, can also open by key
# sheet = client.open_by_url('')
# #open existing spreadsheet
# request_sheet = client.open("try").worksheet("Sheet1")
# #get data from spreadsheet as a list of dicts
# request_data = request_sheet.get_all_records()
# #get data from spreadsheet as a list of dicts
# request_data = request_sheet.get_all_values()
# #getting values from rows or columns:
# values_list = worksheet.row_values(1)
# #Getting values from cells:
# worksheet.acell('B1').value
# #Find rows and columns of a certain value worksheet.find("value")
# # cell.row
