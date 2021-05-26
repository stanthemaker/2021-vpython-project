from numpy import * 
from vpython import *
B_ground = 45*10**(-3)
u0 = 4*pi*10**(-7)
R_earth = 6371*10**3
i_earth = 4*(2**0.5)*B_ground*R_earth/u0
h , N , k= 1E-2 , 5, 1E6


scene = canvas(title='magnetic field of earth ', height=1000, width=1000, center = vec(0 , 0 , 0))
scene.lights = []
scene.ambient=color.gray(0.99)
pos = zeros([2,N,N])
# for i in range(0, N):
# 	for j in range(0, N):
        
print (pos)

pos -= (N*k/2)
print (pos)
input()
earth = sphere( pos = vec( 0,0,0) , 
    radius = R_earth , texture={'file':textures.earth}) # earth_orbit['r']??

# for i in range(N):
# 	for j in range(N):
# 		point = box( pos=vec(i*h, j*h, 0), length = h, height= h, width = h/10,
#          color=vec((V[i,j]+100)/200,(100-V[i,j])/200,0.0) )

for i in range(0, N):
	for j in range(0, N):
		ar = arrow(pos = vec( i*k-(N*k/2), j*k-(N*k/2), 0), axis =vec( i*k-(N*k/2), j*k-(N*k/2), 0),
         shaftwidth = 1E5, color=color.red)

