# Creates new txt files to clean up the logs

def create_settings_log() -> None:
    """Given the initial log, it finds and clips only the settings and creates new file with the settings only."""
    settings_found_bool = False

    # Open file
    with open('serial_reading_writing/terminal_log.txt', 'r') as file:
        logs = file.readlines()

    # Seperate the lines
        for line in logs:
            line_separated = line.split()
            terms = len(line_separated)
            if terms > 1:
                if line_separated[1][0:4] == "-Set":
                    settings_found_bool = True
                if line_separated[1][0:4] == "-End":
                    settings_found_bool = False
            if settings_found_bool:
                with open('validate_logs/settings.txt', 'a') as file:
                    file.write(f"{line}")

def get_boot_index() -> None:
    """Separates the boot cycles into separate logs."""
    # Open file
    with open('serial_reading_writing/terminal_log.txt', 'r') as file:
        logs = file.readlines()

        boot_starts_index = [0, len(logs)]
        boot_num = 1
        for loop_var in range(len(logs)):
            if logs[loop_var].strip() == "system clock 32 MHz":
                boot_num += 1
                boot_starts_index.append(loop_var)

    boot_starts_index.sort()
    return boot_starts_index

def seperate_by_index(boot_starts_index: list[int]) -> None:
    with open('serial_reading_writing/terminal_log.txt', 'r') as file:
        logs = file.readlines()

    # Iterate through the boot_starts_index and create new files for each interval
    for i in range(len(boot_starts_index) - 1):
        start = boot_starts_index[i]
        end = boot_starts_index[i + 1]
        output_file = f"validate_logs/boot_{i+1}.txt"

        # Write the slice of lines to a new file
        with open(output_file, 'w') as out_f:
            out_f.writelines(logs[start:end])

def check_target_message(target: str) -> None:
    """Determines if target message is in logs. If so, it prints the line index."""
    with open('serial_reading_writing/terminal_log.txt', 'r') as file:
        logs = file.readlines()
    
    for loop_var in range(len(logs)):
        if target in logs[loop_var]:
            print(f"Target message found in line {loop_var+1}")

def main() -> None:
    create_settings = input("Would you like to create a seperate log for settings (Y/N): ")
    if create_settings.upper() == "Y":
        create_settings_log()
    create_settings = input("Would you like to create a seperate log for each boot (Y/n): ")
    if create_settings.upper() == "Y":
        seperate_by_index(get_boot_index())
    create_settings = input("Would you like to search for a target message (Y/n): ")
    if create_settings.upper() == "Y":
        check_target_message(input("Enter the target message: "))

if __name__ == "__main__":
    main()