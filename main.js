var AWS = require('aws-sdk');
AWS.config.region = 'us-east-1';
var kinesis = new AWS.Kinesis;
var content = "asdfasdf";
var recordData = [];
var record = {
    Data: JSON.stringify({
        content: content,
        time: new Date()
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


