from firebase_admin import credentials
from firebase_admin import db
import firebase_admin
import pandas as pd
import json
import math

'''
config = {
    "apiKey": "AIzaSyAWlR3t3ke31sOJhHwqg4q60aSyGw_nJaw",
    "authDomain": "drg-romania.firebaseapp.com",
    "projectId": "drg-romania",
    "storageBucket": "drg-romania.appspot.com",
    "messagingSenderId": "442484137135",
    "serviceAccount": "serviceAccount.json"
}
firebase_storage = pyrebase.initialize_app(config)
storage = firebase_storage.storage()
'''



if __name__ == "__main__":
    '''cred = credentials.Certificate(
        'drg-romania-firebase-adminsdk-ohhhf-7ca20346ae.json')
    firebase_admin.initialize_app(
        cred, 'https://drg-romania-default-rtdb.europe-west1.firebasedatabase.app/')'''
    file_name = 'Clasificarea spitalelor.xlsx'
    data1 = pd.read_excel('Clasificarea spitalelor.xlsx', 'Sheet1', usecols=['Col1', 'Col2', 'Col3'])
    data1 = data1[1:]
    
    for i in range( data1.__len__() ):
        if( type(data1.iloc[i][0]) == int and type(data1.iloc[i][1]) == str ):
            print(data1.iloc[i][0], data1.iloc[i][1], data1.iloc[i][2], sep="  |  ", end="\n")
            a = input()