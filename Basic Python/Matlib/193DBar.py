from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
import numpy as np

fig=plt.figure()

chart=fig.add_subplot(1,1,1,projection='3d')

x=[1,2,3,4,5,6,7,8,9,10]
y=[2,3,4,5,6,1,2,3,4,7]
z=[0,0,0,0,0,0,0,0,0,0]

dx=np.ones(10)
dy=np.ones(10)
dz=[1,2,3,4,5,6,7,8,9,10]

chart.bar3d(x,y,z,dx,dy,dz,color='cyan')

chart.set_xlabel('x axis')
chart.set_ylabel('y axis')
chart.set_zlabel('z axis')
plt.show()