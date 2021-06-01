from numpy import * 
from vpython import *
B_ground = 45*10**(-3)
u0 = 4*pi*10**(-7)
R_earth,R_earth_core = 6371*10**3, 1220 * 1E3
# i_earth = 4*(2**0.5)*B_ground*R_earth/u0
mu = 9.15*1E-4/(u0*R_earth**3)
V_solar_storm = vec(0,0,0)
Q_electric = -1.602 * 1E-19
h , N , k= 1E-2 ,50, 1E6
w = vec(0,0,0)
c = 299792458 
n=250
# theta=array([2*pi*i/n for i in range(n)])
# L_ds=2*pi*R_earth_core /n 
# L_ds_vec =[vec(L_ds*sin(theta[i]),0,L_ds*cos(theta[i])) for i in range(n)]
# L_ds_pos=[R_earth_core * vec(cos(theta[i]),0,sin(theta[i])) for i in range(n)]


scene = canvas(title='magnetic field of earth ', height=1000, width=1000, center = vec(0 , 0 , 0))
scene.lights = []
scene.ambient=color.gray(0.99)
pos = zeros([2,N,N])
for i in range(0,N):
    for j in range(0,N):
        pos[0,i,j] = j*k
        pos[1,i,j] = i*k

pos -= (N*k/2)
pos_x = pos[0]
pos_y = pos[1]

# print (pos_x)
# print (pos_y)

earth = sphere( pos = vec( 0,0,0) , 
    radius = R_earth , texture={'file':textures.earth}) # earth_orbit['r']??

# def BiotSavart(ds_vec,vec_r):
#     return u0 * i_earth * ds_vec.cross(vec_r.norm())/(vec_r.mag**2 * 4*pi)
def B_by_solar_storm(p):
    theta = acos (dot(V_solar_storm,p-w) / V_solar_storm.mag / (p-w).mag)
    E = Q_electric * (1-V_solar_storm**2/c**2) * (p-w) / (4*pi*u0) / (1-V_solar_storm**2 * sin(theta)**2 / c**2 )**1.5 /(p-w)**3
    B = V_solar_storm.cross(E/c**2)
def mag_field_at_p(p):

    c = mu/(4*pi*(p.x**2.0+p.y**2.0+p.z**2.0)**1.5)
    B_earth = c*(3*(dot(vec(0,mu,0),norm(p))) * norm(p) - vec(0,mu,0))

    return B_earth


for i in range(0, N):
    for j in range(0, N):
        point_pos = vec(pos_x[i,j],pos_y[i,j],0)
        if (point_pos.x ** 2 + point_pos.y **2 <= (1.1*R_earth) **2 ):
            print( "in if")
            continue
        B = mag_field_at_p(point_pos)
        ar = arrow(pos = vec( pos_x[i,j], pos_y[i,j], 0), axis = 2E63 * B, 
        shaftwidth = 8E4, color=color.red)
        print("B = ", 2E63 * B)
        # print("B.mag = ",0.1* mag(1E7 * B))

