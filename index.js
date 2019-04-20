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

var audio_files = [["humble.mp3":8],
["ric.mp3" , 0],
["taste.mp3" , 3],
["zeze.mp3" , 10.5],
["forever.mp3" , 12.5],
["indaclub.mp3" , 5.5],
["stilldre.mp3" , 10.5],
["win.mp3" ,  7]];

var uuidv1 = require('uuid/v1');
//var admin = require("firebase-admin");
//var serviceAccount = require("firebaseAdmin.json");

// admin.initializeApp({
//   credential: admin.credential.cert(serviceAccount),
//   databaseURL: "https://spitfire-351dd.firebaseio.com"
// });
//
// var db = admin.database();
// var users = db.ref("users");
// -------------- express initialization -------------- //
// PORT SETUP - NUMBER SPECIFIC TO THIS SYSTEM

app.set('port', process.env.PORT || 8080 );
app.use(bodyParser.urlencoded({ extended: false }));
app.use(bodyParser.json());
python_exe = 'python';

// -------------- express 'get' handlers -------------- //
// These 'getters' are what fetch your pages

app.get('/', function(req, res){
    res.sendFile(__dirname + "/frontpage/");
});

// app.get('/taste', function(req, res){
//     res.sendFile(__dirname + "/audio/taste.mp3");
// });

// app.get('/zeze', function(req, res){
//     res.sendFile(__dirname + "/audio/zeze.mp3");
// });

// app.get('/humble', function(req, res){
//     res.sendFile(__dirname + "/audio/humble.mp3");
// })
app.use(express.static(__dirname ));
app.use(express.static("frontpage"));
app.use(express.static("audio"));
app.post('/rap', assistantApp);

assistantApp.intent('doyouknow', conv => {
    var artist = conv.parameters.artist;
    conv.ask("Of course I know " + artist + ", anything else, fool?");
});

// assistantApp.intent('rap', conv => {
//     conv.ask('<speak>Tell me someone to rap like, fool!</speak>');
// });
var b1 = '<speak><par><media xml:id = "rap" begin = "';
var b2 = '"><prosody rate="medium" pitch="-3st">';
var e1 = '</prosody></media><media fadeOutDur = "5.0s" end = "rap.end+5.0s"><audio src = "';
var e2 = '"/></media></par></speak>';
var audio_dir = "https://jay-z.herokuapp.com/audio/";

assistantApp.intent('raplike', conv => {
    pythonFile = path.join(__dirname, 'python', 'raplike.py');
    var artist = conv.parameters.artist;
    var process = spawn(python_exe, [pythonFile, artist]);

    var rand = audio_dir[Math.floor(Math.random() * audio_dir.length)];
    var ssml_str = b1+ rand[1]+"s"+ b2 + process.stdout + e1 + audio_dir + rand[0] + e2;
    conv.close(ssml_str);

});

assistantApp.intent('Default Welcome Intent', conv => {
  conv.ask('<speak>' + sayMature(conv) + '<prosody rate="x-fast">What up <emphasis level = "strong"><prosody rate="x-slow" pitch="-2st">fool?</prosody></emphasis></prosody></speak>');
})

assistantApp.intent('Default Fallback Intent', conv => {
  conv.ask('<speak><emphasis level = "strong">Didn\'t catch yo drift!</emphasis><prosody rate="x-fast">What up <emphasis level = "strong"><prosody rate="x-slow" pitch="-2st">fool?</prosody></emphasis></prosody></speak>');
})

assistantApp.intent('freestyle', conv => {

    pythonFile = path.join(__dirname, 'python', 'py_freestyle.py');
    var process = spawn(python_exe, [pythonFile]);
    conv.close(b1 + "8s"+b2 + sayMature(conv) + process.stdout + e1 + audio_dir + "humble.mp3"+e2);
});

app.post('/rap2', function(req, res){
    res.send("YO");
});

// -------------- listener -------------- //
// // The listener is what keeps node 'alive.'

var listener = app.listen(app.get('port'), function() {
  console.log( 'Express server started on port: '+listener.address().port );
});

function sayMature(conv){
    let userId;
    // if a value for userID exists un user storage, it's a returning user so we can
    // just read the value and use it. If a value for userId does not exist in user storage,
    // it's a new user, so we need to generate a new ID and save it in user storage.
    if ('userId' in conv.user.storage) {
      userId = conv.user.storage.userId;
      return "";
    } else {
      // generateUUID is your function to generate ids.
      userId = uuidv1();
      conv.user.storage.userId = userId
      return '<emphasis level = "strong">Warning: this app contains mature content</emphasis>';
    }
}
