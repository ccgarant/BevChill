''' This file defines the beverage container material properties to define the heat transfer '''

class Container:
    """
    A class used to represent the beverage container properties
    
    
    Attributes
    ___________
    
    
    Methods
    ___________
    
    
    
    """
    
    def __init__(self,container_type):
        self.container_type = container_type
        if self.container_type == 'bottle':
            return self.bottle()
        else:
            print('container type not available yet')
        
    def bottle(self):
        self.r_inner = .0273  #m
        self.r_outter = .0309 #m
        self.V_volume = 3.55e-4        
        
#     def containerAttributes(self, r_in, r_out, V_volume):
#         self.
        
    # Geometric Properties
    
    # Material Properties
#     rho_glass = 2500 #[kg/m^3]
    # k = 1.4 #[W/m*K]
    # C = 750 #[J/kg*K]
    # e = .93
    # A_inner = 2*np.pi*r_inner*H_equiv
    # A_outter = 2*np.pi*r_outter*H_equiv
        
