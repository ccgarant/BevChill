''' This file determines the time it takes for the beverage to reach the optimal temperature based on heat transfer physics'''

#import
from peroni_bottle import peroni_bottle
from thermalResistance import *
from scipy.integrate import odeint, solve_ivp
import matplotlib.pyplot as plt
from numpy import linspace, exp, arange


# R_total = R1 + R2 + (1/R3 + 1/R4)**(-1)
t_hrs = 4
t_sec = t_hrs*60*60  #60 min/hr * 60 sec/min = sec/hr
t_eval = arange(0,t_sec+1,1)
T_init = T_atm

#heat transfer equation ,first order ordinary differential equation (ODE)
#see scipy.integrate.solve_ivp docs
def dTdt(t,T):
    return -(T - T_inf)/((R_total)*(beer.rho*bottle.volume*beer.C))


#sol = solve_ivp(dTdt,[0, t_sec],[T_init],max_step=60)
sol = solve_ivp(dTdt,[0, t_sec],[T_init],t_eval=t_eval)

#print(sol)
print(sol.nfev)
#print(sol.t)
#print(sol.y[0])

t = sol.t       #seconds
t_hrs = t/3600  #hours
T = sol.y[0]

'''best fit line work'''
#Y = a*exp(b*t)+c*exp(d*t)

a = 14.99
b = -2.404e-4
c = 279
d = -2.719e-7

T_approx = a*exp(b*t)+c*exp(d*t)
T_C = T - 273.15 #[celcius] conversion from K to C
#print(f'bev temp F {T}')
#print(f'bev temp C {T_C}')


plt.plot(t_hrs, T, 'b', label='ode')
plt.plot(t_hrs, T_approx,'r',label='approx')
plt.legend(loc='best')
plt.xlabel('time [hrs]')
plt.ylabel('Temp [degK]')
plt.title('Bev Temp vs Time')
#plt.figsize=(10,6)
plt.grid()
plt.show()
