from multiprocessing import Event
import pygame
pygame.init()
WHITE=(255, 255, 255)
RED=(255, 0, 0)
size=width, height=(500, 500)
screen=pygame.display.set_mode(size)
clock=pygame.time.Clock()
x=100
y=100
dx=0
dy=0
speed=20
done=False
while not done:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            done=True
        if event.type==pygame.KEYDOWN and event.key==pygame.K_UP:
            dx=0
            dy=-1*speed
        if event.type==pygame.KEYDOWN and event.key==pygame.K_DOWN:
            dx=0
            dy=1*speed
        if event.type==pygame.KEYDOWN and event.key==pygame.K_LEFT:
            dx=-1*speed
            dy=0
        if event.type==pygame.KEYDOWN and event.key==pygame.K_RIGHT:
            dx=1*speed
            dy=0
    screen.fill(WHITE)
    x+=dx
    y+=dy
    if x>width-50 or x<0:
        dx=-1*dx
    if y>height-50 or y<0:
        dy=-1*dy
    pygame.draw.ellipse(screen, RED, [x,y,50,50])
    clock.tick(30)
    pygame.display.update()