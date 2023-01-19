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
    for p in (player1, player2, player3, player4):
        if p:
            p.draw(win)
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
    winn=[]
    while run:
        clock.tick(60)
        p2 = n.send(p)
        p3 = n.send(p2)
        p4 = n.send(p3)
        #print(p,p2,p3,p4)
        #p = n.send (p4)
        winn=[pl for pl in[p, p2, p3, p4] if pl!=None and pl.winner]
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
        if p and p.start_flag or p2 and p2.start_flag or p3 and p3.start_flag or p4 and p4.start_flag:
            p.move()
            p.start_flag=True
            if winn: 
                p.start_flag=False
                win.fill((0,0,0))
                continue
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
            if winn:
                l=list(np.argwhere(n.m==1))
                l=np.array([l[i] for i in np.random.choice(len(l),1)])
                p.x,p.y=l[0]*25
                wt=font.render(f'El ganador es: {winn[0].desc} ', True, (255,255,255))
                win.blit(wt, (100,50))
            win.blit(img, (100,385))
        redrawWindow(p, p2, p3,p4)
            

main()
