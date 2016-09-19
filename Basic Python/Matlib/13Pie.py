import matplotlib.pyplot as plt

size=[50,12,13,9,5,36]
colors=['yellow','blue','cyan','magenta','red','white']
labels=['English','French','German','Tamil','Kannada','Hindi']

plt.pie(size,colors=colors,startangle=92,labels=labels)
plt.title('PieChart')
plt.legend(title='Legend',loc='lower left')
plt.axis('equal')

plt.show()
