from tkinter import *
from tkinter import ttk
import threading
import sys
from tkinter import messagebox

from web_part import *
from controllers.controls import Controls
from controllers.auto_control import AutoControl
from controllers.control_lr import ControlsLR
from controllers.control_ud import ControlsUD
from controllers.control_ud_c import ControlsUDC
from controllers.control_solenoid import ControlSolenoid


class Crane:
    controls = Controls()
    auto_control = AutoControl()
    controls_solenoid = ControlSolenoid()
    controls_lr = ControlsLR()
    controls_ud = ControlsUD()
    controls_ud_c = ControlsUDC()
    root = Tk()

    t_of_return_to_start_position_methods = (controls_solenoid.return_to_start_position,
                                             controls_ud_c.return_to_start_position(),
                                             controls_ud.return_to_start_position(),
                                             controls_lr.return_to_start_position())

    def __init__(self):
        self.btn_left = ttk.Button(self.root, text='Left', command=self.controls_lr.do_left())
        self.btn_right = ttk.Button(self.root, text='Right', command=self.controls_lr.do_right())
        self.btn_up = ttk.Button(self.root, text='Up', command=self.controls_ud.do_up())
        self.btn_down = ttk.Button(self.root, text='Down', command=self.controls_ud.do_down())
        self.btn_up_cargo = ttk.Button(self.root, text='Up cargo', command=self.controls_ud_c.do_up_cargo())
        self.btn_down_cargo = ttk.Button(self.root, text='Down cargo', command=self.controls_ud_c.do_down_cargo())
        self.btn_solenoid_on = ttk.Button(self.root, text='Solenoid ON', command=self.controls_solenoid.solenoid_on())
        self.btn_solenoid_off = ttk.Button(self.root, text='Solenoid OFF', command=self.controls_solenoid.solenoid_off())
        self.btn_auto = ttk.Button(self.root, text='AUTO', command=self.auto_control.auto_control())
        self.btn_return = ttk.Button(self.root, text='RETURN', command=self.t_of_return_to_start_position_methods)

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
            self.controls_solenoid.return_to_start_position()
            self.controls_lr.return_to_start_position()
            self.controls_ud_c.return_to_start_position()
            self.controls_ud.return_to_start_position()
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


if __name__ == "__main__":
    crane = Crane()
    crane.run_gui()
