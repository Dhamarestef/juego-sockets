import socket
#from _thread import *
from player import Player
import pickle
from maze import gen_maze
server = "127.0.0.1"
port = 5555
import threading
import numpy as np

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((server, port))
except socket.error as e:
    print(e)

s.listen(4)
print("Waiting for a connection, Server Started")


conn_list=[]

maze=gen_maze()
l=list(np.argwhere(maze==1))
l=np.array([l[i] for i in np.random.choice(len(l),5)])
maze[l[0][0],l[0][1]]=255
l=25*l

print(l)

players = [Player(l[1][0],l[1][1],20,20,(255,0,0), 'Rojo'),
           Player(l[2][0],l[2][1], 20,20, (0,255,255),'Cyan'),
           Player(l[3][0],l[3][1], 20,20, (0,255,0),'Verde'),
           Player(l[4][0],l[4][1], 20,20, (255,255,0),'Amarillo')]



ginfo=[maze,False,""]
active_players=set()
conns=[]

def threaded_client(conn, player):
    global conns
    global maze
    conns.append(conn)
    conn.send(pickle.dumps((players[player],maze)))
    #conn.send((players[player],maze).encode())
    reply = ""
    global active_players
    active_players.add(player)
    while True:
        #print(player, active_players)
        try:
            data = pickle.loads(conn.recv(4096)) #numero de bits que permite el socket y pickle load hace cuentas binarias del socket
            
            players[player] = data

            if not data:
                print("Disconnected")
                break
            else:
                if players[player].winner:
                    #for c in conns:
                    for k in active_players:
                        players[k].start=False
                        conn.sendall(pickle.dumps(players[k]))
                for k in active_players:
                    reply = players[k]
                    print("Received: ", data)
                    print("Sending : ", reply)
                    conn.sendall(pickle.dumps(reply))
        except:
            break
    print("Lost connection")
    active_players.remove(player)
    conn.close()

currentPlayer = 0

threads=[]
while True:
    conn, addr = s.accept()
    print("Connected to", addr)
    x=threading.Thread(target=threaded_client, args=(conn, currentPlayer))
    x.start()
    currentPlayer += 1

