import numpy as np
import math
from matplotlib import pyplot as plt
from shapely.geometry import Point, Polygon

def patch(x,y,phi,theta,h,fov):
	# Function to calculate the Cartesian coordinates of a point in space

	pointing = np.array([[phi-fov/2,theta-fov/2],[phi-fov/2,theta+fov/2],[phi+fov/2,theta+fov/2],[phi+fov/2,theta-fov/2]])

	pat = np.zeros((4,3))

	for i in range(4):
		xu = math.cos(pointing[i,0])*math.sin(pointing[i,1])
		yu = math.sin(pointing[i,0])*math.sin(pointing[i,1])
		zu = math.cos(pointing[i,1])

		scale = h / zu
		xh = xu * scale + x
		yh = yu * scale + y

		pat[i,0] = xh
		pat[i,1] = yh
		pat[i,2] = h
		r = math.sqrt(pow(xh-x,2)+pow(yh-y,2)+h*h)/1000

	return pat, r

def patcharea(poly):
	a = (poly[0,0], poly[0,1])
	b = (poly[1,0], poly[1,1])
	c = (poly[2,0], poly[2,1])
	d = (poly[3,0], poly[3,1])

	polygon = Polygon([a, b, c, d])

	parea = polygon.area
	return parea/1000000

def patchoverlap(poly1,poly2):
	a = (poly1[0,0], poly1[0,1])
	b = (poly1[1,0], poly1[1,1])
	c = (poly1[2,0], poly1[2,1])
	d = (poly1[3,0], poly1[3,1])

	e = (poly2[0,0], poly2[0,1])
	f = (poly2[1,0], poly2[1,1])
	g = (poly2[2,0], poly2[2,1])
	h = (poly2[3,0], poly2[3,1])

	polygon1 = Polygon([a, b, c, d])
	polygon2 = Polygon([e, f, g, h])
	overlap = polygon1.intersection(polygon2)
	area = overlap.area / 1000000
	if area > 0:
		points = np.asarray(overlap.exterior)
	else:
		points = np.array([[0,0],[0,0],[0,0]])
	return points, area



# Elginfield
xloc2 = 474332.51
yloc2 = 4782239.36

# Desired
# phi2F = 85 * math.pi/180 # angle measured west from east=0
# theta2F = 15.6 * math.pi/180 # angle measured south from zenith
# fov2F = 14.7 * math.pi/180 # field of view

# phi2G = 90 * math.pi/180 # angle measured west from east=0 (ideal is 74.48, 26.1)
# theta2G = 42 * math.pi/180 # angle measured south from zenith
# fov2G = 14.7 * math.pi/180

# Current
phi2F = 74.46 * math.pi/180 # angle measured west from east=0. Currently 85.74. Want 81
theta2F = 24.21 * math.pi/180 # angle measured south from zenith. Currently 16.22. Want 25
fov2F = 14.7 * math.pi/180 # field of view

phi2G = 90.43 * math.pi/180 # angle measured west from east=0 (ideal is 74.48, 26.1) Currently 96.16. Want 88
theta2G = 42.82 * math.pi/180 # angle measured south from zenith. Currently at 39.27. Want 42
fov2G = 14.7 * math.pi/180

# Tavistock
xloc1 = xloc2 + 43500
yloc1 = yloc2 + 7500

phi1F = 128.22 * math.pi/180 # angle measured west from east=0. Currently 148.74. Want 128
theta1F = 25.05 * math.pi/180 # angle measured south from zenith. Currently 25.21. Want 26
fov1F = 14.47 * math.pi/180 # field of view

phi1G = 120.32 * math.pi/180 # angle measured west from east=0 132.25 125. Currently 120.42. Want 120.5
theta1G = 42.99 * math.pi/180 # angle measured south from zenith 27.66 43. Currently 43.08. Want 42.7
fov1G = 14.7 * math.pi/180 # field of view

baseH = 100
heightF = 100
heightG = 80

# Start main part of program
# Loop over this from 80km to 140km in 1 km increments
# Create 
overF = []
overG = []
range1F = []
range1G = []
range2F = []
range2G = []

for i in range(50,141):
	pat1, r1 = patch(xloc1,yloc1,phi1F,theta1F,i*1000,fov1F)
	pat2, r2 = patch(xloc2,yloc2,phi2F,theta2F,i*1000,fov2F)
	#print r1
	range1F.append(r1)
	range2F.append(r2)

	pat3, r3 = patch(xloc1,yloc1,phi1G,theta1G,i*1000,fov1G)
	pat4, r4 = patch(xloc2,yloc2,phi2G,theta2G,i*1000,fov2G)
	range1G.append(r3)
	range2G.append(r4)

	parea1 = patcharea(pat1)
	parea2 = patcharea(pat2)
	parea3 = patcharea(pat3)
	parea4 = patcharea(pat4)

	overlapptsF, overlapareaF = patchoverlap(pat1,pat2)
	overlapptsG, overlapareaG = patchoverlap(pat3,pat4)

	overF.append(overlapareaF)
	overG.append(overlapareaG)

