import RPi.GPIO as GPIO  # sudo apt-get install python-rpi.gpio
import time
from statistics import mean

class HallSensor:
    def __init__(self,pin):
        self.start_time = time.time()
        self.sensor_pin = pin
        self.rpm = 0
        
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.sensor_pin,GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.add_event_detect(self.sensor_pin, GPIO.FALLING, callback= self.update_rpm)

    def update_rpm(self,channel):
        rpm_test = 60/ ((time.time() - self.start_time) *4)
        if rpm_test < 5000:
            self.rpm = rpm_test
        self.start_time = time.time()
        