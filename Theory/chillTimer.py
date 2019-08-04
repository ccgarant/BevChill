''' This file determines the time it takes for the beverage to reach the optimal temperature based on heat transfer physics'''

#import
from thermalResistance import *


##R1
#print(f'R1 is {R1_conv_int} \n')
##R2
#print(f'R2 is {R2_cond_wall} \n')
##R3
#print(f'R3 is {R3_conv_ext} \n')
##R4
#print(f'R4 is {R4_rad} \n')
##R_total
#print(f'R_total is {R_total} \n')

# R_total = R1 + R2 + (1/R3 + 1/R4)**(-1)
# dTdt = ((-T1 - Tinf)/R_total)*(1/(rho*V*c))

#Y = a*exp(b*t)+c*exp(d*t)

a = 14.99
b = -2.404e-4
c = 279
d = -2.719e-7
# t = np.linspace(0,5000,5001)
#t = np.arange(0,2*60*60+1) # 2 hours in seconds
time = 2*60*60

T = a*m.exp(b*time)+c*m.exp(d*time)
T_C = T - 273.15 #[celcius] conversion from K to C
print(f'bev temp F {T}')
print(f'bev temp C {T_C}')
