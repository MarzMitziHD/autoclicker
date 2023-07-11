# import functions
import mouse
import keyboard
import time
import tkinter as tk
import threading

clicker_running = False
# change stuff to read from *.ini instead from script
left_click_keyboardbind = "["
right_click_keyboardbind = "]"
cliccdelay = 0.1

def left_mouse():
    mouse.click("left")
    time.sleep(cliccdelay)

def right_mouse():
    mouse.click("right")
    time.sleep(cliccdelay)

def mainclicker():
    global left_click_keyboardbind
    global right_click_keyboardbind
    print("Clicker running")
    while True:
        if clicker_running == True and keyboard.is_pressed(left_click_keyboardbind):
            left_mouse()
        if clicker_running == True and keyboard.is_pressed(right_click_keyboardbind):
            right_mouse()



def mainwindow():
    print("Window initializing...")
    window = tk.Tk()
    label1 = tk.Label(text="Hello, world!")
    label1.pack()
    button1 = tk.Button(text="Toggle clicker")
    button1.pack()
    button1.bind("<Button-1>", toggleClickerRunning)
    global label2
    label2 = tk.Label(text="CLICKER: OFF")
    label2.pack()
    label3 = tk.Label(text="\nTori's Autoclicker version 0.1-veryearly")
    label3.pack()
    print("Window loop started")
    window.mainloop()

def toggleClickerRunning(event):
    global clicker_running
    global label2
    if clicker_running == False:
        print("Clicker is now running. Press one of the binds to autoclick.")
        clicker_running = True
        label2["text"] = "CLICKER: ON"
        return
    if clicker_running == True:
        print("Clicker is not running anymore.")
        clicker_running = False
        label2["text"] = "CLICKER: OFF"
        return

x = threading.Thread(target=mainclicker)
x.start()
y = threading.Thread(target=mainwindow)
y.start()