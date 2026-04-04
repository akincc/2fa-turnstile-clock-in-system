import serial
import serial.tools.list_ports
from config import BAUD_RATE
from db import insert_log, get_user_name

ports = serial.tools.list_ports.comports()

for port in ports:
    print(port.device, port.description)

    # For Ubuntu
    if "Arduino" in port.description:
        arduino_port = port.device
    # For MacOS
    elif "IOUSBHostDevice" in port.description:
        arduino_port = port.device

print("Selected:", arduino_port)

def serial_listener():
    ser = serial.Serial(arduino_port, BAUD_RATE, timeout=1)

    print("Ready to read from serial port...")

    while True:
        uid_received = ser.readline().decode("utf-8").strip()

        if not uid_received:
            continue

        if get_user_name(uid_received) == "Unknown":
            ser.write("DENIED\n".encode())
            insert_log(uid_received, "DENIED")
        else:
            ser.write("GRANTED\n".encode())
            insert_log(uid_received, "GRANTED")
