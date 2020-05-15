int fsrPin_1 = 1;
int fsrReading_1;
int fsrPin_2 = 2;
int fsrReading_2;
int fsrPin_3 = 3;
int fsrReading_3;

void setup(){
  Serial.begin(9600);
}

void loop(){
  fsrReading_1 = analogRead(fsrPin_1);
  fsrReading_2 = analogRead(fsrPin_2);
  fsrReading_3 = analogRead(fsrPin_3);
  
  delay(250);
  Serial.print(fsrReading_1);
  Serial.print(",");
  Serial.print(fsrReading_2);
  Serial.print(",");
  Serial.print(fsrReading_3);
  Serial.println(",");
  
  
}

