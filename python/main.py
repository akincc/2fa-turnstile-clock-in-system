from db import create_tables, insert_user
from serial_handler import serial_listener
from config import allowed_uids


def main():
    create_tables()
    for uid, name in allowed_uids.items():
        insert_user(uid, name)
    serial_listener()


if __name__ == "__main__":
    main()