overy = np.arange(50,141)

overlaparr = np.stack((overy, overF,overG,range1F,range1G,range2F,range2G))
overlaparr = np.transpose(overlaparr)
np.savetxt('/home/mmazur/emccd/Analysis/overlaps.txt',overlaparr)

pat1, r1 = patch(xloc1,yloc1,phi1F,theta1F,baseH*1000,fov1F)
pat2, r2 = patch(xloc2,yloc2,phi2F,theta2F,baseH*1000,fov2F)

pat3, r3 = patch(xloc1,yloc1,phi1G,theta1G,baseH*1000,fov1G)
pat4, r4 = patch(xloc2,yloc2,phi2G,theta2G,baseH*1000,fov2G)

pat1F, r1F = patch(xloc1,yloc1,phi1F,theta1F,heightF*1000,fov1F)
pat2F, r2F = patch(xloc2,yloc2,phi2F,theta2F,heightF*1000,fov2F)

pat3F, r3F = patch(xloc1,yloc1,phi1G,theta1G,heightF*1000,fov1G)
pat4F, r4F = patch(xloc2,yloc2,phi2G,theta2G,heightF*1000,fov2G)

pat1G, r1G = patch(xloc1,yloc1,phi1F,theta1F,heightG*1000,fov1F)
pat2G, r2G = patch(xloc2,yloc2,phi2F,theta2F,heightG*1000,fov2F)

pat3G, r3G = patch(xloc1,yloc1,phi1G,theta1G,heightG*1000,fov1G)
pat4G, r4G = patch(xloc2,yloc2,phi2G,theta2G,heightG*1000,fov2G)

parea1 = patcharea(pat1)
parea2 = patcharea(pat2)
parea3 = patcharea(pat3)
parea4 = patcharea(pat4)

overlapptsF, overlapareaF = patchoverlap(pat1,pat2)
overlapptsG, overlapareaG = patchoverlap(pat3,pat4)

overlapptsFF, overlapareaFF = patchoverlap(pat1F,pat2F)
overlapptsGF, overlapareaGF = patchoverlap(pat3F,pat4F)

overlapptsFG, overlapareaFG = patchoverlap(pat1G,pat2G)
overlapptsGG, overlapareaGG = patchoverlap(pat3G,pat4G)



for i in range(5):
	gpF = math.sqrt(pow(overlapptsF[i,0]-xloc2,2)+pow(overlapptsF[i,1]-yloc2,2))
	arF = math.sqrt(pow(gpF,2)+pow(110000,2))
	print gpF, arF

fig = plt.figure(figsize=(16,12))
ax0 = plt.subplot(121)
ax0.tick_params(axis='both', which='major', labelsize=12)
ax0.tick_params(axis='both', which='minor', labelsize=12)
plt.fill(pat1[:,0],pat1[:,1], color='C0', alpha=0.7, label='AOV @ ' + str(baseH) + 'km (1F)')
plt.fill(pat2[:,0],pat2[:,1], color='C1', alpha=0.7, label='AOV @ ' + str(baseH) + 'km (2F)')
plt.fill(pat3[:,0],pat3[:,1], color='C2', alpha=0.7, label='AOV @ ' + str(baseH) + 'km (1G)')
plt.fill(pat4[:,0],pat4[:,1], color='C3', alpha=0.7, label='AOV @ ' + str(baseH) + 'km (2G)')
plt.plot(overlapptsF[:,0],overlapptsF[:,1], color='c', lw=3, label='F Overlap')
plt.plot(overlapptsG[:,0],overlapptsG[:,1], color='m', lw=3, label='G Overlap')
plt.scatter(xloc1, yloc1, marker='*', s=200, color='c', edgecolors='k', label='Tavistock')
plt.scatter(xloc2, yloc2, marker='*', s=200, color='m', edgecolors='k', label='Elginfield')
plt.xlabel('Easting (m)', size=15)
plt.ylabel('Northing (m)', size=15)
plt.legend(loc='upper right')
plt.axis('equal')

