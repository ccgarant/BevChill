''' This file defines the beverage container material properties to define the heat transfer '''

class Container:
    """
    A class used to represent the beverage container geometric and
    material properties
    
    The expected container_type arguement is a String.
    
    The supported container_type are:
    - bottle
    - can (coming soon)
    
    Example:
    b = Container('bottle')
    c = Container('can')
    
    Attributes
    ___________
    
    self.r_inner     #bottle cylinder inner radius
    self.r_outter    #bottle cylinder inner radius
    self.volume      #bottle fluid volume capacity
    self.thickness   #bottle wall thickness
    self.H_equiv     #fluid volume equivalent cylindrical height
    self.A_inner     #inner surface area
    self.A_outter    #outter surface area
    self.rho_glass   #material density rho
    self.k           #thermal resistance ***check***
    self.C           #thermal heat capacity ***check***
    self.e           #radiation emmisivity
    
    
    Methods
    ___________
    
    
    
    """

    #init
    def __init__(self,container_type):
        self.container_type = container_type
        if self.container_type == 'bottle':
            return self.bottle()
        else:
            print('container type not available yet')
        
    def bottle(self):
        '''defines geometric and material attributes for the
            container type'''
        
        '''geometry properties'''

        #bottle cylinder inner radius
        self.r_inner = .0273  #m
        
        #bottle cylinder inner radius
        self.r_outter = .0309 #m
        
        #bottle fluid volume capacity
        self.volume = 3.55e-4 #m
        
        #bottle wall thickness
        self.thickness = self.r_outter-self.r_inner #m
        
        from math import pi
        #fluid volume equivalent cylindrical height
        #note: there is a portion of fluid in the bottle neck
        #the equivalent height assumes all the fluid is in the main
        #body in an ideal cylinder of radius inner.
        self.H_equiv = self.volume / (pi * self.r_inner**2)
        
        #inner surface area
        self.A_inner = 2 * pi * self.r_inner * self.H_equiv
        
        #outter surface area
        self.A_outter = 2 * pi * self.r_outter * self.H_equiv
        
        '''material properties'''
        
        #material density rho
        self.rho_glass = 2500 #[kg/m^3]
        
        #thermal resistance ***check***
        self.k = 1.4 #[W/m*K]
        
        #thermal heat capacity ***check***
        self.C = 750 #[J/kg*K]
        
        #radiation emmisivity
        self.e = .93
        


