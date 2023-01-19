import socket
import pickle
import numpy as np

class Network:
    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server = "127.0.0.1"
        self.port = 5555
        self.addr = (self.server, self.port)
        self.p,self.m= self.connect()

    def getP(self):
        return self.p

    def getM(self):
        return self.m

    def connect(self):
        try:
            self.client.connect(self.addr)
            return pickle.loads(self.client.recv(4096))
        except:
            pass

    def send(self, data):
        try:
            self.client.send(pickle.dumps(data))
            #self.client.send(data.encode())
            x=pickle.loads(self.client.recv(4096))
            return x
        except socket.error as e:
            print(e)

