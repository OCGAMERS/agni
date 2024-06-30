import tkinter as tk
import cv2
from PIL import Image, ImageTk
import pygame
from pygame import mixer

mixer.init()

def play_intro():
    
    try:
        # Load audio
        mixer.music.load("bgm_audio.mp3")  # Change the file name to your MP3 audio
        mixer.music.play()
    except pygame.error as e:
        print("Error loading audio:", e)


play_intro()
