from tkinter import *
from tkinter import ttk
import threading
import sys
from time import sleep
import RPi.GPIO as gpio
from tkinter import messagebox
from math import fabs


from web_part import *


root = Tk()
root.title("Crane")

left_pin = 29
right_pin = 31
up_pin = 33
down_pin = 35
up_cargo_pin = 36
down_cargo_pin = 37
solenoid_pin = 40


gpio.setmode(gpio.BOARD)
# left move
gpio.setup(left_pin, gpio.OUT)
# right move
gpio.setup(right_pin, gpio.OUT)
# up
gpio.setup(up_pin, gpio.OUT)
# down
gpio.setup(down_pin, gpio.OUT)
# up cargo
gpio.setup(up_cargo_pin, gpio.OUT)
# down cargo
gpio.setup(down_cargo_pin, gpio.OUT)
# solenoid
gpio.setup(solenoid_pin, gpio.OUT)

# limitations and running parameters
# lr it's left_right
lr = 10
lr_min = 1
lr_max = 10

# ud it's up_down
ud = 7
ud_min = 1
ud_max = 7

# ud_c it's up_down_cargo
ud_c = 5
ud_c_min = 1
ud_c_max = 5

difference = fabs(ud - ud_c)


# control functions
def left():
    gpio.output(left_pin, 1)
    sleep(0.1)	
    gpio.output(left_pin, 0)


def right():
    gpio.output(right_pin, 1)
    sleep(0.1)	
    gpio.output(right_pin, 0)


def up():
    gpio.output(up_pin, 1)
    sleep(0.34)
    gpio.output(up_pin, 0)


def down():
    gpio.output(down_pin, 1)
    sleep(0.3)
    gpio.output(down_pin, 0)


def down_cargo():
    gpio.output(down_cargo_pin, 1)
    sleep(0.3)
    gpio.output(down_cargo_pin, 0)


def up_cargo():
    gpio.output(up_cargo_pin, 1)
    sleep(0.45)
    gpio.output(up_cargo_pin, 0)


def solenoid_on():
    gpio.output(solenoid_pin, 1)


def solenoid_off():
    gpio.output(solenoid_pin, 0)


# buttons functions
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
    global ud, ud_min, ud_max, ud_c, difference
    if ud >= ud_min and ud < ud_max:
        # check of positions
        if ud == ud_c + difference:
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
    global ud_c, ud_c_min, ud_c_max
    if ud_c >= ud_c_min and ud_c < ud_c_max:
        ud_c += 1
        up_cargo()
    else:
        messagebox.showinfo("Cran ERROR", "Minimum is over!!!")


def downG_prov():
    global ud_c, ud_c_min, ud_c_max, ud, difference
    if ud_c > ud_c_min and ud_c <= ud_c_max:
        #check of positions
        if ud == ud_c + difference:
            down_prov()
        ud_c -= 1
        down_cargo()
    else:
        messagebox.showinfo("Cran ERROR", "Maximum is over!!!")


# return to the start position
def returning():
    global lr, lr_min, ud, ud_max, ud_c, ud_max
    solenoid_off()
    while (lr < lr_max):
        lr += 1
        left()
        sleep(0.5)
    sleep(0.5)
    while (ud_c < ud_c_max):
        ud_c += 1
        up_cargo()
        sleep(0.2)
    while (ud < ud_max):
        ud += 1
        up()
        sleep(0.2)


