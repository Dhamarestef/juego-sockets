import pygame
from networkj import Network
from player import Player
import numpy as np
from scipy import ndimage

width = 775
height = 775
pygame.font.init()
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Client")
win.fill((0,0,0))
font = pygame.font.Font('freesansbold.ttf', 24)
img = font.render('Presiona enter para comenzar', True, (255,255,255))
#maze=pygame.surfarray.make_surface(np.ones((width,height)))
def redrawWindow(player1, player2, player3, player4):
    player1.draw(win)
    player2.draw(win)
    player3.draw(win)
    player4.draw(win)
    pygame.display.update()

def gscale(m):
    mt=np.ones((width,height))
    for i in range(31):
        for j in range(31):
            I=i*25
            J=j*25
            mt[I:I+25,J:J+25]=m[i,j]
    return mt



def main():
    run = True
    n = Network()
    p = n.getP()
    maze = pygame.surfarray.make_surface(gscale(n.m))
    clock = pygame.time.Clock()
    w,h=p.width,p.height
    while run:
        clock.tick(60)
        p2 = n.send(p)
        p3 = n.send(p2)
        p4 = n.send(p3)
        #print(p,p2,p3,p4)
        #p = n.send (p4)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
        if p.start_flag or p2.start_flag or p3.start_flag or p4.start_flag:
            p.move()
            p.start_flag=True
            #if True in [p.winner, p2.winner or p3.winner or p4.winner]:
            #p.start_flag=False
            #win.fill((0,0,0))
            #continue
            esq=[maze.get_at((p.x+w,p.y)),maze.get_at((p.x,p.y)),
                   maze.get_at((p.x,p.y+h)),maze.get_at((p.x+w,p.y+h))]
            if (0,0,0,255) in esq:
                if (0,0,0,255)==maze.get_at((p.x+w,p.y)):
                    p.x-=p.vel
                if (0,0,0,255)==maze.get_at((p.x,p.y)):
                    p.x+=p.vel
                    p.y+=p.vel
                if (0,0,0,255)==maze.get_at((p.x,p.y+h)):
                    p.y-=p.vel
                if (0,0,0,255)==maze.get_at((p.x+w,p.y+h)):
                    p.y-=p.vel
                    p.x-=p.vel
            if (255,255,255,255) in esq:
                p.winner=True
            win.blit(maze, (0, 0))
        else:
            p.start()
            win.blit(img, (100,385))
        redrawWindow(p, p2, p3,p4)
            

main()
