'''

Code for plotting quasar spectra and the MIRI MRS coverage 


URLs::
  https://www.aanda.org/articles/aa/abs/2016/01/aa27096-15/aa27096-15.html
  https://github.com/jselsing/QuasarComposite
'''

import math
import numpy as np
import matplotlib.pyplot as plt

from pylab import * 
from matplotlib.ticker import ScalarFormatter 
from astropy.io import ascii
from astropy.io import fits
#import pyfits 
from matplotlib import colors as mcolors

##
## The MIRI Filters
##
## Not sure where I originally got these from;
## quite likely P. Klaassen or A. Glasse
path = 'filter_curves/MIRI/'


#ifu_short = pyfits.open(path+'jwst_miri_mirifushort_qe.fits')


# jwst_miri_f560w_filter.fits
f560w_filter = fits.open(path+'jwst_miri_f560w_filter.fits')
f560w_data   = f560w_filter[1].data
f560w_wave   = f560w_data['WAVELENGTH'] 
f560w_trans  = f560w_data['TRANSMISSION'] 

f770w_filter = fits.open(path+'jwst_miri_f770w_filter.fits')
f770w_data   = f770w_filter[1].data
f770w_wave   = f770w_data['WAVELENGTH'] 
f770w_trans  = f770w_data['TRANSMISSION'] 

f1000w_filter = fits.open(path+'jwst_miri_f1000w_filter.fits')
f1000w_data   = f1000w_filter[1].data
f1000w_wave   = f1000w_data['WAVELENGTH'] 
f1000w_trans  = f1000w_data['TRANSMISSION'] 

# Not an official filter...
# f1065c_filter = fits.open(path+'jwst_miri_f1065c_filter.fits')

f1130w_filter = fits.open(path+'jwst_miri_f1130w_filter.fits')
f1130w_data   = f1130w_filter[1].data
f1130w_wave   = f1130w_data['WAVELENGTH'] 
f1130w_trans  = f1130w_data['TRANSMISSION'] 

# Not an official filter...
# f1140c_filter = fits.open(path+'jwst_miri_f1140c_filter.fits')

f1280w_filter = fits.open(path+'jwst_miri_f1280w_filter.fits')
f1280w_data   = f1280w_filter[1].data
f1280w_wave   = f1280w_data['WAVELENGTH'] 
f1280w_trans  = f1280w_data['TRANSMISSION'] 

f1500w_filter = fits.open(path+'jwst_miri_f1500w_filter.fits')
f1500w_data   = f1500w_filter[1].data
f1500w_wave   = f1500w_data['WAVELENGTH'] 
f1500w_trans  = f1500w_data['TRANSMISSION'] 

f1800w_filter = fits.open(path+'jwst_miri_f1800w_filter.fits')
f1800w_data   = f1800w_filter[1].data
f1800w_wave   = f1800w_data['WAVELENGTH'] 
f1800w_trans  = f1800w_data['TRANSMISSION'] 

f2100w_filter = fits.open(path+'jwst_miri_f2100w_filter.fits')
f2100w_data   = f2100w_filter[1].data
f2100w_wave   = f2100w_data['WAVELENGTH'] 
f2100w_trans  = f2100w_data['TRANSMISSION']

f2550w_filter = fits.open(path+'jwst_miri_f2550w_filter.fits')
f2550w_data   = f2550w_filter[1].data
f2550w_wave   = f2550w_data['WAVELENGTH'] 
f2550w_trans  = f2550w_data['TRANSMISSION']







##
##  Q S O    ``Composite''   spectra
##
path  = '../../ETC_calc/'
file  = 'quasar_SED_WavelenInmu_blue.dat'
table = path+file
quasar_sed = ascii.read(table)

## Vanden Berk et al. 2001
path = '/cos_pc19a_npr/data/SDSS/VdB01/'
file = 'Vanden_Berk_2001_Table1.dat'
table = path+file
VdB01_comp = ascii.read(table)

## Glikman et al. 2006. 
## TABLE 3:
##   Composite Quasar Spectrum, Arithmetic and Geometric Mean
path = '/cos_pc19a_npr/data/Glikman2006/'
file = 'Glikman_2006_ApJ_Table3.dat'
table = path+file
Glikman_tab3 = ascii.read(table)
## TABLE 7:
##   Optical-to-Near-Infrared Composite Quasar Spectrum, Arithmetic and Geometric Means
path = '/cos_pc19a_npr/data/Glikman2006/'
file = 'Glikman_2006_ApJ_Table7.dat'
table = path+file
Glikman_tab7 = ascii.read(table)

