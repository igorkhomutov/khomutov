import RPi.GPIO as GPIO
import time
leds=[9, 10, 22, 27, 17, 4, 3, 2]
GPIO.setmode(GPIO.BCM)
for i in range(0, 8):
    GPIO.setup(int(leds[i]), GPIO.OUT)
for k in range(3):
    for i in range(7, 0, -1):
        GPIO.output(leds[i], 1)
        time.sleep(0.2)
        GPIO.output(leds[i], 0)
for i in range(7, 0, -1):
    GPIO.output(leds[i], 0)
GPIO.cleanup()