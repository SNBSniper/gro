var file = '/dev/ttyAMA0';

var GPS = require('gps');
var SerialPort = require('serialport');
var request = require('request');


var port = 8088;
var url = "http://localhost:"+port;
function PostToServer(data){
    request.post(
       url,
       { json: data  },
            function (error, response, body) {
                if (!error && response.statusCode == 200) {
                    console.log(body)
                }
            }

    );
}


var port = new SerialPort.SerialPort(file, {
    baudrate: 9600,
    parser: SerialPort.parsers.readline('\r\n')

});

var gps = new GPS;

gps.on('data', function(data) {
    console.log("GPS:") ;
    if(data.lat !== undefined){
        var data2= {};
        data.carId = "aaabb2dksk2";
        data2.GPS = data;
        if(data) 
            PostToServer(data2);
        else {
            console.log("No data to post");
            process.exit(-1);
        }
    }
});

port.on('data', function(data) {
    console.log("PORT");
      gps.update(data);

});



