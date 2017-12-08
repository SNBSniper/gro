# from urllib.parse import urlencode
# from urllib.request import Request, urlopen
import threading
import json
import requests
import rfid
import obd2
import obd


domain ="http://localhost"
port = "8088"

url = domain+":"+port # Set destination URL here
post_fields = {'foo': 'bar'}     # Set POST fields here


url_rfid = url
url_obd2 = url

def postToServer(data, url, key):
    data_json = json.dumps(data) 
    payload = data 
    r = requests.post(url, json={key: payload}) 

def worker(num):
    print(num)
    if(num == 0): #RFID
        print("RFID MODULE")
        data = rfid.getRfidData()
        key = "RFID"
        postToServer(data, url_rfid, key)
    if(num == 1): #ODB2
        print("ODB2 MODULE")
        data = obd2.getObd2Data()
        key="OBD2"  
        postToServer(data, url_obd2,key) 
        print("END")


threads = []
for i in range(3):
    t = threading.Thread(target=worker, args=(i,))
    threads.append(t)
    t.start()


# threads = []
# t =threading.Thread(target=worker, args=(1,))
# threads.append(t)
# t.start()
