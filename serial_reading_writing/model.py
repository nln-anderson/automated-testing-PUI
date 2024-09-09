# Uses the model class for the backend operations

import serial
import serial.tools.list_ports
import json

class Model():
    """Organizes the program into a class."""

    # Instance Variables
    json_settings = json
    targets_and_commands: list[str, str]
    targets_found: int
    target_counter: int

    def __init__(self) -> None:
        self.targets_and_commands = None
        self.targets_found = None
        self.target_counter = None

    # Methods
    def load_json_settings(self) -> None:
        """Returns the data from the json file for later use"""
        with open('serial_reading_writing/settings.json', 'r') as file:
            data = json.load(file)
            self.json_settings = data

    def list_serial_ports(self) -> None:
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

    def open_com_port(self, port: str, baudrate: int, timeout: int) -> serial.Serial:
        """Creates serial object to open com communication. 
        port (str) - specifies port like 'COM3'
        baudrate (int) - specifies baud
        timeout (int) - specifies timeout"""
        try:
            ser_obj = serial.Serial(port, baudrate, timeout = timeout)
            return ser_obj
        except Exception as e:
            print(f"Unable to open {port}. Error: {e}")

    def ask_com_connection(self) -> str:
        """Asks the user for the com port to use. Returns the answer as a string."""
        com_str = input("\nWhich port would you like to open (ex: COM3): ")
        return com_str.strip()
    
    def read_from_serial(self, ser_obj: serial.Serial) -> None:
        """Reads and prints a line from the serial connection."""
        line = ser_obj.readline()
        line = line.decode('utf-8', errors="ignore").strip()
        
        # this is to ensure no blank lines are printed
        if line:
            print(line)
            check_message_do_action(line, "OK", send_command, ser_obj, "shipping")
            with open('serial_reading_writing/terminal_log.txt', 'a') as file:
                file.write(f"{line}\n")
    
    def read_loop(self, ser_obj: serial.Serial) -> None:
        """Loops the read function"""
        while True:
            self.read_from_serial(ser_obj)

    def send_command(self, ser_obj: serial.Serial, command: str) -> None:
        """Sends the command to the device."""
        command_message = f"{command}\r\n".encode("utf-8")
        ser_obj.write(command_message)
        print(command_message)
        with open('serial_reading_writing/terminal_log.txt', 'a') as file:
            file.write(f"{command_message}\n")

    def check_message_do_action(self, message: str, target: str, func: callable, *args, **kwargs) -> None:
        """Checks message and performs a function if necessary."""
        if message == target:
            print("Target Message Found")
            func(*args, **kwargs)