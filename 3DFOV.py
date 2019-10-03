import numpy as np
import matplotlib as mpl
import mpl_toolkits.mplot3d as a3
import matplotlib.pyplot as plt
import matplotlib.colors as colors
import pylab as pl
import scipy as sp
import math
import utm
from matplotlib.patches import Polygon
from matplotlib import pyplot
from shapely.geometry import Point, Polygon
from descartes import PolygonPatch

def plotlines1(theta,phi,h,fov):
	# Plot lines for site 1 (Elginfield)
	z = np.linspace(0, h, 100)

	theta1 = theta - fov/2
	theta2 = theta + fov/2
	phi1 = phi - fov/2
	phi2 = phi + fov/2

	rho = z / math.cos(phi1)
	x = rho * math.sin(phi1) * math.cos(theta1)
	y = rho * math.sin(phi1) * math.sin(theta1)
	poly1[0,0] = x[len(x)-1]
	poly1[0,1] = y[len(x)-1]
	poly1[0,2] = h

	ax.plot(x, y, z, 'b', lw=1)

	rho = z / math.cos(phi1)
	x = rho * math.sin(phi1) * math.cos(theta2)
	y = rho * math.sin(phi1) * math.sin(theta2)
	poly1[1,0] = x[len(x)-1]
	poly1[1,1] = y[len(x)-1]
	poly1[1,2] = h

	ax.plot(x, y, z, 'b', lw=1)

	rho = z / math.cos(phi2)
	x = rho * math.sin(phi2) * math.cos(theta2)
	y = rho * math.sin(phi2) * math.sin(theta2)
	poly1[2,0] = x[len(x)-1]
	poly1[2,1] = y[len(x)-1]
	poly1[2,2] = h

	ax.plot(x, y, z, 'b', lw=1)

	rho = z / math.cos(phi2)
	x = rho * math.sin(phi2) * math.cos(theta1)
	y = rho * math.sin(phi2) * math.sin(theta1)
	poly1[3,0] = x[len(x)-1]
	poly1[3,1] = y[len(x)-1]
	poly1[3,2] = h

	ax.plot(x, y, z, 'b', lw=1)

	rho = z / math.cos(phi)
	x = rho * math.sin(phi) * math.cos(theta)
	y = rho * math.sin(phi) * math.sin(theta)

	ax.plot(x, y, z, color='r')

def plotlines2(x,y,theta,phi,h,fov):

	z = np.linspace(0, h, 100)
	theta3 = theta - fov/2
	theta4 = theta + fov/2
	phi3 = phi - fov/2
	phi4 = phi + fov/2

	rho = z / math.cos(phi3)
	x = rho * math.sin(phi3) * math.cos(theta3) + xloc
	y = rho * math.sin(phi3) * math.sin(theta3) + yloc
	poly2[0,0] = x[len(x)-1]
	poly2[0,1] = y[len(x)-1]
	poly2[0,2] = h

	ax.plot(x, y, z,'g', lw=1)

	rho = z / math.cos(phi3)
	x = rho * math.sin(phi3) * math.cos(theta4) + xloc
	y = rho * math.sin(phi3) * math.sin(theta4) + yloc
	poly2[1,0] = x[len(x)-1]
	poly2[1,1] = y[len(x)-1]
	poly2[1,2] = h

	ax.plot(x, y, z, 'g', lw=1)

	rho = z / math.cos(phi4)
	x = rho * math.sin(phi4) * math.cos(theta4) + xloc
	y = rho * math.sin(phi4) * math.sin(theta4) + yloc
	poly2[2,0] = x[len(x)-1]
	poly2[2,1] = y[len(x)-1]
	poly2[2,2] = h

	ax.plot(x, y, z, 'g', lw=1)

	rho = z / math.cos(phi4)
	x = rho * math.sin(phi4) * math.cos(theta3) + xloc
	y = rho * math.sin(phi4) * math.sin(theta3) + yloc
	poly2[3,0] = x[len(x)-1]
	poly2[3,1] = y[len(x)-1]
	poly2[3,2] = h

	ax.plot(x, y, z, 'g', lw=1)

	rho = z / math.cos(phi)
	x = rho * math.sin(phi) * math.cos(theta) + xloc
	y = rho * math.sin(phi) * math.sin(theta) + yloc

	ax.plot(x, y, z, color='m')