## IR templates at::
## /cos_pc19a_npr/BOSS/WISE/templates
## http://www.iasf-milano.inaf.it/~polletta/templates/swire_templates.html
path = '/cos_pc19a_npr/BOSS/WISE/templates/Polletta_templates/'
file_qso1 = 'QSO1_template_norm.sed'
file_qso2 = 'QSO2_template_norm.sed'
file_sey2 = 'Sey2_template_norm.sed'
table_qso1 = path+file_qso1
table_qso2 = path+file_qso2
table_sey2 = path+file_sey2
QSO1_template = ascii.read(table_qso1)
QSO2_template = ascii.read(table_qso2)
Sey2_template = ascii.read(table_sey2)



'''
Characterizing quasars in the mid-infrared: high signal-to-noise ratio
spectral templates
Allison R. Hill  S. C. Gallagher  R. P. Deo  E. Peeters  Gordon T. Richards
2014, MNRAS, 438, 2317
https://doi.org/10.1093/mnras/stt2346

 Table 2 of Allison R. Hill et al (2013)
 Entries which contain a '-1' indicate no wavelength coverage for that template.
col 1: wavelength [micron]
col 2: total template (spectral average of all objects) in units of L_{nu}
col 3,4,5: the most luminous, intermediate luminosity and least luminous template (corresponding to values 1, 2 and 3 from col 10 of Table 1) in units if L_{nu}
'''

path = '/cos_pc19a_npr/data/Spitzer/Hill2014_IRS/'
Hill2014_data =  ascii.read(path+'table2.txt')
##data =  ascii.read('table2.txt')

IRS_wavelength = Hill2014_data['col1']
IRS_total      = Hill2014_data['col2']
IRS_most_lum   = Hill2014_data['col3']
IRS_medium_lum = Hill2014_data['col4']
IRS_least_lum  = Hill2014_data['col5']


## Setting up the composites up...
## wavelengths now into um
VdB01_wave = (VdB01_comp['Wavelength']/10000.)
VdB01_flux =  VdB01_comp['Flux']

Glik_wave = (Glikman_tab7['Wavelength']/10000.)
Glik_flux =  Glikman_tab7['Flux']

QSO1_wave = (QSO1_template['col1']/10000.)
QSO1_flux =  QSO1_template['col2']
QSO2_wave = (QSO2_template['col1']/10000.)
QSO2_flux =  QSO2_template['col2']
Sey2_wave = (Sey2_template['col1']/10000.)
Sey2_flux =  Sey2_template['col2']


##  R E D S H I F T  !!!!
redshift =  17.54
#redshift = 6.7
#redshift = float(input("What redshift are we at??   "))



## Some NPR plotting defaults 
alpha           = 1.0
fontsize        = 22
linewidth       = 2.4
labelsize       = 18
tickwidth       = 2.0
ticklabelsize   = labelsize
majorticklength = 12
minorticklength = 6


## Plotting things up...
plt.rcParams.update({'font.size': 24})
fig, ax = plt.subplots(figsize=(16.0, 8.0))

#print(plt.style.available)
plt.style.use('seaborn-poster')
## colormap
cmap=plt.get_cmap('viridis')


## Setting the limits.
## If log
xmin =   .400           ##  0.1um = 1e-7 = 100e-9 = 1000Ang
xmax = 60.              ## 30.0um
##
xmin = 4.4
xmax = 30.0
#ax.set_xscale("log", nonposx='clip')

ymin = -0.05  
ymax = 100.2    


