# imports
# import RPi.GPIO as GPIO
# from w1thermsensor import W1ThermSensor
import threading
import sys, getopt
import time
import csv
import socketio
import pprint

# import from other file
# sys.path.append('/home/pi/BevChill/DHT11_Python')
# import dht11
# GPIO.setwarnings(True)
# GPIO.setmode(GPIO.BCM)

def read_temp():
    threading.Timer(sleep_time, read_temp).start()
    
    ### Data Gathering ###
    # tempHumid = DHT11.read()
    # tempC_amb = tempHumid.temperature
    # tempF_amb = (tempC_amb*1.8)+32
    # humidity = tempHumid.humidity
    # tempC_probe = THERM.get_temperature()
    # tempF_probe = THERM.get_temperature(W1ThermSensor.DEGREES_F)
    tempC_amb = 0
    tempF_amb = 32
    humidity = 69
    tempC_probe = 0
    tempF_probe = 32
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
    print("\nSending Data")
    print("-----------------------------------------------")
    pprint.pprint(chill_data)
    print("-----------------------------------------------\n")

    #write data to file
    with open(test_file_name, 'a') as file:
        #writes dictionary in csv format
        w = csv.DictWriter(file, chill_data.keys())
        w.writerow(chill_data)

    sio.emit('data', chill_data)

def check_arguments(argv):
    inputfile = ''
    outputfile = ''
    try:
        opts, args = getopt.getopt(argv,"hi:o:",["ifile=","ofile="])
    except getopt.GetoptError:
        print('test.py -i <inputfile> -o <outputfile>')
        sys.exit(2)

    for opt, arg in opts:
        if opt == '-h':
            print('test.py -i <inputfile> -o <outputfile>')
            sys.exit()
        elif opt in ("-i", "--ifile"):
            inputfile = arg
        elif opt in ("-o", "--ofile"):
            outputfile = arg

    print('Input file is ' + inputfile)
    print('Output file is ' + outputfile)
    return inputfile, outputfile

if __name__ == "__main__":
    ip, test_file_name = check_arguments(sys.argv[1:])

    #initialization
    start_time = time.time()
    sleep_time = 10  #time between temperature readings

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
    with open(test_file_name, 'w') as file:
        w = csv.DictWriter(file, chill_data.keys())
        w.writeheader()

    ##for probe DS18 sensor ##
    # THERM = W1ThermSensor()

    ##for ambient DHT11 temp & humidity sensor ##
    # read data using pin 12
    # DHT11 = dht11.DHT11(pin=12)

    sio = socketio.Client()
    sio.connect('http://'+ip+':5000')
    read_temp()
    sio.wait()

    @sio.event
    def connect():
        print("Client connected!")

    @sio.event
    def disconnect():
        print("Client disconnected!")

