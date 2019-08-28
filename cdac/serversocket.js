// @ts-nocheck
const express = require('express');//Used Express 
//const cv = require('opencv4nodejs');//Using Opencv
const path = require('path');
//const fs = require('fs');
const app = express();
const server = require('http').Server(app);
const io = require('socket.io')(server);//Socket
let { PythonShell } = require('python-shell');
app.get('/', (req ,res) => {
   res.sendFile(path.join(__dirname, 'index.html'));
});

//Socket Connection
io.on('connection', function(socket){
   console.log('made a socket connection', socket.id);
  // const cwap = new cv.VideoCapture(0);
    
  
  
   //Listening Client forward Command//
   socket.on('forward', function(data){
     // console.log(data.message);
     
    if(data.message == 'forward'){
    //Giving response to Client of forward command//
     var options = {
            mode: 'text',
            args: 'f'
        };
  var test = PythonShell.run('backward.py', options, function (err) {
       if (err) throw err;
    // results is an array consisting of messages collected during execution
    
    });
    test.on('message', function(message){      
      
     console.log(message)
       //io.sockets.emit('image', message);
  
     io.sockets.emit('forward', message);
  });
         

      
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

       var test = PythonShell.run('backward.py', options, function (err) {
          
         // results is an array consisting of messages collected during execution
         
         });
         test.on('message', function(message){      
           
           console.log(message)
            //io.sockets.emit('image', message);
       
        io.sockets.emit('backward', message);
           });
         
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

       var test = PythonShell.run('backward.py', options, function (err) {
         
         // results is an array consisting of messages collected during execution
         
         });
         test.on('message', function(message){      
           
           console.log(message)
            //io.sockets.emit('image', message);
       
            io.sockets.emit('right', message);
           });
      
         
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

       var test = PythonShell.run('backward.py', options, function (err) {
        
         // results is an array consisting of messages collected during execution
         
         });
         test.on('message', function(message){      
           
           console.log(message)
            //io.sockets.emit('image', message);
           io.sockets.emit('left', message);
        
           });
      
         
      }
   });
   
   //Listening Client Auto Control on Command//
   socket.on('autocontrolon', function(data){
      console.log(data.message);
       
      if(data.message == 'autocontrolon'){
         //Giving response to Client autocontrol command//
          var options = {
            mode: 'text',
            args: '1'
        }; 

       var test = PythonShell.run('robotcontrol.py', options, function (err) {
         if (err) throw err;
         // results is an array consisting of messages collected during execution
         
         });
         test.on('message', function(message){      
           
           console.log(message)
            //io.sockets.emit('image', message);
       
        
           });
         io.sockets.emit('autocontrolon', 'Auto Control On');
      }
     
   });
   //Listening Client Auto Control Off Command//
    socket.on('autocontroloff', function(data){
      console.log(data.message);
      if(data.message == 'autocontroloff'){
         //Giving response to Client autocontrol command//
        var options = {
            mode: 'text',
            args: ['1','0']
        }; 

       var test = PythonShell.run('robotcontrol.py', options, function (err) {
         if (err) throw err;
         // results is an array consisting of messages collected during execution
         
         });
         test.on('message', function(message){      
           
           console.log(message)
            //io.sockets.emit('image', message);
       
        
           });
         io.sockets.emit('autocontroloff', 'Auto Control Off');
      }
   });
   //Listening Client Start Streaming Command//
   socket.on('chat', function(data){
      if(data.message == 'yes'){
         //Giving response to Client of Start Streaming command//
      
      }
   });


   //Listening Client Capture Command//
   socket.on('capture', function(data){
     const frame = cwap.read();
     const image = cv.imencode('.jpeg', frame).toString('base64');
     io.sockets.emit('capture', 'image Capture');
     let base64Image = image.split(';base64,').pop();
     let name = 'uploads/IMG-' + Date.now() + '.jpg';
     fs.writeFile(name,base64Image, { encoding: 'base64'}, function(err){
      console.log('file Created');
      });
   });
});
server.listen(3000, () => {
   console.log('Running on port 3000');
});