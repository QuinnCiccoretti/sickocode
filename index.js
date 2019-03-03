#!/usr/bin/nodejs

// -------------- load packages -------------- //
// INITIALIZATION STUFF

var express = require('express')
var app = express();
var { dialogflow } = require('actions-on-google');
var assistantApp = dialogflow();
var bodyParser = require('body-parser');
var spawn = require('child_process').spawnSync;
var path = require('path');

// -------------- express initialization -------------- //
// PORT SETUP - NUMBER SPECIFIC TO THIS SYSTEM

app.set('port', process.env.PORT || 8080 );
app.use(bodyParser.urlencoded({ extended: false }));
app.use(bodyParser.json());

python_exe = 'python';
pythonFile = path.join(__dirname, 'python', 'py_script_01.py');

// -------------- express 'get' handlers -------------- //
// These 'getters' are what fetch your pages

app.get('/', function(req, res){
    var process = spawn(python_exe, [pythonFile, 'heyyy']);
    // process.stdout.on('data', function(data) {
    //     res.send(data.toString());
    // });
    res.send("" + process.stdout);
});

app.post('/rap', assistantApp);

assistantApp.intent('rap', conv => {
    var subj = conv.parameters.Subject;
    //console.log("Subject:" + subj);
    var process = spawn(python_exe, [pythonFile, subj]);
    // process.stdout.on('data', function(data) {
    //     conv.close(data.toString());
    // });
    conv.close("" + process.stdout);
    //conv.close(subj + " Look up in the sky, it’s a bird, it’s a plane/it’s the Funk Doctor spot smoking Buddha on a train/how high? So high so I can kiss the sky/how sick, so sick that you can suck my dick");
});

assistantApp.intent('rap like', conv => {
    var subj = conv.parameters.Subject;
    console.log("Rapping like:" + subj);
   
    conv.close("Rap like "+ subj + "? I ain't no copycat bitch.");
});

assistantApp.intent('Default Welcome Intent', conv => {
  conv.ask('<speak><prosody rate="x-fast">What up <emphasis level = "strong"><prosody rate="x-slow" pitch="-2st">fool?</prosody></emphasis></prosody></speak>');
})

assistantApp.intent('Default Fallback Intent', conv => {
  conv.ask('I didn\'t understand. Can you tell me something else, fool?')
});

// -------------- listener -------------- //
// // The listener is what keeps node 'alive.'

var listener = app.listen(app.get('port'), function() {
  console.log( 'Express server started on port: '+listener.address().port );
});
