from tkinter import *
from tkinter import ttk
from time import sleep
import RPi.GPIO as gpio
from tkinter import messagebox
from math import fabs
from web_part import *

root = Tk()
root.title("Crane")

gpio.setmode(gpio.BOARD) 
gpio.setup(29, gpio.OUT) 
gpio.setup(31, gpio.OUT) 
gpio.setup(33, gpio.OUT)  
gpio.setup(35, gpio.OUT)
gpio.setup(36, gpio.OUT)#solenoid
gpio.setup(37, gpio.OUT)
gpio.setup(38, gpio.OUT)#all on
gpio.setup(40, gpio.OUT)


#preparing board
gpio.output(38, 0)#all on
gpio.output(36, 1)#solenoid
gpio.output(29, 1)
gpio.output(31, 0)
gpio.output(33, 1)
gpio.output(35, 0)
gpio.output(37, 1)
gpio.output(40, 0)

#limitations and runing parametrs
lr = 10
lr_min = 1
lr_max = 10

ud = 7
ud_min = 1
ud_max = 7

udG = 5
udG_min = 1
udG_max = 5

differance = fabs(ud - udG)

#control functions
def left():
    gpio.output(29, 0)
    gpio.output(31, 0)
    sleep(0.1)	
    gpio.output(29, 1)
    gpio.output(31, 0)

def right():
    gpio.output(31, 1)
    gpio.output(29, 1)
    sleep(0.1)	
    gpio.output(31, 1)
    gpio.output(29, 0)
    
def up():
    gpio.output(33, 0)
    gpio.output(35, 0)
    sleep(0.34)	
    gpio.output(33, 1)
    gpio.output(35, 0)
    
def down():
    gpio.output(35, 1)
    gpio.output(33, 1)
    sleep(0.3)	
    gpio.output(35, 1)
    gpio.output(33, 0)
    
def downG():
    gpio.output(37, 0)
    gpio.output(40, 0)
    sleep(0.3)	
    gpio.output(37, 1)
    gpio.output(40, 0)
    
def upG():
    gpio.output(40, 1)
    gpio.output(37, 1)
    sleep(0.45)	
    gpio.output(40, 1)
    gpio.output(37, 0)

def solenoidON():
    gpio.output(36, 0)
    
def solenoidOFF():
    gpio.output(36, 1)


#buttons functions
def left_prov():
    global lr, lr_min, lr_max
    if lr >= lr_min and lr < lr_max:
        lr += 1
        left()
    else:
        messagebox.showinfo("Cran ERROR", "Minimum is over!!!")

def right_prov():
    global lr, lr_min, lr_max
    if lr > lr_min and lr <= lr_max:
        lr -= 1
        right()
    else:
        messagebox.showinfo("Cran ERROR", "Maximum is over!!!")



def up_prov():
    global ud, ud_min, ud_max, udG, differance
    if ud >= ud_min and ud < ud_max:
        #check of positions
        if ud == udG + differance:
            upG_prov()
        ud += 1
        up()
    else:
        messagebox.showinfo("Cran ERROR", "Minimum is over!!!")

def down_prov():
    global ud, ud_min, ud_max
    if ud > ud_min and ud <= ud_max:
        ud -= 1
        down()
    else:
        messagebox.showinfo("Cran ERROR", "Maximum is over!!!")



def upG_prov():
    global udG, udG_min, udG_max
    if udG >= udG_min and udG < udG_max:
        udG += 1
        upG()
    else:
        messagebox.showinfo("Cran ERROR", "Minimum is over!!!")

def downG_prov():
    global udG, udG_min, udG_max, ud, differance
    if udG > udG_min and udG <= udG_max:
        #check of positions
        if ud == udG + differance:
            down_prov()
        udG -= 1
        downG()
    else:
        messagebox.showinfo("Cran ERROR", "Maximum is over!!!")

#return to the start position
def returning():
    global lr, lr_min, ud, ud_max, udG, ud_max
    solenoidOFF()
    while (lr < lr_max):
        lr +=1
        left()
        sleep(0.5)
    sleep(0.5)
    while (udG < udG_max):
        udG += 1
        upG()
        sleep(0.2)
    while (ud < ud_max):
        ud += 1
        up()
        sleep(0.2)

