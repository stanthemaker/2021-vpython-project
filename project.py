from numpy import * 
from vpython import *
import numpy as np
c = 299792458
B_ground = 45*1E-3
mu0 = 4*pi* 1E-7
e0 = 1/(c**2 * mu0)
R_earth,R_earth_core = 6371*1E3, 1220 * 1E3
# i_earth = 4*(2**0.5)*B_ground*R_earth/mu0
mu = B_ground* 2 *pi * (2*R_earth_core**2)**1.5 / mu0
V_wind = vec(4.5E5,0,0)
Q_electric = -1.602 * 1E-19 * 1E20
h , N , k , n = 1E-2 ,30, 1E6 , 100
 

# theta=array([2*pi*i/n for i in range(n)])
# L_ds=2*pi*R_earth_core /n 
# L_ds_vec =[vec(L_ds*sin(theta[i]),0,L_ds*cos(theta[i])) for i in range(n)]
# L_ds_pos=[R_earth_core * vec(cos(theta[i]),0,sin(theta[i])) for i in range(n)]
particles, particles_v = [],[]
scene = canvas(title='magnetic field of earth ', height=1000, width=1000, center = vec(0 , 0 , 0))
scene.lights = []
scene.ambient = color.gray(0.99)
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

earth = sphere( pos = vec( 0,0,0) , canvas = scene,
    radius = R_earth , texture={'file':textures.earth}) # earth_orbit['r']??
for j in range (n):
    particle = sphere(canvas=scene , pos = vec (-5E7 ,-25E6 + j * 1E6,0), 
    radius = 1.5E5 , color = color.blue)
    particle.v = V_wind
    particles.append(particle) #particles[i].pos

def B_by_solar_wind(p):
    B , E = vec(0,0,0) , vec(0,0,0)
    for i in range (n):
        # theta = acos (dot(V_wind,p - particles[i].pos) / V_wind.mag / (p-particles[i].pos).mag)
        # E = Q_electric * (1-V_wind.mag**2/c**2) * (p-particles[i].pos) \
        # / (4*pi*e0) / (1-V_wind.mag**2 * sin(theta)**2 / c**2 )**1.5 /mag(p-particles[i].pos)**3
        Bi = mu0 * Q_electric * V_wind.cross( (p-particles[i].pos) )  \
            / (4*pi*e0) / mag(p-particles[i].pos)**3
        # B += V_wind.cross(Bi/c**2)
        B += Bi
        
    return B

def mag_field_at_p(p):
    B = vec(0,0,0)
    B += B_by_solar_wind(p) 
    print("pos = ",  p)
    print ("B by wind = ", B)
    c = mu0/(4*pi*(p.x**2.0+p.y**2.0+p.z**2.0)**1.5)
    print("B by earth = ", c*(3*(dot(vec(0,mu,0),norm(p))) * norm(p) - vec(0,mu,0)))
    # input()
    #1233213
    B += c*(3*(dot(vec(0,mu,0),norm(p))) * norm(p) - vec(0,mu,0))

    return B

dt = 30
while True:
    rate (1000)
    for i in range (n) :
        particles[i].pos += particles[i].v * dt
    
    for i in range(0, N):
        for j in range(0, N):
            point_pos = vec(pos_x[i,j],pos_y[i,j],0)
            if (point_pos.x ** 2 + point_pos.y **2 <= (1.1*R_earth) **2 ):
                continue
            B = mag_field_at_p(point_pos)
            ar = arrow(pos = vec( pos_x[i,j], pos_y[i,j], 0), axis =  B * 1E10, 
            shaftwidth = 8E4, color=color.red)
            print("B = ",  B)
    print("done drawing")
    input()