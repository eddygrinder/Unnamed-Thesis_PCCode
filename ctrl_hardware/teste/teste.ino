#include <Arduino.h>

const byte bufferSize = 12;
int inputBuffer[bufferSize];
int i = 0;
//int inByte;

const int rele_um = 2;
const int rele_dois = 3;
const int rele_tres = 4;
const int rele_quatro = 5;

void setup() {
  pinMode(rele_um, OUTPUT);
  pinMode(rele_dois, OUTPUT);
  pinMode(rele_tres, OUTPUT);
  pinMode(rele_quatro, OUTPUT);

  digitalWrite(rele_um, HIGH);
  digitalWrite(rele_tres, HIGH);
  digitalWrite(rele_dois, HIGH);
  digitalWrite(rele_quatro, HIGH);


  // initialize both serial ports:

  Serial.begin(9600);

  Serial1.begin(9600);
  pinMode(LED_BUILTIN, OUTPUT);
}

void loop() {
  while (Serial1.available() > 0) {
    int x = Serial1.read();
    inputBuffer[i] = x;
    Serial.write(inputBuffer[i]);
    i++;
  }

  switch (inputBuffer[2]) {
    case '1':
      Serial.println("relé um");
      break;
    case '2':
      Serial.println("relé dois");
      digitalWrite(rele_um, LOW);
      digitalWrite(rele_dois, LOW);
      break;
    case '3':
      Serial.println("relé três");
      break;
    case '4':
      digitalWrite(rele_tres, LOW);
      digitalWrite(rele_quatro, LOW);
      digitalWrite(rele_um, LOW);
      digitalWrite(rele_dois, LOW);
      break;
  }
  delay(5000);
}