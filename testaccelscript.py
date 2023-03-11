import csv
import time
from halldetector import HallSensor
from currentsense import CurrentSensor
from Driver import Driver
import os

def testaccelthing(start=0,end=10,duration=3):
    dadriver = Driver()
    dahall = HallSensor(22)
    dacur = CurrentSensor()

    new_directory = f'testdata//{time.time()}'
    os.makedirs(new_directory)

    for level in range(start,end):
        time.sleep(1)

        #RUN DA TING
        dadriver.left(level)
        
        #track stuff
        filename = f"{new_directory}//{level}.csv"
        with open(filename, 'a', newline='') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow(["datetime","rpm","voltage","current"])

        starttime = int(time.time() * 1000000)

        # print(int(time.time() * 1000000) - starttime)
        # print(duration * 1000000)
        while(int(time.time() * 1000000) - starttime) < (duration * 1000000):
            datime = int(time.time() * 1000000)
            rpm = dahall.rpm
            vees = dacur.duty_cycleV(level)
            curs = dacur.getdaA()
            row = [datime,rpm,vees,curs]
            #print("runninf")
            with open(filename, 'a', newline='') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow(row)
            time.sleep(0.01)

        dadriver.neutral()

        x = input(f"Level: {level}. Press enter to continue.")

testaccelthing(0,10,3)