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

# ifu_short = pyfits.open(path+'jwst_miri_mirifushort_qe.fits')
# f1065c, f1140c  not an `official' filters

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

f1130w_filter = fits.open(path+'jwst_miri_f1130w_filter.fits')
f1130w_data   = f1130w_filter[1].data
f1130w_wave   = f1130w_data['WAVELENGTH'] 
f1130w_trans  = f1130w_data['TRANSMISSION'] 

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
##      W I S E    filter curves (for comparison)
##
path = 'filter_curves/WISE/'
infile = 'RSR-W1.txt'
table = path+infile
W1_band      = ascii.read(table)
W1_band_wave = W1_band['W1']
W1_band_thru = W1_band['RSR']
infile = 'RSR-W2.txt'
table = path+infile
W2_band      = ascii.read(table)
W2_band_wave = W2_band['W2']
W2_band_thru = W2_band['RSR']
infile = 'RSR-W3.txt'
table = path+infile
W3_band      = ascii.read(table)
W3_band_wave = W3_band['W3']
W3_band_thru = W3_band['RSR']
infile = 'RSR-W4.txt'
table = path+infile
W4_band      = ascii.read(table)
W4_band_wave = W4_band['W4']
W4_band_thru = W4_band['RSR']


##
##  Q S O    ``Composite''   spectra
##
path  = '../../ETC_calc/'
file  = 'Glikman_2006_ApJ_Table7.dat' 
table = path+file
quasar_sed = ascii.read(table)

## Emission Line list
linelist_file = 'emission_lines.dat'
linelist = ascii.read(linelist_file)



##  R E D S H I F T  !!!!
redshift = 7.00
#redshift = float(input("What redshift are we at??   "))

##   S e t t i n g     u p   t h e      p l o t 
fig, ax = plt.subplots(figsize=(22.0, 8.0), dpi=80, facecolor='w', edgecolor='k')

## Adjusting the Whitespace for the plots
left   = 0.12   # the left side of the subplots of the figure
right  = 0.98   # the right side of the subplots of the figure
bottom = 0.18   # the bottom of the subplots of the figure
top    = 0.96   # the top of the subplots of the figure
wspace = 0.26   # the amount of width reserved for blank space between subplots
hspace = 0.06   # the amount of height reserved for white space between subplots
plt.subplots_adjust(left=left, bottom=bottom, right=right, top=top, wspace=wspace, hspace=hspace)

## Some NPR plotting defaults
ls = 'solid'
lw = 1.0
alpha           = 1.0
fontsize        = 28
linewidth       = 2.4
labelsize       = 28
tickwidth       = 2.0
ticklabelsize   = labelsize
majorticklength = 18
minorticklength = 9

plt.style.use('seaborn-poster')
cmap = plt.get_cmap('viridis')


## Setting the axes range
xmin, xmax = 4.85, 35.                   #3.85, 30 for W2, W3 and W4
ax.set_xscale("log", nonposx='clip')
ymin, ymax = 0.00, 1.25    


##
## MIRI Imaging filters
##
ax.plot( f560w_wave, ( f560w_trans/f560w_trans.max()),    color='darkviolet',      alpha=alpha, linewidth=linewidth)
ax.fill( f560w_wave, ( f560w_trans/f560w_trans.max()),    color='darkviolet',      alpha=alpha/2)
ax.plot( f770w_wave, ( f770w_trans/f770w_trans.max()),    color='mediumslateblue', alpha=alpha, linewidth=linewidth)
ax.fill( f770w_wave, ( f770w_trans/f770w_trans.max()),    color='mediumslateblue', alpha=alpha/2)
ax.plot(f1000w_wave, (f1000w_trans/f1000w_trans.max()),   color='cornflowerblue',  alpha=alpha, linewidth=linewidth)
ax.fill(f1000w_wave, (f1000w_trans/f1000w_trans.max()),   color='cornflowerblue',  alpha=alpha/2)
ax.plot(f1130w_wave, (f1130w_trans/f1130w_trans.max()),   color='steelblue',       alpha=alpha, linewidth=linewidth)
ax.fill(f1130w_wave, (f1130w_trans/f1130w_trans.max()),   color='steelblue',       alpha=alpha/2)
ax.plot(f1280w_wave, (f1280w_trans/f1280w_trans.max()),   color='lightseagreen',   alpha=alpha, linewidth=linewidth)
ax.fill(f1280w_wave, (f1280w_trans/f1280w_trans.max()),   color='lightseagreen',   alpha=alpha/2)
ax.plot(f1500w_wave, (f1500w_trans/f1500w_trans.max()),   color='darkseagreen',    alpha=alpha, linewidth=linewidth)
ax.fill(f1500w_wave, (f1500w_trans/f1500w_trans.max()),   color='darkseagreen',    alpha=alpha/2)
ax.plot(f1800w_wave, (f1800w_trans/f1800w_trans.max()),   color='darkkhaki',       alpha=alpha, linewidth=linewidth)
ax.fill(f1800w_wave, (f1800w_trans/f1800w_trans.max()),   color='darkkhaki',       alpha=alpha/2)
ax.plot(f2100w_wave, (f2100w_trans/f2100w_trans.max()),   color='peru',            alpha=alpha, linewidth=linewidth)
ax.fill(f2100w_wave, (f2100w_trans/f2100w_trans.max()),   color='peru',            alpha=alpha/2)
ax.plot(f2550w_wave, (f2550w_trans/f2550w_trans.max()),   color='red',             alpha=alpha, linewidth=linewidth)
ax.fill(f2550w_wave, (f2550w_trans/f2550w_trans.max()),   color='red',             alpha=alpha/2)

