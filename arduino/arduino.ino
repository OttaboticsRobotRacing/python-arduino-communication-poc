void setup()
{
    pinMode(LED_BUILTIN, OUTPUT);
    Serial.begin(9600);
}

void loop()
{
    String input = "";

    if (Serial.available() > 0)
    {
        input = Serial.readString();
        Serial.println(input);

        if (input == "test")
        {
            Serial.println("match");

            digitalWrite(LED_BUILTIN, HIGH);
            delay(100);
            digitalWrite(LED_BUILTIN, LOW);
            delay(100);
            digitalWrite(LED_BUILTIN, HIGH);
            delay(100);
            digitalWrite(LED_BUILTIN, LOW);
            delay(100);
            digitalWrite(LED_BUILTIN, HIGH);
            delay(100);
            digitalWrite(LED_BUILTIN, LOW);
            delay(100);
        }
        else
        {
            Serial.println("else");
        }
    }
}
