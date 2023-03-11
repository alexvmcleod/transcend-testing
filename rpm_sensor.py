import RPi.GPIO as GPIO  # sudo apt-get install python-rpi.gpio
import time
from statistics import mean

sensor_pin = 22
GPIO.setmode(GPIO.BCM)
GPIO.setup(sensor_pin,GPIO.IN, pull_up_down=GPIO.PUD_UP)

rpm = 0


start_time = time.time()

def calculate_RPM(channel,start_time):
    global rpm
    rpm = 60/ ((time.time() - start_time) *4)
    start_time = time.time()

GPIO.add_event_detect(sensor_pin, GPIO.FALLING, callback= calculate_RPM)

# try:
#     while True:
        
#         print("RPM: {:.2f}".format(rpm))

# except KeyboardInterrupt:
#     GPIO.cleanup()

