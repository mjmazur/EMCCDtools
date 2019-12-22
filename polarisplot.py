import numpy as np
import pandas as pd
import matplotlib.ticker as ticker
from matplotlib import pyplot as plt
from datetime import datetime
from ephem import Sun, Observer, pi, hours

data = pd.read_csv('polaris2019.log', comment='#', delim_whitespace=True, low_memory=False, skip_blank_lines=True)
data.columns = ['time', 'cx', 'cy', 'mag', '5', '6', '7', '8']

data.drop(data[data.mag > -14].index, inplace=True)
data.reset_index(drop=True, inplace=True)

#print(datetime.utcfromtimestamp(data['time'][0]).strftime('%H:%M:%S'))

data['t2'] = 99

for i in range(len(data.index)):
	t = int(datetime.fromtimestamp(data['time'][i]).strftime('%H')) + float(datetime.fromtimestamp(data['time'][i]).strftime('%M'))/60 + float(datetime.fromtimestamp(data['time'][i]).strftime('%S'))/3600
	if t < 12.0:
		data.loc[i,'t2'] = t
	else:
		data.loc[i,'t2'] = t -24

# print(data[pd.to_numeric(data['time'], errors=coerce).isnull()])

#data['time'] = data[pd.to_numeric(data['time'], errors=coerce)]

#data.astype({'time':'int32'}).dtypes

# print data.dtypes
# print int(data['time'][0])
# print(data['time'])

# plt.figure(figsize=(14,10))
# #plt.scatter(data['t2'],data['mag'])
# n, bins, patches = plt.hist(data['t2'], bins=96)
# plt.xlim(-12,12)
# plt.show()

dt = '2016/5/27 00:00'
sun = Sun()
sun.compute(dt)

elginfield = Observer()
elginfield.lat = 43.19237
elginfield.lon = -81.31799
elginfield.date = dt
ra, dec = elginfield.radec_of('0', '-90')

print('RA_sun:',sun.ra)
print('Elgin nadir', ra)
print('Solar time:', hours((ra-sun.ra)%(2*pi)), 'hours')

fig, ax = plt.subplots(figsize=(14,10))
n, bins, patches = ax.hist(data['t2'], bins=192, rwidth=0.9, edgecolor='black')
ax.axvline(0, color='red')

plt.xlim(-12,12)

ax.xaxis.set_major_locator(ticker.MultipleLocator(1))
ticks = ax.get_xticks()
ticks[ticks <0] += 24
ax.set_xticklabels([int(tick) for tick in ticks])
ax.xaxis.set_tick_params(labelsize=12)
ax.yaxis.set_tick_params(labelsize=12)

ax.set_xlabel('Local Time (24h)', size=15)
ax.set_ylabel('Count', size=15)

#plt.xlim(-12,12)
plt.tight_layout()
plt.savefig('ShedOpenTimes.png', dpi=300)
plt.show()