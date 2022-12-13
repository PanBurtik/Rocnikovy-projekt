const http = require('http');
const path = require('path');
const express = require('express');
const unzipper = require('unzipper');
const fileUpload = require('express-fileupload');
const fs = require('fs');

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

app.post('/upload', async function(req, res) {
  console.log(req.files.filename.data);
  const directory = await unzipper.Open.buffer(req.files.filename.data);;
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