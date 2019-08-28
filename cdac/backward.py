import RPi.GPIO as GPIO
import sys
import time

in1 = 24 # 18
in2 = 23 # 16
en = 25 # 22
in3 = 27 # 13
in4 = 22 # 15
en1 = 17 #11
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
x = sys.argv[1]
if(x == 'f'):
  sleep_time = 0.50
  print("forward moving")
  GPIO.output(in1,GPIO.HIGH)
  GPIO.output(in2,GPIO.LOW)
  GPIO.output(in3,GPIO.HIGH)
  GPIO.output(in4,GPIO.LOW)
  time.sleep(sleep_time)
elif(x == 'b'):
  sleep_time = 0.50
  print("backward moving")
  GPIO.output(in1,GPIO.LOW)
  GPIO.output(in2,GPIO.HIGH)
  GPIO.output(in3,GPIO.LOW)
  GPIO.output(in4,GPIO.HIGH)
  time.sleep(sleep_time)
elif x=='r':
  sleep_time = 3.0
  print("right moving")
  GPIO.output(in1,GPIO.HIGH)
  GPIO.output(in2,GPIO.LOW)
  GPIO.output(in3,GPIO.LOW)
  GPIO.output(in4,GPIO.HIGH)
  time.sleep(sleep_time)
elif x=='l':
  sleep_time = 3.0
  print("left moving")
  GPIO.output(in1,GPIO.LOW)
  GPIO.output(in2,GPIO.HIGH)
  GPIO.output(in3,GPIO.HIGH)
  GPIO.output(in4,GPIO.LOW)
  time.sleep(sleep_time)
