import json
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pyautogui
import logging

# Set up logging to print to console
logging.basicConfig(level=logging.INFO, format='%(message)s')

# Function to load the JSON data
def load_json(json_file_path):
    try:
        with open(json_file_path, 'r') as json_file:
            data = json.load(json_file)
        logging.info(f"Loaded JSON file from {json_file_path}.")
        return data
    except FileNotFoundError:
        logging.error(f"Error: The file at {json_file_path} was not found.")
    except Exception as e:
        logging.error(f"An error occurred while loading the JSON file: {e}")
    return None

# Function to move the cursor to the end of the text
def move_cursor_to_end_of_text(driver):
    js_script = """
    var sel = window.getSelection();
    var range = document.createRange();
    var p = document.querySelector('#ak-editor-textarea p');
    range.selectNodeContents(p);
    range.collapse(false);
    sel.removeAllRanges();
    sel.addRange(range);
    """
    driver.execute_script(js_script)
    time.sleep(2)  # Ensure the cursor move is registered before the next action

# Function to open a JIRA link and log in (only once for the first test case)
def login_and_prepare(driver, url, email, password):
    try:
        logging.info(f"Opening JIRA link: {url}")
        driver.get(url)
        time.sleep(5)  # Wait for the page to load

        # Find and click the Microsoft authentication button
        microsoft_button = driver.find_element(By.ID, "microsoft-auth-button")
        if microsoft_button:
            microsoft_button.click()
            logging.info("Clicked the Microsoft authentication button.")
            time.sleep(5)  # Wait for the Microsoft login page to load

            # Enter the email address
            email_input = driver.find_element(By.ID, "i0116")
            email_input.send_keys(email)
            logging.info(f"Entered email: {email}")

            # Click the "Next" button
            next_button = driver.find_element(By.ID, "idSIButton9")
            next_button.click()
            logging.info("Clicked the 'Next' button.")

            time.sleep(5)  # Wait for the password page to load

            # Enter the password (you'll manually replace 'your_password' with your actual password)
            password_input = driver.find_element(By.ID, "i0118")
            password_input.send_keys(password)
            logging.info("Entered password.")

            # Click the "Sign in" button
            sign_in_button = driver.find_element(By.ID, "idSIButton9")
            sign_in_button.click()
            logging.info("Clicked the 'Sign in' button.")

            time.sleep(5)  # Wait for the "Stay signed in?" page to load

            # Click the "No" button on the "Stay signed in?" page
            no_button = driver.find_element(By.ID, "idBtn_Back")
            no_button.click()
            logging.info("Clicked the 'No' button.")

        else:
            logging.warning("An error occurred during the JIRA interaction.")

    except Exception as e:
        logging.error(f"An error occurred while interacting with the JIRA link: {e}")

