#imports
import RPi.GPIO as GPIO
from w1thermsensor import W1ThermSensor
import threading
import sys
import time

#import from other file
sys.path.append('/home/pi/BevChill/DHT11_Python')
import  dht11
GPIO.setwarnings(True)
GPIO.setmode(GPIO.BCM)

#initialization
start_time = time.time()
sleep_time = 10 #seconds, time between temperature readings




def read_temp():
  
    ### Data Gathering ###
    
    ##for ambient DHT11 temp & humidity sensor ##
    # read data using pin 12
    instance = dht11.DHT11(pin=12)
    result = instance.read()
#    print("Temperature: %-3.1f C" % result.temperature)
#    print("Humidity: %-3.1f %%" % result.humidity)
    tempC_amb = result.temperature
    tempF_amb = (tempC_amb*1.8)+32
    tempC_humidity = result.humidity
#    GPIO.cleanup() 
    
    ##for probe DS18 sensor ##
    threading.Timer(sleep_time, read_temp).start()
    tempC_probe = sensor.get_temperature()
    tempF_probe = sensor.get_temperature(W1ThermSensor.DEGREES_F)
 

    ### Time Gathering ###
    time_stamp = time.strftime('%x %X')
    elapsed_time = time.time() - start_time  #seconds
    elapsed_time = round(elapsed_time,3)

    ### Data List ###
    data = [
      time_stamp, 
      elapsed_time, 
      tempC_probe,
      tempF_probe,
      tempC_amb,
      tempF_amb,
      tempC_humidity
    ]

    #info to print to screen
    print("---------------------")
    print(tempC_probe, "probe temp deg C")
    print(tempF_probe, "probe temp deg F")
    print(tempC_amb, "ambiet temp deg C")
    print(tempF_amb, "ambient temp deg F")
    print(tempC_humidity, "ambient humidity %")
    print(elapsed_time, "sec, time elapsed")
    print("---------------------")
      
    #write data to file
    with open(file_name, 'a') as file:
        file.write(str(data) + "\n")
        

#run checks
if len(sys.argv) < 2:
    print("Give me a file name argument i.e. 'python chill.py test.csv'")
    sys.exit()
elif ".csv" not in sys.argv[1]:
    print("Nedd a .csv brah")
    sys.exit()
else:
    file_name = sys.argv[1]
    seconds = sleep_time
    sensor = W1ThermSensor()
    read_temp()
    
    

    
