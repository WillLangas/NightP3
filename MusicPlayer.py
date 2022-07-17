from pygame import mixer
import os

pygame.init()
pygame.mixer.init()
volume = 0.5

def load_music(title):
    mixer.music.load(title)

def play_music():
    mixer.music.play()

def pause_music():
    mixer.music.pause()

def unpause_music():
    mixer.music.unpause()

def set_volume(direction):
    if direction = "up":
        volume += 0.1
    elif direction = "down":
        volume -= 0.1

    mixer.music.set_volume(volume)