# Function to process each test case (excluding login after the first test case)
def process_test_case(driver, url, message, settings_image_path, location_packet1_image_path, location_packet2_image_path):
    try:
        logging.info(f"Opening JIRA link: {url}")
        driver.get(url)
        time.sleep(5)  # Wait for the page to load

        # Manual breakpoint: Wait for the user to manually click in the text area
        input("Please click in the text area where you want to type the message, then press 'Y' to continue...")
        
        # Enter the message from the JSON
        driver.switch_to.active_element.send_keys(message)
        logging.info(f"Entered message: {message}")

        # Upload the settings image
        add_media_button = driver.find_element(By.CSS_SELECTOR, "button[data-testid='Add image, video, or file']")
        add_media_button.click()
        logging.info("Clicked the 'Add image, video, or file' button for settings image.")
        time.sleep(3)  # Wait for the file dialog to open
        file_input = driver.find_element(By.CSS_SELECTOR, "input[type='file']")
        file_input.send_keys(settings_image_path)
        logging.info(f"Uploaded settings image from path: {settings_image_path}")
        pyautogui.hotkey('alt', 'f4')
        logging.info("Closed the file explorer window after uploading settings image.")
        
        # Move cursor to the end of the text after uploading the first image
        move_cursor_to_end_of_text(driver)

        # Upload the first location packet image
        if os.path.exists(location_packet1_image_path):
            add_media_button.click()  # Click the button again to open the file dialog for the first location packet image
            time.sleep(3)  # Wait for the file dialog to open
            file_input.send_keys(location_packet1_image_path)
            logging.info(f"Uploaded first location packet image from path: {location_packet1_image_path}")
            pyautogui.hotkey('alt', 'f4')
            logging.info("Closed the file explorer window after uploading first location packet image.")
            
            # Move cursor to the end of the text after uploading the first location packet image
            move_cursor_to_end_of_text(driver)
        else:
            logging.info(f"Location Packet 1 Not Available: {location_packet1_image_path}")

        # Upload the second location packet image
        if os.path.exists(location_packet2_image_path):
            add_media_button.click()  # Click the button again to open the file dialog for the second location packet image
            time.sleep(3)  # Wait for the file dialog to open
            file_input.send_keys(location_packet2_image_path)
            logging.info(f"Uploaded second location packet image from path: {location_packet2_image_path}")
            pyautogui.hotkey('alt', 'f4')
            logging.info("Closed the file explorer window after uploading second location packet image.")
            
            # Move cursor to the end of the text after uploading the second location packet image
            move_cursor_to_end_of_text(driver)
        else:
            logging.info(f"Location Packet 2 Not Available: {location_packet2_image_path}")

        # Click the Save button
        save_button = driver.find_element(By.CSS_SELECTOR, "button[data-testid='comment-save-button']")
        save_button.click()
        logging.info("Clicked the 'Save' button to save the comment.")

        # Explicit 15-second wait to ensure everything is saved
        time.sleep(15)
        logging.info("Waited 15 seconds after clicking the 'Save' button.")

    except Exception as e:
        logging.error(f"An error occurred while interacting with the JIRA link: {e}")

# Main function to process all JIRA links and log in
def process_all_jira_links(json_file_path, email, password):
    # Load JSON data
    data = load_json(json_file_path)
    if data is None:
        return

    # Chrome Driver Path Initialization
    driver = webdriver.Chrome()

    try:
        # Process the first test case with login
        first_test_key = list(data.keys())[0]
        first_test_case = data[first_test_key]
        jira_link = first_test_case.get('jiraLink')
        message = first_test_case.get('message')
        settings_image_path = first_test_case.get('settingsImagePath')
        location_packet1_image_path = first_test_case.get('locationPacket1ImagePath')
        location_packet2_image_path = first_test_case.get('locationPacket2ImagePath')

        if jira_link and message and settings_image_path:
            logging.info(f"Processing {first_test_key} with login...")
            login_and_prepare(driver, jira_link, email, password)
            process_test_case(driver, jira_link, message, settings_image_path, location_packet1_image_path, location_packet2_image_path)
            logging.info(f"Finished processing {first_test_key}.")

        # Process remaining test cases without login
        for test_key, test_case in list(data.items())[1:]:
            jira_link = test_case.get('jiraLink')
            message = test_case.get('message')
            settings_image_path = test_case.get('settingsImagePath')
            location_packet1_image_path = test_case.get('locationPacket1ImagePath')
            location_packet2_image_path = test_case.get('locationPacket2ImagePath')

            if jira_link and message and settings_image_path:
                logging.info(f"Processing {test_key} without login...")
                process_test_case(driver, jira_link, message, settings_image_path, location_packet1_image_path, location_packet2_image_path)
                logging.info(f"Finished processing {test_key}.")
                time.sleep(5)  # delay between processing test cases

            else:
                logging.warning(f"No JIRA link, message, or settings image path found for {test_key}.")

    except Exception as e:
        logging.error(f"An error occurred during JIRA link processing: {e}")

    finally:
        # Keep the browser open until manual quit
        logging.info("Script finished. The browser will remain open. Press Ctrl+C to quit.")
        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            logging.info("ript interrupted. Exiting...")
            driver.quit()

if __name__ == "__main__":
    # Define paths and credentials
    json_file_path = "C:/Users/KeyurNallani/KeyurLogsTest/258/json/258_test_cases.json"  # Replace with your JSON file path
    email = "email@website.com"  # Your email address
    password = "password"  # Your password

    # Process all JIRA links and log in
    process_all_jira_links(json_file_path, email, password)
