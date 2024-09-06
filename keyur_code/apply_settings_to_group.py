from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import json

def run_selenium_script(form_data):
    # Extract and log the form data to ensure all values are present
    print("Form Data: " + json.dumps(form_data, indent=2))
    
    username = form_data.get('username', '')
    password = form_data.get('password', '')
    group_id = form_data.get('groupID', '')
    settings_tag_id = form_data.get('settingsTagID', '')

    # Debug log for values
    print(f"Running Selenium script with: username={username}, password={password}, group_id={group_id}, settings_tag_id={settings_tag_id}") 

    # Set up the Selenium WebDriver
    driver = webdriver.Chrome()
    driver.get('https://test.dmanservice.com/login')

    # Use explicit waits to wait for the elements to be present
    wait = WebDriverWait(driver, 10)
    username_field = wait.until(EC.presence_of_element_located((By.ID, 'input-14')))
    username_field.send_keys(username)

    password_field = wait.until(EC.presence_of_element_located((By.ID, 'input-18')))
    password_field.send_keys(password)

    login_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//div[@id="app"]/div/main/div/div/div/div/div[3]/button/span')))
    login_button.click()

    # Wait for the 2FA code from the user
    two_fa_code = input("Please enter your 2FA code in the terminal once you receive it: ")

    # Locate the 2FA input field and enter the 2FA code
    two_fa_field = wait.until(EC.presence_of_element_located((By.ID, 'input-25')))
    two_fa_field.send_keys(two_fa_code)

    # Locate and click the correct "Verify" button
    verify_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//button[contains(@class, "v-btn--is-elevated") and contains(@class, "success")]')))
    verify_button.click()

    # Click the "Groups" button
    settings_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.v-list-item:nth-child(3)')))
    settings_button.click()

    # Explicitly wait for 8 seconds to ensure the page has loaded
    time.sleep(8)

    # Debugging information to ensure the page has loaded
    print("Groups page loaded, looking for Group ID '{group_id}'...")

    try:
        # Scroll and search for the row containing "{group_id}" in the "Group ID" column
        found = False
        while not found:
            row = driver.execute_script("""
                const rows = document.querySelectorAll('tr');
                for (let i = 0; i < rows.length; i++) {
                    const cells = rows[i].querySelectorAll('td');
                    if (cells.length > 0) {
                        const groupId = cells[3].innerText;
                        if (groupId === arguments[0]) {
                            rows[i].scrollIntoView();
                            return rows[i];
                        }
                    }
                }
                window.scrollBy(0, 200);  // Scroll down incrementally
                return null;
            """, group_id)

            if row:
                # Highlight the row to ensure we have found the correct one (for debugging purposes)
                driver.execute_script("arguments[0].style.border='3px solid red'", row)
                print("Found the row for Group ID '{group_id}'.")
                found = True
            else:
                time.sleep(1)  # Give some time for the page to load more content

        # Adjust scroll position to account for the sticky navbar
        driver.execute_script("window.scrollBy(0, -100);")

        # Click the pencil icon in the found row
        if found:
            time.sleep(1)  # Wait a second before clicking the pencil icon
            pencil_icon = row.find_element(By.CSS_SELECTOR, '.mdi-pencil')
            pencil_icon.click()
            print("Clicked the pencil icon for Group ID '{group_id}'.")

            # Inform the user to manually save settings
            input("Press Enter after saving the settings to end the script")

    except Exception as e:
        print(f"An error occurred: {e}")

    # Keep the browser open to observe the result
    input("Press Enter to close the browser and end the script...")
    driver.quit()
