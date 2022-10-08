from pynput import keyboard


def keystroke(pressed_key):
    print('key pressed: {0} '.format(pressed_key))

# Collect events
with keyboard.Listener(on_press=keystroke) as listener:
  listener.join()
