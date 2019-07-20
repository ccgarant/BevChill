#Plots the recorded bev chill data

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns; sns.set()
%matplotlib inline

def bevPlot(data_file_csv):
    str(data_file_csv)
    if ".csv" not in data_file_csv:
        print('add .csv extension')
    p = pd.read_csv(data_file_csv, names=['datetime','elapsed time','T deg C','T deg F'])
    p.plot(x='elapsed time',y='T deg C',figsize=(15,10),lw=4,title='Bev Chill Plot')