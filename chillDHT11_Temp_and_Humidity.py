import RPi.GPIO as GPIO
import sys
import time

#import from other file
sys.path.append('/home/pi/BevChill/DHT11_Python')
import  dht11

# initialize GPIO
GPIO.setwarnings(True)
GPIO.setmode(GPIO.BCM)

# read data using pin 12
instance = dht11.DHT11(pin=12)

#def read_temp():
#    result = instance.read()
#    return result.temperature
#    return result.humidity
#    print("Last valid input: " + time.strftime('%x %X'))
#    print("Temperature: %-3.1f C" % result.temperature)
#    print("Humidity: %-3.1f %%" % result.humidity)
#    print('read temp complete')

try:
    while True:
        result = instance.read()
        if result.is_valid():
            print("Last valid input: " + time.strftime('%x %X'))
            print("Temperature: %-3.1f C" % result.temperature)
            print("Humidity: %-3.1f %%" % result.humidity)
#            read_temp()
        time.sleep(2)

except KeyboardInterrupt:
    print("Cleanup")
    GPIO.cleanup()