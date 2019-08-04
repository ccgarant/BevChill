import math as m

from peroni_bottle import peroni_bottle
from container import Container
from beer import Beverage


bottle = Container(peroni_bottle)
beer = Beverage(peroni_bottle)


''' total resistance
# R_total = R1 + R2 + (1/R3 + 1/R4)**(-1)
'''

'''Assumptions'''
#For now assume freezer temp T_inf = 273.15K (0 deg C, 32 deg F)
T_atm = 294  #[degK] 69.7 degF
T_inf = 276  #[degK] 37.6 degF
T_s   = 294  #[degK] 69.7 degF - for now assume T_s = T_inf
gravity = 9.81 #m/s**2, gravity

'''R1, internal convection from beer'''
#R1_conv_int = 1/(h_inner*A_surface)
#R1_conv_int = 1/(h_inner*2*pi*r*H)

#Rayleigh Number, Ra, dimensionless number associated with bouyancy-driven flow
Ra = (gravity*beer.beta*(T_s-T_inf)*bottle.H_equiv**3)/(beer.v*beer.alpha)
print(f'Ra is {Ra}')

#solving for internal convection coefficient h_inner
h_inner = (beer.k/bottle.H_equiv)*0.55*Ra**(1/4)  #[W/(m**2*degK)]
print(f'h_inner is {h_inner}')

#therefore the resistance R1 of convection is
R1_conv_int = 1/(h_inner * bottle.A_inner)
print(f'R1 is {R1_conv_int} \n')





'''R2, conduction thru container wall'''
#R2_cond_wall = L/(k*A_surface) = ln(r_2/r_1)/(2*pi*k*L) for radial cylinderical coordinates

R2_cond_wall = m.log(bottle.r_outter/bottle.r_inner)/(2*m.pi*bottle.k*bottle.thickness)
print(f'R2 is {R2_cond_wall} \n')




'''R3, external convection from air'''
#For h_outter


#Pradult number interpolated from Table A.4 Ref [1]
Pr = ((.707-.720)/(300-250))*(T_inf - 250) + .720

#Find the Pr number empirically from the following equation Eq 9.20 ref [1]
def g(Pr):
    top = (.75*Pr)**(1/2)
    bottom = (.609+1.221*Pr**(1/2)+1.238*Pr)**(1/4)
    g = top/bottom
    return g

#volumetric thermal expansion coefficient, B for beta, for ideal air gas
B_air = 1/T_inf

#Grahsof Number, Gr, a measure of the ratio of buoyancy forces to the viscous forces

#dynamic viscousity of air, u/rho
v_air = ((15.89-11.44)/(300-250)*(T_inf-250)+11.44)*10**-6

Gr = (gravity*B_air*(T_atm-T_inf)*bottle.H_equiv**3)/v_air**2
#print(f'Gr number is {Gr}')

Nu = (4/3)*(Gr/4)**(1/4)*g(Pr)

#fluid air, freezer, coefficient of conduction, Table A.4 Ref[1]
k_air = ((26.3-22.3)/(300-250)*(T_inf-250)+22.3)*10**-3

#solving for h_outter is
h_outter = (k_air/bottle.H_equiv)*Nu  #[W/(m**2*degK)]
print(f'h_outter is {h_outter}')

#R3 thermal resistance for external convection is
R3_conv_ext = 1/(h_outter * bottle.A_outter)
print(f'R3 is {R3_conv_ext} \n')

'''R4, external radiation'''
#R4_rad = 1/(h_rad*A_outter)


#radiation coefficient sigma
sigma = 5.67e-8  #[W/(m**2*degK**4)]

#radiation coefficient of convection
h_rad = bottle.e*sigma*(T_s**4-T_inf**4)
print(f'h_rad is {h_rad}')

R4_rad = 1/(h_rad*bottle.A_outter)
print(f'R4 is {R4_rad} \n')


'''R_total Resistance'''

# R_total = R1_conv_int + R2_cond_wall + (1/R3_conv_ext + 1/R4_rad)**(-1)

R_total = R1_conv_int + R2_cond_wall + (1/R3_conv_ext + 1/R4_rad)**(-1)
print(f'R_total is {R_total} \n')
