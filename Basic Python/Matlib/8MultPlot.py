import matplotlib.pyplot as pl

fig=pl.figure()

rect=fig.patch
rect.set_facecolor("blue")

x=[1,2,3,5,6,7,8]
y=[3,5,7,9,11,14,17]
x2=[3,4,23,6]
y2=[24,24,6,24]
x3=[21,77,3,24]
y3=[6,87,4,32]

graph1=fig.add_subplot(1,1,1,axisbg="black")
graph1.plot(x,y,"red",linewidth=4.0)
graph1.plot(x2,y2,"yellow",linewidth=4.0)
graph1.plot(x3,y3,"white",linewidth=4.0)

graph1.tick_params(axis="x",color="white")
graph1.tick_params(axis="y",color="yellow")

graph1.spines["top"].set_color('w')
graph1.spines["bottom"].set_color('w')
graph1.spines["left"].set_color('w')
graph1.spines["right"].set_color('w')

graph1.set_title("Random Graph",color="white")
graph1.set_xlabel("This is the x axis",color="white")
graph1.set_ylabel("This is the y axis",color="white")
pl.show()