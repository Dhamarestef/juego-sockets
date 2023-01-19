import random
import numpy as np

WIDTH,HEIGHT = 31,31 # celdas de ancho
EMPTY = 1
WALL = 0
NORTH, SOUTH, EAST, WEST = 'n', 's', 'e', 'w'


def printMaze(maze, markX=None, markY=None):
    """Imprimir el laberitno"""
    for y in range(HEIGHT):
        for x in range(WIDTH):
                print(maze[(x, y)], end='')
        print() # Espacio despues de cada fila


def visit(maze, x, y, hasVisited):
    """"Cavar el algoritmo"""
    maze[x, y] = EMPTY # Cavar en la posicion x,y

    while True:
        # Verificar los espacios adjacentes
        # aun no se a visitado la poscición actual
        unvisitedNeighbors = []
        if y > 1 and (x, y - 2) not in hasVisited:
            unvisitedNeighbors.append(NORTH)
        if y < HEIGHT - 2 and (x, y + 2) not in hasVisited:
            unvisitedNeighbors.append(SOUTH)
        if x > 1 and (x - 2, y) not in hasVisited:
            unvisitedNeighbors.append(WEST)
        if x < WIDTH - 2 and (x + 2, y) not in hasVisited:
            unvisitedNeighbors.append(EAST)
        if len(unvisitedNeighbors) == 0:
            # Caso base
            # todos los vecinos ya han sido visitados, hacer backtraking
            return
        else:
            # Caso recursico
            # Seleccionar aleatoriamente un vecino no visitado
            nextIntersection = random.choice(unvisitedNeighbors)

            # despazarse al lugar no visitado

            if nextIntersection == NORTH:
                nextX = x
                nextY = y - 2
                maze[x, y - 1] = EMPTY # Conectar pasillo
            elif nextIntersection == SOUTH:
                nextX = x
                nextY = y + 2
                maze[x, y + 1] = EMPTY # Conectar pasillo
            elif nextIntersection == WEST:
                nextX = x - 2
                nextY = y
                maze[x - 1, y] = EMPTY # Conectar pasillo
            elif nextIntersection == EAST:
                nextX = x + 2
                nextY = y
                maze[x + 1, y] = EMPTY # Conectar pasillo

            hasVisited.append((nextX, nextY)) # Marcar como visitado.
            visit(maze,nextX, nextY,hasVisited) # Visitare recursivamente

from scipy import ndimage

def gen_maze():
    maze = np.zeros((31,31),dtype=np.int8)
    for x in range(WIDTH):
        for y in range(HEIGHT):
            maze[(x, y)] = WALL # Solo muros
    hasVisited = [(1, 1)] # Start by visiting the top-left corner.
    visit(maze,1, 1, hasVisited)
    maze[15,15]=1
    return maze
import matplotlib.pyplot as plt
if __name__=="__main__":
    m=gen_maze()
    m=ndimage.zoom(m, (25, 25))
    print(m)
    #px = 1/plt.rcParams['figure.dpi']
    #fig,ax=plt.subplots(figsize=(775*px,775*px))
    #ax.set_xticks([])
    #ax.set_yticks([])
    #ax.axis('off')
    #ax.imshow(gen_maze(), cmap='binary')
    #plt.tight_layout()
   # .subplots_adjust(top = 1, bottom = 0, right = 1, left = 0, 
   #         hspace = 0, wspace = 0)
    #plt.margins(0,0)
    #plt.gca().xaxis.set_major_locator(plt.NullLocator())
    #plt.gca().yaxis.set_major_locator(plt.NullLocator())
    plt.savefig('x.png')
