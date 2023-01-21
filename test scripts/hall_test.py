import RPi.GPIO as GPIO  # sudo apt-get install python-rpi.gpio
import time


GPIO.setmode(GPIO.BCM)

hallthing = 17
GPIO.setup(hallthing, GPIO.IN)

while True:
    ison = GPIO.input(hallthing)
    if ison == 0:
        print("oof")
    else:
        print('nothing')
    time.sleep(0.01)