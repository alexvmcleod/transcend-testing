from gpiozero import MCP3008
from time import sleep

class CurrentSensor:
    def __init__(self):
        self.FLEX_CHANNEL = 1
        self.CLK = 11
        self.MOSI = 10
        self.MISO = 9
        self.CS = 8

        self.counterval = 0
        self.MIN_VOLTAGE =0 
        self.MAX_VOLTAGE = 4.5

        self.MIN_FORCE= 0 #ratio of V_MULTIMETER/V_CHIP (raw_val() in this case)
        self.MAX_FORCE = 100 #using a 1000 ohm resistor, the BTS7960's output current should be self.CRATIO * self.VRATIO * raw_val()

        self.adc = MCP3008(channel=self.FLEX_CHANNEL, clock_pin=self.CLK, mosi_pin=self.MOSI, miso_pin=self.MISO, select_pin=self.CS)

        


    def read_force(self):
        voltage = adc.read_adc(FLEX_CHANNEL)
        voltage = voltage / 1023.0 * 5.0
        force = (voltage -MIN_VOLTAGE)/ (MAX_VOLTAGE-MIN_VOLTAGE) * (MAX_FORCE - MIN_FORCE) + MIN_FORCE
        
        return self.force

    def avg_force(self):
        self.total_force = 0
        for i in range(10):
            self.force = read_force()
            self.total_force += self.force
            time.sleep(0.1)
            
        self.avg_force = self.total_force/10.
        return self.avg_force
   
if __name__ == "__main__":
    thing = CurrentSensor()
    while True:
        print(thing.avg_force)
