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

        ''' fluid properities '''

        '''geometry properties'''

        '''material properties'''

        #material density rho
        self.rho = 1000 * beverage['specific_gravity']  #[kh/m^3]

        #thermal resistance ***check***
        self.k = 0.5985 #[W/m*K]

        #thermal heat capacity ***check***
        self.C = 4189 #[J/kg*K]






