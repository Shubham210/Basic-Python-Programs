from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt

fig=plt.figure()

chart=fig.add_subplot(1,1,1,projection='3d')

X,Y,Z=[1,2,3,4,6,7,8],[2,4,6,8,12,14,16],[3,5,7,8,14,24,43]
Xx,Yy,Zz=[-1,-2,-3,-4,-6,-7,-8],[-2,-4,-6,-8,-12,-14,-16],[-3,-5,-7,-8,-14,-24,-43]

chart.scatter(X,Y,Z,c='red',marker='o')	# try marker='x'
chart.scatter(Xx,Yy,Zz,c='blue',marker='^')	# try marker='x'

chart.set_xlabel('x axis')
chart.set_ylabel('y axis')
chart.set_zlabel('z axis')
plt.show()