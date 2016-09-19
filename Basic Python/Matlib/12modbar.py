import matplotlib.pyplot as plt
import numpy as np

pos=np.arange(6)+2.5

names=['Shubham','Krishna','Sudama','Prabhupada','Gopal','Madan']

plt.barh(pos,(2,4,8,6,17,15),align='center',color='blue' )
plt.xlabel("Height of Students",color='red')
plt.ylabel("Students",color='red')
plt.title('Hieght of St in inches',color='blue')
plt.tick_params(axis='x',color='white' )
plt.tick_params(axis='y',color='yellow' )

plt.subplots_adjust(left=.11,bottom=.12,right=.94)

plt.yticks(pos,names)

plt.show()