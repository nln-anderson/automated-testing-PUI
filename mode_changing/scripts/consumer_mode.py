## This is a Python Selenium Script that will put the unit into Consumer Mode. 
## Manual Selection of "Consumer Mode" is required, everything else is automated. 

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

def run_consumer_mode(driver):
    print("Running Consumer Mode...")

    # Find the search input field and enter the number 355014519251591
    search_input = driver.find_element(By.CSS_SELECTOR, 'input[type="search"].form-control.filter-field')
    search_input.send_keys("355014519251591")
    print("Search number entered")

    # Wait 5 seconds for the result to appear
    time.sleep(5)

    # Find the div containing the result 355014519251591 and click it
    result_div = driver.find_element(By.XPATH, '//div[contains(@class, "cell") and contains(.,"355014519251591")]')
    result_div.click()
    print("Result Div Clicked")

    # Wait for the menu to appear (adjust time if necessary)
    time.sleep(2)

    # **Direct JavaScript execution to simulate 10 Tab presses**
    try:
        for i in range(1, 11):  # Simulate pressing the Tab key 10 times directly via JavaScript
            driver.execute_script("document.activeElement.blur();")  # Remove focus from the current element to tab
            driver.switch_to.active_element.send_keys(Keys.TAB)  # Press Tab 10 times
            print(f"Tab Pressed {i} Time(s)")
            time.sleep(0.5)  # 0.5-second delay between Tabs

        print("Reached Mode dropdown via Tab")

    except Exception as e:
        print(f"Failed to reach the dropdown via Tab: {e}")

    # **Pause and Wait for Manual Selection**
    print("Manually select 'Consumer Mode' in the dropdown.")
    input("Press Enter here after selecting Consumer Mode to continue...")

    # **Proceed with clicking the Save Changes button**
    try:
        save_button = driver.find_element(By.CSS_SELECTOR, 'button[type="submit"].btn-custom.primary')
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
