# from w1thermsensor import W1ThermSensor
import socketio
import threading
import sys
import time

# standard Python
sio = socketio.Client()

@sio.event
def connect():
    print("I'm connected!")

@sio.event
def disconnect():
    print("I'm disconnected!")

start_time = time.time()
sleep_time = 10 #seconds, time between temperature readings

def read_temp():
  threading.Timer(sleep_time, read_temp).start()
  # temp_in_celsius = sensor.get_temperature()
  # temp_in_fahrenheit = sensor.get_temperature(W1ThermSensor.DEGREES_F)
  temp_in_celsius = 75
  temp_in_fahrenheit = 75

  #data
  time_stamp = time.strftime('%x %X')
  elapsed_time = time.time() - start_time
  elapsed_time = round(elapsed_time,3)
        
  data = [
      time_stamp, 
      elapsed_time, 
      temp_in_celsius,
      temp_in_fahrenheit
  ]

  #info to print to screen
  print("---------------------")
  print(temp_in_celsius, " deg C")
  print(temp_in_fahrenheit, " deg F")
  print(elapsed_time, " sec, time elapsed")
  print("---------------------")
  
  #write data to file
  with open(file_name, 'a') as file:
    file.write(str(data) + "\n")

  #send data to server
  sio.emit('newnumber', {'number': 69}, namespace='/test')

#run checks
if len(sys.argv) < 2:
  print("Give me a file name argument i.e. 'python chill.py test001.csv'")
  sys.exit()
elif ".csv" not in sys.argv[1]:
  print("Nedd a .csv brah")
  sys.exit()
else:
  file_name = sys.argv[1]
  # sensor = W1ThermSensor()
  sio.connect('http://192.168.1.180:5000')
  read_temp()
