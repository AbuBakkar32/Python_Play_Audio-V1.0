import pygame
from time import sleep

pygame.mixer.init()
pygame.mixer.music.load(open("demo.mp3","rb"))
pygame.mixer.music.play()
while pygame.mixer.music.get_busy():
    print("Playing..")

print("End Program")