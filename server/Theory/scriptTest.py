#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug  3 12:10:36 2019

@author: christophegarant
"""

from peroni_bottle import peroni_bottle
from thermal_resistance import *
from scipy.integrate import odeint, solve_ivp
import matplotlib.pyplot as plt
from numpy import linspace

#(T - T_inf)/R_total = (beer.rho*bottle.volume*beer.C)*dTdt
#dTdt = ()/(R_total*(beer.rho*bottle.volume*beer.C))

x = (beer.rho*bottle.volume*beer.C)
print(x)
