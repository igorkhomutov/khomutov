import RPi.GPIO as GPIO
import time
leds=[9, 10, 22, 27, 17, 4, 3, 2]
GPIO.setmode(GPIO.BCM)
aux=[21, 20, 26, 16, 19, 25, 23, 24]
for i in range(0, 8):
    GPIO.setup(int(leds[i]), GPIO.OUT)
    GPIO.setup(int(aux[i]), GPIO.IN)
while 1<2:
    for i in range(0, 8):
        GPIO.output(leds[i], GPIO.input(int(aux[i]))