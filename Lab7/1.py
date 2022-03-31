import pygame
import os
pygame.init()
screen=pygame.display.set_mode((800,800))
_image_library={}
def get_image(path):
    global _image_library
    image=_image_library.get(path)
    if image is None:
        path=path.replace('/', os.sep).replace('\\', os.sep)
        image=pygame.image.load(path)
        _image_library[path]=image
    return image
done=False
while not done:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            done=True
    screen.fill((255, 255, 255))
    screen.blit(get_image('clock.png'), (0, 0))
    screen.blit(get_image('lefthand.png'), (256, 300))
    screen.blit(get_image('righthand.png'), (245, 261))
    pygame.display.flip()
pygame.quit()



