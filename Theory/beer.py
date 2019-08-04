''' This file defines the beverage fluid properties necessary to define the heat transfer'''

class Beverage:
    """
    A class used to represent the beverage fluid
    properties
    
    
    Attributes
    ___________
    
    
    Methods
    ___________
    
        
    """
    
    #init
    def __init__(self,beverage):
        self.container_type = beverage['beverage_type']
        if self.container_type == 'beer':
            return self.beer(beverage)
        else:
            print('container type not available yet')

    def beer(self,beverage):
        '''defines geometric and material attributes for the
        container type'''

        '''fluid properities'''
        #Assumption, properties of water at 275 degK (37.6 degF)
        #Table A.6 and A.4, Ref[1]
        
        #volumetric thermal expansion, Beta
        self.beta = 46/10**6 #[m**3]
        
        #viscosity, u
        self.u = 1652/10**6
        
        #thermal resistance ***check***
        self.k = 0.5985 #[W/m*K]
        
        #material density rho
        self.rho = 1000 * beverage['specific_gravity']  #[kh/m^3]

        #thermal heat capacity ***check***
        self.C = 4211 #[J/kg*K]

        #dynamic viscosity, v
        self.v = self.u/self.rho  #[m**2/s]

        #alpha
        self.alpha = 1.3631e-7


'''References:

    [1] Fundamentals of Heat and Mass Transfer, 6th Edition, Incropera, 2007
    
    
'''







