int ledpins[] = {2, 0, 17, 18, 21};
int numled = 5;

void setup()
{
    Serial.begin(9600);

    for (int i = 0; i < numled; i++)
    {
        pinMode(ledpins[i], OUTPUT);
        digitalWrite(ledpins[i], LOW);
    }
}

void loop()
{
    if (Serial.available() > 0)
    {
        int fingerCount = Serial.parseInt();

        Serial.print("Received: ");
        Serial.println(fingerCount);

        // Limit 0~5
        if (fingerCount < 0)
            fingerCount = 0;

        if (fingerCount > 5)
            fingerCount = 5;

        for (int i = 0; i < numled; i++)
        {
            if (i < fingerCount)
            {
                digitalWrite(ledpins[i], HIGH);
            }
            else
            {
                digitalWrite(ledpins[i], LOW);
            }
        }
    }
}