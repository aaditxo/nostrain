import tkinter as tk
from tkinter import messagebox
import time
import winsound
import random

#edit 'actions' to change excercises
#edit 'sleepTime' to change interval between breaks, in seconds

def Mbox(title, text):
    root = tk.Tk()
    root.withdraw()
    return messagebox.showinfo(title=title, message=text)

sleepTime = 1200
actions = ["Perform Wrist stretches",
        "Perform Neck stretches",
        "Go for a plank",
        "Get a snack",
        "Take a stroll",
        "Do Some Eye Excercises"]
tempactions = list(actions)

while 1:
    winsound.Beep(3000,1000)
    length = len(tempactions)-1
    num = random.randint(0, length)
    message = tempactions[num]
    tempactions.pop(num)
    if len(tempactions) == 0:
        tempactions = list(actions)
    Mbox('Take a Break!', message)
    time.sleep(sleepTime)