##
## MIRI Imaging filter  L A B E L
##
filterLabels = 'y'
if filterLabels == 'y':
    xlab_off = 0.96
    y_labelplacement = 1.10
    labelratio = 1.3
    plt.text( 5.20, y_labelplacement, r'F560W',  color ='darkviolet',       fontsize=fontsize/labelratio, weight='bold')
    plt.text( 7.00, y_labelplacement, r'F770W',  color ='mediumslateblue',  fontsize=fontsize/labelratio, weight='bold')
    plt.text( 9.10, y_labelplacement, r'F1000W', color ='cornflowerblue',   fontsize=fontsize/labelratio, weight='bold')
    plt.text(10.45, y_labelplacement-.08, r'F1130W', color ='steelblue',     fontsize=fontsize/labelratio, weight='bold')
    plt.text(11.70, y_labelplacement, r'F1280W', color ='lightseagreen',    fontsize=fontsize/labelratio, weight='bold')
    plt.text(13.85, y_labelplacement, r'F1500W', color ='darkseagreen',     fontsize=fontsize/labelratio, weight='bold')
    plt.text(16.60, y_labelplacement, r'F1800W', color ='darkkhaki',        fontsize=fontsize/labelratio, weight='bold')
    plt.text(19.50, y_labelplacement, r'F2100W', color ='peru',             fontsize=fontsize/labelratio, weight='bold')
    plt.text(24.50, y_labelplacement, r'F2550W', color ='red',              fontsize=fontsize/labelratio, weight='bold')


    
##
## WISE IMAGING FILTERS
##
plot_WISEfilters = 'n'
extra_factor = 4.
alpha = 1.00
alpha_factor = 1/4.
if plot_WISEfilters  == 'y':
    WISE_xlabel = 0.195
    ax.plot( (W1_band_wave),  (W1_band_thru/(W1_band_thru.max()*extra_factor)), color='peru',      alpha=alpha, linewidth=linewidth)
    ax.fill( (W1_band_wave),  (W1_band_thru/(W1_band_thru.max()*extra_factor)), color='k',         alpha=alpha_factor)
    ax.plot( (W2_band_wave),  (W2_band_thru/(W2_band_thru.max()*extra_factor)), color='orangered', alpha=alpha, linewidth=linewidth)
    ax.fill( (W2_band_wave),  (W2_band_thru/(W2_band_thru.max()*extra_factor)), color='k',         alpha=alpha_factor)
    ax.plot( (W3_band_wave),  (W3_band_thru/(W3_band_thru.max()*extra_factor)), color='red',       alpha=alpha, linewidth=linewidth)
    ax.fill( (W3_band_wave),  (W3_band_thru/(W3_band_thru.max()*extra_factor)), color='k',         alpha=alpha_factor)
    ax.plot( (W4_band_wave),  (W4_band_thru/(W4_band_thru.max()*extra_factor)), color='darkred',   alpha=alpha, linewidth=linewidth)
    ax.fill( (W4_band_wave),  (W4_band_thru/(W4_band_thru.max()*extra_factor)), color='k',         alpha=alpha_factor)
    
    #plt.text( 3.280, WISE_xlabel, r'W1', color ='peru',      fontsize=fontsize, weight='bold')
    plt.text( 4.350, WISE_xlabel, r'W2', color ='orangered', fontsize=fontsize, weight='bold')
    plt.text(10.820, WISE_xlabel, r'W3', color ='red',       fontsize=fontsize, weight='bold')
    plt.text(20.380, WISE_xlabel, r'W4', color ='darkred',   fontsize=fontsize, weight='bold')


    
##
##  P l o t t i n g    Q S O    composites
##
#plt.plot((VdB01_wave              *(1.+redshift)), (VdB01_flux/VdB01_flux.max()),                 color='k', linestyle='-')
quasar_flux_damper = 2.3
#plt.plot((quasar_sed['wavelength']*(1.+redshift)), (quasar_sed['flux']/(quasar_sed['flux'].max()*quasar_flux_damper)), color='k')
    
## Putting in the emission lines..
for ll in range(len(linelist)):
    label = linelist['LineName'][ll]
    ## Need to convert from Ang to um; and then redshift...
    xylabel = (   ((linelist['Wavelength'][ll]/1e4)*(1.+redshift)), .30)
#    ax.axvline(x= ((linelist['Wavelength'][ll]/1e4)*(1.+redshift)),    color='gray', linestyle='--', linewidth=linewidth/3.4)
#    ax.annotate(label, xy=xylabel, ha='center', va='center', rotation=90, fontsize=fontsize/1.6 )
    print(ll, xylabel, label)


ax.set_xlim((xmin, xmax))
ax.set_ylim((ymin, ymax))
ax.tick_params('x', which='major', top='on',   labelsize=labelsize,  length=majorticklength, width=tickwidth)
ax.tick_params('x', which='minor', top='on',   labelsize=labelsize,  length=majorticklength, width=tickwidth)
ax.tick_params('y', which='major', right='on', labelsize=labelsize,  length=majorticklength, width=tickwidth)
ax.tick_params('y', which='minor', right='on', labelsize=labelsize,  length=majorticklength, width=tickwidth)


## Formatting axes ticks
from matplotlib.ticker import ScalarFormatter
for axis in [ax.xaxis, ax.yaxis]:
    axis.set_major_formatter(ScalarFormatter())
    axis.set_minor_formatter(ScalarFormatter())

    
plt.xlabel(r'Wavelength [$\mu$m]',                      fontsize=fontsize)
#plt.ylabel('Photon-to-electron\nconversion efficiency', fontsize=fontsize)
plt.ylabel('Transmission (normalized)',                fontsize=fontsize)
#ax.xaxis.label.set_size(32)
#ax.xtick.label.set_size(32)

#plt.show()
plt.savefig('MIRI_Imaging_vs_QSO_temp.png', format='png')
plt.close(fig)

