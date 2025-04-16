from tkinter import *
from PIL import Image, ImageTk, ImageSequence
import time
import pygame
from pygame import mixer

mixer.init()

root = Tk()
root.geometry("1000x500")


def play_gif():
    root.lift()
    root.attributes("-topmost", True)
    gif_path = "snap.gif"  # Enter the path to the GIF file
    img = Image.open(gif_path)
    lbl = Label(root)
    lbl.place(x=0, y=0)
    i = 0
    music_path = "ip.mp3"  # Enter the path to the music file
    mixer.music.load(music_path)
    mixer.music.play()


    duration_per_frame = 4  # Duration to display each frame in seconds
    start_time = time.time()
    for img_seq in ImageSequence.Iterator(img):
        img_resized = img_seq.resize((1000, 500))
        img_tk = ImageTk.PhotoImage(img_resized)
        lbl.config(image=img_tk)
        root.update()
        elapsed_time = time.time() - start_time
        if elapsed_time >= duration_per_frame:
            break
        time.sleep(0.05)
    mixer.music.stop()

    root.destroy()


# play_gif()
# root.mainloop()




