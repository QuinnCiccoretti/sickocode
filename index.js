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
    res.send('hola');
});

app.post('/rap', assistantApp);

assistantApp.intent('rap', conv => {
    conv.close("<speak>Yeah,Yeah,Yeah. Goin on you with the pick and roll, Young La Flame he in sicko mode</speak>");
});

assistantApp.intent('Default Welcome Intent', conv => {
  conv.ask('<speak>What up,<break time="3s"/> <emphasis level = "strong">fool?</emphasis></speak>');
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
