import RPi.GPIO as IO
import RPi.GPIO as GPIO

import time
from time import sleep
IO.setwarnings(False)
IO.setmode(IO.BCM)

IO.setup(20,IO.IN) #GPIO 14 -> IR sensor as input
IO.setup(21,IO.IN) #GPIO 14 -> IR sensor as input
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
GPIO.setmode(GPIO.BCM)
GPIO.setup(in3,GPIO.OUT)
GPIO.setup(in4,GPIO.OUT)
GPIO.setup(en1,GPIO.OUT)
GPIO.output(in3,GPIO.LOW)
GPIO.output(in4,GPIO.LOW)
q=GPIO.PWM(en1,1000)
p.start(75)
q.start(75)
#print("\n")
#print("The default speed & direction of motor is LOW & Forward.....")
#print("r-run s-stop f-forward b-backward l-low m-medium h-high e-exit")
#print("\n")    

while 1:

    if(IO.input(20)==True and IO.input(21)==True): #object is far away
      #print("stop")
      GPIO.output(in1,GPIO.LOW)
      GPIO.output(in2,GPIO.LOW)
      GPIO.output(in3,GPIO.LOW)
      GPIO.output(in4,GPIO.LOW)
    elif(IO.input(20)==True and IO.input(21)==False):
      #print("left")
      GPIO.output(in1,GPIO.HIGH)
      GPIO.output(in2,GPIO.LOW)
      GPIO.output(in3,GPIO.LOW)
      GPIO.output(in4,GPIO.HIGH)
    elif(IO.input(21)==True and IO.input(20)==False): #GPIO 14 -> IR sensor as input:
      #print("right")
      GPIO.output(in1,GPIO.LOW)
      GPIO.output(in2,GPIO.HIGH)
      GPIO.output(in3,GPIO.HIGH)
      GPIO.output(in4,GPIO.LOW)

    elif(IO.input(20)==False and IO.input(21)==False): #GPIO 14 -> IR sensor as input:
      #print("run")
      GPIO.output(in1,GPIO.HIGH)
      GPIO.output(in2,GPIO.LOW)
      GPIO.output(in3,GPIO.HIGH)
      GPIO.output(in4,GPIO.LOW)