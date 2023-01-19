import socket
from _thread import *
import sys

servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

HOST = socket.gethostname()


PORT = 5555

IP_SERVER = socket.gethostbyname(HOST)
print(HOST, IP_SERVER)

try:
    servidor.bind((IP_SERVER, PORT))
except socket.error as e:
    print(str(e))

servidor.listen()
print(f"Esperando conexión en {HOST} con la ip {IP_SERVER}")

# crear hilo
def hilo_cliente(conexion):
    conexion.send(str.encode('1'))


while True:
    conexion,direccion = servidor.accept()
    print("conectado : ",direccion)

    start_new_thread(hilo_cliente,(conexion,))
