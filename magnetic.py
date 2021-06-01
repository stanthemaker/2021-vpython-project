# -*- coding: cp950 -*-
#�N�p���K�����q�l�ϰ����x(electron magnetic dipole moment)�A�ݩP�D�ϳ�������
from IPython.core.display import display
from vpython import*
import math

mu = 9.27e-24 #Bohr magneton
mu0 = 4*pi*e-7 #permeability of free space
phi=[-1*pi/2.0+pi*(t+1)/5.0 for t in range(4)]
theta = [2*pi*t/6.0  for t in range(10)]
ch1 = []
t = 0

scene1 = canvas(title="magnet", background=vec(0.5,0.6,0.5),
autoscale = 0,width=600, height=600)

#scene.background = (0.9,0.8,0.4)
pos1 = box(display = scene1,pos =vec(0.5,0,0),color = color.red,
length=1, width=0.5, height=0.5)
neg1 = box(display = scene1,pos =vec(-0.5,0,0),color = color.blue,
length=1, width=0.5, height=0.5)


def B(x,y,z):
    c = mu0/(4*pi*(x**2.0+y**2.0+z**2.0)**1.5)
    return c*(3*(dot(vec(-mu,0,0),norm(vec(x,y,z))))*norm(vec(x,y,z))-vec(-mu,0,0))

for i in range(10):
    for j in range(4):
        ch1.append(sphere(display = scene1,
                          pos = vec(pos1.pos.x+0.1*sin(phi[j]),
                          pos1.pos.y+0.1*cos(phi[j])*sin(theta[i]),
                          pos1.pos.z+0.1*cos(phi[j])*cos(theta[i])),
                          color = vec(0.9,1,0.3),radius = 0.015,
                          make_trail = True, count=0))

while(1):
    rate(10000)
    t = t +1
    for i in range(40):
        if ((ch1[i].pos.x+1.0)**2+ch1[i].pos.y**2+ch1[i].pos.z**2)>0.01:
            ch1[i].pos = ch1[i].pos +norm(B(ch1[i].pos.x,ch1[i].pos.y,ch1[i].pos.z))*0.007
        if ch1[i].pos.x<= 0.1 and mag(ch1[i].pos) > 0.5 and ch1[i].count < 0:
            arrow(pos=ch1[i].pos, axis=norm(B(ch1[i].pos.x, ch1[i].pos.y, ch1[i].pos.z)), color=color.black)
            #print i, ch1[i].pos, B(ch1[i].pos.x, ch1[i].pos.y, ch1[i].pos.z)
            ch1[i].count += 1
    if t>70000:
        break