def plotpatches(poly,r,g,b,alpha):
	pts = []
	# Plot polygon patches
	tri = a3.art3d.Poly3DCollection([poly])
	#tri.set_color(colors.rgb2hex(sp.rand(3)))
	tri.set_facecolor((r,g,b,alpha))
	tri.set_edgecolor('w')
	ax.add_collection3d(tri)

def polygonarea(poly):
	a = (poly[0,0], poly[0,1])
	b = (poly[1,0], poly[1,1])
	c = (poly[2,0], poly[2,1])
	d = (poly[3,0], poly[3,1])

	polygon = Polygon([a, b, c, d])
	parea = polygon.area
	return parea

def polygonoverlap(poly1,poly2):
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
	overlaparea = overlap.area
	points = np.asarray(overlap.exterior)
	return points

def returnpoly(x,y,theta,phi,h,fov):

	z = np.linspace(0, h, 100)
	theta3 = theta - fov/2
	theta4 = theta + fov/2
	phi3 = phi - fov/2
	phi4 = phi + fov/2

	rho = z / math.cos(phi3)
	x = rho * math.sin(phi3) * math.cos(theta3) + xloc
	y = rho * math.sin(phi3) * math.sin(theta3) + yloc
	poly[0,0] = x[len(x)-1]
	poly[0,1] = y[len(x)-1]
	poly[0,2] = h

	rho = z / math.cos(phi3)
	x = rho * math.sin(phi3) * math.cos(theta4) + xloc
	y = rho * math.sin(phi3) * math.sin(theta4) + yloc
	poly[1,0] = x[len(x)-1]
	poly[1,1] = y[len(x)-1]
	poly[1,2] = h

	rho = z / math.cos(phi4)
	x = rho * math.sin(phi4) * math.cos(theta4) + xloc
	y = rho * math.sin(phi4) * math.sin(theta4) + yloc
	poly[2,0] = x[len(x)-1]
	poly[2,1] = y[len(x)-1]
	poly[2,2] = h

	rho = z / math.cos(phi4)
	x = rho * math.sin(phi4) * math.cos(theta3) + xloc
	y = rho * math.sin(phi4) * math.sin(theta3) + yloc
	poly[3,0] = x[len(x)-1]
	poly[3,1] = y[len(x)-1]
	poly[3,2] = h

	return poly


def kmlstart():
	file.write('<Placemark>\n')
	file.write('<Style>\n')
	file.write('  <PolyStyle>\n')
	file.write('   <color>#50555555</color>\n')
	file.write('  <outline>1</outline>\n')
	file.write('  </PolyStyle>\n') 
	file.write(' </Style>\n')
	file.write('        <Polygon>\n')
	file.write('            <altitudeMode>relativeToGround</altitudeMode>\n')
	file.write('            <outerBoundaryIs>\n')
	file.write('                <LinearRing>\n')
	file.write('<coordinates>\n')

def kmlend():
	file.write('</coordinates>\n')
	file.write('                </LinearRing>\n')
	file.write('            </outerBoundaryIs>\n')
	file.write('        </Polygon>\n')
	file.write('</Placemark>\n')

# Setup site parameters. Site 1 is assumed to be at the axis
# origin. Site 2 is offset from 1 by xloc and yloc.

height1 = 100
height2 = 100

offseteast = 474332.51
offseteastutm = -81.315894
offsetnorth = 4782239.36
offsetnorthutm = 43.1924908

print utm.to_latlon(offseteast,offsetnorth,17,'T')

# Site 1, Camera 1 (2F)
theta11 = 84.604 * math.pi/180 # angle measured west from east=0 (ideal is 89.25, 17.63)
phi11 = 16.155 * math.pi/180 # angle measured south from zenith
fov11 = 14.7 * math.pi/180

# Site 1, Camera 2 (2G)
theta12 = 96.769 * math.pi/180 # angle measured west from east=0 (ideal is 74.48, 26.1)
phi12 = 39.355 * math.pi/180 # angle measured south from zenith
fov12 = 14.7 * math.pi/180

# Site 2, Camera 1 (1F)
xloc = 43.5
yloc = 7.5
site2long = -80.7724527
site2lat = 43.2639855

