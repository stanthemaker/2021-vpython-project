##aurora project
from numpy import * 
from vpython import *
import numpy as np
import random
c = 299792458
B_ground = 45*1E-3
mu0 = 4*pi* 1E-7
e0 = 1/(c**2 * mu0)
R_earth, R_earth_core = 6371*1E3, 600 * 1E3
mu = B_ground* 2 *pi * (2*R_earth_core**2)**1.5 / mu0
Q_electric, M_proton = 1.602 * 1E-19  , 1.672 * 1E-27
n = 30
 
points, particles = [], []
scene = canvas(title='magnetic field of earth ', height=1000, width=1000, center = vec(0 , 0 , 0))
scene.lights = []
scene.ambient = color.gray(0.99)

earth = sphere( pos = vec( 0,0,0) , canvas = scene,
    radius = R_earth , texture={'file':textures.earth}) # earth_orbit['r']??

def mag_field_at_p(r):
    B = vec(0,0,0) 
    c = mu0/(4* pi * r.mag**3 )
    B = c*(3*(dot(vec(0,-mu,0),norm(r))) * norm(r) - vec(0,-mu,0))
    # print("pos = ", r)
    # print("B by earth = ", B.mag)
    return B
def F_on_particles(pos,v):
    F = Q_electric * v.cross(mag_field_at_p(pos))
    return F
loss = 0
for i in range (n):
    particle = sphere(canvas=scene , pos = vec (-5E7 ,-45E6 + i * 3E6,0), 
    radius = 3E5 , color = color.blue)
    particle.v = vec(random.randint(500,900),random.randint(500,900),0) # V_wind between 2E5 ~ 8E5
    particles.append(particle)
    for j in range (n):
        for  k in range (n):
            point = sphere( canvas=scene , pos = vec (-15E6 ,-15E6 , -15E6) + 1E6 * vec(i,j,k),
             visible = False)
            if point.pos.mag <=  (R_earth * 1.05):
                loss += 1
                continue
            else:
                points.append(point)
M = n**3 - loss
##test for B earth earth 
h = 0
for i in range (M):
    if (points[i].pos.y == 0):
        if ( points[h].pos.mag > points[i].pos.mag):
            h = i

print("R = ",points[h].pos.mag)
print("B naer earth = ", mag_field_at_p(points[h].pos))
##done test

for i in range (M):
    B = mag_field_at_p(points[i].pos)
    ar = arrow(pos = points[i].pos , axis =  B * 1E11, 
    shaftwidth = 4E4, color=color.red)
    if (ar.pos.z != 0):
        ar.visible = False
dt = 5E-3
while True:
    rate (700)
    for i in range (n) :
        particles[i].pos += particles[i].v * dt
        a = F_on_particles(particles[i].pos, particles[i].v) / M_proton
        particles[i].v += a *dt
        if (particles[i].pos.mag <= R_earth):
            particles[i].color = color.red
        