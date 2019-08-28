import RPi.GPIO as IO
import RPi.GPIO as GPIO
import sys
import time
from time import sleep
IO.setwarnings(False)
IO.setmode(IO.BCM)

st = sys.argv[1]
print(st)
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
def main():
 while st < 34:
   print(st)
   st += 1
  
  
    
    
    #starting of process
if __name__ == '__main__':
    main()