theta21 = 147.670 * math.pi/180 # angle measured west from east=0
phi21 = 25.356 * math.pi/180 # angle measured south from zenith
#theta21 = 148.97 * math.pi/180
#phi21 = 25.57 * math.pi/180

fov21 = 14.47 * math.pi/180 # field of view

# Site 2, Camera 2 (1G)
theta22 = 120.343 * math.pi/180 # angle measured west from east=0 132.25 125
phi22 = 42.735 * math.pi/180 # angle measured south from zenith 27.66 43
fov22 = 14.7 * math.pi/180 # field of view

# Start plotting
mpl.rcParams['legend.fontsize'] = 10

fig = plt.figure()
ax = fig.gca(projection='3d')

poly1 = np.zeros([4,3])
poly2 = np.zeros([4,3])

plotlines1(theta11,phi11,height1,fov11)
print 'poly1'
print poly1
plotlines2(xloc,yloc,theta21,phi21,height1,fov21)
print 'poly1'
print poly1
plotpatches(poly1,0,0,1,0.3)
plotpatches(poly2,0,1,0,0.3)

#print poly2

overlap = polygonoverlap(poly1,poly2)
p1 = poly1
p2 = poly2
overlap = np.insert(overlap, 2, values=height1, axis=1)
plotpatches(overlap,0,0,0,1)
print poly1
overlap1 = overlap

parea = polygonarea(overlap)
#textstr = 'Overlap @ ' + str(height1) + ' km = ' + str(parea) + 'km'
textstr1 = 'F Overlap @ %.2fkm = %.1fkm**2' % (height1, parea)
props = dict(boxstyle='round', facecolor='wheat', alpha=0.5)
ax.text2D(-0.1, 0.06, textstr1, transform=ax.transAxes, fontsize=10, verticalalignment='top', bbox=props)

poly1 = np.zeros([4,3])
poly2 = np.zeros([4,3])

plotlines1(theta12,phi12,height2,fov12)
plotlines2(xloc,yloc,theta22,phi22,height2,fov22)

plotpatches(poly1,0.5,0.5,1,0.3)
plotpatches(poly2,0.5,1,0.5,0.3)

overlap = polygonoverlap(poly1,poly2)
print poly1
p3 = poly1
p4 = poly2
overlap = np.insert(overlap, 2, values=height2, axis=1)
plotpatches(overlap,0,0,0,1)

print p1, p3

overlap2 = overlap

file = open('overlap.kml','w')


file.write('<?xml version="1.0" encoding="UTF-8"?>\n')
file.write('<kml xmlns="http://www.opengis.net/kml/2.2" xmlns:gx="http://www.google.com/kml/ext/2.2" xmlns:kml="http://www.opengis.net/kml/2.2" xmlns:atom="http://www.w3.org/2005/Atom">\n')
file.write('<Document>\n')
file.write('    <name>pm1.kml</name>\n')
file.write('    <Style id="poly">\n')
file.write('        <LineStyle>\n')
file.write('            <color>f0ffed42</color>\n')
file.write('        </LineStyle>\n')
file.write('        <PolyStyle>\n')
file.write('            <color>e8ff9257</color>\n')
file.write('        </PolyStyle>\n')
file.write('    </Style>\n')
file.write('<Placemark>\n')
file.write('<Style>\n')
file.write('  <PolyStyle>\n')
file.write('   <color>#a00000ff</color>\n')
file.write('  <outline>0</outline>\n')
file.write('  </PolyStyle>\n') 
file.write(' </Style>\n')
file.write('        <Polygon>\n')
file.write('            <altitudeMode>relativeToGround</altitudeMode>\n')
file.write('            <outerBoundaryIs>\n')
file.write('                <LinearRing>\n')

file.write('<coordinates>\n')

for i in range(len(overlap1)):
	overlapcoords = utm.to_latlon(offseteast + overlap1[i,0]*1000, offsetnorth + overlap1[i,1]*1000, 17, 'T')
	file.write(str(overlapcoords[1]) + ',' + str(overlapcoords[0]) + ',' + str(height1*1000) + '\n')

file.write('</coordinates>\n')
file.write('                </LinearRing>\n')
file.write('            </outerBoundaryIs>\n')
file.write('        </Polygon>\n')
file.write('</Placemark>\n')

