from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time


class LoginMonitor:
    def __init__(self, login_url, failure_indicator, driver_path="chromedriver"):
        self.login_url = login_url
        self.failure_indicator = failure_indicator
        self.driver_path = driver_path
        self.unsuccessful_logins = 0
        self.driver = webdriver.Chrome()

    def login(self, email, password):
        self.driver.get(self.login_url)
        time.sleep(10)  # Wait for page to load

        # Adjusted selectors for Coursera's login page
        email_field = self.driver.find_element(
            By.XPATH, "//input[@type='email']")
        password_field = self.driver.find_element(
            By.XPATH, "//input[@type='password']")

        email_field.send_keys(email)
        password_field.send_keys(password + Keys.RETURN)

        time.sleep(10)  # Wait for response

        if self.is_login_successful():
            print("Login unsuccessful.")
            self.unsuccessful_logins += 1
            print(f"Unsuccessful login attempts: {self.unsuccessful_logins}")
        else:
            print("Login successful!")
            self.unsuccessful_logins = 0  # Reset counter on successful login

    def is_login_successful(self):
        try:
            # Using concat function in XPath
            self.driver.find_element(
                By.XPATH, "//*[contains(text(), concat('We don', \"'\", 't'))]")
            return False
        except NoSuchElementException:
            return True

    def close_browser(self):
        self.driver.quit()


# Example usage
if __name__ == "__main__":
    LOGIN_URL = "https://www.coursera.org/login"
    # Text indicating a failed login
    FAILURE_INDICATOR = "We don't recognize that username or password."
    DRIVER_PATH = "path/to/your/webdriver"  # Update this path based on your system

    monitor = LoginMonitor(LOGIN_URL, FAILURE_INDICATOR, DRIVER_PATH)

    email = input("Enter email: ")
    password = input("Enter password: ")

    monitor.login(email, password)
    # You can add more logic here to handle multiple attempts, etc.

    monitor.close_browser()
