import httplib2
import os
from apiclient import discovery
import oauth2client
from oauth2client import client
from oauth2client import tools
global http 
try:
	import argparse
	flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
except ImportError:
	flags = None
value = 1 
# If modifying these scopes, delete your previously saved credentials
# at ~/.credentials/sheets.googleapis.com-python-quickstart.json
SCOPES = 'https://www.googleapis.com/auth/spreadsheets'
CLIENT_SECRET_FILE = 'client_secret.json'
APPLICATION_NAME = 'Google Sheets API Python Quickstart'
spreadsheetId = '1VeFwfXykn7ifa-i8ewEojLRDiZkREXNaLRRZMV2huEE'
rangeName = 'A1:F'

 
def get_credentials():
	"""Gets valid user credentials from storage.
 
	If nothing has been stored, or if the stored credentials are invalid,
	the OAuth2 flow is completed to obtain the new credentials.
 
	Returns:
    	Credentials, the obtained credential.
	"""
	home_dir = os.path.expanduser('~')
	credential_dir = os.path.join(home_dir, '.credentials')
	if not os.path.exists(credential_dir):
            
            os.makedirs(credential_dir)
        credential_path = os.path.join(credential_dir,'mail_to_g_app.json')
 
        store = oauth2client.file.Storage(credential_path)
        credentials = store.get()
	if credentials:
            
            flow = client.flow_from_clientsecrets(CLIENT_SECRET_FILE, SCOPES)
            flow.user_agent = APPLICATION_NAME
            if flags:
                credentials = tools.run_flow(flow, store, flags)
            else: # Needed only for compatibility with Python 2.6
                credentials = tools.run(flow, store)
            print('Storing credentials to ' + credential_path)
        return credentials

credentials = get_credentials()
http = credentials.authorize(httplib2.Http())
 

def update_authenticate(spreadsheetId, rangeName, values):
   
    credentials = get_credentials()
    http = credentials.authorize(httplib2.Http())
    discoveryUrl = ('https://sheets.googleapis.com/$discovery/rest?'
                	'version=v4')
    service = discovery.build('sheets', 'v4', http=http,discoveryServiceUrl=discoveryUrl)
 
    result = service.spreadsheets().values().update(
    spreadsheetId=spreadsheetId, range=rangeName,
    valueInputOption='RAW',
    body=values).execute()
 
def authenticate():
    credentials = get_credentials()
    global http 
    http = credentials.authorize(httplib2.Http())

def update_sheet(spreadsheetId, rangeName, values):
    discoveryUrl = ('https://sheets.googleapis.com/$discovery/rest?'
                	'version=v4')
    service = discovery.build('sheets', 'v4', http=http,
                              discoveryServiceUrl=discoveryUrl)
    result = service.spreadsheets().values().update(spreadsheetId=spreadsheetId, range=rangeName,valueInputOption='RAW',body=values).execute()
