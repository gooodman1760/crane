import RPi.GPIO as gpio
from time import sleep

from const_module import const_pin, const_position
from controllers.controls import Controls


class ControlsLR(Controls):
    # limitations and running parameters
    # lr it's left_right
    lr_min = 1
    lr_max = 10

    def left(self):
        gpio.output(const_pin.LEFT_PIN, 1)
        sleep(0.5)
        gpio.output(const_pin.LEFT_PIN, 0)

    def right(self):
        gpio.output(const_pin.RIGHT_PIN, 1)
        sleep(0.5)
        gpio.output(const_pin.RIGHT_PIN, 0)

    def do_left(self):
        if self.minimum_check(const_position.LR, self.lr_min, self.lr_max):
            const_position.LR += 1
            self.left()

    def do_right(self):
        if self.maximum_check(const_position.LR, self.lr_min, self.lr_max):
            const_position.LR -= 1
            self.right()

    def return_to_start_position(self):
        while const_position.LR < self.lr_max:
            const_position.LR += 1
            self.left()
            sleep(0.5)
        sleep(0.5)
