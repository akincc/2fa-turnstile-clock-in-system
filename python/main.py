from db import create_table
from serial_handler import start_serial_listener


def main():
    create_table()
    start_serial_listener()


if __name__ == "__main__":
    main()