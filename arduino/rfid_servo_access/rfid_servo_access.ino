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

String allowedUIDs[] = {
  "FDD812FC",
  "4B2D74CF6180",
  "2958DF8E"
};

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

void accessGranted(String uid) {
  Serial.print("UID:");
  Serial.print(uid);
  Serial.println(",STATUS:GRANTED");

  myServo.write(90);
  digitalWrite(GRANTED_LED, HIGH);

  beep(100, 100, 2);

  delay(2000);

  digitalWrite(GRANTED_LED, LOW);
  myServo.write(0);
}

void accessDenied(String uid) {
  Serial.print("UID:");
  Serial.print(uid);
  Serial.println(",STATUS:DENIED");

  digitalWrite(DENIED_LED, HIGH);
  beep(600, 0, 1);
  digitalWrite(DENIED_LED, LOW);
}

bool isAuthorized(String uid) {
  int count = sizeof(allowedUIDs) / sizeof(allowedUIDs[0]);

  for (int i = 0; i < count; i++) {
    if (uid == allowedUIDs[i]) {
      return true;
    }
  }
  return false;
}

void loop() {
  if (!rfid.PICC_IsNewCardPresent()) return;
  if (!rfid.PICC_ReadCardSerial()) return;

  String uid = readUID();

  if (isAuthorized(uid)) {
    accessGranted(uid);
  } else {
    accessDenied(uid);
  }

  rfid.PICC_HaltA();
  delay(300);
}