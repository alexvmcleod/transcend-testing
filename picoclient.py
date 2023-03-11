#import network
import time
import socket

class Clientthing:
    def __init__(self):
        self.ip0 = "192.168.43.172"
        self.ip1 = "192.168.254.142"

    def make_request(self,type):
        ai = socket.getaddrinfo(self.ip0, 80) # Address of Web Server
        addr = ai[0][-1]
        s = socket.socket() # Open socket
        s.connect(addr)
        if type == "start":
            s.send(type.encode(b"start")) # Send request
            ss=str(s.recv(512)) # Store reply
        elif type == "end":
            s.send(type.encode(b"end")) # Send request
            ss=str(s.recv(512)) # Store reply
        else:
            pass
    
if __name__ == "__main__":
    dt = Clientthing()

    start = time.time()
    print(start)
    print(dt.make_request())
    end = time.time()

    print(end-start)