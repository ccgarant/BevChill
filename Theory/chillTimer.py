''' This file determines the time it takes for the beverage to reach the optimal temperature based on heat transfer physics'''

# import container
# import beverage
import math as m
import numpy as np


#R1

#R2

#R3

#R4


# R_total = R1 + R2 + (1/R3 + 1/R4)**(-1)
# dTdt = ((-T1 - Tinf)/R_total)*(1/(rho*V*c))

#Y = a*exp(b*t)+c*exp(d*t)

a = 14.99
b = -2.404e-4
c = 279
d = -2.719e-7
# t = np.linspace(0,5000,5001)
t = 100


T = a*m.exp(b*t)+c*m.exp(d*t)
T_C = T - 273.15 #[celcius] conversion from K to C
print(f'bev temp F {T}')
print(f'bev temp C {T_C}')