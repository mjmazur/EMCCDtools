import numpy as np
import math
from matplotlib import pyplot as plt

hsteps = 12
vsteps = 8

# v = np.linspace(1,72,vsteps+1)
# h = np.linspace(70,130,hsteps+1)

v = [1,5,11.2,20,30,40,50,60,72]
h = [70,75,80,85,90,95,100,105,110,115,120,125,130]

framerate = 32 # frame rate in fps
pangsize = 103 # detector pixel size in arcsecs

motionlimit = 2 # Minimum motion (pixels) per frame

psize = []
for i in range(hsteps+1):
	psize.append(math.atan((2*np.pi/360)*pangsize/3600)*h[i]*2*1000) # size of pixel on sky at range h. In meters.

traillength = np.zeros((vsteps+1,hsteps+1)) # rows = height list, columns = speed list

for i in range(vsteps+1):
	for j in range(hsteps+1):
		traillength[i,j] = (v[i]*1000/psize[j] / framerate)

print(np.shape(traillength))

# Above calculates for a meteor that is orthogonal to the look direction. A real meteor will
# typically not move orthogonal to the camera look direction. To deal with this, we need to
# calculate the angular rate for angles from 90 (orthogonal) to 0 (line-of-sight) degrees.

angrate = np.zeros((vsteps+1,hsteps+1))

entryangle = 10

for i in range(vsteps+1):
	for j in range(hsteps+1):
		angrate[i,j] = math.atan((v[i]/2)/h[j])*2*np.sin((2*np.pi/360)*entryangle) # angular rate of motion of trail in degrees / second

print(angrate)

# length = np.sin((2*np.pi/360)*entryangle)

fig, ax = plt.subplots(2, figsize=(8,8))

for i in range(int(hsteps/2)+1):
	i = i*2
	ax[0].plot(angrate[:,0],traillength[:,i])
	ax[0].text(72.5,max(traillength[:,i]-0.5),str(int(h[i])) + ' km', size=8)

#ax[0].set_xlim(0,72)
ax[0].set_ylim(0,max(traillength[:,0]))
ax[0].plot((min(v),max(v)),(motionlimit,motionlimit), linestyle='--', color='black', label='Motion threshold')
ax[0].plot((11.2,11.2),(0,max(traillength[:,0])), linestyle=':', color='black', label='11.2 km/s')
ax[0].set_xlabel('Speed (km/s)', size=15)
ax[0].set_ylabel('Trail length (pixels/frame', size=15)

ax[0].legend(loc='upper left')

for i in range(vsteps+1):
	i = i
	if v[i] == 11.2:
		ax[1].plot(h,traillength[2,:], linestyle=':', color='black', label='11.2 km/s')
		ax[1].text(130.5,min(traillength[i,:]-0.5),str(v[i]) + ' km/s', size=8)
	else:
		ax[1].plot(h,traillength[i,:])
		ax[1].text(130.5,min(traillength[i,:]-0.5),str(v[i]) + ' km/s', size=8)

ax[1].set_xlim(70,130)
ax[1].plot((min(h),max(h)),(motionlimit,motionlimit), linestyle='--', color='black', label='Motion threshold')
ax[1].set_xlabel('Range (km)', size=15)
ax[1].set_ylabel('Trail length (pixels/frame)', size=15)

plt.legend()

plt.tight_layout()

plt.savefig('TrailLengths.png', dpi=300)

plt.show()
