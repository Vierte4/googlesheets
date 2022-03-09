# Подключаем библиотеки
import httplib2
import apiclient
from oauth2client.service_account import ServiceAccountCredentials
from data.config import spreadsheetId

CREDENTIALS_FILE = 'utils\google_sheets_api\positions-330217-dccec5f7b18a.json'  # Имя файла с закрытым ключом

# Читаем ключи из файла
credentials = ServiceAccountCredentials.from_json_keyfile_name(CREDENTIALS_FILE, [
    'https://www.googleapis.com/auth/spreadsheets', 'https://www.googleapis.com/auth/drive'])

httpAuth = credentials.authorize(httplib2.Http()) # Авторизуемся в системе
service = apiclient.discovery.build('sheets', 'v4', http = httpAuth) # Выбираем работу с таблицами и 4 версию API


driveService = apiclient.discovery.build('drive', 'v3', http = httpAuth) # Выбираем работу с Google Drive и 3 версию API
access = driveService.permissions().create(
    fileId = spreadsheetId,
    body = {'type': 'user', 'role': 'writer', 'emailAddress': 'argut.98@gmail.com'},  # Открываем доступ на редактирование
    fields = 'id'
).execute()

def update_table(data):
    resp = service.spreadsheets().values().append(
        spreadsheetId=spreadsheetId,
        range="Лист номер один!A1:C1",
        valueInputOption="RAW",
        body = {
        'values' : [data, # строка
        ]}).execute()