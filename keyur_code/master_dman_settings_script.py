## 0 For GPS Values means Use Cell, 1 means Use GPS
## Dealership Mode Test - Use GPS in Dealership Mode, Dealership Move Interval 60, Dealership Stop Interval 120

import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Function to prompt for user input in the terminal
def get_user_credentials():
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    return username, password

# Get user credentials from the terminal
username, password = get_user_credentials()

# Load the JSON file containing the settings
with open('master_dman_settings.json', 'r') as f:
    settings_list = json.load(f)

# Chrome Driver Path Initialization
driver = webdriver.Chrome()

# Open DMAN URL
driver.get('https://test.dmanservice.com/login')

# Use explicit waits for elements
wait = WebDriverWait(driver, 10)

# Locate username input and enter username
username_field = wait.until(EC.presence_of_element_located((By.ID, 'input-14')))
username_field.send_keys(username)

# Locate password input field and enter password
password_field = wait.until(EC.presence_of_element_located((By.ID, 'input-18')))
password_field.send_keys(password)

# Click login button
login_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//div[@id="app"]/div/main/div/div/div/div/div[3]/button/span')))
login_button.click()

# 2FA code
two_fa_code = input("Please enter your 2FA code in the terminal once you receive it: ")

# Locate 2FA input field and enter 2FA code
two_fa_field = wait.until(EC.presence_of_element_located((By.ID, 'input-25')))
two_fa_field.send_keys(two_fa_code)

# Click Verify button
verify_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//button[contains(@class, "v-btn--is-elevated") and contains(@class, "success")]')))
verify_button.click()

