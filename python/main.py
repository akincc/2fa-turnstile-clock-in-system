from db import create_tables, insert_user
from serial_handler import start_serial_listener


def main():
    create_tables()

    insert_user("FDD812FC", "Akin")
    insert_user("4B2D74CF6180", "Ismail")
    insert_user("2958DF8E", "Yuksel")

    start_serial_listener()


if __name__ == "__main__":
    main()