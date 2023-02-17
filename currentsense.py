from gpiozero import MCP3008
from time import sleep

class CurrentSensor:
    def __init__(self):
        currentsensechannel = 0
        self.CLK = 11
        self.MOSI = 10
        self.MISO = 9
        self.CS = 8

        self.ldr = MCP3008(channel=currentsensechannel, clock_pin=self.CLK, mosi_pin=self.MOSI, miso_pin=self.MISO, select_pin=self.CS)

    def raw_val(self):
        return self.ldr.value

    

