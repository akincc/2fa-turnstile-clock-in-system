import serial
from config import SERIAL_PORT, BAUD_RATE
from db import insert_log, get_user_name

def serial_listener():
    ser = serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=1)

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
