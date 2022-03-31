import pygame 
pygame.init()
size=(400,300)
screen=pygame.display.set_mode(size)
screen.fill((255,255,255))
pygame.draw.rect(screen, (100,100,100), (100,100, 100,100))
done=False
while not done:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            done=True
    pygame.display.flip()
pygame.quit()