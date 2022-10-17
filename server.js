const http = require('http');
const path = require('path');
const express = require('express');

const hostname = '127.0.0.1';
const port = 3000;
const app = express();

app.use(express.static(path.join(__dirname, "object")));

const server = http.createServer(app);

server.listen(port, hostname, () => {
  console.log(`Server running at http://${hostname}:${port}/`);
});