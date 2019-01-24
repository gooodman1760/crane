import RPi.GPIO as gpio
from time import sleep

from const_module import const_pin, const_position
from controls import Controls


class ControlsUD(Controls):
    # ud it's up_down
    ud_min = 1
    ud_max = 7

    def up(self):
        gpio.output(const_pin.UP_PIN, 1)
        sleep(0.5)
        gpio.output(const_pin.UP_PIN, 0)

    def down(self):
        gpio.output(const_pin.DOWN_PIN, 1)
        sleep(0.5)
        gpio.output(const_pin.DOWN_PIN, 0)

    def do_up(self):
        if self.minimum_check(const_position.UD, self.ud_min, self.ud_max):
            if const_position.UD == const_position.UD_C + self.difference:
                self.do_down()
            const_position.UD += 1
            self.up()

    def do_down(self):
        if self.maximum_check(const_position.UD, self.ud_min, self.ud_max):
            if const_position.UD == const_position.UD_C + self.difference:
                self.do_down_cargo()
            const_position.UD -= 1
            self.down()

