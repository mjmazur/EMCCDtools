
# coding: utf-8

# ## GAIA Data Retrieval
# The code below reads from a SExtractor output catalog and retrieves the G-band magnitude of the star from the GAIA DR1 catalogue

# In[33]:


# import astropy.units as u
from astropy.coordinates.sky_coordinate import SkyCoord
from astropy.units import Quantity
from astroquery.gaia import Gaia
import matplotlib.pyplot as plt
import numpy as np
from astroquery.gaia import Gaia
import warnings
import os, sys
import pandas as pd

warnings.filterwarnings('ignore')

SR = 0.1

data = pd.read_csv('test.cat', delim_whitespace=True, skiprows=14)
data.columns = ['Number','XWIN','YWIN','XWORLD','YWORLD','MAG','MAGERROR','FLUX','FLUXERROR','FLUXRADIUS','FWHM','BACKGROUND','RA','DEC']
RA = data.loc[1,'RA']
DEC = data.loc[1,'DEC']

print len(data.index)

tables = Gaia.load_tables(only_names=True)

#for table in (tables):
#    print (table.get_qualified_name())

job = Gaia.launch_job_async("SELECT * 	FROM gaiadr1.gaia_source  	WHERE CONTAINS(POINT('ICRS',gaiadr1.gaia_source.ra,gaiadr1.gaia_source.dec),	CIRCLE('ICRS'," + str(RA) + "," + str(DEC) + "," + str(SR) + "))=1    AND  (phot_g_mean_mag<=14);" , dump_to_file=True)

print (job)

r = job.get_results()
print (r['source_id'])
#print (r['ra'])
#print (r['dec'])
#print (r['phot_g_mean_mag'])

plt.scatter(r['pmra'], r['pmdec'], color='r', alpha=0.3)
plt.xlim(-60,80)
plt.ylim(-120,30)

plt.show()

