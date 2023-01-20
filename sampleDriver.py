class Sim_Driver:
    def __init__(self):
        print("Starting Test Program up!")

    def neutral(self,time_elapse=5):
        print("Going neutral")

    def right(self,power=10,time_elapse=5):
        print(f"Going right at {power}% power")
        

    def left(self,power=10,time_elapse=5):
        print(f"Going left at {power}% power")

    def cleanup(self):
        print("Stopping and cleaning up")