file.write('<Placemark>\n')
file.write('<Style>\n')
file.write('  <PolyStyle>\n')
file.write('   <color>#a00000ff</color>\n')
file.write('  <outline>0</outline>\n')
file.write('  </PolyStyle>\n') 
file.write(' </Style>\n')
file.write('        <Polygon>\n')
file.write('            <altitudeMode>relativeToGround</altitudeMode>\n')
file.write('            <outerBoundaryIs>\n')
file.write('                <LinearRing>\n')
file.write('<coordinates>\n')

for i in range(len(overlap2)):
	overlapcoords = utm.to_latlon(offseteast + overlap2[i,0]*1000, offsetnorth + overlap2[i,1]*1000, 17, 'T')
	file.write(str(overlapcoords[1]) + ',' + str(overlapcoords[0]) + ',' + str(height1*1000) + '\n')

file.write('</coordinates>\n')
file.write('                </LinearRing>\n')
file.write('            </outerBoundaryIs>\n')
file.write('        </Polygon>\n')
file.write('</Placemark>\n')

kmlstart()

polycoords = utm.to_latlon(offseteast + p1[0,0]*1000, offsetnorth + p1[0,1]*1000, 17, 'T')
file.write(str(polycoords[1]) + ',' + str(polycoords[0]) + ',' + str(height1*1000) + '\n')
polycoords = utm.to_latlon(offseteast + p1[1,0]*1000, offsetnorth + p1[1,1]*1000, 17, 'T')
file.write(str(polycoords[1]) + ',' + str(polycoords[0]) + ',' + str(height1*1000) + '\n')
file.write(str(offseteastutm) + ',' + str(offsetnorthutm) + ',' + str(0) + '\n')
polycoords = utm.to_latlon(offseteast + p1[0,0]*1000, offsetnorth + p1[0,1]*1000, 17, 'T')
file.write(str(polycoords[1]) + ',' + str(polycoords[0]) + ',' + str(height1*1000) + '\n')

kmlend()
kmlstart()

polycoords = utm.to_latlon(offseteast + p1[1,0]*1000, offsetnorth + p1[1,1]*1000, 17, 'T')
file.write(str(polycoords[1]) + ',' + str(polycoords[0]) + ',' + str(height1*1000) + '\n')
polycoords = utm.to_latlon(offseteast + p1[2,0]*1000, offsetnorth + p1[2,1]*1000, 17, 'T')
file.write(str(polycoords[1]) + ',' + str(polycoords[0]) + ',' + str(height1*1000) + '\n')
file.write(str(offseteastutm) + ',' + str(offsetnorthutm) + ',' + str(0) + '\n')
polycoords = utm.to_latlon(offseteast + p1[1,0]*1000, offsetnorth + p1[1,1]*1000, 17, 'T')
file.write(str(polycoords[1]) + ',' + str(polycoords[0]) + ',' + str(height1*1000) + '\n')

kmlend()
kmlstart()

polycoords = utm.to_latlon(offseteast + p1[2,0]*1000, offsetnorth + p1[2,1]*1000, 17, 'T')
file.write(str(polycoords[1]) + ',' + str(polycoords[0]) + ',' + str(height1*1000) + '\n')
polycoords = utm.to_latlon(offseteast + p1[3,0]*1000, offsetnorth + p1[3,1]*1000, 17, 'T')
file.write(str(polycoords[1]) + ',' + str(polycoords[0]) + ',' + str(height1*1000) + '\n')
file.write(str(offseteastutm) + ',' + str(offsetnorthutm) + ',' + str(0) + '\n')
polycoords = utm.to_latlon(offseteast + p1[2,0]*1000, offsetnorth + p1[2,1]*1000, 17, 'T')
file.write(str(polycoords[1]) + ',' + str(polycoords[0]) + ',' + str(height1*1000) + '\n')

kmlend()
kmlstart()

polycoords = utm.to_latlon(offseteast + p1[3,0]*1000, offsetnorth + p1[3,1]*1000, 17, 'T')
file.write(str(polycoords[1]) + ',' + str(polycoords[0]) + ',' + str(height1*1000) + '\n')
polycoords = utm.to_latlon(offseteast + p1[0,0]*1000, offsetnorth + p1[0,1]*1000, 17, 'T')
file.write(str(polycoords[1]) + ',' + str(polycoords[0]) + ',' + str(height1*1000) + '\n')
file.write(str(offseteastutm) + ',' + str(offsetnorthutm) + ',' + str(0) + '\n')
polycoords = utm.to_latlon(offseteast + p1[3,0]*1000, offsetnorth + p1[3,1]*1000, 17, 'T')
file.write(str(polycoords[1]) + ',' + str(polycoords[0]) + ',' + str(height1*1000) + '\n')

