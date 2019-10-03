import numpy as np
import math
from matplotlib import pyplot as plt

v = np.linspace(0,72,73)
h = np.linspace(70,130,61)

framerate = 32 # frame rate in fps
pangsize = 103 # detector pixel size in arcsecs

motionlimit = 2 # Minimum motion (pixels) per frame

psize = []
for i in range(61):
	psize.append(math.atan((2*np.pi/360)*pangsize/3600)*h[i]*2*1000) # size of pixel on sky at range h. In meters.

traillength = np.zeros((73,61))

for i in range(73):
	for j in range(61):
		traillength[i,j] = (v[i]*1000/psize[j] / framerate)

print(np.shape(traillength))

angrate = math.atan((72/2)/100)*2 # angular rate of motion of trail in degrees / second

entryangle = 90

length = np.sin((2*np.pi/360)*entryangle)

fig, ax = plt.subplots(2, figsize=(10,10))

for i in range(61):
	ax[0].plot(v,traillength[:,i])

ax[0].set_xlim(0,72)
ax[0].plot((min(v),max(v)),(motionlimit,motionlimit), color='black')
ax[0].set_xlabel('Speed (km/s)', size=15)
ax[0].set_ylabel('Trail length (pixels/frame', size=15)

for i in range(73):
	ax[1].plot(h,traillength[i,:])

ax[1].set_xlim(70,130)
ax[1].plot((min(h),max(h)),(motionlimit,motionlimit), color='black')
ax[1].set_xlabel('Range (km)', size=15)
ax[1].set_ylabel('Trail length (pixels/frame)', size=15)

plt.tight_layout()

plt.show()
