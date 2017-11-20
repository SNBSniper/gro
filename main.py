from urllib.parse import urlencode
from urllib.request import Request, urlopen
import threading
import gsm
import rfid
import odb2




def worker(num):
	if(num == 1): #GSM
		print("GSM MODULE")
		gsm.getGsmData()
	if(num == 2): #RFID
		print("RFID MODULE")
		rfid.getRfidData()
	if(num == 3): #ODB2
		print("ODB2 MODULE")
		odb2.getOdb2Data()

	

url = 'https://httpbin.org/post' # Set destination URL here
post_fields = {'foo': 'bar'}     # Set POST fields here


url_rfid = "http://rfid.com"
url_gsm = "http://gsm.co"
url_odb2 = "http://odb2.com"

def sendRFIDDataToServer(data):
	request = Request(url_rfid, urlencode(data).encode())
	json = urlopen(request).read().decode()
	print(json)	

def sendGSMDataToServer(data):
	request = Request(url_gsm, urlencode(data).encode())
	json = urlopen(request).read().decode()
	print(json)	

def sendODB2DataToServer(data):
	request = Request(url_odb2b, urlencode(data).encode())
	json = urlopen(request).read().decode()
	print(json)	




threads = []
for i in range(4):
    t = threading.Thread(target=worker, args=(i,))
    threads.append(t)
    t.start()



