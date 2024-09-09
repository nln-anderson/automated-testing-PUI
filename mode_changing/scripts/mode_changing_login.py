## This is a Python Selenium Script that will login to the backend, and bring up the pop up menu for the user 
## to put the GG100 unit into Dealership, Consumer, or Recovery Mode

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def login_and_navigate():
    # Suppress unnecessary logs
    options = webdriver.ChromeOptions()
    options.add_argument("--log-level=3")  # Suppresses log messages

    # Prompt user for email and password BEFORE starting the browser actions
    email = input("Please enter your email: ")
    password = input("Please enter your password: ")

    # Initialize the Chrome WebDriver with log suppression
    driver = webdriver.Chrome(options=options)

    # Open the URL
    driver.get('https://admin.positioninguniversal.com/')

    # Allow the page to load (adjust the sleep time if necessary)
    time.sleep(5)

    # Find the email input field and enter the email
    email_input = driver.find_element(By.NAME, 'email')
    email_input.send_keys(email)
    print("Username Entered")

    # Find the password input field and enter the password
    password_input = driver.find_element(By.CSS_SELECTOR, 'input[type="password"]')
    password_input.send_keys(password)
    print("Password Entered")

    # Find and click the Login button
    login_button = driver.find_element(By.CSS_SELECTOR, 'button[type="submit"].btn.btn-primary')
    login_button.click()
    print("Login Button Clicked")

    # Allow the page to load after login
    time.sleep(5)

    # Find the accountId input field and enter the value 10000001
    account_id_input = driver.find_element(By.NAME, 'accountId')
    account_id_input.send_keys("10000001")
    print("Account ID Entered")

    # Scroll down to the Search button
    search_button = driver.find_element(By.CSS_SELECTOR, 'button[type="submit"].btn.btn-primary')
    driver.execute_script("arguments[0].scrollIntoView(true);", search_button)  # Scrolls to the button
    time.sleep(1)  # Brief pause to ensure the scroll happens

    # Click the Search button
    search_button.click()
    print("Search Button Clicked")

    # Allow the results page to load
    time.sleep(5)

    # Find the anchor tag with account number 10000001 and click it
    account_link = driver.find_element(By.XPATH, '//a[contains(text(), "10000001")]')
    account_link.click()
    print("Account Link Clicked")

    # Wait for the new page to load after clicking the account link
    time.sleep(5)

    # Scroll down to the Login button
    login_button = driver.find_element(By.CSS_SELECTOR, 'button[ng-click="login(account);"]')
    driver.execute_script("arguments[0].scrollIntoView(true);", login_button)  # Scrolls to the button
    time.sleep(1)  # Brief pause for scroll

    # Click the Login button, which will open a new tab
    login_button.click()
    print("Login Button Clicked on Account")

    # Wait for the new tab to open
    time.sleep(3)

    # Switch to the newly opened tab
    driver.switch_to.window(driver.window_handles[-1])
    print("Switched to the new tab")

    # Wait for the new page to load
    time.sleep(5)

    # Returning the driver object for further use
    return driver
