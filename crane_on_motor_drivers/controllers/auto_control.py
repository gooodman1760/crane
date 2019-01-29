from time import sleep

from controllers.text_reader import TextReader
from controllers.control_lr import ControlsLR
from controllers.control_ud import ControlsUD
from controllers.control_ud_c import ControlsUDC
from controllers.control_solenoid import ControlSolenoid


class AutoControl:
    file_name = "auto.txt"

    controls_solenoid = ControlSolenoid()
    controls_lr = ControlsLR()
    controls_ud = ControlsUD()
    controls_ud_c = ControlsUDC()

    def auto_control(self):
        commands = TextReader().get_commands_from_file(self.file_name)

        i = 0
        # sleep_time = 0
        while i != len(commands):
            command = commands[i]
            str(command)
            if command == "left" or command == "left\n":
                self.controls_lr.do_left()
            elif command == "right" or command == "right\n":
                self.controls_lr.do_right()
            elif command == "up" or command == "up\n":
                self.controls_ud.do_up()
            elif command == "down" or command == "down\n":
                self.controls_ud.do_down()
            elif command == "up_cargo" or command == "up_cargo\n":
                self.controls_ud_c.do_up_cargo()
            elif command == "down_cargo" or command == "down_cargo\n":
                self.controls_ud_c.do_down_cargo()
            elif command == "s_on" or command == "s_on\n":
                self.controls_solenoid.solenoid_on()
            elif command == "s_off" or command == "s_off\n":
                self.controls_solenoid.solenoid_off()
            else:
                try:
                    sleep_time = float(command)
                    sleep(sleep_time)
                except ValueError:
                    print("Check you file")
                    break
            i += 1
            sleep(0.5)
