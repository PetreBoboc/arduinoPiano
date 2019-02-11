void setup()
{
  Serial.begin(9600);
}

void loop()
{

  unsigned int sensorValue[6] = {800, 800, 800, 800, 800, 800};
  unsigned int sensorDelay[6] = {850, 950, 870, 820, 830, 880};

  if (analogRead(0) < sensorValue[0])
  {
    Serial.println(1);
    delay(sensorDelay[0]);
  }

  if (analogRead(1) < sensorValue[1])
  {
    Serial.println(2);
    delay(sensorDelay[1]);
  }

  if (analogRead(2) < sensorValue[2])
  {
    Serial.println(3);
    delay(sensorDelay[2]);
  }

  if (analogRead(3) < sensorValue[3])
  {
    Serial.println(4);
    delay(sensorDelay[3]);
  }

  if (analogRead(4) < sensorValue[4])
  {
    Serial.println(5);
    delay(sensorDelay[4]);
  }

  if (analogRead(5) < sensorValue[5])
  {
    Serial.println(6);
    delay(sensorDelay[5]);
  }

}

