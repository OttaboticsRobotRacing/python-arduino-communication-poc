const int MAX_SIZE = 16;

int incomingByte = 0;
char buffer[MAX_SIZE];
int count = 0;

unsigned long prev_time;

const int LED_W = 3;
const int LED_A = 5;
const int LED_S = 6;
const int LED_D = 4;

const int LED_DELAY = 5;

void setup()
{
    Serial.begin(9600);
    pinMode(LED_BUILTIN, OUTPUT);

    pinMode(LED_W, OUTPUT);
    pinMode(LED_A, OUTPUT);
    pinMode(LED_S, OUTPUT);
    pinMode(LED_D, OUTPUT);

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
        if (s == "w")
        {
            digitalWrite(LED_W, HIGH);
            delay(LED_DELAY);
            digitalWrite(LED_W, LOW);
            Serial.println("ACK: " + s);
        }
        else if (s == "a")
        {
            digitalWrite(LED_A, HIGH);
            delay(LED_DELAY);
            digitalWrite(LED_A, LOW);
            Serial.println("ACK: " + s);
        }
        else if (s == "s" || s == "SPACE")
        {
            digitalWrite(LED_S, HIGH);
            delay(LED_DELAY);
            digitalWrite(LED_S, LOW);
            Serial.println("ACK: " + s);
        }
        else if (s == "d")
        {
            digitalWrite(LED_D, HIGH);
            delay(LED_DELAY);
            digitalWrite(LED_D, LOW);
            Serial.println("ACK: " + s);
        }
        else
        {
            digitalWrite(LED_BUILTIN, HIGH);
            delay(LED_DELAY);
            digitalWrite(LED_BUILTIN, LOW);
            Serial.println("ACK E: " + s);

        }

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
