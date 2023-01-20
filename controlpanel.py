from tkinter import *
from Driver import Driver
from sampleDriver import Sim_Driver

root = Tk()  
root.geometry("400x130") 

#default direction
direction = "left"
is_simulation = True

da_driver = Sim_Driver()

if not is_simulation:
    da_driver = Driver()

def move_motor(power):
    if direction == "left":
        da_driver.left(power=power)
    else:
        da_driver.right(power=power)

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
root.mainloop()
print("Finished!")
da_driver.cleanup()