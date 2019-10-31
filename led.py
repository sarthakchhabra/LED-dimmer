import RPi.GPIO as g
import time
g.setmode(g.BCM)
g.setup(2,g.OUT)
a=g.PWM(2,100)
       
a.start(0) 
       
for i in range (1,101):
            a.ChangeDutyCycle(i)
            time.sleep(0.05)
for i in range (1,100):
            a.ChangeDutyCycle(100-i)
            time.sleep(0.05)
