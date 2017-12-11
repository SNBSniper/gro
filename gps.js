var file = '/dev/ttyAMA0';

var GPS = require('gps');
var SerialPort = require('serialport');
var AWS = require('aws-sdk');
AWS.config.region = 'us-east-1';
var kinesis = new AWS.Kinesis;
var recordData = [];
// var request = require('request');


// // var port = 8088;
// // var url = "http://localhost:"+port;
function PostToServer(data){
    console.log(data);
    var recordData = [];
    var record = {
        Data: JSON.stringify({
            content: content,
            time: new Date(),
            carId: data.GPS.carId
        }),
        PartitionKey: 'partition-' + AWS.config.credentials.identityId
      };
    recordData.push(record); 

    kinesis.putRecords({
        Records: recordData,
        StreamName: 'FiretruckStatusData'
    }, function(err, data) {
        if (err) {
            console.error(err);
        }
    });
}


var port = new SerialPort.SerialPort(file, {
    baudrate: 9600,
    parser: SerialPort.parsers.readline('\r\n')

});

var gps = new GPS;

gps.on('data', function(data) {
    
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
      gps.update(data);
});



