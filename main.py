import requests, os
from requests.auth import HTTPBasicAuth
from pynput.keyboard import Key, Listener
BASE_URL = "http://192.168.1.100/"
RIGHT = 0
LEFT = 1
UP = 2
DOWN = 3

KEYS = {
    Key.down: DOWN,
    Key.up: UP,
    Key.left: LEFT,
    Key.right: RIGHT
}


def move_cam(dir):
    requests.get(f"{BASE_URL}Pantiltctrl.cgi?DirMove={dir}", auth=HTTPBasicAuth('root', 'admin'))


def on_press(key):
    print('{0} pressed'.format(
        key))

def on_release(key):
    try:
        move_cam(KEYS[key])
    except KeyError:
        pass


while True:
    with Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()

