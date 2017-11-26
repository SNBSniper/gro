# from urllib.parse import urlencode
# from urllib.request import Request, urlopen
import threading
import json
import requests
import gsm
import rfid
import obd2
import obd


domain ="http://localhost"
port = "8083"

url = domain+":"+port # Set destination URL here
post_fields = {'foo': 'bar'}     # Set POST fields here


url_rfid = url
url_gsm = url
url_odb2 = url


def worker(num):
	if(num == 1): #GSM
		print("GSM MODULE")
		data = gsm.getGsmData()
		key =  "GSM"
		postToServer(data, url_gsm, key)
		
	if(num == 2): #RFID
		print("RFID MODULE")
		data = rfid.getRfidData()
		key = "RFID"
		postToServer(data, url_rfid, key)
	if(num == 3): #ODB2
		print("ODB2 MODULE")
		data = odb2.getOdb2Data()
		postToServer(data, url_odb2)
	



def postToServer(data, url, key):
	data_json = json.dumps(data)
	payload = data
	r = requests.post(url, json={key: payload})




threads = []
for i in range(4):
    t = threading.Thread(target=worker, args=(i,))
    threads.append(t)
    t.start()


# threads = []
# t =threading.Thread(target=worker, args=(1,))
# threads.append(t)
# t.start()