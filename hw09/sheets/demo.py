#!/usr/bin/env python3
# From: https://developers.google.com/sheets/api/quickstart/python
# Copyright 2018 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# [START sheets_quickstart]
from __future__ import print_function
from googleapiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools
import time, sys
import smbus

bus = smbus.SMBus(2)
TempSensor = 0x49


# If modifying these scopes, delete the file token.json.
SCOPES = 'https://www.googleapis.com/auth/spreadsheets'

# The ID and range of a sample spreadsheet.
SPREADSHEET_ID = '1uT_70KLhZ-EFuhLCsox-osa30AJHEXFiuvTdCfiNJsw'
RANGE_NAME = 'A2'

def main():
    """Shows basic usage of the Sheets API.
    Writes values to a sample spreadsheet.
    """
    store = file.Storage('tokenPython.json')
    creds = store.get()
    if not creds or creds.invalid:
        flow = client.flow_from_clientsecrets('credentials.json', SCOPES)
        creds = tools.run_flow(flow, store)
    service = build('sheets', 'v4', http=creds.authorize(Http()))

    
    
    while(True):
        tempC = bus.read_byte_data(TempSensor,0)
        tempF = tempC*(9/5)+32
    

        # Call the Sheets API
        # Compute a timestamp and pass the first two arguments
        values = [ [(time.time()-3600)/60/60/24+ 25569 - 4/24, tempC, tempF]]
        body = { 'values': values }
        result = service.spreadsheets().values().append(spreadsheetId=SPREADSHEET_ID,
                                range=RANGE_NAME,
                                #  How the input data should be interpreted.
                                valueInputOption='USER_ENTERED',
                                # How the input data should be inserted.
                                # insertDataOption='INSERT_ROWS'
                                body=body
                                ).execute()
    
        updates = result.get('updates', [])
        # print(updates)

        if not updates:
            print('Not updated')
        time.sleep(5)

if __name__ == '__main__':
    main()
# [END sheets_quickstart]
