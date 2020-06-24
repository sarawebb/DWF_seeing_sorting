import numpy as np
import matplotlib as mpl
#mpl.use('Agg')
import matplotlib.pyplot as plt
from astropy import wcs
from astropy.wcs import WCS
from astropy.io import fits
import sys
import math
import os
import glob
import sys
from sortedcontainers import SortedDict
import datetime as dt
import imageio
import os
from PIL import Image
from matplotlib.colors import LogNorm
from astropy.nddata.utils import Cutout2D
from astropy.table import Table, Column, join 
from astropy import units as u
import datetime as dt 
import glob

path = '/mnt/dwf/archive_NOAO_data/data/2017/02/Antlia/g_band/single/'
path2 = '/mnt/dwf/archive_NOAO_data/data/2017/02/Prime/g_band/stacked/'

paths = [path, path2]

seeing_table = Table()
	
image_field = []
image_year = []
image_seeing1 = []
image_seeing2 =[]
image_type = []
image_filename = []
	

for filename in os.listdir(path): 
	if filename.endswith('.fits'): 
		print(filename)
		hdulist = fits.open(path + '/'+ filename)
		head = hdulist[0].header
		field = head['OBJECT']
		date = dt.datetime.strptime(head['DATE-OBS'], '%Y-%m-%dT%H:%M:%S.%f')
		year = date.strftime('%Y')
		month = date.strftime('%m')
		
		try: 
			dimmsee = float(head['DIMMSEE'])
		except: 
			pass
		try: 
			dimm2see = float(head['DIMM2SEE'])
		except: 
			pass
		imtype = head['PRODTYPE']
		
		image_field.append(field)
		
		image_year.append(year)
		try: 
			image_seeing1.append(dimmsee)
		except: 
			pass
		try: 
			image_seeing2.append(dimm2see)
		except: 
			pass
		image_type.append(imtype)
		image_filename.append(str(os.path.splitext(filename)[0]))
	
seeing_table['field'] = image_field 
seeing_table['file'] = image_filename
seeing_table['year'] = image_year
seeing_table['dimmsee'] = image_seeing1
try: 
	seeing_table['dimm2see'] = image_seeing2
except: 
	pass
seeing_table['type'] = image_type  
print(seeing_table)
print(np.average(seeing_table['dimmsee']))
output = '/mnt/dwf/archive_NOAO_data/scripts/seeing_scripts/seeing_conditions/' + field + '_seeing_results.ascii' 
seeing_table.write(output, format='ascii', overwrite = 'True')
		
		
		
