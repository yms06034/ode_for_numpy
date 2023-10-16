import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation
import seaborn as sns

L = 100

x = np.linspace(0, 1, L)
u = np.zeros(L)

#Initial Condition
u[L//2] = 1  

#Boundary Conditions
#This is not necessary to declare since u = zeros(L)
u[0] = 0
u[L-1] = 0

for t in range(100):
    for i in range(1, L-1):
        u[i] += (u[i+1] - 2*u[i] + u[i-1])/4

fig, ax = plt.subplots(figsize=(20,10))
ax.axis('off')
ax.scatter(x,u, linewidth=15, c=u, cmap='jet')
plt.show()




sns.set()
T = 400
u = np.zeros((100,100))
u[30,20] = 1

fig, ax = plt.subplots(figsize=(20,10))
ax.axis('off')
plot = ax.contourf(u, cmap='jet')
def ans(f):
    global u, plot
    
    #Time is not defined as the animation will do the loop for T times.
    for j in range(100):
        for i in range(1,99):
            u[i,j] += (u[i+1,j] + u[i,j+1] + u[i-1,j] + u[i,j-1] - 4*u[i,j])/4
    for c in plot.collections:
        c.remove()
    plot = ax.contourf(u, cmap='jet')
    return plot

anim = animation.FuncAnimation(fig, ans, frames=T)
plt.show()



sns.set()
sns.set_style('white')
x = np.linspace(0,1,101)
y = np.linspace(0,1,101)
X,Y = np.meshgrid(x,y)
u = np.zeros((101,101))
u[40,50] = 100
T = 400
fig = plt.figure()
ax = plt.axes(projection='3d')
ax._axis3don = False
c = ax.contourf3D(X,Y,u,1000, cmap='jet')

def ans(f):
    global u, c

    #Time is not defined as the animation will do the loop for T times.
    for j in range(100):
        for i in range(1,100):
            u[i,j] += (u[i+1,j] + u[i,j+1] + u[i-1,j] + u[i,j-1] - 4*u[i,j])/4
    for xx in c.collections:
        xx.remove()
    c = ax.contourf3D(X,Y,u,1000, cmap='jet')
    return c

anim = animation.FuncAnimation(fig, ans, frames=T)
plt.show()