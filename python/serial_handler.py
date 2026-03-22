import serial
from config import SERIAL_PORT, BAUD_RATE
from utils import parse_line
from db import insert_log


def start_serial_listener():
    ser = serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=1)

    print("Ready to read from serial port...")

    while True:
        line = ser.readline().decode("utf-8").strip()

        if not line:
            continue

        print("Data received:", line)

        uid, status = parse_line(line)

        if uid and status:
            insert_log(uid, status)
            print(f"Record inserted -> UID: {uid}, STATUS: {status}")
        else:
            print("Format not recognized:", line)