from flask import Flask, jsonify, render_template
from flask_cors import CORS

from controls.control_lr import ControlLR

file_name = "page.html"

app = Flask(__name__)
CORS(app)

control_lr = ControlLR()


@app.route('/left_button')
def left_button():
    control_lr.print_lr()
    return jsonify(result="left")


@app.route('/up_button')
def up_button():
    control_lr.print_lr()
    return jsonify(result="up")


@app.route('/down_button')
def down_button():
    control_lr.print_lr()
    return jsonify(result="down")


@app.route('/right_button')
def right_button():
    control_lr.print_lr()
    return jsonify(result="right")


@app.route('/up_cargo_button')
def up_cargo_button():
    control_lr.print_lr()
    return jsonify(result="up_cargo")


@app.route('/down_cargo_button')
def down_cargo_button():
    control_lr.print_lr()
    return jsonify(result="down_cargo")


@app.route('/solenoid_on_button')
def solenoid_on_button():
    control_lr.print_lr()
    return jsonify(result="solenoid_on")


@app.route('/solenoid_off_button')
def solenoid_off_button():
    control_lr.print_lr()
    return jsonify(result="solenoid_off")


@app.route('/auto_button')
def auto_button():
    control_lr.print_lr()
    return jsonify(result="auto")


@app.route('/return_button')
def return_button():
    control_lr.print_lr()
    return jsonify(result="return")


@app.route('/exit_button')
def exit_button():
    control_lr.print_lr()
    return jsonify(result="exit")


@app.route('/')
def index():
    return render_template(file_name)


if __name__ == '__main__':
    app.run(host='192.168.88.33', port=5000)
