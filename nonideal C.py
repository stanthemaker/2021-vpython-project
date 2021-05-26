from numpy import *
from vpython import *
epsilon = 8.854E-12
N = 10
h = 1E-2/(N-1)
L, d= 4E-3,1E-3
V0 = 200
def solve_laplacian(u, u_cond, h, Niter=5000):
	V = array(u)
	for i in range(Niter):
		V[u_cond] = u[u_cond]
		V[1:-1, 1:-1] = (V[2:, 1:-1] + V[:-2, 1:-1] + V[1:-1, 2:] + V[1:-1, :-2])/4 # replace this 0 by your Laplacian Solver
	return V

def get_field(V, h):
	Ex, Ey = gradient(V)
	Ex, Ey = -Ex/h, -Ey/h
	return Ex, Ey

u = zeros([N, N])
u[int(N/2)-int(L/h/2.0):int(N/2)+int(L/h/2.0), int(N/2) - int(d/h/2.0)] = -V0/2
u[int(N/2)-int(L/h/2.0):int(N/2)+int(L/h/2.0), int(N/2) + int(d/h/2.0)] = V0/2
u_cond = not_equal(u, 0)

V = solve_laplacian(u, u_cond, h)
print(V)
print(gradient(V))
input()
# scene = canvas(title='non-ideal capacitor', height=1000, width=1000, center = vec(N*h/2, N*h/2, 0))
# scene.lights = []
# scene.ambient=color.gray(0.99)
# box(pos = vec(N*h/2 , N*h/2 - d/2 - h , 0), length = L, height = h/5, width = h)
# box(pos = vec(N*h/2 , N*h/2 + d/2 - h , 0), length = L, height = h/5, width = h)

for i in range(N):
	for j in range(N):
		point = box(pos=vec(i*h, j*h, 0), length = h, height= h, width = h/10, color=vec((V[i,j]+100)/200,(100-V[i,j])/200,0.0) )

Ex, Ey = get_field(V, h)
print (Ex)
print (Ey)

# points(color = color.orange, pos = vec(N*h/2, N*h/2, 0), radius = 100)
for i in range(0, N):
	for j in range(0, N):
		ar = arrow(pos = vec( i*h, j*h, h/10), axis =vec(Ex[i,j]/2E9, Ey[i,j]/2E9, 0), shaftwidth = h/6.0, color=color.black)

flux = 0
boundary_y_up = int(N/2) + int(d/h/2.0) + 4 
boundary_y_down = int(N/2) + int(d/h/2.0) - 4
boundary_x_right = int(N/2) + int(L/h/2.0) + 4
boundary_x_left = int(N/2) - int(L/h/2.0) - 4
for i in range (boundary_x_left , boundary_x_right+1):
	# points(color = color.orange, pos = [vec(i,boundary_y_up,0), vec(i,boundary_y_down,0)], radius = 100)
	# print(i)
	flux += Ey[i, boundary_y_up]
	flux -= Ey[i, boundary_y_down]

for i in range (boundary_y_down, boundary_y_up+1):
	flux += Ex[boundary_x_right, i]
	flux -= Ex[boundary_x_left, i]

flux *= h
Q = flux*epsilon

C_nonideal = Q/V0
C_ideal = epsilon * L * 1/d
print('C_ideal = ',C_ideal, '\nC_nonideal = ', C_nonideal)
input()




# for i in range(int(N/2-L/(2*h))-3, int(N/2-L/(2*h))+3):
# 	flux += Ey[i, int(N/2+d/(2*h))+2]*h
# 	flux -= Ey[i, int(N/2+d/(2*h))-2]*h
# for i in range(int(N/2+d/(2*h)-3), int(N/2+d/(2*h))+3):
# 		flux += Ex[int(N/2+L/(2*h))+2, i]*h
# 		flux -= Ex[int(N/2+L/(2*h))-2, i]*h
# for m in range (0,5):
# 	flux = 0
# 	for i in range(int(N/2-L/(2*h))-m, int(N/2+L/(2*h))+m+1):
# 		flux += Ey[i, int(N/2+d/(2*h))+m]*h
# 		flux -= Ey[i, int(N/2+d/(2*h))-m]*h
# 	for i in range(int(N/2+d/(2*h)-m), int(N/2+d/(2*h))+m+1):
# 		flux += Ex[int(N/2+L/(2*h))+m, i]*h
# 		flux -= Ex[int(N/2-L/(2*h))-m, i]*h
# Q = flux*epsilon
# C_ideal = L*epsilon/d
# C_nonideal = Q/V0
# # print("m =", m)
# print("Q = ", Q)
# print("C_ideal = ", C_ideal)
# print("C_nonideal = ", C_nonideal)
# input()
#find Q, find C_nonideal = Q/(delta V)
#Compare C_nonideal to C_ideal