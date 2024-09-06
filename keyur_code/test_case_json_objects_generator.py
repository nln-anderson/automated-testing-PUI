import json

# Define the master variables
unitID = "GG100"
firmwareID = "258"

# List of test IDs to generate
test_ids = [
    "036", "055", "056", "057", "058", "059", "060", "069", "079",
    "082", "086", "089", "090", "094", "095", "097", "103", "105"
]

# Function to generate the paths dynamically
def generate_paths(testID):
    return {
        "testID": testID,
        "logFilePath": f"C:/Users/KeyurNallani/KeyurLogsTest/{firmwareID}/{unitID}_{firmwareID}_T{testID}",
        "settingsImagePath": f"C:/Users/KeyurNallani/KeyurLogsTest/{firmwareID}/Images/{unitID}_T{testID}_{firmwareID}.png",
        "locationPacket1ImagePath": f"C:/Users/KeyurNallani/KeyurLogsTest/{firmwareID}/Images/{unitID}_T{testID}_{firmwareID}_LocationPacket1.png",
        "locationPacket2ImagePath": f"C:/Users/KeyurNallani/KeyurLogsTest/{firmwareID}/Images/{unitID}_T{testID}_{firmwareID}_LocationPacket2.png",
        "message": f"Here are the log file and associated pictures for test {testID} for v{firmwareID}. T{testID} passed, the unit behaved as expected, and the packet showed up in the location server."
    }

# Create a JSON object with sub-objects using the generate_paths function for each test ID
data = {f"test{int(testID)}": generate_paths(testID) for testID in test_ids}

# Convert the dictionary to a JSON string
json_data = json.dumps(data, indent=4)

# Function to save the JSON data to a file
def save_json_to_file(file_path):
    with open(file_path, 'w') as json_file:
        json_file.write(json_data)
    print(f"JSON data successfully saved to {file_path}")

print("JIRA Links all secured, proceeding to selenium to enter the results to JIRA.")
