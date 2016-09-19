from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt

fig=plt.figure()

chart=fig.add_subplot(1,1,1,projection='3d')

X,Y,Z=[1,2,3,4,6,7,8],[2,4,6,8,12,14,16],[3,5,7,8,4,2,7]

chart.plot_wireframe(X,Y,Z)

plt.show()