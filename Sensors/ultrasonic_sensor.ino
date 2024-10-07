//defining pin numbers 
const int trigPin = 9;
const int echoPin = 10;

//hold the length of the sound wave and how far away the object is
float duration, distance;

void setup() {

  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT);
  Serial.begin(9600);
}

void loop() {
  long duration, distance;

//clears the trigPin
  digitalWrite(trigPin, LOW);        

  delayMicroseconds(2);

//HIGH for 10 microseconds, sends out an 8 cycle sonic burst that hits the object and to the receiver(echoPin)
  digitalWrite(trigPin, HIGH);

  delayMicroseconds(10);

  digitalWrite(trigPin, LOW);

//the echoPin is HIGH for as long as the waves was traveling. The time is stored in duration
  duration = pulseIn(echoPin, HIGH);

//calculate into cm
  distance = (duration / 2) / 29.1;

  //Serial.print("Distance: ");
  Serial.println(distance);
  delay(1000);
}
