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

// -------------- express 'get' handlers -------------- //
// These 'getters' are what fetch your pages

app.get('/', function(req, res){
    var process = spawn(python_exe, [pythonFile, 'heyyy']);
    res.send("" + process.stdout);
});

app.post('/rap', assistantApp);

assistantApp.intent('doyouknow', conv => {
    var artist = conv.parameters.artist;
    pythonFile = path.join(__dirname, 'python', 'doYouKnow.py');
    var process = spawn(python_exe, [pythonFile, artist]);
    console.log(process.stdout[1]);
    conv.ask("I " + process.stdout + "know " + artist);
});

assistantApp.intent('rap', conv => {
    pythonFile = path.join(__dirname, 'python', 'py_script_01.py');
    var subj = conv.parameters.subject;
    var process = spawn(python_exe, [pythonFile, subj]);
    conv.close("" + process.stdout);
});

assistantApp.intent('raplike', conv => {
    pythonFile = path.join(__dirname, 'python', 'py_script_01.py');
    var artist = conv.parameters.artist;
    var process = spawn(python_exe, [pythonFile, artist]);
    conv.close("Rap like "+ process.stdout + "? I ain't no copycat bitch!");
});

assistantApp.intent('Default Welcome Intent', conv => {
  conv.ask('<speak><prosody rate="x-fast">What up <emphasis level = "strong"><prosody rate="x-slow" pitch="-2st">fool?</prosody></emphasis></prosody></speak>');
})

assistantApp.intent('Default Fallback Intent', conv => {
  conv.ask('Say it again, fool, I\'m a damn robot with no ears.')
});

// -------------- listener -------------- //
// // The listener is what keeps node 'alive.'

var listener = app.listen(app.get('port'), function() {
  console.log( 'Express server started on port: '+listener.address().port );
});
