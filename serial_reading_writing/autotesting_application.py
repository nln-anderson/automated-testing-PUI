# This module is responsible for completeting autotesting

import serial
import serial.tools.list_ports
import json
import time
import clean_logs
import threading

def load_json_settings() -> json:
    """Returns the data from the json file for later use"""
    with open('serial_reading_writing/settings.json', 'r') as file:
        data = json.load(file)
    return data

def list_serial_ports() -> None:
    """Lists the serial ports available on the computer."""
    print("---------------- AVAILABLE COMS-------------------\n")
    ports = serial.tools.list_ports.comports()
    for port in ports:
        print(f"Device: {port.device}")
        print(f"  Name: {port.name}")
        print(f"  Description: {port.description}")
        print(f"  HWID: {port.hwid}")
        print(f"  VID: {port.vid}")
        print(f"  PID: {port.pid}")
        print(f"  Manufacturer: {port.manufacturer}")
        print(f"  Serial Number: {port.serial_number}")
        print("-" * 40)
    print("---------------- AVAILABLE COMS-------------------\n")

def open_com_port(port: str, baudrate: int, timeout: int) -> serial.Serial:
    """Creates serial object to open com communication. 
    port (str) - specifies port like 'COM3'
    baudrate (int) - specifies baud
    timeout (int) - specifies timeout"""
    try:
        ser_obj = serial.Serial(port, baudrate, timeout = timeout)
        return ser_obj
    except Exception as e:
        print(f"Unable to open {port}. Error: {e}")

def ask_com_connection() -> str:
    """Asks the user for the com port to use. Returns the answer as a string."""
    com_str = input("\nWhich port would you like to open (ex: COM3): ")
    return com_str.strip()

def read_from_serial(ser_obj: serial.Serial) -> None:
    """Reads and prints a line from the serial connection."""
    line = ser_obj.readline()
    line = line.decode('utf-8', errors="ignore").strip()
    
    # this is to ensure no blank lines are printed and appropriate responses are made based on the message
    if line:
        print(line)
        #check_message_do_action(line, settings['commands']['target'], send_command, ser_obj, settings['commands']['command'])
        with open('serial_reading_writing/terminal_log.txt', 'a') as file:
            file.write(f"{line}\n")

def read_loop(ser_obj: serial.Serial, threads) -> None:
    """Loops the read function if boolean is true"""
    while threads.read_thread_switch:
        read_from_serial(ser_obj)

def send_command(ser_obj: serial.Serial, command: str) -> None:
    """Sends the command to the device."""
    command_message = f"{command}\r\n".encode("utf-8")
    ser_obj.write(command_message)
    print(command)
    with open('serial_reading_writing/terminal_log.txt', 'a') as file:
        file.write(f"{command}\n")

def check_message_do_action(message: str, target: str, func: callable, *args, **kwargs) -> None:
    """Checks message and performs a function if necessary."""
    if message == target:
        print(f"Target Message Found, Sending Command in 2 seconds")
        time.sleep(2)
        func(*args, **kwargs)

def ask_for_commands() -> list[str, str]:
    """Asks the user for commands that should be inputted, as well as the trigger for them. Returns a dictionary with key as target and value and command."""
    target_and_commands = []
    break_bool = True
    while break_bool == True:
        if input("Would you like to add a message/command pair? (Y/N): ").upper() == "Y":
            target = input("Message to look for: ")
            command = input(f"Command to send after {target}: ")
            target_and_commands.append[target, command]
        else:
            break_bool = False
    
    return target_and_commands

def read_for_inputs(ser_obj, threads) -> None:
    """User can type commands and send them to the device."""
    while threads.write_thread_switch:
        command = input().strip()
        if command == "quit":
            pass
        send_command(ser_obj, command)

class Thread_Switches:
    """This class holds the boolean values for the threads."""
    read_thread_switch: bool
    write_thread_switch: bool

    def __init__(self) -> None:
        self.read_thread_switch = None
        self.write_thread_switch = None

    def read_thread_on(self, ser_obj) -> None:
        self.read_thread_switch = True
        threading.Thread(target=read_loop, args=(ser_obj, self)).start()

    def write_thread_on(self, ser_obj) -> None:
        self.write_thread_switch = True
        threading.Thread(target=read_for_inputs, args=(ser_obj, self)).start()

    def read_thread_off(self) -> None:
        self.read_thread_switch = False

    def write_thread_off(self) -> None:
        self.write_thread_switch = False

def main() -> None:
    # Load settings and test case info
    settings = load_json_settings()

    # Enable serial connection
    list_serial_ports()
    com_target = ask_com_connection()
    ser_obj = open_com_port(com_target, settings['settings']['port_settings']['baudrate'],
                            settings['settings']['port_settings']['timeout'])

    # Start the read/write threads
    threads = Thread_Switches()
    threads.read_thread_on(ser_obj)
    threads.write_thread_on(ser_obj)

if __name__ == "__main__":
    main()
