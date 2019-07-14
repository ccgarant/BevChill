from w1thermsensor import W1ThermSensor
import threading
import sys

def read_temp():
  threading.Timer(2.0, read_temp).start()
  temp_in_celsius = sensor.get_temperature()
  temp_in_fahrenheit = sensor.get_temperature(W1ThermSensor.DEGREES_F)
  print("---------------------")
  print(temp_in_celsius)
  print(temp_in_fahrenheit)
  print("---------------------")
  with open(file_name, 'a') as file:
    file.write(str(temp_in_celsius) + ",")

if len(sys.argv) < 2:
  print("Give me a file name argument")
  sys.exit()
elif ".csv" not in sys.argv[1]:
  print("Nedd a .csv brah")
  sys.exit()
else:
  file_name = sys.argv[1]
  seconds = 2.0
  sensor = W1ThermSensor()
  read_temp()