ax1 = plt.subplot(122)
ax1.grid()
ax1.tick_params(axis='both', which='major', labelsize=12)
ax1.tick_params(axis='both', which='minor', labelsize=12)
over1 = ax1.plot(overF,overy, color='c', lw=3, label='F Overlap')
over2 = ax1.plot(overG,overy, color='m', lw=3, label='G Overlap')
ax1.axhline(y=heightF/1000, color='c', ls='-', lw=1)
ax1.axhline(y=heightG/1000, color='m', ls=':', lw=1)
plt.xlim(0,1200)
plt.ylim(50,140)
plt.xlabel('Overlap Area ($\mathregular{km^2}$)', size=15)
plt.ylabel('Height (km)', size=15)
ax1t = ax1.twiny()
rng1 = ax1t.plot(range1F,overy, color='C0', linestyle='--', alpha=0.7, label='Range Field Centre (1F)')
rng2 = ax1t.plot(range2F,overy, color='C1', linestyle='--', alpha=0.7, label='Range Field Centre (2F)')
rng3 = ax1t.plot(range1G,overy, color='C2', linestyle='--', alpha=0.7, label='Range Field Centre (1G)')
rng4 = ax1t.plot(range2G,overy, color='C3', linestyle='--', alpha=0.7, label='Range Field Centre (2G)')
ax1t.set_xlabel('Range to Field Centre (km)', size=15)

data = over1+over2+rng1+rng2+rng3+rng4
labs = [l.get_label() for l in data]
ax1.legend(data, labs, loc='upper right')

#plt.legend()
plt.savefig('/home/mmazur/emccd/Analysis/EMCCDoverlaps100km.png', dpi=300, bbox_inches='tight')
plt.savefig('/home/mmazur/emccd/Analysis/EMCCDoverlaps100km.pdf', dpi=300, bbox_inches='tight')
plt.savefig('/home/mmazur/emccd/Analysis/EMCCDoverlaps100km.eps', dpi=300, bbox_inches='tight')

plt.tight_layout()
plt.show()

fig = plt.figure(figsize=(16,12))

ax0 = plt.subplot(121)
ax0.grid()
ax0.tick_params(axis='both', which='major', labelsize=12)
ax0.tick_params(axis='both', which='minor', labelsize=12)
plt.fill(pat1F[:,0],pat1F[:,1], color='C0', alpha=0.7, label='AOV @ ' + str(heightF) + 'km (1F)')
plt.fill(pat2F[:,0],pat2F[:,1], color='C1', alpha=0.7, label='AOV @ ' + str(heightF) + 'km (2F)')
plt.fill(pat3F[:,0],pat3F[:,1], color='C2', alpha=0.7, label='AOV @ ' + str(heightF) + 'km (1G)')
plt.fill(pat4F[:,0],pat4F[:,1], color='C3', alpha=0.7, label='AOV @ ' + str(heightF) + 'km (2G)')
plt.plot(overlapptsFF[:,0],overlapptsFF[:,1], color='c', lw=3, label='F Overlap')
plt.plot(overlapptsGF[:,0],overlapptsGF[:,1], color='m', lw=3, label='G Overlap')
plt.scatter(xloc1, yloc1, marker='*', s=200, color='c', edgecolors='k', label='Tavistock')
plt.scatter(xloc2, yloc2, marker='*', s=200, color='m', edgecolors='k', label='Elginfield')
plt.xlabel('Easting (m)', size=15)
plt.ylabel('Northing (m)', size=15)
plt.legend(loc='upper right')
plt.axis('equal')

ax1 = plt.subplot(122, sharex=ax0, sharey=ax0)
ax1.grid()
ax1.tick_params(axis='both', which='major', labelsize=12)
ax1.tick_params(axis='both', which='minor', labelsize=12)
plt.fill(pat1G[:,0],pat1G[:,1], color='C0', alpha=0.7, label='AOV @ ' + str(heightG) + 'km (1F)')
plt.fill(pat2G[:,0],pat2G[:,1], color='C1', alpha=0.7, label='AOV @ ' + str(heightG) + 'km (2F)')
plt.fill(pat3G[:,0],pat3G[:,1], color='C2', alpha=0.7, label='AOV @ ' + str(heightG) + 'km (1G)')
plt.fill(pat4G[:,0],pat4G[:,1], color='C3', alpha=0.7, label='AOV @ ' + str(heightG) + 'km (2G)')
plt.plot(overlapptsFG[:,0],overlapptsFG[:,1], color='c', lw=3, label='F Overlap')
plt.plot(overlapptsGG[:,0],overlapptsGG[:,1], color='m', lw=3, label='G Overlap')
plt.scatter(xloc1, yloc1, marker='*', s=200, color='c', edgecolors='k', label='Tavistock')
plt.scatter(xloc2, yloc2, marker='*', s=200, color='m', edgecolors='k', label='Elginfield')
plt.xlabel('Easting (m)', size=15)
plt.ylabel('Northing (m)', size=15)
plt.legend(loc='upper right')
plt.axis('equal')

#plt.legend()
plt.savefig('/home/mmazur/emccd/Analysis/EMCCDoverlaps-2heights.png', dpi=300, bbox_inches='tight')
plt.savefig('/home/mmazur/emccd/Analysis/EMCCDoverlaps-2heights.pdf', dpi=300, bbox_inches='tight')
plt.savefig('/home/mmazur/emccd/Analysis/EMCCDoverlaps-2heights.eps', dpi=300, bbox_inches='tight')

plt.tight_layout()
plt.show()