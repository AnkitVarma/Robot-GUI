// @ts-nocheck
const express = require('express');//Used Express 
const cv = require('opencv4nodejs');//Using Opencv
const path = require('path');
const fs = require('fs');
const app = express();
const server = require('http').Server(app);
const io = require('socket.io')(server);//Socket
let { PythonShell } = require('python-shell');

app.get('/', (req ,res) => {
   res.sendFile(path.join(__dirname, 'index.html'));
});
//Socket Connection
var socketlist = [];
io.on('connection', function(socket){
   console.log('made a socket connection', socket.id);
   socketlist.push(socket);
  
  
   //Listening Client forward Command//
   socket.on('forward', function(data){
      console.log(data.message);
      if(data.message == 'forward'){
         //Giving response to Client of forward command//
         var options = {
            mode: 'text',
            args: 'f'
        };
         var test = PythonShell.run('logingbasic.py', options, function (err) {
            if (err) throw err;
            // results is an array consisting of messages collected during execution
            
            });
            test.on('message', function(message){      
              
              console.log(message)
               //io.sockets.emit('image', message);
          
           
              });
       
         io.sockets.emit('forward', 'yes i am moving forward');

      }

   });
 
   //Listening Client backward Command//
   socket.on('backward', function(data){
      console.log(data.message);
      if(data.message == 'backward'){
         //Giving response to Client of backward command//
         var options = {
            mode: 'text',
            args: 'b'
        };
         var test = PythonShell.run('logingbasic.py', options, function (err) {
            if (err) throw err;
            // results is an array consisting of messages collected during execution
            
            });
            test.on('message', function(message){      
              
              console.log(message)
               //io.sockets.emit('image', message);
          
           
              });
         io.sockets.emit('backward', 'yes i am moving backward');
      }
   });
   //Listening Client right Command//
   socket.on('right', function(data){
      console.log(data.message);
      if(data.message == 'right'){
         var options = {
            mode: 'text',
            args: 'r'
        };
         var test = PythonShell.run('logingbasic.py', options, function (err) {
            if (err) throw err;
            // results is an array consisting of messages collected during execution
            
            });
            test.on('message', function(message){      
              
              console.log(message)
               //io.sockets.emit('image', message);
          
           
              });
         io.sockets.emit('right', 'yes i am moving right');
      }
   });
   //Listening Client left Command//
   socket.on('left', function(data){
      console.log(data.message);
      if(data.message == 'left'){
         //Giving response to Client of left command//
         var options = {
            mode: 'text',
            args: 'l'
        };
         var test = PythonShell.run('logingbasic.py', options, function (err) {
            if (err) throw err;
            // results is an array consisting of messages collected during execution
            
            });
            test.on('message', function(message){      
              
              console.log(message)
               //io.sockets.emit('image', message);
          
           
              });
         io.sockets.emit('left', 'yes i am moving Left');
      }
   });
   //Listening Client Start Streaming Command//
   socket.on('chat', function(data){
      if(data.message == 'yes'){
         //Giving response to Client of Start Streaming command//
         var test = PythonShell.run('stream.py', null, function (err) {
            if (err) throw err;
            
          });
          test.on('message', function(message){      
           
           
              //console.log(message);
              io.sockets.emit('image', message);
         
           
         });
      }
   });
   //Edge detection//
   socket.on('edge', function(data){
      if(data.message == 'edge'){
         var test = PythonShell.run('roboedge.py', null, function (err) {
            if (err) throw err;
            
          });
          test.on('message', function(message){      
           
           
              
              io.sockets.emit('edge', message);
         
           
         });
      }
   });
   //Listening Client Close Command//
   socket.on('chip', function(data){
      if(data.message == 'chip'){
         console.log('Closeing');
         socket.disconnect();
      }
   });
});
server.listen(3000, () => {
   console.log('Running on port 3000');
});