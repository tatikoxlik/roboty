int swiatelko = 0;
int jasnosc = 0;

void setup()
{
  pinMode(A0, INPUT);
  pinMode(9, OUTPUT);
  Serial.begin(9600);
}

void loop()
{
  swiatelko = analogRead(A0);

  jasnosc = map(swiatelko, 0, 1023, 0, 255);
  analogWrite(9, jasnosc);
  Serial.print("opór = ");
  Serial.print(swiatelko);
  Serial.print("natężenie = ");
  Serial.println(jasnosc);

  delay(5);
}
