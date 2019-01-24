import RPi.GPIO as gpio
from time import sleep
from math import fabs
from tkinter import messagebox

from const_module import const_pin, const_position


class Controls:
    # It exists for check if cargo is under the jib
    difference = fabs(const_position.UD - const_position.UD_C)

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
        """
        Return to the start position
        """
        self.solenoid_off()
        while const_position.LR < self.lr_max:
            const_position.LR += 1
            self.left()
            sleep(0.5)
        sleep(0.5)
        while const_position.UD_C < self.ud_c_max:
            const_position.UD_C += 1
            self.up_cargo()
            sleep(0.2)
        while const_position.UD < self.ud_max:
            const_position.UD += 1
            self.up()
            sleep(0.2)

    def cleanup_board(self):
        gpio.cleanup()

    def auto_control(self):
        commands = []
        file = open('auto.txt', 'r')
        for line in file:
            commands.append(line)
        file.close()

        i = 0
        # sleep_time = 0
        while i != len(commands):
            command = commands[i]
            str(command)
            if command == "left" or command == "left\n":
                self.do_left()
            elif command == "right" or command == "right\n":
                self.do_right()
            elif command == "up" or command == "up\n":
                self.do_up()
            elif command == "down" or command == "down\n":
                self.do_down()
            elif command == "up_cargo" or command == "up_cargo\n":
                self.do_up_cargo()
            elif command == "down_cargo" or command == "down_cargo\n":
                self.do_down_cargo()
            elif command == "s_on" or command == "s_on\n":
                self.solenoid_on()
            elif command == "s_off" or command == "s_off\n":
                self.solenoid_off()
            else:
                try:
                    sleep_time = float(command)
                    sleep(sleep_time)
                except ValueError:
                    print("Check you file")
                    break
            i += 1
            sleep(0.5)
