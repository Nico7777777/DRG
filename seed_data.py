from firebase_admin import credentials, db, firestore
import firebase_admin
import pandas as pd
import json
import math


hospital = {
    "criteriu": "",
    "nume": "",
    "judeţ": "",
    "clasificare": "",
}

if __name__ == "__main__":
    #json.dumps(obj=, skipkeys=True, ensure_ascii=True, indent=4, sort_keys=True)
    spreadsheet = []
    cred = credentials.Certificate(
        'drg-romania-firebase-adminsdk-ohhhf-199aaa17cd.json')
    app = firebase_admin.initialize_app(cred)
    db = firestore.client()

    file_name = 'Clasificarea spitalelor.xlsx'
    data1 = pd.read_excel(file_name, 'Sheet1', usecols=['Col1', 'Col2', 'Col3'])
    data1 = data1[1:]
    
    doc_ref = db.collection(u'Spitale')

    keyword = "Judeţul"
    county = "Alba"
    with open("hospital.json", "w", encoding="iso-8859-1", newline='\n', ) as file:
        file.write("[\n")
        for i in range( data1.__len__() ):
            if( type(data1.iloc[i][0]) == str and  data1.iloc[i][0][:7] == keyword):
                county = data1.iloc[i][0][7:]
                print( "county=" +str(county) )
            if( type(data1.iloc[i][0]) == int and type(data1.iloc[i][1]) == str ):
                print(data1.iloc[i][0], data1.iloc[i][1], data1.iloc[i][2], sep="|")
                hospital["criteriu"] = data1.iloc[i][0]
                hospital["nume"] = data1.iloc[i][1]
                hospital["clasificare"] = data1.iloc[i][2]
                hospital["judeţ"] = county
                json_object = json.dumps(hospital, indent=4)
                file.write( json_object +",\n")
        file.write("\n]")

