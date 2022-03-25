const fs = require('fs');
const express = require("express");
const cors = require("cors");
const app = express();
const path = __dirname + '/app/views/';
app.use(express.static(path));

app.use(cors({
  origin: 'http://localhost:8081'
}));
//Start Data:
/*
var gesList;
var gestures;
fs.readFile(path +'data/GESlist.json', (err, dataGES) => {
  if (err) throw err;
  gesList = JSON.parse(dataGES);
  console.log("Suggested GES loaded");
});
fs.readFile(path +'data/data.json', (err, dataGestures) => {
  if (err) throw err;
  gestures = JSON.parse(dataGestures);
  console.log("Gestures loaded");
});*/
// parse requests of content-type - application/json
app.use(express.json());
// parse requests of content-type - application/x-www-form-urlencoded
app.use(express.urlencoded({ extended: true }));
// simple route
app.get('/', function (req,res) {
  res.sendFile(path + "index.html");
});
app.post('/newGestureSug', function (req,res) {
  
  //const dataG = JSON.stringify(req.body);
  const dataG = JSON.stringify(req.body, null, 2);
  //console.log(dataG);
  fs.writeFileSync('./app/views/data/GESlist.json', dataG);
  
  console.log("New suggested gesture")
  res.send('{ "message": "Gesture successfully received" }') 
});
app.post('/newGestureGEStory', function (req,res) {

  const dataG = JSON.stringify(req.body, null, 2);
  fs.writeFileSync('./app/views/data/data.json', dataG);
  console.log("New gesture in GEStory")
  res.send('{ "message": "New Gesture received in GESture" }') 
});

// set port, listen for requests
const PORT = process.env.PORT || 8080;
app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}.`);
});