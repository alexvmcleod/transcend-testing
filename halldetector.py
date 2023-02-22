import RPi.GPIO as GPIO  # sudo apt-get install python-rpi.gpio
import time
from statistics import mean

class HallSensor:
    def __init__(self,pin):
        GPIO.setmode(GPIO.BCM)

        self.hall = pin
        GPIO.setup(self.hall, GPIO.IN)

        self.start_time = time.time_ns()

        self.is_tripped = False
        self.list_o_time = []
        self.ma_count = 5
        self.magnet_count = 4

        self.trip_count = 0

        self.target_rpm = 60
        self.rpm_error_bound = 30

        self.rpm = 0

    def convertSPRtoRPM(self,spr):
        if spr == 0:
            return 0
        else:
            return 60 / spr

    def convertToSPR(self,n,count):
        #print(n)
        return (n * count) / 1000000000

    def findDifferenceMA(self):
        if len(self.list_o_time) > 1:
            return mean([j-i for i, j in zip(self.list_o_time[:-1], self.list_o_time[1:self.ma_count])]) * -1
        else:
            return 0

    def hallDetection(self):
        time_elapsed = time.time_ns() - self.start_time
        hall_val  = GPIO.input(self.hall)

        if hall_val == 0:
            if self.is_tripped == False:
                self.trip_count += 1
                print(self.trip_count)

                #print(list_o_time)
                #print("Detected!")
                avg = self.findDifferenceMA()
                spr = self.convertToSPR(avg,4)
                rpm = self.convertSPRtoRPM(spr)

                self.rpm = rpm
                #print(f"GPIO Pin: {self.hall}, RPM: {rpm}")
                #print("#############################")

                self.is_tripped = True
                self.list_o_time.insert(0,time_elapsed)

        if hall_val == 1:
            if self.is_tripped == True:
                self.is_tripped = False

    def generate_RPM(self):
        avg = self.findDifferenceMA()
        spr = self.convertToSPR(avg,self.magnet_count)
        rpm = self.convertSPRtoRPM(spr)
        return rpm