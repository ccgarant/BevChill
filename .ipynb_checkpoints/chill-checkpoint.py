from w1thermsensor import W1ThermSensor
import threading
import sys
import time

start_time = time.time()
sleep_time = 10 #seconds, time between temperature readings

def read_temp():
  threading.Timer(sleep_time, read_temp).start()
  temp_in_celsius = sensor.get_temperature()
  temp_in_fahrenheit = sensor.get_temperature(W1ThermSensor.DEGREES_F)
  print("---------------------")
  print(temp_in_celsius, " deg C")
  print(temp_in_fahrenheit, " deg F")
  print("---------------------")

  #data
  
  time_stamp = time.strftime('%x %X')
  elapsed_time = time.time() - start_time  #seconds
  data = []
  data = [
      time_stamp, 
      elapsed_time, 
      temp_in_celsius,
      temp_in_fahrenheit
  ]


  #write data to file
  with open(file_name, 'a') as file:
    file.write(str(data) + "\n")

if len(sys.argv) < 2:
  print("Give me a file name argument")
  sys.exit()
elif ".csv" not in sys.argv[1]:
  print("Nedd a .csv brah")
  sys.exit()
else:
  file_name = sys.argv[1]
  seconds = sleep_time
  sensor = W1ThermSensor()
  read_temp()
