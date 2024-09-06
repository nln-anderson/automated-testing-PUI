import serial
import serial.tools.list_ports
from typing import Optional
import send_commands
import time

def list_serial_ports():
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

def read_from_serial(port_name, baud_rate=115200):
    try:
        ser = serial.Serial(port_name, baud_rate, timeout=10)
        print(f"Successfully opened {port_name}")
        
        while True:
            # Boolean for 0x00
            reboot_ready = False

            # Read a line of data from the serial port
            line = ser.readline()
            
            # Decode the byte string to a regular string and print it
            if line:
                formatted = line.decode('utf-8', errors="ignore").strip()
                print(formatted)
                reboot_ready = filter(formatted)

            if reboot_ready == True:
                break
                

    except serial.SerialException as e:
        print(f"Failed to open {port_name}: {e}")
    except KeyboardInterrupt:
        print("Exiting...")
    finally:
        ser.close()

def filter(formatted: str) -> None:
    """
    Filters the messages to only log the ones we want.
    """
    with open("terminal_log.txt", "a") as f:
        
        if formatted[0:5] == "< PID":
            print(formatted[0:5])
            f.write(f"{time.time()} {formatted}\n")
            f.flush()
            if formatted[6:10] == "0x00":
                return True

        elif formatted[0:8] == "tryCmd()":
            f.write(f"{time.time()} {formatted}\n")
            f.flush()
        elif formatted[0:8] == "Bootload":
            f.write(f"{time.time()} Device Succesfully Rebooted\n")
            f.flush()
        
        return False
    

if __name__ == "__main__":  
    port_name = 'COM6'
    while True:
        send_commands.send_command_func("settings")
        read_from_serial(port_name)