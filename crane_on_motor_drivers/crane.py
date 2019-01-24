from tkinter import *
from tkinter import ttk
import threading
import sys
from tkinter import messagebox

from web_part import *
from controls import Controls


class Crane:
    controls = Controls()
    root = Tk()

    btn_left = ttk.Button(root, text='Left', command=Controls().do_left())
    btn_right = ttk.Button(root, text='Right', command=Controls().do_right())
    btn_up = ttk.Button(root, text='Up', command=Controls().do_up())
    btn_down = ttk.Button(root, text='Down', command=Controls().do_down())
    btn_up_cargo = ttk.Button(root, text='Up cargo', command=Controls().do_up_cargo())
    btn_down_cargo = ttk.Button(root, text='Down cargo', command=Controls().do_down_cargo())
    btn_solenoid_on = ttk.Button(root, text='Solenoid ON', command=Controls().solenoid_on())
    btn_solenoid_off = ttk.Button(root, text='Solenoid OFF', command=Controls().solenoid_off())
    btn_auto = ttk.Button(root, text='AUTO', command=Controls().auto_control())
    btn_return = ttk.Button(root, text='RETURN', command=Controls().return_to_start_position())

    def config_buttons(self, state_of_button):
        """
        Method for enable and disable buttons
        """
        self.btn_left.config(state=state_of_button)
        self.btn_left.grid(row=0, column=0)

        self.btn_right.config(state=state_of_button)
        self.btn_right.grid(row=1, column=0)

        self.btn_up.config(state=state_of_button)
        self.btn_up.grid(row=0, column=1)

        self.btn_down.config(state=state_of_button)
        self.btn_down.grid(row=1, column=1)

        self.btn_up_cargo.config(state=state_of_button)
        self.btn_up_cargo.grid(row=0, column=2)

        self.btn_down_cargo.config(state=state_of_button)
        self.btn_down_cargo.grid(row=1, column=2)

        self.btn_solenoid_on.config(state=state_of_button)
        self.btn_solenoid_on.grid(row=0, column=3)

        self.btn_solenoid_off.config(state=state_of_button)
        self.btn_solenoid_off.grid(row=1, column=3)

    def auto(self):
        """
        Automatic mode method
        """
        # disable buttons
        state_of_button = DISABLED
        self.config_buttons(state_of_button)

        self.controls.auto_control()

        # enable buttons
        state_of_button = NORMAL
        self.config_buttons(state_of_button)

    def on_closing(self):
        """
        Closing method
        """
        if messagebox.askokcancel("Quit", "Do you want to quit?"):
            # model return to start position

            self.controls.return_to_start_position()
            # cleanup pins for normal work after closing program
            self.controls.cleanup_board()
            # close interface of managing model
            self.root.destroy()
            # stop video translation
            close_web()
            # close program window
            sys.exit()

    def run_gui(self):
        """
        Run GUI
        """
        # create features for work with GUI
        self.root.title("Crane")
        self.btn_left.grid(row=0, column=0)
        self.btn_right.grid(row=1, column=0)
        self.btn_up.grid(row=0, column=1)
        self.btn_down.grid(row=1, column=1)
        self.btn_up_cargo.grid(row=0, column=2)
        self.btn_down_cargo.grid(row=1, column=2)
        self.btn_solenoid_on.grid(row=0, column=3)
        self.btn_solenoid_off.grid(row=1, column=3)
        self.btn_auto.grid(row=0, column=4)
        self.btn_auto.grid(row=1, column=4)

        # create a thread for video translation
        vid_tr = threading.Thread(target=go_web)
        vid_tr.start()


Crane().run_gui()
