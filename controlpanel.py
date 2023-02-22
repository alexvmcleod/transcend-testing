from tkinter import *
from Driver import Driver
from sampleDriver import Sim_Driver
from halldetector import HallSensor
from currentsense import CurrentSensor
import time
root = Tk()  
root.geometry("400x130") 

#default direction
direction = "left"
is_simulation = False

da_driver = Sim_Driver()
hall_drive_pulley = HallSensor(17)
hall_driven_pulley = HallSensor(27)
cur_sensor = CurrentSensor()

if not is_simulation:
    da_driver = Driver()


duty_rating = 0
# hall0 = 0
# hall1 = 1
# cursense = 0
# volsense = 0
# watsense = 0

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
    hall_drive_pulley.hallDetection()
    hall_driven_pulley.hallDetection()

    #print(f"HERE IS RAW VAL THING:   {cur_sensor.raw_val()}")
    
    volts_IS = cur_sensor.voltage_sense_static()
    amps = cur_sensor.convertVtoA(volts_IS)
    volts = cur_sensor.duty_cycleV(duty_rating)
    watts = cur_sensor.calcwattage(a=amps,v=volts)

    hall0rpm = hall_drive_pulley.rpm
    hall1rpm = hall_driven_pulley.rpm
    
    if counter % 200 == 0:
        print("############     METRICS     ############\n")
        print(f"VOLTS FROM CHIP: {volts_IS}V\n")
        print(f"VOLTS: {volts}V")
        print(f"AMPS: {amps}A")
        print(f"WATTS: {watts}W\n")
        print(f"HALL SENSOR 0: {hall0rpm}RPM")
        print(f"HALL SENSOR 1: {hall1rpm}RPM\n")
    
    counter += 1
    time.sleep(0.01)

print("Finished!")
da_driver.cleanup()