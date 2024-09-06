import json
import pandas as pd
import logging

# Set up logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

def open_excel_file(file_path, sheet_name):
    try:
        # Read the Excel file, specifically the "GG100 Validation Test" sheet starting from the 4th row to account for headers
        excel_data = pd.read_excel(file_path, sheet_name=sheet_name, header=3)
        logging.info(f"Excel file at {file_path} (Sheet: {sheet_name}) opened successfully.")
        return excel_data
    except FileNotFoundError:
        logging.error(f"Error: The file at {file_path} was not found.")
    except Exception as e:
        logging.error(f"An error occurred while opening the Excel file: {e}")

def update_json_with_jira_links(json_file_path, excel_data):
    try:
        # Load the JSON data from the file
        with open(json_file_path, 'r') as json_file:
            data = json.load(json_file)
        logging.info(f"Loaded JSON file from {json_file_path}.")

        # Ensure the columns exist in the Excel data
        if 'Test No' not in excel_data.columns or 'Jira ID (SWE1,2,3)' not in excel_data.columns:
            raise ValueError("Required columns 'Test No' (testID) and 'Jira ID (SWE1,2,3)' (JIRA links) were not found in the Excel file.")

        # Iterate over each test case in the JSON data
        for test_case in data.values():
            test_id = test_case['testID']
            logging.debug(f"Processing testID: {test_id}")

            # Find the corresponding JIRA link in the Excel data
            jira_link = excel_data.loc[excel_data['Test No'] == int(test_id), 'Jira ID (SWE1,2,3)'].values
            
            if jira_link.size > 0:
                test_case['jiraLink'] = jira_link[0]
                logging.info(f"Added JIRA link for testID {test_id}: {jira_link[0]}")
            else:
                test_case['jiraLink'] = "JIRA link not found"
                logging.warning(f"No JIRA link found for testID {test_id}.")

        # Save the updated JSON data back to the file
        with open(json_file_path, 'w') as json_file:
            json.dump(data, json_file, indent=4)
        logging.info(f"JSON file at {json_file_path} updated successfully with JIRA links.")
    
    except Exception as e:
        logging.error(f"An error occurred while updating the JSON file: {e}")
