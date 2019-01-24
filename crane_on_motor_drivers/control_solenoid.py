import RPi.GPIO as gpio

from const_module import const_pin
from controls import Controls


class ControlSolenoid(Controls):
    def solenoid_on(self):
        gpio.output(const_pin.SOLENOID_PIN, 1)

    def solenoid_off(self):
        gpio.output(const_pin.SOLENOID_PIN, 0)
