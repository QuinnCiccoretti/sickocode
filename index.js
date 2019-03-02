#!/usr/bin/nodejs

// -------------- load packages -------------- //
// INITIALIZATION STUFF

var express = require('express')
var app = express();
var { dialogflow } = require('actions-on-google');
var assistantApp = dialogflow();
var bodyParser = require('body-parser');
var child_process = require('child_process');
var path = require('path');

// -------------- express initialization -------------- //
// PORT SETUP - NUMBER SPECIFIC TO THIS SYSTEM

app.set('port', process.env.PORT || 8080 );
app.use(bodyParser.urlencoded({ extended: false }));
app.use(bodyParser.json());

// -------------- express 'get' handlers -------------- //
// These 'getters' are what fetch your pages

app.get('/', function(req, res){
    // python_exe = 'python3';
    // pythonFile = path.join(__dirname, 'python', 'py_script_01.py');
    // py = child_process.spawnSync(python_exe, [pythonFile, 'heyyy']);
    // py_response = py['stdout'];
    // console.log(py_response);
    res.send('hola');
});

app.post('/rap', assistantApp);

assistantApp.intent('rap', conv => {
    // python_exe = 'python3';
    // pythonFile = path.join(__dirname, 'python', 'py_script_01.py');
    // py = child_process.spawnSync(python_exe, [pythonFile], 'yooo' );
    // py_response = py['stdout'].toString();
    conv.close('Look up in the sky, it’s a bird, it’s a plane. It’s the Funk Doctor pot smoking Buddha on a train. How high, So high so I can kiss the sky. How sick, so sick that you can suck my dick.');
});

assistantApp.intent('Default Welcome Intent', conv => {
  conv.ask('<speak><emphasis level = "strong"> What up,<break time="3s"/> fool?</emphasis></speak>');
})

assistantApp.intent('rap about', conv => {
    conv.close('Yo');
});

assistantApp.intent('Default Fallback Intent', conv => {
  conv.ask(`I didn't understand. Can you tell me something else?`)
})
// -------------- listener -------------- //
// // The listener is what keeps node 'alive.'

var listener = app.listen(app.get('port'), function() {
  console.log( 'Express server started on port: '+listener.address().port );
});
