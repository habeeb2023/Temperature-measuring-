#importing libraries
import dht
from machine import Pin, PWM
import utime

# Define pin numbers
DHT_PIN = 16
KY011_GREEN_PIN = 14
KY011_RED_PIN = 15
KY006_PIN = 17

# Initialize DHT sensor
dht_sensor = dht.DHT22(Pin(DHT_PIN))

# Initialize KY-011 LEDs
ky011_green_led = Pin(KY011_GREEN_PIN, Pin.OUT)
ky011_red_led = Pin(KY011_RED_PIN, Pin.OUT)

# Initialize KY-006 buzzer
buzzer = PWM(Pin(KY006_PIN))

# Function to play different notes on the buzzer
def play_note(frequency, duration):
    buzzer.freq(frequency)
    buzzer.duty_u16(500)
    utime.sleep_ms(duration)
    buzzer.duty_u16(0)

while True:
    try:
        # Read temperature and humidity from DHT sensor
        dht_sensor.measure()

        # Get temperature in Celsius
        temperature = dht_sensor.temperature()
    
        # Read values
        temp = dht_sensor.temperature()
        humi = dht_sensor.humidity()
        # output values
        print('Temperature:', temp, '°C')
        print('humidity:', humi, '%')

        if temperature > 30:
            # Temperature is above 20 degrees Celsius
            ky011_red_led.on()
            ky011_green_led.off()
            play_note(1000, 200)  # Play a note on the buzzer
            print('Temperature exceeds out of range Output signal activated.')
        elif temperature < 15:
            # Temperature is below 15 degrees Celsius
            ky011_red_led.on()
            ky011_green_led.off()
            play_note(2000, 500)  # Play a different note on the buzzer
            print('Temperature below acceptable range.')
        else:
            # Temperature is between 15 and 20 degrees Celsius
            ky011_green_led.on()
            ky011_red_led.off()
            buzzer.duty_u16(0)  # Turn off the buzzer
        print()
    except OSError as e:
        print("Sensor reading error:", e)

    utime.sleep(2)  # Delay before taking the next reading

