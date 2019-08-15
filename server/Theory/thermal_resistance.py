import math as m

''' This file calculates the thermal resistance properties necessary to define the heat transfer'''

class ThermalResistance:
    """
    A class used to calculate the thermal resistance properties
    
    Attributes
    beverage
    container 
    ___________
    
    
    Methods
    ___________
    
        
    """
    
    def __init__(self, beverage, container, start_temp, atm_temp):
        self.container = container
        self.beverage = beverage

        '''Assumptions'''
        #For now assume freezer temp T_inf = 273.15K (0 deg C, 32 deg F)
        self.T_atm = atm_temp + 273.15
        self.T_inf = 276  #[degK] 37.6 degF
        self.T_s   = start_temp + 273.15
        self.gravity = 9.81 #m/s**2, gravity
        self.sigma = 5.67e-8  #[W/(m**2*degK**4)] radiation coefficient sigma
        
        print('\nInitial Conditions')
        print('------------------------------')
        print(f'T_atm {self.T_atm} degK')
        print(f'T_inf {self.T_inf} degK')
        print(f'T_s {self.T_s} degK')
        print(f'gravity {self.gravity} m/s^2')
        print(f'radiation coefficient sigma {self.sigma} [W/(m**2*degK**4)]')
        print('------------------------------\n')

    #Find the Pr number empirically from the following equation Eq 9.20 ref [1]
    def g(sefl, Pr):
        top = (.75*Pr)**(1/2)
        bottom = (.609+1.221*Pr**(1/2)+1.238*Pr)**(1/4)
        g = top/bottom
        return g

    def get_T_atm(self):
        return self.T_atm

    def get_T_inf(self):
        return self.T_inf

    def get_T_init(self):
        return self.T_s

    def calculate_total_resistance(self):
        ''' 
        # Total resistance
        # R_total = R1 + R2 + (1/R3 + 1/R4)**(-1)
        '''

        '''R1, internal convection from beverage'''
        #R1_conv_int = 1/(h_inner*A_surface)
        #R1_conv_int = 1/(h_inner*2*pi*r*H)
        #Rayleigh Number, Ra, dimensionless number associated with bouyancy-driven flow
        Ra = (self.gravity*self.beverage.beta*(self.T_s-self.T_inf)*self.container.H_equiv**3)/(self.beverage.v*self.beverage.alpha)

        #solving for internal convection coefficient h_inner
        h_inner = (self.beverage.k/self.container.H_equiv)*0.55*Ra**(1/4)  #[W/(m**2*degK)]

        #therefore the resistance R1 of convection is
        R1_conv_int = 1/(h_inner * self.container.A_inner)

        '''R2, conduction thru container wall'''
        #R2_cond_wall = L/(k*A_surface) = ln(r_2/r_1)/(2*pi*k*L) for radial cylinderical coordinates
        R2_cond_wall = m.log(self.container.r_outter/self.container.r_inner)/(2*m.pi*self.container.k*self.container.thickness)

        '''R3, external convection from air'''
        #For h_outter
        #Pradult number interpolated from Table A.4 Ref [1]
        Pr = ((.707-.720)/(300-250))*(self.T_inf - 250) + .720

        #volumetric thermal expansion coefficient, B for beta, for ideal air gas
        B_air = 1/self.T_inf

        #Grahsof Number, Gr, a measure of the ratio of buoyancy forces to the viscous forces
        #dynamic viscousity of air, u/rho
        v_air = ((15.89-11.44)/(300-250)*(self.T_inf-250)+11.44)*10**-6
        Gr = (self.gravity*B_air*(self.T_atm-self.T_inf)*self.container.H_equiv**3)/v_air**2
        Nu = (4/3)*(Gr/4)**(1/4)*self.g(Pr)

        #fluid air, freezer, coefficient of conduction, Table A.4 Ref[1]
        k_air = ((26.3-22.3)/(300-250)*(self.T_inf-250)+22.3)*10**-3

        #solving for h_outter is
        h_outter = (k_air/self.container.H_equiv)*Nu  #[W/(m**2*degK)]        

        #R3 thermal resistance for external convection is
        R3_conv_ext = 1/(h_outter * self.container.A_outter)

        '''R4, external radiation'''
        #R4_rad = 1/(h_rad*A_outter)
        #radiation coefficient of convection
        h_rad = self.container.e*self.sigma*(self.T_s**4-self.T_inf**4)
        R4_rad = 1/(h_rad*self.container.A_outter)

        '''R_total Resistance'''
        # R_total = R1_conv_int + R2_cond_wall + (1/R3_conv_ext + 1/R4_rad)**(-1)
        R_total = R1_conv_int + R2_cond_wall + (1/R3_conv_ext + 1/R4_rad)**(-1)
        
        print('Calculations')
        print('------------------------------')
        print(f'Ra is {Ra}')
        print(f'h_inner is {h_inner}')
        print(f'R1 is {R1_conv_int}')
        print(f'R2 is {R2_cond_wall}')
        print(f'h_outter is {h_outter}')
        print(f'R3 is {R3_conv_ext}')
        print(f'h_rad is {h_rad}')
        print(f'R4 is {R4_rad}')
        print(f'R_total is {R_total}')
        print('------------------------------\n')
        return R_total


'''References:

    [1] Fundamentals of Heat and Mass Transfer, 6th Edition, Incropera, 2007
    
    
'''







