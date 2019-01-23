import webbrowser
import socket
import os


def go_web():
    gw = os.popen("ip -4 route show default").read().split()
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect((gw[2], 0))
    ip = s.getsockname()[0]
    print("IP:", ip)

    webbrowser.open('http://' + ip + ':8080')

    import vidst


def close_web():
    os.system("pkill " + "chromium-browser")