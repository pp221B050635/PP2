import pygame
import os
pygame.init()
size=(500, 500)
screen=pygame.display.set_mode(size)
_image_library={}
def get_image(path):
    global _image_library
    image=_image_library.get(path)
    if image is None:
        path=path.replace('/', os.sep).replace('\\', os.sep)
        image=pygame.image.load(path)
        _image_library[path]=image
    return image
pygame.mixer.music.load('1.mp3')
pygame.mixer.music.play()
done=False
while not done:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            done=True
        screen.blit(get_image('1.jpg'), (500,500))
        if event.type==pygame.KEYDOWN and event.key==pygame.K_UP:
            pygame.mixer.music.pause()
        if event.type==pygame.KEYDOWN and event.key==pygame.K_DOWN:
            pygame.mixer.music.unpause()
        if event.type==pygame.KEYDOWN and event.key==pygame.K_RIGHT:
            pygame.mixer.music.stop()
            pygame.mixer.music.load('2.mp3')
            pygame.mixer.music.play()
        if event.type==pygame.KEYDOWN and event.key==pygame.K_LEFT:
            pygame.mixer.music.stop()
            pygame.mixer.music.load('1.mp3')
            pygame.mixer.music.play()
    
    pygame.display.flip()
pygame.quit()