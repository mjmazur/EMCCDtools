# import astropy.units as u
#from astropy.coordinates.sky_coordinate import SkyCoord
#from astropy.units import Quantity
from astroquery.gaia import Gaia
import matplotlib.pyplot as plt
#import numpy as np
#from astroquery.gaia import Gaia
import warnings
import sys
import pandas as pd

def getdata(RA,DEC,SR):
    job = Gaia.launch_job_async("SELECT * \
	FROM gaiadr2.gaia_source  \
	WHERE CONTAINS(POINT('ICRS',gaiadr2.gaia_source.ra,gaiadr2.gaia_source.dec),\
	CIRCLE('ICRS'," + str(RA) + "," + str(DEC) + "," + str(SR) + "))=1 ORDER BY phot_g_mean_mag ASC;" \
, dump_to_file=True)

    r = job.get_results()

    return r

warnings.filterwarnings('ignore')

# filename = 'test.cat'
filename = sys.argv[1]

SR = 0.15 # Search Radius

data = pd.read_csv(filename, delim_whitespace=True, skiprows=14)
data.columns = ['Number','XWIN','YWIN','XWORLD','YWORLD','MAG','MAGERROR','FLUX','FLUXERROR','FLUXRADIUS','FWHM','BACKGROUND','RA','DEC']

# print RA, DEC
# print len(data.index)

data['BMAG'] = 99
data['GMAG'] = 99
data['RMAG'] = 99

# print(data.MAG)

tables = Gaia.load_tables(only_names=True)

for i in range(len(data.index)):
    RA = data.loc[i,'RA']
    DEC = data.loc[i,'DEC']
    gdata = getdata(RA,DEC,SR)
    if len(gdata) > 0:
        data.loc[i,'BMAG'] = gdata[0]['phot_bp_mean_mag']
        data.loc[i,'GMAG'] = gdata[0]['phot_g_mean_mag']
        data.loc[i,'RMAG'] = gdata[0]['phot_rp_mean_mag']
    print(i)
    # data.to_pickle('out.pkl')

print('Pickling...')
data.to_pickle('out.pkl')
print('Pickled...')
       

#print (gdata['phot_g_mean_mag'])
#print data.loc[0,'MAG']

print('Plotting figure...')

plt.figure(figsize=(14,10))

plt.scatter(data['GMAG'],data['MAG'])
plt.xlabel('GAIA DR2 G-band Magnitude', size=15)
plt.ylabel('Instrumental Magnitude', size=15)
plt.xlim(5,13)
plt.ylim(-15,-5)
plt.tight_layout()
plt.savefig('Imag-vs-Gmag.png', dpi=300)

plt.show()


