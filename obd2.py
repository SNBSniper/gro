import obd

def getObd2Data():
    print("ODB2 Data")
    connection = obd.OBD() # auto-connects to USB or RF port
    if(not connection.is_connected()):
        print("ODB2 not Connected, please make the connetion")
        return None
    cmd = obd.commands.SPEED # select an OBD command (sensor)
    response = connection.query(cmd) # send the command, and parse the response
    print(response.value) # returns unit-bearing values thanks to Pint
    print(response.value.to("mph")) # user-friendly unit conversions
getObd2Data()
