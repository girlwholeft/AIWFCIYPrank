from pygame import mixer
import random
import time

file = "aiwfciy.mp3"

def countdown_mariah(t):
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs) 
        time.sleep(1) 
        t -= 1

    song = file
    mixer.init()
    mixer.music.load(song)
    mixer.music.play()

seconds = random.randint(1200, 3600)

while True:
    countdown_mariah(seconds)
