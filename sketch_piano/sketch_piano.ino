void setup()
{
  Serial.begin(9600);
}

void loop()
{

  int sensorValue[6] = {800, 800, 800, 800, 800, 800};

  if (analogRead(0) < sensorValue[0])
  {
    Serial.println(1);
    delay(850);
  }

  if (analogRead(1) < sensorValue[1])
  {
    Serial.println(2);
    delay(950);
  }

  if (analogRead(2) < sensorValue[2])
  {
    Serial.println(3);
    delay(870);
  }

  if (analogRead(3) < sensorValue[3])
  {
    Serial.println(4);
    delay(820);
  }

  if (analogRead(4) < sensorValue[4])
  {
    Serial.println(5);
    delay(830);
  }

  if (analogRead(5) < sensorValue[5])
  {
    Serial.println(6);
    delay(880);
  }

}

