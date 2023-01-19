import socket

class Network:
    def __init__(self) -> None:
        self.cliente=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.servidor='localhost'#ip del servidor
        self.puerto=5555
        self.direccion=(self.servidor,self.puerto)
        self.id=self.conectar()

    def conectar(self):
        self.cliente.connect(self.direccion)
        return self.cliente.recv(2048).decode()

    def enviar(self,datos):
        try:
            self.cliente.send(str.encode(datos))
            respuesta=self.cliente.recv(2048).decode()
            return respuesta
        except socket.error as e:
            return str(e)
