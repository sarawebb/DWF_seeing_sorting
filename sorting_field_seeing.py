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

path = '/mnt/dwf/archive_NOAO_data/scripts/seeing_scripts/seeing_conditions/'

for filename in os.listdir(path):
	if filename.endswith('.csv'): 
		field, file_name, year, dimmsee, dimm2see, magzpt, exp_sec, image_type = np.loadtxt(path + filename, unpack=True)
		print(field)
		
	
	
