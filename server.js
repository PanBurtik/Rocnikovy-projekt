const http = require('http');
const path = require('path');
const express = require('express');
const unzipper = require('unzipper');
const fileUpload = require('express-fileupload');
const fs = require('fs');
const MongoClient = require('mongodb').MongoClient;
const uri = "mongodb://localhost:27017";


const client = new MongoClient(uri, { useNewUrlParser: true });

const dbName = "model"


function sendFileToDB(name, file) {
  // Use the client to connect to the database
  client.connect(err => {
    // Create a reference to the collection
    const collection = client.db(dbName).collection(dbName);

    // Create a new document to insert
    const document = { name: name, data: file };

    // Use the insertOne() method to index the document
    collection.insertOne(document, function(err, result) {
      console.log("Document indexed");
      client.close();
    });
  });
}

function getFileByName(name) {
  client.connect(err => {
    // Create a reference to the collection
    const collection = client.db(dbName).collection(dbName);

    // Use the find() method to retrieve the document with the specified name
    collection.find({ name: name }).toArray(function(err, docs) {
      console.log(docs);
      client.close();
    });
  });
}

function listAllFiles(name) {
  client.connect(err => {
    // Create a reference to the collection
    const collection = client.db(dbName).collection(dbName);

    // Use the find() method to retrieve the document with the specified name
    collection.find({}).toArray(function(err, docs) {
      docs.map(e => console.log(e.name));
      client.close();
    });
  });
}

listAllFiles()

const hostname = '127.0.0.1';
const port = 3000;
const app = express();

app.use(express.static(path.join(__dirname, "object")));
app.use(fileUpload({
  limits: { fileSize: 50 * 1024 * 1024 },
}));

const server = http.createServer(app);

server.listen(port, hostname, () => {
  console.log(`Server running at http://${hostname}:${port}/`);
});


//Posílání a odzipování zip souboru do složky s cestou na řádku 29:
app.post('/upload', async function(req, res) {
  console.log(req.files.filename.data);
  const directory = await unzipper.Open.buffer(req.files.filename.data);;

  sendFileToDB("xddmodel", req.files.filename.data)

  await directory.extract({
    path: "object\\"+ req.files.filename.name
  }) // the uploaded file object
  res.writeHead(301, {
    Location: "/"
  }).end();
});

app.get('/objects', async function(req, res){
  fs.readdir("object", (err, files) => {
    if (err)
      console.log(err);
    else {
      res.write(JSON.stringify(files));
      res.end();
      console.log("\nCurrent directory filenames:");
      files.forEach(file => {
        console.log(file);
      })
    }
  })

});