# Second site

kmlend()
kmlstart()

polycoords = utm.to_latlon(offseteast + p2[0,0]*1000, offsetnorth + p2[0,1]*1000, 17, 'T')
file.write(str(polycoords[1]) + ',' + str(polycoords[0]) + ',' + str(height1*1000) + '\n')
polycoords = utm.to_latlon(offseteast + p2[1,0]*1000, offsetnorth + p2[1,1]*1000, 17, 'T')
file.write(str(polycoords[1]) + ',' + str(polycoords[0]) + ',' + str(height1*1000) + '\n')
file.write(str(site2long) + ',' + str(site2lat) + ',' + str(0) + '\n')
polycoords = utm.to_latlon(offseteast + p2[0,0]*1000, offsetnorth + p2[0,1]*1000, 17, 'T')
file.write(str(polycoords[1]) + ',' + str(polycoords[0]) + ',' + str(height1*1000) + '\n')

kmlend()
kmlstart()

polycoords = utm.to_latlon(offseteast + p2[1,0]*1000, offsetnorth + p2[1,1]*1000, 17, 'T')
file.write(str(polycoords[1]) + ',' + str(polycoords[0]) + ',' + str(height1*1000) + '\n')
polycoords = utm.to_latlon(offseteast + p2[2,0]*1000, offsetnorth + p2[2,1]*1000, 17, 'T')
file.write(str(polycoords[1]) + ',' + str(polycoords[0]) + ',' + str(height1*1000) + '\n')
file.write(str(site2long) + ',' + str(site2lat) + ',' + str(0) + '\n')
polycoords = utm.to_latlon(offseteast + p2[1,0]*1000, offsetnorth + p2[1,1]*1000, 17, 'T')
file.write(str(polycoords[1]) + ',' + str(polycoords[0]) + ',' + str(height1*1000) + '\n')

kmlend()
kmlstart()

polycoords = utm.to_latlon(offseteast + p2[2,0]*1000, offsetnorth + p2[2,1]*1000, 17, 'T')
file.write(str(polycoords[1]) + ',' + str(polycoords[0]) + ',' + str(height1*1000) + '\n')
polycoords = utm.to_latlon(offseteast + p2[3,0]*1000, offsetnorth + p2[3,1]*1000, 17, 'T')
file.write(str(polycoords[1]) + ',' + str(polycoords[0]) + ',' + str(height1*1000) + '\n')
file.write(str(site2long) + ',' + str(site2lat) + ',' + str(0) + '\n')
polycoords = utm.to_latlon(offseteast + p2[2,0]*1000, offsetnorth + p2[2,1]*1000, 17, 'T')
file.write(str(polycoords[1]) + ',' + str(polycoords[0]) + ',' + str(height1*1000) + '\n')

kmlend()
kmlstart()

polycoords = utm.to_latlon(offseteast + p2[3,0]*1000, offsetnorth + p2[3,1]*1000, 17, 'T')
file.write(str(polycoords[1]) + ',' + str(polycoords[0]) + ',' + str(height1*1000) + '\n')
polycoords = utm.to_latlon(offseteast + p2[0,0]*1000, offsetnorth + p2[0,1]*1000, 17, 'T')
file.write(str(polycoords[1]) + ',' + str(polycoords[0]) + ',' + str(height1*1000) + '\n')
file.write(str(site2long) + ',' + str(site2lat) + ',' + str(0) + '\n')
polycoords = utm.to_latlon(offseteast + p2[3,0]*1000, offsetnorth + p2[3,1]*1000, 17, 'T')
file.write(str(polycoords[1]) + ',' + str(polycoords[0]) + ',' + str(height1*1000) + '\n')

# Other field
kmlend()
kmlstart()

