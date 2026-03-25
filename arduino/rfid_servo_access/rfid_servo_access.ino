#include <SPI.h>
#include <MFRC522.h>
#include <Servo.h>

#define SS_PIN 10
#define RST_PIN 7
#define SERVO_PIN 9
#define DENIED_LED 4
#define GRANTED_LED 3
#define BUZZER_PIN 5

MFRC522 rfid(SS_PIN, RST_PIN);
Servo myServo;

void setup() {
  Serial.begin(9600);
  SPI.begin();
  rfid.PCD_Init();

  pinMode(DENIED_LED, OUTPUT);
  pinMode(GRANTED_LED, OUTPUT);
  pinMode(BUZZER_PIN, OUTPUT);

  myServo.attach(SERVO_PIN);

  digitalWrite(DENIED_LED, LOW);
  digitalWrite(GRANTED_LED, LOW);
  digitalWrite(BUZZER_PIN, LOW);
  myServo.write(0);
}

void beep(int duration, int pause, int repeat) {
  for (int i = 0; i < repeat; i++) {
    digitalWrite(BUZZER_PIN, HIGH);
    delay(duration);
    digitalWrite(BUZZER_PIN, LOW);

    if (i < repeat - 1) {
      delay(pause);
    }
  }
}

String readUID() {
  String uid = "";

  for (byte i = 0; i < rfid.uid.size; i++) {
    uid += String(rfid.uid.uidByte[i], HEX);
  }

  uid.toUpperCase();
  return uid;
}

String serialResponse() {
  if (Serial.available() > 0) {
    String response = Serial.readStringUntil('\n');
    response.trim();
    return response;
  }
  return "";
}

void accessGranted() {
  myServo.write(90);
  digitalWrite(GRANTED_LED, HIGH);
  beep(100, 100, 2);
  delay(2000);
  digitalWrite(GRANTED_LED, LOW);
  myServo.write(0);
}

void accessDenied() {
  digitalWrite(DENIED_LED, HIGH);
  beep(600, 0, 1);
  digitalWrite(DENIED_LED, LOW);
}

bool waitingForResponse = false;
void loop() {
  if (waitingForResponse) {
    if (Serial.available()) {
      String response = Serial.readStringUntil('\n');
      response.trim();

      if (response == "GRANTED") {
        accessGranted();
      } else if (response == "DENIED") {
        accessDenied();
      }

      waitingForResponse = false;
    }
  return;
}

  if (!rfid.PICC_IsNewCardPresent()) return;
  if (!rfid.PICC_ReadCardSerial()) return;

  String uid = readUID();

  Serial.println(uid);

  waitingForResponse = true;

  rfid.PICC_HaltA();
}