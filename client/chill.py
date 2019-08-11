# imports
import RPi.GPIO as GPIO
from w1thermsensor import W1ThermSensor
import threading
import sys
import time
import csv
import socketio

# import from other file
sys.path.append('/home/pi/BevChill/DHT11_Python')
import dht11
GPIO.setwarnings(True)
GPIO.setmode(GPIO.BCM)

#initialization
global chill_data
global sio
start_time = time.time()
sleep_time = 10  #time between temperature readings

def read_temp():
    threading.Timer(sleep_time, read_temp).start()
    ### Data Gathering ###
    tempHumid = DHT11.read()
    tempC_amb = tempHumid.temperature
    tempF_amb = (tempC_amb*1.8)+32
    humidity = tempHumid.humidity
    tempC_probe = THERM.get_temperature()
    tempF_probe = THERM.get_temperature(W1ThermSensor.DEGREES_F)
    # print("Temperature: %-3.1f C" % tempHumid.temperature)
    # print("Humidity: %-3.1f %%" % tempHumid.humidity)

    ### Time Gathering ###
    time_stamp = time.strftime('%x %X')
    elapsed_time = time.time() - start_time  #seconds
    elapsed_time = round(elapsed_time, 3)

    ### Data List ###
    chill_data["time_stamp"] = time_stamp
    chill_data["elapsed_time"] = elapsed_time
    chill_data["tempC_probe"] = tempC_probe
    chill_data["tempF_probe"] = tempF_probe
    chill_data["tempC_amb"] = tempC_amb
    chill_data["tempF_amb"] = tempF_amb
    chill_data["humidity"] = humidity

    #info to print to screen
    print("---------------------")
    print(tempC_probe, "probe temp deg C")
    print(tempF_probe, "probe temp deg F")
    print(tempC_amb, "ambient temp deg C")
    print(tempF_amb, "ambient temp deg F")
    print(humidity, "ambient humidity %")
    print(elapsed_time, "sec, time elapsed")
    print("---------------------")

    #write data to file
    with open(file_name, 'a') as file:
        #writes dictionary in csv format
        w = csv.DictWriter(file, chill_data.keys())
        w.writerow(chill_data)

    sio.emit('data', chill_data)

#run checks
if len(sys.argv) < 2:
    print("Give me a file name argument i.e. 'python chill.py test.csv'")
    sys.exit()
elif ".csv" not in sys.argv[1]:
    print("Nedd a .csv brah")
    sys.exit()
else:
    file_name = sys.argv[1]

    ### Init Data ###
    chill_data = {
        "time_stamp": "",
        "elapsed_time": 0,
        "tempC_probe": 0,
        "tempF_probe": 0,
        "tempC_amb": 0,
        "tempF_amb": 0,
        "humidity": 0
    }

    #add column titles to file
    with open(file_name, 'w') as file:
        w = csv.DictWriter(file, chill_data.keys())
        w.writeheader()

    ##for probe DS18 sensor ##
    THERM = W1ThermSensor()

    ##for ambient DHT11 temp & humidity sensor ##
    # read data using pin 12
    DHT11 = dht11.DHT11(pin=12)

    sio = socketio.Client()
    sio.connect('http://192.168.1.180:5000')
    read_temp()
    sio.wait()

    @sio.event
    def connect():
        print("Client connected!")

    @sio.event
    def disconnect():
        print("Client disconnected!")