polycoords = utm.to_latlon(offseteast + p3[0,0]*1000, offsetnorth + p3[0,1]*1000, 17, 'T')
file.write(str(polycoords[1]) + ',' + str(polycoords[0]) + ',' + str(height1*1000) + '\n')
polycoords = utm.to_latlon(offseteast + p3[1,0]*1000, offsetnorth + p3[1,1]*1000, 17, 'T')
file.write(str(polycoords[1]) + ',' + str(polycoords[0]) + ',' + str(height1*1000) + '\n')
file.write(str(offseteastutm) + ',' + str(offsetnorthutm) + ',' + str(0) + '\n')
polycoords = utm.to_latlon(offseteast + p3[0,0]*1000, offsetnorth + p3[0,1]*1000, 17, 'T')
file.write(str(polycoords[1]) + ',' + str(polycoords[0]) + ',' + str(height1*1000) + '\n')

kmlend()
kmlstart()

polycoords = utm.to_latlon(offseteast + p3[1,0]*1000, offsetnorth + p3[1,1]*1000, 17, 'T')
file.write(str(polycoords[1]) + ',' + str(polycoords[0]) + ',' + str(height1*1000) + '\n')
polycoords = utm.to_latlon(offseteast + p3[2,0]*1000, offsetnorth + p3[2,1]*1000, 17, 'T')
file.write(str(polycoords[1]) + ',' + str(polycoords[0]) + ',' + str(height1*1000) + '\n')
file.write(str(offseteastutm) + ',' + str(offsetnorthutm) + ',' + str(0) + '\n')
polycoords = utm.to_latlon(offseteast + p3[1,0]*1000, offsetnorth + p3[1,1]*1000, 17, 'T')
file.write(str(polycoords[1]) + ',' + str(polycoords[0]) + ',' + str(height1*1000) + '\n')

kmlend()
kmlstart()

polycoords = utm.to_latlon(offseteast + p3[2,0]*1000, offsetnorth + p3[2,1]*1000, 17, 'T')
file.write(str(polycoords[1]) + ',' + str(polycoords[0]) + ',' + str(height1*1000) + '\n')
polycoords = utm.to_latlon(offseteast + p3[3,0]*1000, offsetnorth + p3[3,1]*1000, 17, 'T')
file.write(str(polycoords[1]) + ',' + str(polycoords[0]) + ',' + str(height1*1000) + '\n')
file.write(str(offseteastutm) + ',' + str(offsetnorthutm) + ',' + str(0) + '\n')
polycoords = utm.to_latlon(offseteast + p3[2,0]*1000, offsetnorth + p3[2,1]*1000, 17, 'T')
file.write(str(polycoords[1]) + ',' + str(polycoords[0]) + ',' + str(height1*1000) + '\n')

kmlend()
kmlstart()

polycoords = utm.to_latlon(offseteast + p3[3,0]*1000, offsetnorth + p3[3,1]*1000, 17, 'T')
file.write(str(polycoords[1]) + ',' + str(polycoords[0]) + ',' + str(height1*1000) + '\n')
polycoords = utm.to_latlon(offseteast + p3[0,0]*1000, offsetnorth + p3[0,1]*1000, 17, 'T')
file.write(str(polycoords[1]) + ',' + str(polycoords[0]) + ',' + str(height1*1000) + '\n')
file.write(str(offseteastutm) + ',' + str(offsetnorthutm) + ',' + str(0) + '\n')
polycoords = utm.to_latlon(offseteast + p3[3,0]*1000, offsetnorth + p3[3,1]*1000, 17, 'T')
file.write(str(polycoords[1]) + ',' + str(polycoords[0]) + ',' + str(height1*1000) + '\n')

# Second site

kmlend()
kmlstart()

polycoords = utm.to_latlon(offseteast + p4[0,0]*1000, offsetnorth + p4[0,1]*1000, 17, 'T')
file.write(str(polycoords[1]) + ',' + str(polycoords[0]) + ',' + str(height1*1000) + '\n')
polycoords = utm.to_latlon(offseteast + p4[1,0]*1000, offsetnorth + p4[1,1]*1000, 17, 'T')
file.write(str(polycoords[1]) + ',' + str(polycoords[0]) + ',' + str(height1*1000) + '\n')
file.write(str(site2long) + ',' + str(site2lat) + ',' + str(0) + '\n')
polycoords = utm.to_latlon(offseteast + p4[0,0]*1000, offsetnorth + p4[0,1]*1000, 17, 'T')
file.write(str(polycoords[1]) + ',' + str(polycoords[0]) + ',' + str(height1*1000) + '\n')

