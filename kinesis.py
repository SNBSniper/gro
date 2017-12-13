from boto import kinesis
import json

obd2 = {"mph": 82,
        "RPM": 23000,
        "SPEED": 329,
        "THROTTLE_POS": -10
        }

data = {"ODB2": obd2}

kinesis = kinesis.connect_to_region("us-east-1")
lists_streams = kinesis.describe_stream("FiretruckStatusData")
print(lists_streams)
kinesis.put_record("FiretruckStatusData", json.dumps(data), "partitionkey")
