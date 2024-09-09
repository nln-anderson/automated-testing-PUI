import os
from scripts.mode_changing_login import login_and_navigate
from scripts.dealership_mode import run_dealership_mode
from scripts.consumer_mode import run_consumer_mode
from scripts.recovery_mode import run_recovery_mode
from scripts.remove_recovery_mode import run_remove_recovery_mode

def main():
    # Run the login and navigation function from mode_changing_login.py
    driver = login_and_navigate()

    while True:
        # Present the options to the user
        print("\nSelect an action to perform:")
        print("Press D to put the unit into Dealership Mode")
        print("Press C to put the unit into Consumer Mode")
        print("Press R to put the unit into Recovery Mode")
        print("Type 'REMOVE R' to remove the unit from Recovery Mode")
        print('Type "QUIT" to exit.')

        user_input = input("Enter your choice (D, C, R, REMOVE R, QUIT): ").strip().upper()

        # Handle the user's choice
        if user_input == 'D':
            run_dealership_mode(driver)
            print("\nUnit is in Dealership Mode")
        elif user_input == 'C':
            run_consumer_mode(driver)
            print("\nUnit is in Consumer Mode")
        elif user_input == 'R':
            run_recovery_mode(driver)
            print("\nUnit is in Recovery Mode")
        elif user_input == 'REMOVE R':
            run_remove_recovery_mode(driver)
            print("\nUnit has been removed from Recovery Mode")
        elif user_input == 'QUIT':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

    # Close the browser when exiting
    driver.quit()

if __name__ == "__main__":
    main()
