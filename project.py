##aurora project
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
h , N , k , n = 1E-2 ,30, 1E6 , 20
 
points, particles = [], []
scene = canvas(title='magnetic field of earth ', height=1000, width=1000, center = vec(0 , 0 , 0))
scene.lights = []
scene.ambient = color.gray(0.99)

earth = sphere( pos = vec( 0,0,0) , canvas = scene,
    radius = R_earth , texture={'file':textures.earth}) # earth_orbit['r']??
loss = 0
for i in range (n):
    for j in range (n):
        particle = sphere(canvas=scene , pos = vec (-5E7 ,-25E6 + j * 1E6,0), 
        radius = 1.5E3 , color = color.blue)
        particle.v = V_wind
        particles.append(particle) #particles[i].pos
        for  k in range (n):
            point = sphere( canvas=scene , pos = vec (-10E6 ,-10E6 , -10E6) + 1E6 * vec(i,j,k), 
            radius = 0.01 , color = color.red , visible = False)
            if point.pos.mag**2 <=  R_earth**2:
                loss += 1
                continue
            else:
                points.append(point)
M = n**3 - loss


def mag_field_at_p(p):
    B = vec(0,0,0) 
    c = mu0/(4*pi*(p.x**2.0+p.y**2.0+p.z**2.0)**1.5)
    print("B by earth = ", c*(3*(dot(vec(0,mu,0),norm(p))) * norm(p) - vec(0,mu,0)))
    B = c*(3*(dot(vec(0,mu,0),norm(p))) * norm(p) - vec(0,mu,0))
    return B
for i in range (M):
    B = mag_field_at_p(points[i].pos)
    ar = arrow(pos = points[i].pos , axis =  B * 1E10, 
    shaftwidth = 4E4, color=color.red)
input()
dt = 30
while True:
    rate (1000)
    for i in range (n) :
        particles[i].pos += particles[i].v * dt
    
    for i in range(0, N):
        for j in range(0, N):
            if (points[i].pos.x ** 2 + points[i].pos.y **2 <= (1.1*R_earth) **2 ):
                continue
            B = mag_field_at_p(points[i].pos)
            ar = arrow(pos = points[i].pos.x , axis =  B * 1E10, 
            shaftwidth = 8E4, color=color.red)
            print("B = ",  B)
    print("done drawing")
    input()