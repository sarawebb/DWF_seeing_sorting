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

path = '/mnt/dwf/archive_NOAO_data/data/2018/06/8hr/colors'
path2 = '/mnt/dwf/archive_NOAO_data/data/2018/06/8hr/colors/stacked'

p1 = '/mnt/dwf/archive_NOAO_data/data/2015/02/9hr_field/colors'
p2 = '/mnt/dwf/archive_NOAO_data/data/2015/02/9hr_field/colors/stacked'
p3 = '/mnt/dwf/archive_NOAO_data/data/2015/02/FRB131104/colors'
p4 = '/mnt/dwf/archive_NOAO_data/data/2015/02/FRB131104/colors/stacked'
p5 = '/mnt/dwf/archive_NOAO_data/data/2015/02/FRB150215/colors'
p6 = '/mnt/dwf/archive_NOAO_data/data/2015/02/FRB150215/colors/stacked'
p7 = '/mnt/dwf/archive_NOAO_data/data/2015/02/Prime_field/colors'
p8 = '/mnt/dwf/archive_NOAO_data/data/2015/02/Prime_field/colors/stacked'
p9 = '/mnt/dwf/archive_NOAO_data/data/2015/03/3hr_field/colors'
p10 = '/mnt/dwf/archive_NOAO_data/data/2015/03/3hr_field/colors/stacked'
p11 = '/mnt/dwf/archive_NOAO_data/data/2015/03/9hr_field/colors'
p12 = '/mnt/dwf/archive_NOAO_data/data/2015/03/9hr_field/colors/stacked'
p13 = '/mnt/dwf/archive_NOAO_data/data/2015/03/FRB090625/colors'
p14 = '/mnt/dwf/archive_NOAO_data/data/2015/03/FRB090625/colors/stacked'
p15 = '/mnt/dwf/archive_NOAO_data/data/2015/03/FRB150215/colors'
p16 = '/mnt/dwf/archive_NOAO_data/data/2015/03/Prime_field/colors'
p17 = '/mnt/dwf/archive_NOAO_data/data/2015/03/Prime_field/colors/stacked'
p18 = '/mnt/dwf/archive_NOAO_data/data/2015/03/4hr_field/colors' 
p19 = '/mnt/dwf/archive_NOAO_data/data/2015/03/4hr_field/colors/stacked'
p20 = '/mnt/dwf/archive_NOAO_data/data/2015/03/FRB010724/colors'
p21 = '/mnt/dwf/archive_NOAO_data/data/2015/03/FRB010724/colors/stacked'
p22 = '/mnt/dwf/archive_NOAO_data/data/2015/03/FRB131104/colors'
p23 = '/mnt/dwf/archive_NOAO_data/data/2015/03/FRB131104/colors/stacked'
p24 = '/mnt/dwf/archive_NOAO_data/data/2015/03/Prime_field/colors'
p25 = '/mnt/dwf/archive_NOAO_data/data/2015/03/Prime_field/colors/stacked'
p26 = '/mnt/dwf/archive_NOAO_data/data/2015/12/3hr/colors'
p27 = '/mnt/dwf/archive_NOAO_data/data/2015/12/3hr/colors/stacked'
p29 = '/mnt/dwf/archive_NOAO_data/data/2015/12/FRB151230/colors'
p30 = '/mnt/dwf/archive_NOAO_data/data/2015/12/FRB151230/colors/stacked'
p31 = '/mnt/dwf/archive_NOAO_data/data/2015/12/4hr/colors'
p32 = '/mnt/dwf/archive_NOAO_data/data/2015/12/4hr/colors/stacked'
p33 = '/mnt/dwf/archive_NOAO_data/data/2015/12/FRB010724/colors'
p34 = '/mnt/dwf/archive_NOAO_data/data/2015/12/FRB010724/colors/stacked'
p35 = '/mnt/dwf/archive_NOAO_data/data/2015/12/Prime/colors'
p36 = '/mnt/dwf/archive_NOAO_data/data/2015/12/Prime/colors/stacked'
p37 = '/mnt/dwf/archive_NOAO_data/data/2016/07/ngc6744/colors'
p38 = '/mnt/dwf/archive_NOAO_data/data/2016/07/ngc6744/colors/stacked'
p39 = '/mnt/dwf/archive_NOAO_data/data/2016/07/NSF2/colors'
p40 = '/mnt/dwf/archive_NOAO_data/data/2016/07/NSF2/colors/stacked'
p41 = '/mnt/dwf/archive_NOAO_data/data/2016/07/dusty12/colors'
p42 = '/mnt/dwf/archive_NOAO_data/data/2016/07/dusty12/colors/stacked'
p43 = '/mnt/dwf/archive_NOAO_data/data/2016/08/ngc6101/colors'
p44 = '/mnt/dwf/archive_NOAO_data/data/2016/08/ngc6744/colors'
p45 = '/mnt/dwf/archive_NOAO_data/data/2017/02/4hr/colors'
p46 = '/mnt/dwf/archive_NOAO_data/data/2017/02/4hr/colors/stacked'
p47 = '/mnt/dwf/archive_NOAO_data/data/2017/02/A3558/colors'
p48 = '/mnt/dwf/archive_NOAO_data/data/2017/02/A3558/colors/stacked'
p49 = '/mnt/dwf/archive_NOAO_data/data/2017/02/Abell3558/colors'
p50 = '/mnt/dwf/archive_NOAO_data/data/2017/02/Abell3558/colors/stacked'
p51 = '/mnt/dwf/archive_NOAO_data/data/2017/02/Antlia/colors'
p52 = '/mnt/dwf/archive_NOAO_data/data/2017/02/Antlia/colors/stacked'
p53 = '/mnt/dwf/archive_NOAO_data/data/2017/02/FRB131104/colors'
p54 = '/mnt/dwf/archive_NOAO_data/data/2017/02/FRB131104/colors/stacked'
p55 = '/mnt/dwf/archive_NOAO_data/data/2017/02/Prime/colors'
p56 = '/mnt/dwf/archive_NOAO_data/data/2017/02/Prime/colors/stacked'
p57 = '/mnt/dwf/archive_NOAO_data/data/2018/06/8hr/colors'
p58 = '/mnt/dwf/archive_NOAO_data/data/2018/06/8hr/colors/stacked'
p59 = '/mnt/dwf/archive_NOAO_data/data/2018/06/Antlia/colors'
p60 = '/mnt/dwf/archive_NOAO_data/data/2018/06/Antlia/colors/stacked'
p61 = '/mnt/dwf/archive_NOAO_data/data/2018/06/Centaurus/colors'
p62 = '/mnt/dwf/archive_NOAO_data/data/2018/06/Centaurus/colors/stacked'
p63 = '/mnt/dwf/archive_NOAO_data/data/2018/06/Dusty10/colors'
p64 = '/mnt/dwf/archive_NOAO_data/data/2018/06/Dusty10/colors/stacked'
p65 = '/mnt/dwf/archive_NOAO_data/data/2018/06/Dusty11/colors'
p66 = '/mnt/dwf/archive_NOAO_data/data/2018/06/Dusty11/colors/stacked'
p67 = '/mnt/dwf/archive_NOAO_data/data/2015/02/9hr_field/colors'
p68 = '/mnt/dwf/archive_NOAO_data/data/2015/02/9hr_field/colors/stacked'
p69 = '/mnt/dwf/archive_NOAO_data/data/2015/02/FRB131104/colors'
p70 = '/mnt/dwf/archive_NOAO_data/data/2015/02/FRB131104/colors/stacked'
p71 = '/mnt/dwf/archive_NOAO_data/data/2015/02/FRB150215/colors'
p72 = '/mnt/dwf/archive_NOAO_data/data/2015/02/FRB150215/colors/stacked'
p73 = '/mnt/dwf/archive_NOAO_data/data/2015/02/Prime_field/colors'
p74 = '/mnt/dwf/archive_NOAO_data/data/2015/02/Prime_field/colors/stacked'
p75 = '/mnt/dwf/archive_NOAO_data/data/2015/03/3hr_field/colors'
p76 = '/mnt/dwf/archive_NOAO_data/data/2015/03/3hr_field/colors/stacked'
p77 = '/mnt/dwf/archive_NOAO_data/data/2015/03/9hr_field/colors'
p78 = '/mnt/dwf/archive_NOAO_data/data/2015/03/9hr_field/colors/stacked'
p79 = '/mnt/dwf/archive_NOAO_data/data/2015/03/FRB090625/colors'
p80 = '/mnt/dwf/archive_NOAO_data/data/2015/03/FRB090625/colors/stacked'
p81 = '/mnt/dwf/archive_NOAO_data/data/2015/03/FRB150215/colors'
p82 = '/mnt/dwf/archive_NOAO_data/data/2015/03/FRB150215/colors/stacked'
p83 = '/mnt/dwf/archive_NOAO_data/data/2015/12/3hr/colors'
p84 = '/mnt/dwf/archive_NOAO_data/data/2015/12/3hr/colors/stacked'
p85 = '/mnt/dwf/archive_NOAO_data/data/2016/07/ngc6744/colors'
p86 = '/mnt/dwf/archive_NOAO_data/data/2016/07/ngc6744/colors/stacked'