def auto():
    btn_left.config(state = DISABLED)
    btn_left.grid(row=0,column=0)
    
    btn_right.config(state = DISABLED)
    btn_right.grid(row=1,column=0)
    
    btn_up.config(state = DISABLED)
    btn_up.grid(row=0,column=1)
    
    btn_down.config(state = DISABLED)
    btn_down.grid(row=1,column=1)

    btn_upG.config(state = DISABLED)
    btn_upG.grid(row=0,column=2)
    
    btn_downG.config(state = DISABLED)
    btn_downG.grid(row=1,column=2)
    
    btn_solenoidON.config(state = DISABLED)
    btn_solenoidON.grid(row=0,column=3)

    btn_solenoidOFF.config(state = DISABLED)
    btn_solenoidOFF.grid(row=1,column=3)
    
    commands = []
    file = open('auto.txt', 'r')
    for line in file:
        commands.append(line)
    file.close()
    
    elements = len(commands)
    print("\nElements: ", elements)

    i = 0
    sleep_time = 0
    while i != elements:
        comand = commands[i]
        str(comand)
        if comand == "left" or comand == "left\n":
            left_prov()
        elif comand == "right" or comand == "right\n":
            right_prov()
        elif comand == "up" or comand == "up\n":
            up_prov()
        elif comand == "down" or comand == "down\n":
            down_prov()
        elif comand == "upG" or comand == "upG\n":
            upG_prov()
        elif comand == "downG" or comand == "downG\n":
            downG_prov()
        elif comand == "solenoidON" or comand == "solenoidON\n":
            solenoidON()
        elif comand == "solenoidOFF" or comand == "solenoidOFF\n":
            solenoidOFF()
        else:
            try:
                sleep_time = float(comand)
                sleep(sleep_time)
            except ValueError:
                print("Check you file")
                break
        i += 1
        sleep(0.5)

    btn_left.config(state = NORMAL)
    btn_left.grid(row=0,column=0)
    
    btn_right.config(state = NORMAL)
    btn_right.grid(row=1,column=0)
    
    btn_up.config(state = NORMAL)
    btn_up.grid(row=0,column=1)
    
    btn_down.config(state = NORMAL)
    btn_down.grid(row=1,column=1)

    btn_upG.config(state = NORMAL)
    btn_upG.grid(row=0,column=2)
    
    btn_downG.config(state = NORMAL)
    btn_downG.grid(row=1,column=2)
    
    btn_solenoidON.config(state = NORMAL)
    btn_solenoidON.grid(row=0,column=3)

    btn_solenoidOFF.config(state = NORMAL)
    btn_solenoidOFF.grid(row=1,column=3)

import sys
def on_closing():
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        returning()
        gpio.cleanup()
        root.destroy()
        close_web()
        sys.exit()

#GUI
def run_GUI():
    global btn_left, btn_right, btn_up, btn_down, btn_upG, btn_downG, btn_solenoidON, btn_solenoidOFF
    btn_left = ttk.Button(root, text= 'Left', command = left_prov)
    btn_left.grid(row=0,column=0)
    btn_right = ttk.Button(root, text= 'Right', command = right_prov)
    btn_right.grid(row=1,column=0)
    btn_up = ttk.Button(root, text= 'Up', command = up_prov)
    btn_up.grid(row=0,column=1)
    btn_down = ttk.Button(root, text= 'Down', command = down_prov)
    btn_down.grid(row=1,column=1)
    btn_upG = ttk.Button(root, text= 'UpG', command = upG_prov)
    btn_upG.grid(row=0,column=2)
    btn_downG = ttk.Button(root, text= 'DownG', command = downG_prov)
    btn_downG.grid(row=1,column=2)
    btn_solenoidON = ttk.Button(root, text= 'SoleniodON', command = solenoidON)
    btn_solenoidON.grid(row=0,column=3)
    btn_solenoidOFF = ttk.Button(root, text= 'SoleniodOFF', command = solenoidOFF)
    btn_solenoidOFF.grid(row=1,column=3)
    btn_auto = ttk.Button(root, text= 'AUTO', command = auto)
    btn_auto.grid(row=0,column=4)
    btn_auto = ttk.Button(root, text= 'RETURN', command = returning)
    btn_auto.grid(row=1,column=4)
    #go_web()

import threading

vid_tr = threading.Thread(target = go_web)
vid_tr.start()

run_GUI()

root.protocol("WM_DELETE_WINDOW", on_closing)
root.mainloop()