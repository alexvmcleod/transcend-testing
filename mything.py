import RPi.GPIO as GPIO  # sudo apt-get install python-rpi.gpio
import time


class Driver:
    def __init__(self):
        GPIO.setmode(GPIO.BCM)
        self.R_EN = 26
        self.L_EN = 25
        self.RPWM = 6
        self.LPWM = 5
        GPIO.setup(self.R_EN, GPIO.OUT)
        GPIO.setup(self.RPWM, GPIO.OUT)
        GPIO.setup(self.L_EN, GPIO.OUT)
        GPIO.setup(self.LPWM, GPIO.OUT)
        GPIO.output(self.R_EN, True)
        GPIO.output(self.L_EN, True)

    def neutral(self):
        GPIO.output(self.RPWM, False)  # Stop turning right
        GPIO.output(self.LPWM, False)  # stop turning left

    def right(self):
        GPIO.output(self.LPWM, False)  # stop turning left
        GPIO.output(self.RPWM, True)  # start turning right

    def left(self):
        GPIO.output(self.RPWM, False)  # Stop turning right
        GPIO.output(self.LPWM, True)  # start turning left

    def cleanup(self):import RPi.GPIO as GPIO  # sudo apt-get install python-rpi.gpio

class Driver:
    def __init__(self):
        GPIO.setmode(GPIO.BOARD)
        self.L_EN = 23
        self.LPWM = 24
        GPIO.setup(self.L_EN, GPIO.OUT)
        GPIO.setup(self.LPWM, GPIO.OUT)
        GPIO.output(self.L_EN, True)

    def neutral(self):
        GPIO.output(self.LPWM, False)  # stop turning left

    def right(self):
        GPIO.output(self.LPWM, False)  # stop turning left
        GPIO.output(self.RPWM, True)  # start turning right

    def left(self):
        GPIO.output(self.LPWM, True)  # start turning left

    def cleanup(self):
        GPIO.cleanup()