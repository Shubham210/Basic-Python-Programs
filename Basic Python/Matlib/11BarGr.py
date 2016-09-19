import matplotlib.pyplot as plt
import numpy as np

pos=np.arange(6)+0.5

plt.barh(pos,(2,4,8,6,17,15),align='center',color='blue' )
plt.show()
