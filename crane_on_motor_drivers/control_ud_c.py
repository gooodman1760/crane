import RPi.GPIO as gpio
from time import sleep

from const_module import const_pin, const_position
from controls import Controls


class ControlsUDC(Controls):
    # ud_c it's up_down_cargo
    ud_c_min = 1
    ud_c_max = 5

    def up_cargo(self):
        gpio.output(const_pin.UP_CARGO_PIN, 1)
        sleep(0.5)
        gpio.output(const_pin.UP_CARGO_PIN, 0)

    def down_cargo(self):
        gpio.output(const_pin.DOWN_CARGO_PIN, 1)
        sleep(0.5)
        gpio.output(const_pin.DOWN_CARGO_PIN, 0)

    def do_up_cargo(self):
        if self.maximum_check(const_position.UD_C, self.ud_c_min, self.ud_c_max):
            if const_position.UD == const_position.UD_C + self.difference:
                self.do_up()
            const_position.UD_C += 1
            self.down_cargo()

    def do_down_cargo(self):
        if self.maximum_check(const_position.UD_C, self.ud_c_min, self.ud_c_max):
            const_position.UD_C -= 1
            self.down_cargo()
