import RPi.GPIO as GPIO
import time
dac=[6, 12, 5, 0, 1, 7, 11, 8]
number=[1, 1, 1, 1, 1, 1, 1, 1]
GPIO.setmode(GPIO.BCM)
for i in range(0, 8):
    GPIO.setup(int(dac[i]), GPIO.OUT)
for i in range(0, 8):
    GPIO.output(dac[i], number[7-i])
time.sleep(15)
for i in range(7, 0, -1):
    GPIO.output(dac[i], 0)
GPIO.cleanup()