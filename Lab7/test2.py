import pygame
pygame.init()
screen=pygame.display.set_mode((400, 400))
pygame.mixer.music.load('1.mp3')
pygame.mixer.music.play()
SONG_END=pygame.USEREVENT+1
done=False
while not done:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            done =True
        if event.type==SONG_END:
            print("the song ended")
    screen.fill((255,255,255))
    pygame.display.flip()
pygame.quit()