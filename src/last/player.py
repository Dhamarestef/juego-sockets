import pygame

class Player():
    def __init__(self, x, y, width, height, color, desc):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.rect = (x,y,width,height)
        self.vel = 3
        self.start_flag=False
        self.winner=False
        self.desc=desc

    def  __str__(self):
        return f"x,y:{self.x},{self.y}, color:{str(self.color)} winner? {self.winner}"
        
    def draw(self, win):
        pygame.draw.rect(win, self.color, self.rect)

    def start(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RETURN]:
            self.winner=False
            self.start_flag=True
            

    def move(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            self.x -= self.vel

        if keys[pygame.K_RIGHT]:
            self.x += self.vel

        if keys[pygame.K_UP]:
            self.y -= self.vel

        if keys[pygame.K_DOWN]:
            self.y += self.vel

        self.update()

    def update(self):
        self.rect = (self.x, self.y, self.width, self.height)
