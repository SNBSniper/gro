import threading
import json
import rfid
import obd
import boto3

stream_name="FiretruckStatusData"

def sendToKinesis(data):
    client = boto3.client('kinesis',region_name="us-east-1")
    client.put_record(StreamName=stream_name, Data=json.dumps(data), PartitionKey="partitionKey")
    #connection = kinesis.connect_to_region("us-east-1")
    #lists_streams = kinesis.describe_stream("FiretruckStatusData")
    #print(lists_streams)
    #kinesis.put_record("FiretruckStatusData", json.dumps(data), "partitionkey")

def worker(num):
    print(num)
    #if(num == 0): #RFID
    #    print("RFID MODULE")
    #    data = rfid.getRfidData()
    #    sendToKinesis(data)
    if(num == 1): #ODB2

        print("ODB2 MODULE")
        import obd2
        data = obd2.getObd2Data()

        obd2 = {"mph": 82,
        "RPM": 23000,
        "SPEED": 329,
        "THROTTLE_POS": -10
        }

        data = {"OBD2": obd2}
        sendToKinesis(data)
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


