# remove_recovery.py
## This is a Python Selenium Script that will remove the device from Recovery Mode.

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def run_remove_recovery_mode(driver): 
    # **Click on the Recovery button in the sidebar**
    try:
        recovery_button = driver.find_element(By.XPATH, '//li[contains(@class, "bar-group-item noselect") and .//div[text()="Recovery"]]')
        recovery_button.click()
        print("Clicked the 'Recovery' button")
    except Exception as e:
        print(f"Failed to click the 'Recovery' button: {e}")

    # Wait for the pop-up to appear
    time.sleep(2)

    # **Click the cell with the device number '355014519251591'**
    try:
        device_cell = driver.find_element(By.XPATH, '//div[contains(@class, "cell") and .//span[text()="355014519251591"]]')
        device_cell.click()
        print("Clicked the device with number '355014519251591'")
    except Exception as e:
        print(f"Failed to click the device: {e}")

    # Wait for the form to appear
    time.sleep(2)

    # **Click on the dropdown to change the status**
    try:
        status_dropdown = driver.find_element(By.XPATH, '//label[contains(text(),"Status")]/following-sibling::div//span[@class="select2-selection select2-selection--single"]')
        status_dropdown.click()
        print("Opened the status dropdown")

        # Wait for the dropdown to be clickable
        time.sleep(2)  # Just in case there's a rendering delay

        # **Select the 'Recovered' option**
        recovered_option = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//li[contains(text(),"Recovered")]'))
        )
        recovered_option.click()
        print("Selected 'Recovered' option")

    except Exception as e:
        print(f"Failed to select 'Recovered': {e}")

    # **Click the "Save Changes" button**
    try:
        save_button = driver.find_element(By.XPATH, '//button[contains(@class,"btn-custom primary") and @type="submit"]')
        save_button.click()
        print("Clicked the 'Save Changes' button")
    except Exception as e:
        print(f"Failed to click the 'Save Changes' button: {e}")

    # **Click the "Dashboard" button**
    try:
        dashboard_button = driver.find_element(By.XPATH, '//li[contains(@class, "bar-group-item noselect") and .//div[text()="Dashboard"]]')
        dashboard_button.click()
        print("Clicked the 'Dashboard' button")
    except Exception as e:
        print(f"Failed to click the 'Dashboard' button: {e}")

