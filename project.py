from numpy import *
from vpython import *
B_ground = 45*10**(-3)
u0 = 4*pi*10**(-7)
R_earth = 6371*10**3
i_earth = 4*(2**0.5)*B_ground*R_earth/u0
earth = sphere( pos = vec( 0,0,0) , 
    radius = R_earth , texture={'file':textures.earth}) # earth_orbit['r']??

def 

