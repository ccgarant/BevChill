''' This file defines the beverage fluid properties necessary to define the heat transfer'''

class Beverage:
    
    def __init__(self,container_type):
        self.data = []
        self.container_type = container_type
        self.r_inner = .0273  #m
        self.r_outter = .0309 #m
        self.V_volume = 3.55e-4