##
## MIRI Imaging filters
##
ax.plot( f560w_wave, f560w_trans,    color='darkviolet',      alpha=alpha, linewidth=linewidth)
ax.fill( f560w_wave, f560w_trans,    color='darkviolet',      alpha=alpha/2)
ax.plot( f770w_wave, f770w_trans,    color='mediumslateblue', alpha=alpha, linewidth=linewidth)
ax.fill( f770w_wave, f770w_trans,    color='mediumslateblue', alpha=alpha/2)
ax.plot(f1000w_wave, f1000w_trans,   color='cornflowerblue',  alpha=alpha, linewidth=linewidth)
ax.fill(f1000w_wave, f1000w_trans,   color='cornflowerblue',  alpha=alpha/2)
ax.plot(f1130w_wave, f1130w_trans,   color='steelblue',       alpha=alpha, linewidth=linewidth)
ax.fill(f1130w_wave, f1130w_trans,   color='steelblue',       alpha=alpha/2)
ax.plot(f1280w_wave, f1280w_trans,   color='lightseagreen',   alpha=alpha, linewidth=linewidth)
ax.fill(f1280w_wave, f1280w_trans,   color='lightseagreen',   alpha=alpha/2)
ax.plot(f1500w_wave, f1500w_trans,   color='darkseagreen',    alpha=alpha, linewidth=linewidth)
ax.fill(f1500w_wave, f1500w_trans,   color='darkseagreen',    alpha=alpha/2)
ax.plot(f1800w_wave, f1800w_trans,   color='darkkhaki',       alpha=alpha, linewidth=linewidth)
ax.fill(f1800w_wave, f1800w_trans,   color='darkkhaki',       alpha=alpha/2)
ax.plot(f2100w_wave, f2100w_trans,   color='peru',            alpha=alpha, linewidth=linewidth)
ax.fill(f2100w_wave, f2100w_trans,   color='peru',            alpha=alpha/2)
ax.plot(f2550w_wave, f2550w_trans,   color='red',             alpha=alpha, linewidth=linewidth)
ax.fill(f2550w_wave, f2550w_trans,   color='red',             alpha=alpha/2)

f770w_wave


## Plotting the QSO composites
plt.plot((VdB01_wave*(1.+redshift)), (VdB01_flux/VdB01_flux.max()))
#plt.plot((VdB01_wave*(1.+redshift)), (VdB01_flux/VdB01_flux.max()))
#plt.plot((Glik_wave*(1.+redshift)), (Glik_flux/Glik_flux.max()))
plt.plot((Glik_wave*(1.+redshift)), (Glik_flux*Glik_flux.max()), color='k' )

#plt.plot((QSO1_wave*(1.+redshift)), (QSO1_flux/QSO1_flux.max()))
#plt.plot((QSO2_wave*(1.+redshift)), (QSO2_flux/QSO2_flux.max()))
#plt.plot((Sey2_wave*(1.+redshift)), (Sey2_flux/Sey2_flux.max()))

## Hill et al. 2014 IRS spectra
#plt.plot((IRS_wavelength*(1.+redshift)), ((IRS_least_lum/IRS_least_lum.max())*2.6), linestyle='solid', linewidth=4)
#plt.plot((IRS_wavelength*(1.+redshift)), ((IRS_medium_lum/IRS_medium_lum.max())*2.2), linestyle='dotted', linewidth=4)
#plt.plot((IRS_wavelength*(1.+redshift)), ((IRS_most_lum/IRS_most_lum.max())*1.25), linestyle='dashed', linewidth=4)

#ax.text((xmin+(xmin/10.)), (0.90*ymax), '$z=5.0$', fontsize=26)

#plt.legend([
#             'Vanden Berk (2001)',
 #        'Glikman et al. (2006)', 
  #          'Polletta QSO1',
   #         'Polletta QSO2',
    #        'Polletta Sey2' 
     #       ],
#           loc="lower left", ncol=3, shadow=True, fancybox=True,
      #     loc="upper right", ncol=1, shadow=True, fancybox=True,
       #   fontsize=22, frameon=True)

       
ls = 'solid'
lw = 1.0
ax.set_xlim((xmin, xmax))
ax.set_ylim((ymin, ymax))
ax.tick_params('x',which='major', top='on', direction='in', length=12, width=2)
ax.tick_params('x',which='minor', top='on', direction='in', length=6, width=2)
#ax.tick_params('y', direction='in')
ax.tick_params('y', which='major',right='on', direction='in', length=12, width=2)
ax.tick_params('y',which='minor', right='on', direction='in', length=6, width=2)

##ax.ticklabel_format(style='plain', axis='x')

## https://matplotlib.org/gallery/ticks_and_spines/scalarformatter.html
## https://stackoverflow.com/questions/21920233/matplotlib-log-scale-tick-label-number-formatting
from matplotlib.ticker import ScalarFormatter
for axis in [ax.xaxis, ax.yaxis]:
    axis.set_major_formatter(ScalarFormatter())
    axis.set_minor_formatter(ScalarFormatter())

plt.xlabel(r'wavelength [$\mu$m]', fontsize=fontsize)
plt.ylabel('Relative flux',        fontsize=fontsize)
#ax.xaxis.label.set_size(32)
#ax.xtick.label.set_size(32)

plt.show()
