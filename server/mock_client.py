import threading
import sys, getopt
import time
import csv
import socketio
import pprint

def collect_data_and_send():
    """
    Gathers data from the sensors, writes data to output file,
    emits data to the server.

    Invokes thread that executes a function after a 'sleep_time' interval has passed

    """

    threading.Timer(sleep_time, read_temp).start()
    
    ### Data Gathering ###
    tempC_amb = 0
    tempF_amb = 32
    humidity = 75
    tempC_probe = 0
    tempF_probe = 32

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
    """
    Checks the arguments passed to the program.

    Will only procede with running the porgram if the correct
    arguments are present i.e -i <server ip> -o <outputfile.csv>

    Parameters
    ----------
    argv : list[str]
    list of arguments given when the program was executed

    Returns
    ----------
    ip, output_file_name : touple
    the server ip and the output file name
    """

    ip_address = None
    output_file_name = None
    try:
        opts, args = getopt.getopt(argv,"hi:o:",["ip=","ofile="])
    except getopt.GetoptError:
        print('usage: chill.py -i <server ip> -o <outputfile.csv>')
        sys.exit(2)

    for opt, arg in opts:
        ### Help Argument ###
        if opt == '-h':
            print('usage: chill.py -i <server ip> -o <outputfile.csv>')
            sys.exit()
        
        ### Server IP Argument ###
        elif opt in ("-i", "--ip"):
            ip_address = arg

        ### Output File Name Argument ###
        elif opt in ("-o", "--ofile"):
            if '.csv' in arg:
                output_file_name = arg
            else:
                print('need a .csv output file brah!')
                
    if ip_address and output_file_name:
        return ip_address, output_file_name
    else:
        print('error parsing arguments')
        print('usage: chill.py -i <server ip> -o <outputfile.csv>')
        sys.exit()

if __name__ == "__main__":
    ip, test_file_name = check_arguments(sys.argv[1:])

    #initialization
    start_time = time.time()
    sleep_time = 10  #time between temperature readings

    ### Init Data Structure ###
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
 
    sio = socketio.Client()
    @sio.event
    def connect():
        print("Connected to Server!")
    @sio.event
    def disconnect():
        print("Disconnected from Server!")

    #connect to server and start reading data
    sio.connect('http://'+ip+':5000')
    collect_data_and_send()