kmlend()
kmlstart()

polycoords = utm.to_latlon(offseteast + p4[1,0]*1000, offsetnorth + p4[1,1]*1000, 17, 'T')
file.write(str(polycoords[1]) + ',' + str(polycoords[0]) + ',' + str(height1*1000) + '\n')
polycoords = utm.to_latlon(offseteast + p4[2,0]*1000, offsetnorth + p4[2,1]*1000, 17, 'T')
file.write(str(polycoords[1]) + ',' + str(polycoords[0]) + ',' + str(height1*1000) + '\n')
file.write(str(site2long) + ',' + str(site2lat) + ',' + str(0) + '\n')
polycoords = utm.to_latlon(offseteast + p4[1,0]*1000, offsetnorth + p4[1,1]*1000, 17, 'T')
file.write(str(polycoords[1]) + ',' + str(polycoords[0]) + ',' + str(height1*1000) + '\n')

kmlend()
kmlstart()

polycoords = utm.to_latlon(offseteast + p4[2,0]*1000, offsetnorth + p4[2,1]*1000, 17, 'T')
file.write(str(polycoords[1]) + ',' + str(polycoords[0]) + ',' + str(height1*1000) + '\n')
polycoords = utm.to_latlon(offseteast + p4[3,0]*1000, offsetnorth + p4[3,1]*1000, 17, 'T')
file.write(str(polycoords[1]) + ',' + str(polycoords[0]) + ',' + str(height1*1000) + '\n')
file.write(str(site2long) + ',' + str(site2lat) + ',' + str(0) + '\n')
polycoords = utm.to_latlon(offseteast + p4[2,0]*1000, offsetnorth + p4[2,1]*1000, 17, 'T')
file.write(str(polycoords[1]) + ',' + str(polycoords[0]) + ',' + str(height1*1000) + '\n')

kmlend()
kmlstart()

polycoords = utm.to_latlon(offseteast + p4[3,0]*1000, offsetnorth + p4[3,1]*1000, 17, 'T')
file.write(str(polycoords[1]) + ',' + str(polycoords[0]) + ',' + str(height1*1000) + '\n')
polycoords = utm.to_latlon(offseteast + p4[0,0]*1000, offsetnorth + p4[0,1]*1000, 17, 'T')
file.write(str(polycoords[1]) + ',' + str(polycoords[0]) + ',' + str(height1*1000) + '\n')
file.write(str(site2long) + ',' + str(site2lat) + ',' + str(0) + '\n')
polycoords = utm.to_latlon(offseteast + p4[3,0]*1000, offsetnorth + p4[3,1]*1000, 17, 'T')
file.write(str(polycoords[1]) + ',' + str(polycoords[0]) + ',' + str(height1*1000) + '\n')

file.write('</coordinates>\n')
file.write('                </LinearRing>\n')
file.write('            </outerBoundaryIs>\n')
file.write('        </Polygon>\n')
file.write('</Placemark>\n')
file.write('</Document>\n')
file.write('</kml>\n')

file.close()

parea = polygonarea(overlap)
#textstr = 'Overlap @ ' + str(height2) + ' km = ' + str(parea) + 'km'
textstr2 = 'G Overlap @ %.2fkm = %.1fkm**2' % (height2, parea)
props = dict(boxstyle='round', facecolor='wheat', alpha=0.5)
ax.text2D(-0.1, -0.05, textstr2, transform=ax.transAxes, fontsize=10, verticalalignment='top', bbox=props)

#plotlines1(theta12,phi12,height2+15,fov12)
#plotlines2(xloc,yloc,theta22,phi22,height2+15,fov22)
poly = np.zeros([4,3])

for i in range(-20,20):
	poly1 = returnpoly(0.0,0.0,theta11,phi11,height1+i,fov11)
	poly2 = returnpoly(xloc,yloc,theta21,phi21,height1+i,fov21)
	overlap = polygonoverlap(poly1,poly2)
	overlap = np.insert(overlap, 2, values=height2, axis=1)
	parea = polygonarea(overlap)
	#print parea

# Set labels
ax.set_xlabel('East')
ax.set_ylabel('North')
ax.set_zlabel('Height (km)')
plt.title('Camera Image Patches')

plt.show()