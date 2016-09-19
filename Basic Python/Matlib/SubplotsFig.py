import matplotlib.pyplot as pl

fig=pl.figure()

rect=fig.patch
rect.set_facecolor("blue")

x=[1,2,3,5,6,7,8]
y=[3,5,7,9,11,14,17]

graph1=fig.add_subplot(2,2,1,axisbg="black")
graph2=fig.add_subplot(2,2,2,axisbg="green")
graph3=fig.add_subplot(2,1,2,axisbg="purple")
#graph4=fig.add_subplot(2,2,4,axisbg="yellow")

graph1.plot(x,y,"red",linewidth=4.0)
graph2.plot(x,y,"red",linewidth=4.0)
graph3.plot(x,y,"red",linewidth=4.0)
#graph4.plot(x,y,"red",linewidth=4.0)

pl.show()