from pygame import mixer
import pygame
import os
import eyed3

pygame.mixer.init()
volume = 0.5

# State can have three values: Open, Paused, Playing
state = "Open"

def load_music(filename):
    mixer.music.load(filename)
    
    audiofile = eyed3.load(filename)
    artist = audiofile.tag.artist
    title = audiofile.tag.title
    return title, artist

def play_music(state):
    if state == "Open":
        try:
            mixer.music.play()
        except:
            print("PLEASE LOAD A SONG")        
    elif state == "Paused":
        unpause_music()
    
    return "Playing"

def pause_music():
    mixer.music.pause()
    return "Paused"

def unpause_music():
    mixer.music.unpause()
    return "Playing"

def set_volume(direction):
    if direction == "up":
        volume += 0.1
    elif direction == "down":
        volume -= 0.1

    mixer.music.set_volume(volume)