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

def move_motor(power):
    if direction == "left":
        da_driver.left(power=int(power))
    else:
        da_driver.right(power=int(power))

    

def change_direction(dire):
    global direction
    direction = dire

def stop_motor():
    da_driver.neutral()


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


# run Tk event loop
while True:
    root.update_idletasks()
    root.update()

    print(f"HERE IS RAW VAL THING:   {cur_sensor.raw_val()}")
    hall_drive_pulley.hallDetection()
    hall_driven_pulley.hallDetection()
    time.sleep(0.01)

print("Finished!")
da_driver.cleanup()