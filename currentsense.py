from gpiozero import MCP3008
from time import sleep

class CurrentSensor:
    def __init__(self):
        currentsensechannel = 0
        self.CLK = 11
        self.MOSI = 10
        self.MISO = 9
        self.CS = 8

        self.counterval = 0
        self.counterinterval = 100
        self.voltagevallist = []

        self.VRATIO = 1.0/0.305 #ratio of V_MULTIMETER/V_CHIP (raw_val() in this case)
        self.CRATIO = 8.5 #using a 1000 ohm resistor, the BTS7960's output current should be self.CRATIO * self.VRATIO * raw_val()

        self.ldr = MCP3008(channel=currentsensechannel, clock_pin=self.CLK, mosi_pin=self.MOSI, miso_pin=self.MISO, select_pin=self.CS)

    def raw_val(self):
        return self.ldr.value

    def voltage_sense(self):
        self.voltagevallist.append(self.raw_val())
        self.counterval += 1
        
        if self.counterval % self.counterinterval == 0:
            intervalaverage = sum(self.voltagevallist[-self.counterinterval:])/self.counterinterval
            print(f"DA MOVING AVERAGE IS:  {intervalaverage}")

    def convertVtoA(self, v):
        return v * self.VRATIO * self.CRATIO

if __name__ == "__main__":
    thing = CurrentSensor()
    print(thing.VRATIO)
    print(thing.convertVtoA(0.415))