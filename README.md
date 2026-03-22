# 2FA Turnstile Clock-in System

This project is a prototype access control and clock-in/out system built with Arduino and Python.

The long-term goal is to create a two-factor authentication system using RFID and face recognition, connected to a database for attendance logging.

## Current Features
- RFID card UID reading with RC522
- Access control based on authorized UID
- Servo motor movement for gate simulation
- Green LED for granted access
- Red LED for denied access
- Buzzer feedback for different access results

![21 March 2026 - Prototype](images/rfid_servo_access.gif)

## Planned Features
- Python serial communication (done)
- SQLite database integration
- Clock-in / clock-out logging
- Face recognition as second factor
- Admin panel / reporting interface

## Hardware Used
- Arduino Uno
- RC522 RFID reader
- Servo motor
- LEDs
- Active buzzer
- Breadboard and jumper wires

## Project Status
Work in progress. This repository is being updated as the system develops.