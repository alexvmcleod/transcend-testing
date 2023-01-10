import RPi.GPIO as GPIO  # sudo apt-get install python-rpi.gpio
import time


class Driver:
    def __init__(self):
        #assigns pins numbers to gpio format
        GPIO.setmode(GPIO.BCM)

        #assigns pin numbers
        self.R_EN = 26
        self.L_EN = 25
        self.RPWM = 12
        self.LPWM = 13

        #sets output to assigned pins
        GPIO.setup(self.R_EN, GPIO.OUT)
        GPIO.setup(self.RPWM, GPIO.OUT)
        GPIO.setup(self.L_EN, GPIO.OUT)
        GPIO.setup(self.LPWM, GPIO.OUT)

        #enables output to turn motor left/right
        GPIO.output(self.R_EN, True)
        GPIO.output(self.L_EN, True)

        #creates PWM objects to control motor PWM
        self.rpwm_controller = GPIO.PWM(self.RPWM, 100)
        self.lpwm_controller = GPIO.PWM(self.LPWM, 100)

        #sets pwm to 0%
        self.lpwm_controller.start(0)
        self.rpwm_controller.start(0)


    def neutral(self,time_elapse=5):
        self.rpwm_controller.ChangeDutyCycle(0)  # Stop turning right
        self.lpwm_controller.ChangeDutyCycle(0)  # stop turning left
        time.sleep(time_elapse)

    def right(self,power=10,time_elapse=5):
        self.lpwm_controller.ChangeDutyCycle(0)  # stop turning left
        self.rpwm_controller.ChangeDutyCycle(power)  # start turning right
        time.sleep(time_elapse)

    def left(self,power=10,time_elapse=5):
        self.rpwm_controller.ChangeDutyCycle(0)  # Stop turning right
        self.lpwm_controller.ChangeDutyCycle(power)  # start turning left
        time.sleep(time_elapse)

    def cleanup(self):
        self.rpwm_controller.stop()
        self.lpwm_controller.stop()
        GPIO.cleanup()  # sudo apt-get install python-rpi.gpio