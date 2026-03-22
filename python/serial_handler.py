import serial
from config import SERIAL_PORT, BAUD_RATE
from utils import parse_line
from db import insert_log, get_user_name


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
            name = get_user_name(uid)

            print(f"Record inserted -> Name: {name}, UID: {uid}, STATUS: {status}")
        else:
            print("Format not recognized:", line)