from scipy.integrate import odeint, solve_ivp
import matplotlib.pyplot as plt
from numpy import linspace, exp, arange
import datetime
from Theory.container import Container
from Theory.beer import Beverage
from Theory.thermal_resistance import ThermalResistance


''' This file determines the time it takes for the beverage to reach the optimal temperature based on heat transfer physics'''

class ChillTimer:
    """
    Determines the time it takes for the beverage to reach the optimal temperature
    
    
    Attributes
    T: Temperature values in K indexed by second
    ___________
    
    
    Methods

    ___________
    
        
    """
    
    def __init__(self, drink, start_temp, atm_temp):
        self.drink = drink
        self.bottle = Container(drink)
        self.beer = Beverage(drink)
        self.resistance = ThermalResistance(self.beer, self.bottle, start_temp, atm_temp)
        self.R_total = self.resistance.calculate_total_resistance()
        self.T_atm = self.resistance.get_T_atm()
        self.T_inf = self.resistance.get_T_inf()
        self.t_hrs = 4
        self.t_sec = self.t_hrs*60*60  #60 min/hr * 60 sec/min = sec/hr
        self.t_eval = arange(0,self.t_sec+1,1)
        self.T_init = self.resistance.get_T_init()

        sol = solve_ivp(self.dTdt,[0, self.t_sec],[self.T_init],t_eval=self.t_eval)

        t = sol.t       #seconds
        time = t/3600  #hours
        T = sol.y[0]    #solution temperatures

        '''best fit line work'''
        #Y = a*exp(b*t)+c*exp(d*t)
        a = 14.99
        b = -2.404e-4
        c = 279
        d = -2.719e-7
        T_approx = a*exp(b*t)+c*exp(d*t)

        #[celcius] conversion from K to C
        self.T_C = T - 273.15 
        T_approx_C = T_approx - 273.15

        # plt.plot(time, self.T_C, 'b', label='ode')
        # plt.plot(time, T_approx_C,'r',label='approx')
        # plt.legend(loc='best')
        # plt.xlabel('time [hrs]')
        # plt.ylabel('Temp [degC]')
        # plt.title('Bev Temp vs Time')
        # #plt.figsize=(10,6)
        # plt.grid()
        # plt.show()

    def get_temperature_at_second(self, second):
        return round(self.T_C[second], 3)

    def get_remaining_time_until_temp(self, desired_temp, curr_temp):
        desired_time = min(range(len(self.T_C)), key=lambda i: abs(self.T_C[i]-desired_temp))
        curr_time = min(range(len(self.T_C)), key=lambda i: abs(self.T_C[i]-curr_temp))
        return str(datetime.timedelta(seconds=desired_time - curr_time))

    def get_chill_zone(self, curr_temp):
        if curr_temp > self.drink['warm']:
            return "Piss Warm"
        elif curr_temp > self.drink['good']:
            return "Warm"
        elif curr_temp > self.drink['perfect']:
            return "Good"
        elif curr_temp > self.drink['frozen']:
            return "Perfect"
        else:
            return "Frozen"
    
    #heat transfer equation ,first order ordinary differential equation (ODE)
    #see scipy.integrate.solve_ivp docs
    def dTdt(self,t,T):
        return -(T - self.T_inf)/((self.R_total)*(self.beer.rho*self.bottle.volume*self.beer.C))