paths = [p1 ,p2 ,p3 ,p4 ,p5 ,p6 ,p7 ,p8 ,p9 ,p10 ,p11 ,p12 ,p13 ,p14 ,p15 ,p16 ,p17 ,p18 ,p19, p20 ,p21 ,p22 ,p23 ,p24 ,p25 ,p26 ,p27 ,p29 ,p30 ,p31 ,p32 ,p33 ,p34 ,p35 ,p36 ,p37 ,p38 ,p39 ,p40 ,p41 ,p42, p43 ,p44 ,p45 ,p46 ,p47 ,p48 ,p49 ,p50 ,p51 ,p52 ,p53 ,p54 ,p55 ,p56 ,p57 ,p58 ,p59 ,p60 ,p61 ,p62, p63, p64, p65 , p66, p67, p68, p69, p70, p71, p72, p73, p74, p75, p76, p77, p78, p79, p80, p81, p82, p83, p84, p85, p86 ]

#paths = [p13, p14, p15, p16, p17, p18, p19, p20, p21, p22, p23, p24, p25, p26, p27, p28, p29, p30]


for i in paths: 
	image_field_i = []
	image_year_i = []
	image_filter_i = []
	image_seeing1_i = []
	image_seeing2_i =[]
	image_type_i = []
	image_filename_i = []
	image_magzp_i = []
	image_exp_i = []

	image_field_r = []
	image_year_r = []
	image_filter_r = []
	image_seeing1_r = []
	image_seeing2_r =[]
	image_type_r = []
	image_filename_r = []
	image_magzp_r = []
	image_exp_r = []	
	
	
	
	
	for filename in os.listdir(i): 
		if filename.endswith('.fits'): 
			print(filename)
			
	
			
			hdulist = fits.open(i + '/'+ filename)
			head = hdulist[0].header
			field = head['OBJECT']
			date = dt.datetime.strptime(head['DATE-OBS'], '%Y-%m-%dT%H:%M:%S.%f')
			year = date.strftime('%Y')
			month = date.strftime('%m')
			
			imfilter = head['FILTER'] 
			imtype = head['PRODTYPE']
			
			
			if imfilter == 'r':
				try: 
					dimmsee_r = float(head['DIMMSEE'])
				except:
					pass
				
				try:
					dimm2see_r = float(head['DIMM2SEE'])
				except: 
					pass
		
				imtype_r = head['PRODTYPE']
				imfilter_r = head['FILTER']
				image_field_r.append(field)
			
				try:
					image_magzp_r.append(head['MAGZPT'])
				except: 
					pass 
				
				image_exp_r.append(head['EXPTIME'])
				image_year_r.append(year_r)
				image_filter_r.append(imfilter_r)
				
				try:
					image_seeing1_r.append(dimmsee_r)
				except:
					pass
				try: 
					image_seeing2_r.append(dimm2see_r)
				except:
					pass
				image_type_r.append(imtype_r)
				image_filename_r.append(str(os.path.splitext(filename)[0]))
			
			if imfilter == 'i':
				try: 
					dimmsee_i = float(head['DIMMSEE'])
				except:
					pass
				
				try:
					dimm2see_i = float(head['DIMM2SEE'])
				except: 
					pass
		
				imtype_i = head['PRODTYPE']
				imfilter_i = head['FILTER']
				image_field_i.append(field)
			
				try:
					image_magzp_i.append(head['MAGZPT'])
				except: 
					pass 
				
				image_exp_i.append(head['EXPTIME'])
				image_year_i.append(year_i)
				image_filter_i.append(imfilter_i)
				
				try:
					image_seeing1_i.append(dimmsee_i)
				except:
					pass
				try: 
					image_seeing2_i.append(dimm2see_i)
				except:
					pass
				image_type_i.append(imtype_i)
				image_filename_i.append(str(os.path.splitext(filename)[0]))
			
			
	seeing_table_r = Table()	
	seeing_table_r['field'] = image_field_r 
	seeing_table_r['file'] = image_filename_r
	seeing_table_r['year'] = image_year_r
	try:
		seeing_table_r['dimmsee (arcsec)'] = image_seeing1_r
	except: 
		pass
	try:
		seeing_table_r['dimm2see (arcsec)'] = image_seeing2_r
	except: 
		pass
	
	try: 
		seeing_table_r['magzpt'] = image_magzp_r
	except: 
		pass 
	seeing_table_r['exp (S)'] = image_exp_r
	seeing_table_r['type'] = image_type_r
	print(seeing_table_r)
	output = '/mnt/dwf/archive_NOAO_data/scripts/seeing_scripts/seeing_conditions/' + field + '_'+ str(date) + '_r_' + imtype + '_seeing_results.ascii' 
	seeing_table_r.write(output, format='ascii', overwrite = 'True')
	
	seeing_table_i = Table()			
	seeing_table_i['field'] = image_field_i 
	seeing_table_i['file'] = image_filename_i
	seeing_table_i['year'] = image_year_i
	try:
		seeing_table_i['dimmsee (arcsec)'] = image_seeing1_i
	except: 
		pass
	try:
		seeing_table_i['dimm2see (arcsec)'] = image_seeing2_i
	except: 
		pass
	
	try: 
		seeing_table_i['magzpt'] = image_magzp_i
	except: 
		pass 
	seeing_table_i['exp (S)'] = image_exp_i
	seeing_table_i['type'] = image_type_i
	print(seeing_table_i)
	output = '/mnt/dwf/archive_NOAO_data/scripts/seeing_scripts/seeing_conditions/' + field + '_'+ str(date) + '_i_' + imtype + '_seeing_results.ascii' 
	seeing_table_i.write(output, format='ascii', overwrite = 'True')
				
		
