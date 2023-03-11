from tkinter import *
from Driver import Driver
from sampleDriver import Sim_Driver
from halldetector import HallSensor
from currentsense import CurrentSensor
from rpm_sensor import calculate_RPM
import time
import csv

root = Tk()  
root.geometry("400x130") 

#default direction
direction = "left"
is_simulation = False

da_driver = Sim_Driver()
hall_mass = HallSensor(22)
sensor_pin= 22
start_time = time.time()
cur_sensor = CurrentSensor()

if not is_simulation:
    da_driver = Driver()


duty_rating = 0


def move_motor(power):
    global duty_rating
    duty_rating = power
    if direction == "left":
        da_driver.left(power=int(power))
    else:
        da_driver.right(power=int(power))

def change_direction(dire):
    global direction
    direction = dire

def stop_motor():
    da_driver.neutral()

def update_sensors():
    pass
    


scale1 = Scale(root,
    command = move_motor,
    to = 100,
    orient = HORIZONTAL,
    length = 400,
    label = 'Motor Speed (Percentage)')
scale1.pack(anchor = CENTER)

Radiobutton(root, 
               text="Left",
               padx = 20, 
               command=lambda d="left":change_direction(d), 
               value=1).pack(anchor=W)

Radiobutton(root, 
               text="Right",
               padx = 20, 
               command=lambda d="right":change_direction(d), 
               value=2).pack(anchor=W)

Button(root, 
               text="STOP",
               padx = 40,
               pady = 40, 
               command=stop_motor).pack(anchor=E)

counter = 0
# run Tk event loop
while True:
    #the stuff up here should run every cycle
    root.update_idletasks()
    root.update()
    cur_sensor.voltage_sense()
    

    volts_IS = cur_sensor.voltage_sense_static()
    amps = cur_sensor.convertVtoA(volts_IS)
    volts = cur_sensor.duty_cycleV(duty_rating)
    watts = cur_sensor.calcwattage(a=amps,v=volts)

    rpm = calculate_RPM(sensor_pin,start_time) #calculating the RPM with other module


    with open("/home/transcend/Efficiencycurve.csv","a",newline="") as csvfile:  #writing to csv file
        csvwriter = csv.writer(csvfile)
        data = [volts_IS,amps,volts,watts,rpm]
        csvwriter.writerow(data) 


    time.sleep(0.0001)

    

print("Finished!")
da_driver.cleanup()