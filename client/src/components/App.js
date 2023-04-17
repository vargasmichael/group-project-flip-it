import React, { useEffect, useState } from "react";
import { Switch, Route } from "react-router-dom";
import Header from "./Header";
import Main from "./Main";

function App() {
  // Code goes here!
  return (
    <>
      <Header />
      <Main />

    </>
  )
}
//This is the server
//npm init -y
// npm install socket.io
const http = require("http").createServer();
const io = require("socket.io")(http, {
  cors: {origin: "*"}
});

io.on("connection", socket => {
  console.log("a user connected");
  socket.on("message", message => {
    console.log(message);
    io.emit("message", `${socket.id.substr(0, 2)} said ${message}`);
  });
});

http.listen(3001, () => console.log('listening http://localhost:8080') );

const WebScoket = require("ws")
const server = new WebScoket.Server({ port: 3001 })

server.on("connection", ws => {
  ws.on("message", message => {
    console.log(`Received message => ${message}`)
    ws.send("ho!")
     
  });
});

// This is will go to another component
const socket = new WebSocket("ws://localhost:3001");

socket.onmessage = ({ data }) => {
  console.log('Message from server ', data);
};

document.querySelector('button').onclick = () => {
  socket.send('Hello from the client!');
};




export default App;
