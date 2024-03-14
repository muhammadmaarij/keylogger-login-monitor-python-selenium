from selenium import webdriver
import time

driver = webdriver.Chrome()  # Ensure you have the correct driver for your browser

login_page_url = "https://www.coursera.org/login"  # Corrected login page URL
# You need to replace this with the actual success URL
success_page_url = "https://www.coursera.org/?authMode=login"
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
        # If the URL is the same or contains a login parameter, we assume the login failed.
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
