# -*- coding: utf-8 -*-
#相同電量點電荷的電力線
from __future__ import division
from vpython import*
from math import*

scene = canvas(title='dipole', height=1000, width=1000, range=3.5, auto_scale=False, background=vec(0.4,0.7,0.7))
scene2 = canvas(title='quadrupole',x=1000, y=0, height=1000, width=1000, range=3.5, auto_scale=False, background=vec(0.4,0.7,0.7))
k = 8.99*10**9 # Nm**2/C**2
theta = 0
phi = 0
E = vector(0,0,0) #N/C, electric field

#setup for dipole=============================

scene.select()
size1 = 0.1 #m
c1 = []
c1.append(sphere(pos=vector(1,0,0), radius=size1, color=vec(1,0,0))) #c1[0]
c1.append(sphere(pos=vector(-1,0,0), radius=size1, color=vec(0,0,1))) #c1[1]
c1[0].q = 2*10**-5 #C, the charge of c1[0]
c1[1].q = -10**-5 #C, the charge of c1[1]
ball1 = []

#ball1.append(sphere(pos=vector(1,0.1,0), radius=0.01, color=(1,1,0), make_trail=True, v=vector(0,0,0), acc=vector(0,0,0)))

phi_div=12
theta_div=3
for phi_num in range(0,phi_div):
    for theta_num in range(1-theta_div,theta_div):
        #print phi_num, theta_num
        phi = phi_num/phi_div*2*pi
        theta = theta_num/theta_div*1/2*pi
        ball1.append(sphere(pos=vector(size1*sin(theta), size1*cos(theta)*cos(phi), size1*cos(theta)*sin(phi))+c1[0].pos, \
                            radius=0.01, color=vec(1,1,0), make_trail=True, v=vector(0,0,0), acc=vector(0,0,0)))
        #print vector(size1*sin(theta), size1*cos(theta)*cos(phi), size1*cos(theta)*sin(phi))+c_1.pos, phi, theta

#setup for quadrupole=============================

scene2.select()
size2 = 0.1 #m
c2 = []
c2.append(sphere(pos=vector(1,0,0), radius=size2, color=vec(1,0,0))) #c2[0]
c2.append(sphere(pos=vector(-1,0,0), radius=size2, color=vec(1,0,0))) #c2[1]
c2[0].q = 10**-5 #C, charge
c2[1].q = 10**-5 #C, charge
ball2 = []

#ball2.append(sphere(pos=vector(1,0.1,0), radius=0.01, color=(1,1,0), make_trail=True, v=vector(0,0,0), acc=vector(0,0,0)))
phi_div=8
theta_div=2
for phi_num in range(0,phi_div+1):
    for theta_num in range(1-theta_div,theta_div):
        #print phi_num, theta_num
        phi = phi_num/phi_div*2*pi

        theta = theta_num/theta_div*1/2*pi
        ball2.append(sphere(pos=vector(size2*cos(theta)*cos(phi), size2*cos(theta)*sin(phi), size2*sin(theta))+c2[0].pos, \
                            radius=0.01, color=vec(1,1,0), make_trail=True, v=vector(0,0,0), acc=vector(0,0,0)))
        ball2.append(sphere(pos=vector(size2*cos(theta)*cos(phi), size2*cos(theta)*sin(phi), size2*sin(theta))+c2[1].pos, \
                            radius=0.01, color=vec(1,1,0), make_trail=True, v=vector(0,0,0), acc=vector(0,0,0)))
for i in range(36):
    print ( ball2[i].pos)
    if abs(ball2[i].pos.y + ball2[i].pos.z) <= 0.000001 :
#        ball2[i].color = color.black
#        ball2[i].make_trail = False
        ball2[i].visible = False
        del ball2[i]
#    if ball2[i].pos.y < 1*e-5 and ball2[i].pos.x < 1 and ball2[i].pos.x > -1 :
#        ball2[i].visible = false
    
        #print vector(size2*cos(theta)*cos(phi), size2*cos(theta)*sin(phi), size2*sin(theta))+c2[2].pos
        #print vector(size2*cos(theta)*cos(phi), size2*cos(theta)*sin(phi), size2*sin(theta))+c2[3].pos
        #print phi, theta

################################################################################

t = 0
dt = 0.005
while 1:
    rate(1/dt)
    t+=dt
    #move the balls in 'scene'
    scene.select()
    for b in ball1:
        r0 = b.pos-c1[0].pos
        r1 = b.pos-c1[1].pos
        E = k*((c1[0].q/r0.mag2)*r0.norm() + (c1[1].q/r1.mag2)*r1.norm())
        b.v = E.norm()
        b.pos += b.v*dt
        #print E, r0.norm(), r1.norm()
        #arrow(pos=b.pos, axis=E.norm())

    #move the balls in 'scene2'
    scene2.select()
    for b in ball2:
        r0 = b.pos-c2[0].pos
        r1 = b.pos-c2[1].pos
        E = k*((c2[0].q/r0.mag2)*r0.norm() + (c2[1].q/r1.mag2)*r1.norm())
        b.v = E.norm()
        b.pos += b.v*dt