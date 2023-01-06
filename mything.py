import RPi.GPIO as GPIO  # sudo apt-get install python-rpi.gpio

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


    def left(self):
        GPIO.output(self.LPWM, True)  # start turning left

    def cleanup(self):
        GPIO.cleanup()