const int MAX_SIZE = 16;

int incomingByte = 0;
char buffer[MAX_SIZE];
int count = 0;

unsigned long prev_time; 

void setup()
{
    Serial.begin(9600);
    pinMode(LED_BUILTIN, OUTPUT);

    prev_time = millis();
    
    delay(500);
    Serial.println("======================");
    Serial.println("= Arduino serial POC =");
    Serial.println("======================");
}

void loop()
{
    if (Serial.available() > 0)
    {
        count = 0;
        while (Serial.available())
        {
            incomingByte = Serial.read();
            delay(5);

            // reset buffer if its size reaches the max size for the array
            if (count >= MAX_SIZE - 1)
            {
                count = 0;
                memset(&buffer[0], 0, sizeof(buffer));
                return;
            }

            // add one char at a time to char array buffer
            buffer[count] = char(incomingByte);
            count++;
        }

        String s = (buffer);

        // do stuff here
        Serial.println("ACK: " + s);

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

        // reset buffer
        memset(&buffer[0], 0, sizeof(buffer));
        count = 0;
    }
    else
    {
        if (millis() - prev_time >= 3000)
        {
            Serial.print("heartbeat (");
            Serial.print(millis() / 1000);
            Serial.println(")");
            prev_time = millis();
        }
    }
}
