# Configuration file for the turnstile clock-in system


# Update these values based on your setup
#SERIAL_PORT_ubuntu = "/dev/serial/by-id/usb-Arduino__www.arduino.cc__0043_55930343636351A0E0B1-if00" //for future reference: this is for ubuntu
BAUD_RATE = 9600

# Database configuration
DB_NAME = "turnstile.db"

# Dictionary of allowed UIDs
allowed_uids = {
    "FDD812FC": "Akin",
    "4B2D74CF6180": "Ismail",
    "2958DF8E": "Yuksel"
}