def auto():
    btn_left.config(state=DISABLED)
    btn_left.grid(row=0, column=0)
    
    btn_right.config(state=DISABLED)
    btn_right.grid(row=1, column=0)
    
    btn_up.config(state=DISABLED)
    btn_up.grid(row=0, column=1)
    
    btn_down.config(state=DISABLED)
    btn_down.grid(row=1, column=1)

    btn_up_cargo.config(state=DISABLED)
    btn_up_cargo.grid(row=0, column=2)
    
    btn_down_cargo.config(state=DISABLED)
    btn_down_cargo.grid(row=1, column=2)
    
    btn_solenoid_on.config(state=DISABLED)
    btn_solenoid_on.grid(row=0, column=3)

    btn_solenoid_off.config(state=DISABLED)
    btn_solenoid_off.grid(row=1, column=3)
    
    commands = []
    file = open('auto.txt', 'r')
    for line in file:
        commands.append(line)
    file.close()
    
    elements = len(commands)
    print("\nElements: ", elements)

    i = 0
    # sleep_time = 0
    while i != elements:
        command = commands[i]
        str(command)
        if command == "left" or command == "left\n":
            left_prov()
        elif command == "right" or command == "right\n":
            right_prov()
        elif command == "up" or command == "up\n":
            up_prov()
        elif command == "down" or command == "down\n":
            down_prov()
        elif command == "up_cargo" or command == "up_cargo\n":
            upG_prov()
        elif command == "down_cargo" or command == "down_cargo\n":
            downG_prov()
        elif command == "s_on" or command == "s_on\n":
            solenoid_on()
        elif command == "s_off" or command == "s_off\n":
            solenoid_off()
        else:
            try:
                sleep_time = float(command)
                sleep(sleep_time)
            except ValueError:
                print("Check you file")
                break
        i += 1
        sleep(0.5)

    btn_left.config(state=NORMAL)
    btn_left.grid(row=0, column=0)
    
    btn_right.config(state=NORMAL)
    btn_right.grid(row=1, column=0)
    
    btn_up.config(state=NORMAL)
    btn_up.grid(row=0, column=1)
    
    btn_down.config(state=NORMAL)
    btn_down.grid(row=1, column=1)

    btn_up_cargo.config(state=NORMAL)
    btn_up_cargo.grid(row=0, column=2)
    
    btn_down_cargo.config(state=NORMAL)
    btn_down_cargo.grid(row=1, column=2)
    
    btn_solenoid_on.config(state=NORMAL)
    btn_solenoid_on.grid(row=0, column=3)

    btn_solenoid_off.config(state=NORMAL)
    btn_solenoid_off.grid(row=1, column=3)


def on_closing():
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        returning()
        gpio.cleanup()
        root.destroy()
        close_web()
        sys.exit()


# GUI
def run_gui():
    global btn_left, btn_right, btn_up, btn_down, btn_up_cargo, btn_down_cargo, btn_solenoid_on, btn_solenoid_off
    btn_left = ttk.Button(root, text='Left', command=left_prov)
    btn_left.grid(row=0, column=0)
    btn_right = ttk.Button(root, text='Right', command=right_prov)
    btn_right.grid(row=1, column=0)
    btn_up = ttk.Button(root, text='Up', command=up_prov)
    btn_up.grid(row=0, column=1)
    btn_down = ttk.Button(root, text='Down', command=down_prov)
    btn_down.grid(row=1, column=1)
    btn_up_cargo = ttk.Button(root, text='UpG', command=upG_prov)
    btn_up_cargo.grid(row=0, column=2)
    btn_down_cargo = ttk.Button(root, text='DownG', command=downG_prov)
    btn_down_cargo.grid(row=1, column=2)
    btn_solenoid_on = ttk.Button(root, text='Solenoid ON', command=solenoid_on)
    btn_solenoid_on.grid(row=0, column=3)
    btn_solenoid_off = ttk.Button(root, text='Solenoid OFF', command=solenoid_off)
    btn_solenoid_off.grid(row=1, column=3)
    btn_auto = ttk.Button(root, text='AUTO', command=auto)
    btn_auto.grid(row=0, column=4)
    btn_auto = ttk.Button(root, text='RETURN', command=returning)
    btn_auto.grid(row=1, column=4)


vid_tr = threading.Thread(target=go_web)
vid_tr.start()

run_gui()

root.protocol("WM_DELETE_WINDOW", on_closing)
root.mainloop()
