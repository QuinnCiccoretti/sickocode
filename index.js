#!/usr/bin/nodejs

// -------------- load packages -------------- //
// INITIALIZATION STUFF

var express = require('express')
var app = express();
var { dialogflow } = require('actions-on-google');
var assistantApp = dialogflow();
var bodyParser = require('body-parser');

// -------------- express initialization -------------- //
// PORT SETUP - NUMBER SPECIFIC TO THIS SYSTEM

app.set('port', process.env.PORT || 8080 );
app.use(bodyParser.urlencoded({ extended: false }));
app.use(bodyParser.json());

// -------------- express 'get' handlers -------------- //
// These 'getters' are what fetch your pages

app.get('/', function(req, res){

    res.send('hola');
});

app.post('/rap', assistantApp);

assistantApp.intent('rap', conv => {
    python_exe = 'python3';
    pythonFile = path.join(__dirname, 'python', 'py_script_01.py');
    py = child_process.spawnSync(python_exe, [pythonFile],  );
    py_response = py['stdout'].toString();
    conv.close(py_response);
});

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
