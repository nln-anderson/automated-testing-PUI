# recovery_mode.py
## This is a Python Selenium Script that will put the unit into recovery mode.

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

def run_recovery_mode(driver):
    # **Click on the Recovery button in the sidebar**
    try:
        recovery_button = driver.find_element(By.XPATH, '//li[contains(@class, "bar-group-item noselect") and .//div[text()="Recovery"]]')
        recovery_button.click()
        print("Clicked the 'Recovery' button")
    except Exception as e:
        print(f"Failed to click the 'Recovery' button: {e}")

    # Wait for the pop-up to appear
    time.sleep(2)

    # **Click the button with the icon-plus class**
    try:
        icon_plus_button = driver.find_element(By.CSS_SELECTOR, 'button.btn-custom span.icon-plus')
        icon_plus_button.click()
        print("Clicked the 'plus' button to open the pop-up menu")
    except Exception as e:
        print(f"Failed to click the 'plus' button: {e}")

    # Wait for the pop-up to appear
    time.sleep(2)

    # **Select "Jorma recovery alert" in the first dropdown (Recipient)**
    try:
        first_dropdown = driver.find_element(By.XPATH, '//label[contains(text(),"Recipient")]/following-sibling::div//span[@class="select2-selection select2-selection--single"]')
        first_dropdown.click()
        print("Opened the first dropdown (Recipient)")

        first_dropdown_input = driver.find_element(By.CSS_SELECTOR, 'input.select2-search__field')
        first_dropdown_input.send_keys("Jorma recovery alert")
        print("Entered 'Jorma recovery alert' in the dropdown")

        jorma_option = driver.find_element(By.XPATH, '//li[contains(text(),"Jorma recovery alert")]')
        jorma_option.click()
        print("Selected 'Jorma recovery alert' from the dropdown")

    except Exception as e:
        print(f"Failed to select 'Jorma recovery alert': {e}")

    # **Select '355014519251591' in the second dropdown (Vehicle)**
    try:
        second_dropdown = driver.find_element(By.XPATH, '//label[contains(text(),"Vehicle")]/following-sibling::div//span[@class="select2-selection select2-selection--single"]')
        second_dropdown.click()
        print("Opened the second dropdown (Vehicle)")

        second_dropdown_input = driver.find_element(By.CSS_SELECTOR, 'input.select2-search__field')
        second_dropdown_input.send_keys("355014519251591")
        print("Entered '355014519251591' in the dropdown")

        vehicle_option = driver.find_element(By.XPATH, '//li[contains(text(),"355014519251591")]')
        vehicle_option.click()
        print("Selected '355014519251591' from the dropdown")

    except Exception as e:
        print(f"Failed to select '355014519251591': {e}")

    # **Click the "Save Changes" button**
    try:
        save_button = driver.find_element(By.CSS_SELECTOR, 'button.btn-custom.primary[type="submit"]')
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
        
