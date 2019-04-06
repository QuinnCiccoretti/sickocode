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
var Alexa = require('ask-sdk-core');

// -------------- express initialization -------------- //
// PORT SETUP - NUMBER SPECIFIC TO THIS SYSTEM

app.set('port', process.env.PORT || 8080 );
app.use(bodyParser.urlencoded({ extended: false }));
app.use(bodyParser.json());
python_exe = 'python';

// -------------- express 'get' handlers -------------- //
// These 'getters' are what fetch your pages

app.get('/', function(req, res){
    res.sendFile(__dirname + "/index.html");
});

app.get('/taste', function(req, res){
    res.sendFile(__dirname + "/audio/taste.mp3");
});

app.get('/zeze', function(req, res){
    res.sendFile(__dirname + "/audio/zeze.mp3");
});

app.get('/humble', function(req, res){
    res.sendFile(__dirname + "/audio/humble.mp3");
})
app.use(express.static(__dirname ));
app.post('/rap', assistantApp);

// assistantApp.intent('doyouknow', conv => {
//     var artist = conv.parameters.artist;
//     pythonFile = path.join(__dirname, 'python', 'doYouKnow.py');
//     var process = spawn(python_exe, [pythonFile, artist]);
//     console.log(process.stdout);
//     conv.ask("I " + process.stdout + "know " + artist + ". Anything else, fool?");
// });

var b1 = '<speak><par><media xml:id = "rap" begin = "';
var b2 = '"><prosody rate="medium" pitch="-3st">';
var e1 = '</prosody></media><media fadeOutDur = "5.0s" end = "rap.end+5.0s"><audio src = "';
var e2 = '"/></media></par></speak>';
assistantApp.intent('raplike', conv => {
    pythonFile = path.join(__dirname, 'python', 'py_script_01.py');
    var artist = conv.parameters.artist;
    var process = spawn(python_exe, [pythonFile, artist]);

    var rando = Math.random();
    if(rando < .4){
        conv.close(b1+ "3s"+ b2 + process.stdout + e1 + "https://jay-z.herokuapp.com/audio/taste.mp3" + e2);
    }
    else if (rando < .9){
        conv.close(b1 + "10.5s"+b2 + process.stdout + e1 + "https://jay-z.herokuapp.com/audio/zeze.mp3"+e2);
    }
    else{
        conv.close(b1 + "8s"+b2 + process.stdout + e1 + "https://jay-z.herokuapp.com/audio/humble.mp3"+e2);
    }
});

assistantApp.intent('Default Welcome Intent', conv => {
  conv.ask('<speak><emphasis level = "strong">Warning: this app contains mature content</emphasis><prosody rate="x-fast">What up <emphasis level = "strong"><prosody rate="x-slow" pitch="-2st">fool?</prosody></emphasis></prosody></speak>');
})

assistantApp.intent('freestyle', conv => {
    pythonFile = path.join(__dirname, 'python', 'py_freestyle.py');
    var process = spawn(python_exe, [pythonFile]);
    conv.close(b1 + "8s"+b2 + process.stdout + e1 + "https://jay-z.herokuapp.com/audio/humble.mp3"+e2);
});

app.post('/rap2', function(req, res){
    // Build the context manually, because Amazon Lambda is missing
    var context = {
        succeed: function (result) {
            console.log(result);
            res.json(result);
        },
        fail:function (error) {
            console.log(error);
        }
    };
    // Delegate the request to the Alexa SDK and the declared intent-handlers
    var alexa = Alexa.handler(req.body, context);
    alexa.registerHandlers(handlers);
    alexa.execute();
});

// -------------- listener -------------- //
// // The listener is what keeps node 'alive.'

var listener = app.listen(app.get('port'), function() {
  console.log( 'Express server started on port: '+listener.address().port );
});
