from numpy import * 
from vpython import *
import numpy as np
particles, particles_v = [],[]
for i in range (50):
    particle = sphere(canvas=scene , pos = vec (-5E7 ,-25E6 + i * 1E6,0), 
    radius = 1E5 , color = color.blue)
    particle.v = i * 2E2
    particles.append(particle)
for i in range (50):
    print(particles[i].pos)
    print(particles[i].v)