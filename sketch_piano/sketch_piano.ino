void setup()
{
  Serial.begin(9600);
}

void loop()
{
  Serial.println(analogRead(0));
  Serial.println(analogRead(1));
  Serial.println(analogRead(2));
  Serial.println(analogRead(3));
  Serial.println(analogRead(4));
  Serial.println(analogRead(5));
}

