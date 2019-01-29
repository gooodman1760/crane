import RPi.GPIO as gpio
from math import fabs
from tkinter import messagebox

from const_module import const_pin, const_position
from controllers.auto_control import AutoControl


class Controls:
    # It exists for check if cargo is under the jib
    difference = fabs(const_position.UD - const_position.UD_C)
    auto_control = AutoControl()

    def prepare_board(self):
        gpio.setmode(gpio.BOARD)
        # left move
        gpio.setup(const_pin.LEFT_PIN, gpio.OUT)
        # right move
        gpio.setup(const_pin.RIGHT_PIN, gpio.OUT)
        # up
        gpio.setup(const_pin.UP_PIN, gpio.OUT)
        # down
        gpio.setup(const_pin.DOWN_PIN, gpio.OUT)
        # up cargo
        gpio.setup(const_pin.UP_CARGO_PIN, gpio.OUT)
        # down cargo
        gpio.setup(const_pin.DOWN_CARGO_PIN, gpio.OUT)
        # solenoid
        gpio.setup(const_pin.SOLENOID_PIN, gpio.OUT)

    def minimum_check(self, val, val_min, val_max):
        if val_min <= val < val_max:
            val += 1
            return True
        else:
            messagebox.showinfo("Crane ERROR", "Minimum is over!!!")
            return False

    def maximum_check(self, val, val_min, val_max):
        if val_min < val <= val_max:
            val -= 1
            return True
        else:
            messagebox.showinfo("Crane ERROR", "Maximum is over!!!")
            return False

    def return_to_start_position(self):
        """ """

    def cleanup_board(self):
        gpio.cleanup()

    def do_auto(self):
        self.auto_control.auto_control()
