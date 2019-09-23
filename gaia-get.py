import astropy.units as u
from astropy.coordinates.sky_coordinate import SkyCoord
from astropy.units import Quantity
from astroquery.gaia import Gaia
import matplotlib.pyplot as plt
import numpy as np
from astroquery.gaia import Gaia
import warnings
warnings.filterwarnings('ignore')


tables = Gaia.load_tables(only_names=True)

#for table in (tables):
#    print (table.get_qualified_name())

job = Gaia.launch_job_async("SELECT * \
	FROM gaiadr1.gaia_source  \
	WHERE CONTAINS(POINT('ICRS',gaiadr1.gaia_source.ra,gaiadr1.gaia_source.dec),\
	CIRCLE('ICRS',75.41875,57.13639,0.013888888888888888))=1    AND  (phot_g_mean_mag<=14);" \
, dump_to_file=True)

print (job)

r = job.get_results()
print (r['source_id'])
print (r['ra'])
print (r['dec'])
print (r['phot_g_mean_mag'])

plt.scatter(r['pmra'], r['pmdec'], color='r', alpha=0.3)
plt.xlim(-60,80)
plt.ylim(-120,30)

plt.show()