import serial
import serial.tools.list_ports

def find_ports() -> None:
    # List all serial ports
    ports = serial.tools.list_ports.comports()

    # Iterate over each port and print information
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


def send_command_func(command: str) -> None:
    SERIAL_PORT = "COM6"
    BAUD_RATE = 115200

    # Create connection
    ser = serial.Serial(SERIAL_PORT, baudrate=BAUD_RATE, timeout=90)

    # Define the reboot command
    REBOOT_COMMAND = f"{command}\r\n".encode("utf-8")

    try:
        # Open the serial port if it isn't already open
        if not ser.is_open:
            ser.open()
        # Send the reboot command
        ser.write(REBOOT_COMMAND)
        print("Reboot command sent")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        ser.close()

if __name__ == "__main__":
    send_command_func()
    print("REBOOT")
