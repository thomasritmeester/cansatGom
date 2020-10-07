import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')


Z=np.array([0,1,2,3,4,5,5.5,6,6.2,6.3,6.4,6.3,6,5.5,4.3,3.1,2.1,1,0,0,0])
Y=np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,18,18,18])
X=np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,18,18,18])
ax.plot(X,Y,Z)

plt.show()