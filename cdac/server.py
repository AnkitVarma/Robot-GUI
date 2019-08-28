import sys
import RPi.GPIO as GPIO
from time import sleep

def main():
 
   in1 = 24
   in2 = 23
   en = 25
   in3 = 27
   in4 = 22
   en1 = 17
   temp1=1
   GPIO.setmode(GPIO.BCM)
   GPIO.setup(in1,GPIO.OUT)
   GPIO.setup(in2,GPIO.OUT)
   GPIO.setup(en,GPIO.OUT)
   GPIO.output(in1,GPIO.LOW)
   GPIO.output(in2,GPIO.LOW)
   p=GPIO.PWM(en,1000)
   p.start(75)
   GPIO.setup(in3,GPIO.OUT)
   GPIO.setup(in4,GPIO.OUT)
   GPIO.setup(en1,GPIO.OUT)
   GPIO.output(in3,GPIO.LOW)
   GPIO.output(in4,GPIO.LOW)
   p1=GPIO.PWM(en1,1000)
   p1.start(75)
   while True:
     x = sys.argv[1]
     if x=='f':   
       print("forward")
       GPIO.output(in1,GPIO.HIGH)
       GPIO.output(in2,GPIO.LOW)
       GPIO.output(in3,GPIO.HIGH)
       GPIO.output(in4,GPIO.LOW)
       x='z'
     elif x=='s':
       print("stop")
       GPIO.output(in1,GPIO.LOW)
       GPIO.output(in2,GPIO.LOW)
       GPIO.output(in3,GPIO.LOW)
       GPIO.output(in4,GPIO.LOW)
  
       x='z'

     elif x=='b':
       print("backward")
       GPIO.output(in1,GPIO.LOW)
       GPIO.output(in2,GPIO.HIGH)
       GPIO.output(in3,GPIO.LOW)
       GPIO.output(in4,GPIO.HIGH)
       x='z'

     else:
       print("<<<  wrong data  >>>")
if __name__ == '__main__':
    main()


