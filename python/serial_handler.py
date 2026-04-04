import serial
import serial.tools.list_ports
from config import BAUD_RATE, SERIAL_PORT_ubuntu
from db import insert_log, get_user_name

ports = serial.tools.list_ports.comports()

for port in ports:

    # For MacOS
    if "IOUSBHostDevice" in port.description:
        arduino_port = port.device
        print("Port has been selected automatically for MacOS:", arduino_port)
        break
    # For Ubuntu (because the description is n/a on Ubuntu)
    else:
        arduino_port = SERIAL_PORT_ubuntu
        print("Port has been imported from config.py for Ubuntu:", arduino_port)
        break

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
