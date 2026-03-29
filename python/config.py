# Configuration file for the turnstile clock-in system


# Update these values based on your setup
SERIAL_PORT = "/dev/cu.usbmodem11101"
BAUD_RATE = 9600

# Database configuration
DB_NAME = "turnstile.db"

# Dictionary of allowed UIDs
allowed_uids = {
    "FDD812FC": "Akin",
    "4B2D74CF6180": "Ismail",
    "2958DF8E": "Yuksel"
}