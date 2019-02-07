void setup()
{
  Serial.begin(9600);
}

void loop()
{
  if(analogRead(0)<800)
  {
    Serial.println(1);
    delay(850);
  }

  if(analogRead(1)<800)
  {
    Serial.println(2);
    delay(950);
  }

  if(analogRead(2)<800)
  {
    Serial.println(3);
    delay(870);
  }

  if(analogRead(3)<800)
  {
    Serial.println(4);
    delay(820);
  }

  if(analogRead(4)<800)
  {
    Serial.println(5);
    delay(830);
  }

  if(analogRead(5)<800)
  {
    Serial.println(6);
    delay(880);
  }
  
}

