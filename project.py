from numpy import * 
from vpython import *
B_ground = 45*10**(-3)
u0 = 4*pi*10**(-7)
R_earth = 6371*10**3
i_earth = 4*(2**0.5)*B_ground*R_earth/u0
h , N , k= 1E-2 , 50, 1E6


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

print (pos_x)
print (pos_y)
# input()

earth = sphere( pos = vec( 0,0,0) , 
    radius = R_earth , texture={'file':textures.earth}) # earth_orbit['r']??

# for i in range(N):
# 	for j in range(N):
# 		point = box( pos=vec(i*h, j*h, 0), length = h, height= h, width = h/10,
#          color=vec((V[i,j]+100)/200,(100-V[i,j])/200,0.0) )

for i in range(0, N):
    for j in range(0, N):
        ar = arrow(pos = vec( pos_x[i,j], pos_y[i,j], 0), axis =vec( 1E6, -1E6, 0),
         shaftwidth = 1E5, color=color.red)