# JSON Loop
for key, settings in settings_list.items():

    # Settings button
    settings_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.v-list-item:nth-child(5)')))
    settings_button.click()

    # Wait for settings page to load and click Add button
    add_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//button[contains(@class, "v-btn--has-bg") and contains(@class, "theme--dark") and contains(@class, "success")]')))
    add_button.click()

    # Wait for platform dropdown menu
    platform_dropdown = wait.until(EC.presence_of_element_located((By.ID, 'field-platformId')))

    # Scroll into view and click platform dropdown using JavaScript
    driver.execute_script("arguments[0].scrollIntoView(true);", platform_dropdown)
    driver.execute_script("arguments[0].click();", platform_dropdown)

    # Wait to ensure dropdown is open
    time.sleep(2)

    # Select option from dropdown
    option_platform = wait.until(EC.presence_of_element_located((By.XPATH, f'//select[@id="field-platformId"]/option[@value="{settings["platformId"]}"]')))
    option_platform.click()

    # Firmware dropdown wait
    firmware_dropdown = wait.until(EC.presence_of_element_located((By.ID, 'field-firmwareId')))

    # Scroll into view and click firmware dropdown using JavaScript
    driver.execute_script("arguments[0].scrollIntoView(true);", firmware_dropdown)
    driver.execute_script("arguments[0].click();", firmware_dropdown)

    # Wait to ensure dropdown is open
    time.sleep(2)

    # Select option from dropdown
    option_firmware = wait.until(EC.presence_of_element_located((By.XPATH, f'//select[@id="field-firmwareId"]/option[@value="{settings["firmwareId"]}"]')))
    option_firmware.click()

    # Wait for tag input field to appear
    tag_input = wait.until(EC.presence_of_element_located((By.ID, 'field-tag')))

    # Enter value from the JSON object in the tag input field
    tag_input.send_keys(settings["tag"])

    # Wait for name input field to appear
    name_input = wait.until(EC.presence_of_element_located((By.ID, 'field-name')))

    # Enter value from the JSON object in the name input field
    name_input.send_keys(settings["name"])

    # Wait for the field-28 input field to appear
    field_28_input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input.field-28')))

    # Enter the value from the JSON object in the field-28 input field
    field_28_input.clear()  # Clear the existing value
    field_28_input.send_keys(settings["field_28"])

    # Wait for the field-24 input field to appear
    field_24_input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input.field-24')))

    # Enter the value from the JSON object in the field-24 input field
    field_24_input.clear()  # Clear the existing value
    field_24_input.send_keys(settings["field_24"])

    # Wait for the field-26 input field to appear
    field_26_input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input.field-26')))

    # Enter the value from the JSON object in the field-26 input field
    field_26_input.clear()  # Clear the existing value
    field_26_input.send_keys(settings["field_26"])

    # Wait for the heartbeatInterval input field to appear
    heartbeat_interval_input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input.field-1')))

    # Enter the value from the JSON object in the heartbeatInterval input field
    heartbeat_interval_input.clear()  # Clear the existing value
    heartbeat_interval_input.send_keys(settings["heartbeatInterval"])

    # Wait for the minSatellites input field to appear
    min_satellites_input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input.field-10')))
    min_satellites_input.clear()
    min_satellites_input.send_keys(settings["minSatellites"])

    # Wait for the minHAC input field to appear
    min_hac_input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input.field-11')))
    min_hac_input.clear()
    min_hac_input.send_keys(settings["minHAC"])

    # Wait for the gpsMaxTimeout input field to appear
    gps_max_timeout_input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input.field-9')))
    gps_max_timeout_input.clear()
    gps_max_timeout_input.send_keys(settings["gpsMaxTimeout"])

    # Wait for the useGPSOnHeartbeat dropdown to appear
    use_gps_on_heartbeat_dropdown = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'select.field-59')))
    driver.execute_script("arguments[0].scrollIntoView(true);", use_gps_on_heartbeat_dropdown)
    driver.execute_script("arguments[0].click();", use_gps_on_heartbeat_dropdown)
    time.sleep(1)
    option_use_cell_59 = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, f'select.field-59 option[value="{settings["useGPSOnHeartbeat"]}"]')))
    option_use_cell_59.click()

    # Wait for the useGPSOnTripStart dropdown to appear
    use_gps_on_trip_start = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'select.field-60')))
    driver.execute_script("arguments[0].scrollIntoView(true);", use_gps_on_trip_start)
    driver.execute_script("arguments[0].click();", use_gps_on_trip_start)
    time.sleep(1)
    option_use_cell_60 = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, f'select.field-60 option[value="{settings["useGPSOnTripStart"]}"]')))
    option_use_cell_60.click()

    # Wait for the useGPSOnTripEnd dropdown to appear
    use_gps_on_trip_end = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'select.field-61')))
    driver.execute_script("arguments[0].scrollIntoView(true);", use_gps_on_trip_end)
    driver.execute_script("arguments[0].click();", use_gps_on_trip_end)
    time.sleep(1)
    option_use_cell_61 = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, f'select.field-61 option[value="{settings["useGPSOnTripEnd"]}"]')))
    option_use_cell_61.click()

    # Wait for the useGPSOnMove dropdown to appear
    use_gps_on_move = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'select.field-62')))
    driver.execute_script("arguments[0].scrollIntoView(true);", use_gps_on_move)
    driver.execute_script("arguments[0].click();", use_gps_on_move)
    time.sleep(1)
    option_use_cell_62 = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, f'select.field-62 option[value="{settings["useGPSOnMove"]}"]')))
    option_use_cell_62.click()

    # Wait for the useGPSOnStop dropdown to appear
    use_gps_on_stop = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'select.field-63')))
    driver.execute_script("arguments[0].scrollIntoView(true);", use_gps_on_stop)
    driver.execute_script("arguments[0].click();", use_gps_on_stop)
    time.sleep(1)
    option_use_cell_63 = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, f'select.field-63 option[value="{settings["useGPSOnStop"]}"]')))
    option_use_cell_63.click()

    # Wait for the trackingMoveInterval input field to appear
    tracking_move_interval_input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input.field-12')))
    tracking_move_interval_input.clear()  
    tracking_move_interval_input.send_keys(settings["trackingMoveInterval"])

    # Wait for the trackingStopInterval input field to appear
    tracking_stop_interval_input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input.field-13')))
    tracking_stop_interval_input.clear()
    tracking_stop_interval_input.send_keys(settings["trackingStopInterval"])

    # Wait for the dealershipMoveInterval input field to appear
    dealership_move_interval_input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input.field-44')))
    dealership_move_interval_input.clear()
    dealership_move_interval_input.send_keys(settings["dealershipMoveInterval"])

    # Wait for the dealershipStopInterval input field to appear
    dealership_stop_interval_input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input.field-45')))
    dealership_stop_interval_input.clear()
    dealership_stop_interval_input.send_keys(settings["dealershipStopInterval"])

    # Wait for the engineeringUpdateMaxTimeout input field to appear
    engineering_update_max_timeout_input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input.field-22')))
    engineering_update_max_timeout_input.clear()
    engineering_update_max_timeout_input.send_keys(settings["engineeringUpdateMaxTimeout"])

    # Wait for the engineeringUpdateRetryInterval input field to appear
    engineering_update_retry_interval_input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input.field-23')))
    engineering_update_retry_interval_input.clear()
    engineering_update_retry_interval_input.send_keys(settings["engineeringUpdateRetryInterval"])

    # Wait for the engineeringTempHighThreshold input field to appear
    engineering_temp_high_threshold_input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input.field-5')))
    engineering_temp_high_threshold_input.clear()
    engineering_temp_high_threshold_input.send_keys(settings["engineeringTempHighThreshold"])

    # Wait for the engineeringTempLowThreshold input field to appear
    engineering_temp_low_threshold_input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input.field-6')))
    engineering_temp_low_threshold_input.clear()
    engineering_temp_low_threshold_input.send_keys(settings["engineeringTempLowThreshold"])

    # Wait for the engineeringUpdateSettingInterval input field to appear
    engineering_update_setting_interval_input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input.field-7')))
    engineering_update_setting_interval_input.clear()
    engineering_update_setting_interval_input.send_keys(settings["engineeringUpdateSettingInterval"])

    # Wait for the engineeringMajorSleepCycle input field to appear
    engineering_major_sleep_cycle_input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input.field-38')))
    engineering_major_sleep_cycle_input.clear()
    engineering_major_sleep_cycle_input.send_keys(settings["engineeringMajorSleepCycle"])

    # Wait for the save button to be clickable
    save_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//span[contains(text(), "Save")]')))
    save_button.click()

    # Wait a moment after saving, then go back to add the next settings
    time.sleep(3) 
    driver.back()  # Go back to add the next entry

# Once done, close the browser
input("Press Enter to close the browser and end the script...")
