# Configuration file for the turnstile clock-in system


# This is for Ubuntu. For MacOS, the serial port is detected automatically in serial_handler.py
SERIAL_PORT_ubuntu = "/dev/serial/by-id/usb-Arduino__www.arduino.cc__0043_55930343636351A0E0B1-if00"
BAUD_RATE = 9600

# Database configuration
DB_NAME = "turnstile.db"

# Dictionary of allowed UIDs
allowed_uids = {
    "FDD812FC": "Akin",
    "4B2D74CF6180": "Ismail",
    "2958DF8E": "Yuksel"
}
