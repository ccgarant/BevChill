''' 
# Test Plots on Recorded Temperature Data

This script reads the recorded data into a pandas DataFrame and does a quick plot to visualize the data, as well as quick analysis

in IPython, use "%run Test_Plot.py

'''

import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns; sns.set()


#determine the data test file to read
file = 'Perroni_bottle_20190725.csv'
file_split = file.split('.')
file_name = file_split[0] # e.g. 'DogFishHead_SeaQuenchAle_Can_20190726'

#start in directory /Documents/Github/BevChill
base_dir = os.getcwd()
os.chdir("TestResults")

#read in data as a dataframe
p = pd.read_csv(file,names=['time_stamp','elapsed_time','tempC_probe',
       'tempF_probe','tempC_amb','tempF_amb','humidity %'])

#preprocessing cleaning data

#remove brackets at the beginning and end of the list
p['time_stamp'] = p['time_stamp'].str.strip("[")
p['humidity %'] = p['humidity %'].str.strip("]")

#ambient freezer air temp, plot of intermittent readings
p[:30].plot(x='elapsed_time',y='tempC_amb',figsize=(10,5),lw=4,title=file_name)

#ambient sensor is intermittent, randomly writes 0, this 
#for now smooths the data. It replaces all 0s as NaN then 
#interpolates the gaps with a cubic best fit polynomial
p_nan = p['tempC_amb'].replace(0,np.NaN)
p_smoothed = p_nan.interpolate(method='akima')
p['tempC_amb'] = p_smoothed

#quick plots

#probe beer fluid temp inside container
p.plot(x='elapsed_time',y='tempC_probe',figsize=(10,5),lw=4,title=file_name)

#ambient freezer air temp
p.plot(x='elapsed_time',y='tempC_amb',figsize=(10,5),lw=4,title=file_name)

#freezer and beer temp
p.plot(x='elapsed_time',y=['tempC_probe','tempC_amb'],figsize=(10,5),lw=4,title=file_name)

#freezer and beer temp, first 30 rows
p[:30].plot(x='elapsed_time',y=['tempC_probe','tempC_amb'],figsize=(10,5),lw=4,title=file_name + ', first 30 rows')

#'''matplotlib plots'''
#plt.plot(p.elapsed_time, p.tempC_probe, 'b')
#plt.plot(p.elapsed_time, p.tempC_amb, 'r')
#plt.legend(loc='best')
#plt.xlabel('time [sec]')
#plt.ylabel('Temp [degC]')
#plt.title('Bev Temp vs Time')
##plt.figsize=(10,6)
#plt.grid()
#plt.show()

os.chdir(base_dir)



