// Simulated PIN verification
void setup() {
  Serial.begin(9600);
}
void loop() {
  String pin = "123456";  // Simulated input
  if (pin == "123456") {
    Serial.println("PIN Verified");
  } else {
    Serial.println("Wrong PIN");
  }
  delay(5000);
}
