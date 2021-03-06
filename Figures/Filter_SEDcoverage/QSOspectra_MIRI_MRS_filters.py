'''

Code for plotting quasar spectra and the MIRI MRS coverage 

URLs::
  https://www.aanda.org/articles/aa/abs/2016/01/aa27096-15/aa27096-15.html
  https://github.com/jselsing/QuasarComposite
'''

import math
import numpy  as np
import pandas

import matplotlib.pyplot as plt
import matplotlib.colors as mcolors

from pylab      import * 
from astropy.io import ascii
from astropy.io import fits
from matplotlib.ticker import ScalarFormatter 


##
##  T h e     M I R I    M R S     Filters
##
## From:: 
##   http://ircamera.as.arizona.edu/MIRI/pces.htm
##   MRSPCE_TN-00072-ATC-Iss1
##
path = 'filter_curves/MIRI/'
## df         = pandas.read_csv(path+'MRSPCE_TN-00072-ATC-Iss1.csv')
## Ch1_short  = df[df.Band == 0]

## Setting up the channels 
Ch1_short  = fits.open(path+'MIRI_FM_MIRIFUSHORT_1SHORT_PCE_06.00.00.fits')
Ch1_medium = fits.open(path+'MIRI_FM_MIRIFUSHORT_1MEDIUM_PCE_06.00.00.fits')
Ch1_long   = fits.open(path+'MIRI_FM_MIRIFUSHORT_1LONG_PCE_06.00.00.fits')
Ch2_short  = fits.open(path+'MIRI_FM_MIRIFUSHORT_2SHORT_PCE_06.00.00.fits')
Ch2_medium = fits.open(path+'MIRI_FM_MIRIFUSHORT_2MEDIUM_PCE_06.00.00.fits')
Ch2_long   = fits.open(path+'MIRI_FM_MIRIFUSHORT_2LONG_PCE_06.00.00.fits')
Ch3_short  = fits.open(path+'MIRI_FM_MIRIFULONG_3SHORT_PCE_06.00.00.fits')
Ch3_medium = fits.open(path+'MIRI_FM_MIRIFULONG_3MEDIUM_PCE_06.00.00.fits')
Ch3_long   = fits.open(path+'MIRI_FM_MIRIFULONG_3LONG_PCE_06.00.00.fits')
Ch4_short  = fits.open(path+'MIRI_FM_MIRIFULONG_4SHORT_PCE_06.00.00.fits')
Ch4_medium = fits.open(path+'MIRI_FM_MIRIFULONG_4MEDIUM_PCE_06.00.00.fits')
Ch4_long   = fits.open(path+'MIRI_FM_MIRIFULONG_4LONG_PCE_06.00.00.fits')

Ch1_short_data        = Ch1_short[1].data
Ch1_short.wavelength  = Ch1_short_data['WAVELENGTH']
Ch1_short.efficiency  = Ch1_short_data['EFFICIENCY']
Ch1_medium_data       = Ch1_medium[1].data
Ch1_medium.wavelength = Ch1_medium_data['WAVELENGTH']
Ch1_medium.efficiency = Ch1_medium_data['EFFICIENCY']
Ch1_long_data         = Ch1_long[1].data
Ch1_long.wavelength   = Ch1_long_data['WAVELENGTH']
Ch1_long.efficiency   = Ch1_long_data['EFFICIENCY']

Ch2_short_data        = Ch2_short[1].data
Ch2_short.wavelength  = Ch2_short_data['WAVELENGTH']
Ch2_short.efficiency  = Ch2_short_data['EFFICIENCY']
Ch2_medium_data       = Ch2_medium[1].data
Ch2_medium.wavelength = Ch2_medium_data['WAVELENGTH']
Ch2_medium.efficiency = Ch2_medium_data['EFFICIENCY']
Ch2_long_data         = Ch2_long[1].data
Ch2_long.wavelength   = Ch2_long_data['WAVELENGTH']
Ch2_long.efficiency   = Ch2_long_data['EFFICIENCY']

Ch3_short_data        = Ch3_short[1].data
Ch3_short.wavelength  = Ch3_short_data['WAVELENGTH']
Ch3_short.efficiency  = Ch3_short_data['EFFICIENCY']
Ch3_medium_data       = Ch3_medium[1].data
Ch3_medium.wavelength = Ch3_medium_data['WAVELENGTH']
Ch3_medium.efficiency = Ch3_medium_data['EFFICIENCY']
Ch3_long_data         = Ch3_long[1].data
Ch3_long.wavelength   = Ch3_long_data['WAVELENGTH']
Ch3_long.efficiency   = Ch3_long_data['EFFICIENCY']

Ch4_short_data        = Ch4_short[1].data
Ch4_short.wavelength  = Ch4_short_data['WAVELENGTH']
Ch4_short.efficiency  = Ch4_short_data['EFFICIENCY']
Ch4_medium_data       = Ch4_medium[1].data
Ch4_medium.wavelength = Ch4_medium_data['WAVELENGTH']
Ch4_medium.efficiency = Ch4_medium_data['EFFICIENCY']
Ch4_long_data         = Ch4_long[1].data
Ch4_long.wavelength   = Ch4_long_data['WAVELENGTH']
Ch4_long.efficiency   = Ch4_long_data['EFFICIENCY']


## have to add zeros at the start/end of the arrays to see shaded-areas...
## Ch1
newArray    = np.append((Ch1_short.wavelength.min()-0.005), Ch1_short.wavelength)
newnewArray = np.append(newArray, (Ch1_short.wavelength.max()+0.005))
Ch1_short.wavelength = newnewArray
newArray    = np.append(0.0, Ch1_short.efficiency)
newnewArray = np.append(newArray, 0.0)
Ch1_short.efficiency = newnewArray
newArray    = np.append((Ch1_medium.wavelength.min()-0.005), Ch1_medium.wavelength)
newnewArray = np.append(newArray, (Ch1_medium.wavelength.max()+0.005))
Ch1_medium.wavelength = newnewArray
newArray    = np.append(0.0, Ch1_medium.efficiency)
newnewArray = np.append(newArray, 0.0)
Ch1_medium.efficiency = newnewArray
newArray    = np.append((Ch1_long.wavelength.min()-0.005), Ch1_long.wavelength)
newnewArray = np.append(newArray, (Ch1_long.wavelength.max()+0.005))
Ch1_long.wavelength = newnewArray
newArray    = np.append(0.0, Ch1_long.efficiency)
newnewArray = np.append(newArray, 0.0)
Ch1_long.efficiency = newnewArray
## Ch2
newArray    = np.append((Ch2_short.wavelength.min()-0.005), Ch2_short.wavelength)
newnewArray = np.append(newArray, (Ch2_short.wavelength.max()+0.005))
Ch2_short.wavelength = newnewArray
newArray    = np.append(0.0, Ch2_short.efficiency)
newnewArray = np.append(newArray, 0.0)
Ch2_short.efficiency = newnewArray
newArray    = np.append((Ch2_medium.wavelength.min()-0.005), Ch2_medium.wavelength)
newnewArray = np.append(newArray, (Ch2_medium.wavelength.max()+0.005))
Ch2_medium.wavelength = newnewArray
newArray    = np.append(0.0, Ch2_medium.efficiency)
newnewArray = np.append(newArray, 0.0)
Ch2_medium.efficiency = newnewArray
newArray    = np.append((Ch2_long.wavelength.min()-0.005), Ch2_long.wavelength)
newnewArray = np.append(newArray, (Ch2_long.wavelength.max()+0.005))
Ch2_long.wavelength = newnewArray
newArray    = np.append(0.0, Ch2_long.efficiency)
newnewArray = np.append(newArray, 0.0)
Ch2_long.efficiency = newnewArray
## Ch3
newArray    = np.append((Ch3_short.wavelength.min()-0.005), Ch3_short.wavelength)
newnewArray = np.append(newArray, (Ch3_short.wavelength.max()+0.005))
Ch3_short.wavelength = newnewArray
newArray    = np.append(0.0, Ch3_short.efficiency)
newnewArray = np.append(newArray, 0.0)
Ch3_short.efficiency = newnewArray
newArray    = np.append((Ch3_medium.wavelength.min()-0.005), Ch3_medium.wavelength)
newnewArray = np.append(newArray, (Ch3_medium.wavelength.max()+0.005))
Ch3_medium.wavelength = newnewArray
newArray    = np.append(0.0, Ch3_medium.efficiency)
newnewArray = np.append(newArray, 0.0)
Ch3_medium.efficiency = newnewArray
newArray    = np.append((Ch3_long.wavelength.min()-0.005), Ch3_long.wavelength)
newnewArray = np.append(newArray, (Ch3_long.wavelength.max()+0.005))
Ch3_long.wavelength = newnewArray
newArray    = np.append(0.0, Ch3_long.efficiency)
newnewArray = np.append(newArray, 0.0)
Ch3_long.efficiency = newnewArray
## Ch4
newArray    = np.append((Ch4_short.wavelength.min()-0.005), Ch4_short.wavelength)
newnewArray = np.append(newArray, (Ch4_short.wavelength.max()+0.005))
Ch4_short.wavelength = newnewArray
newArray    = np.append(0.0, Ch4_short.efficiency)
newnewArray = np.append(newArray, 0.0)
Ch4_short.efficiency = newnewArray
newArray    = np.append((Ch4_medium.wavelength.min()-0.005), Ch4_medium.wavelength)
newnewArray = np.append(newArray, (Ch4_medium.wavelength.max()+0.005))
Ch4_medium.wavelength = newnewArray
newArray    = np.append(0.0, Ch4_medium.efficiency)
newnewArray = np.append(newArray, 0.0)
Ch4_medium.efficiency = newnewArray
newArray    = np.append((Ch4_long.wavelength.min()-0.005), Ch4_long.wavelength)
newnewArray = np.append(newArray, (Ch4_long.wavelength.max()+0.005))
Ch4_long.wavelength = newnewArray
newArray    = np.append(0.0, Ch4_long.efficiency)
newnewArray = np.append(newArray, 0.0)
Ch4_long.efficiency = newnewArray



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
#file  = 'quasar_SED_WavelenInmu_blue.dat'
#file  = 'quasar_SED_WavelenInmu_v0pnt9.dat'
file  = 'Glikman_2006_ApJ_Table7.dat' 
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


## Emission Line list
linelist_file = 'emission_lines.dat'
linelist = ascii.read(linelist_file)


##  R E D S H I F T  !!!!
#redshift =  7.54
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


##
## Some NPR plotting defaults
##
alpha           = 1.0
fontsize        = 28
linewidth       = 2.4
labelsize       = 28
tickwidth       = 2.0
ticklabelsize   = labelsize
majorticklength = 18
minorticklength = 9

plt.style.use('seaborn-poster')
cmap=plt.get_cmap('viridis')


## Setting the limits.
## If log

xmin = 4.85 ## 4.85           ## .400 if log;  0.1um = 1e-7 = 100e-9 = 1000Ang
xmax = 30.           ## 60.  if log;  30.0um
ax.set_xscale("log", nonposx='clip')
ymin = 0.00  
ymax = 0.20   #0.35   


ch4_boost = 4.
##
##  Plottting the actual MIRI MRS filters and band-passes
##
ax.plot(Ch1_short.wavelength,  Ch1_short.efficiency,  color='darkviolet',       alpha=alpha, linewidth=linewidth)
ax.fill(Ch1_short.wavelength,  Ch1_short.efficiency,  color='darkviolet',       alpha=alpha/2)
ax.plot(Ch1_medium.wavelength, Ch1_medium.efficiency, color='mediumorchid',     alpha=alpha, linewidth=linewidth)
ax.fill(Ch1_medium.wavelength, Ch1_medium.efficiency, color='mediumorchid',     alpha=alpha/2)
ax.plot(Ch1_long.wavelength,   Ch1_long.efficiency,   color='mediumpurple',     alpha=alpha, linewidth=linewidth)
ax.fill(Ch1_long.wavelength,   Ch1_long.efficiency,   color='mediumpurple',     alpha=alpha/2)

ax.plot(Ch2_short.wavelength,  Ch2_short.efficiency,  color='mediumslateblue',  alpha=alpha, linewidth=linewidth)
ax.fill(Ch2_short.wavelength,  Ch2_short.efficiency,  color='mediumslateblue',  alpha=alpha/2)
ax.plot(Ch2_medium.wavelength, Ch2_medium.efficiency, color='cornflowerblue',   alpha=alpha, linewidth=linewidth)
ax.fill(Ch2_medium.wavelength, Ch2_medium.efficiency, color='cornflowerblue',   alpha=alpha/2)
ax.plot(Ch2_long.wavelength,   Ch2_long.efficiency,   color='dodgerblue',       alpha=alpha, linewidth=linewidth)
ax.fill(Ch2_long.wavelength,   Ch2_long.efficiency,   color='dodgerblue',       alpha=alpha/2)

ax.plot(Ch3_short.wavelength,  Ch3_short.efficiency,  color='mediumaquamarine', alpha=alpha, linewidth=linewidth)
ax.fill(Ch3_short.wavelength,  Ch3_short.efficiency,  color='mediumaquamarine', alpha=alpha/2)
ax.plot(Ch3_medium.wavelength, Ch3_medium.efficiency, color='mediumseagreen',   alpha=alpha, linewidth=linewidth)
ax.fill(Ch3_medium.wavelength, Ch3_medium.efficiency, color='mediumseagreen',   alpha=alpha/2)
ax.plot(Ch3_long.wavelength,   Ch3_long.efficiency,   color='lightseagreen',    alpha=alpha, linewidth=linewidth)
ax.fill(Ch3_long.wavelength,   Ch3_long.efficiency,   color='lightseagreen',    alpha=alpha/2)

ax.plot(Ch4_short.wavelength,  Ch4_short.efficiency*ch4_boost,  color='orange',           alpha=alpha, linewidth=linewidth)
ax.fill(Ch4_short.wavelength,  Ch4_short.efficiency*ch4_boost,  color='orange',           alpha=alpha/2)
ax.plot(Ch4_medium.wavelength, Ch4_medium.efficiency*ch4_boost, color='peru',             alpha=alpha, linewidth=linewidth)
ax.fill(Ch4_medium.wavelength, Ch4_medium.efficiency*ch4_boost, color='peru',             alpha=alpha/2)
ax.plot(Ch4_long.wavelength,   Ch4_long.efficiency*ch4_boost,   color='red',              alpha=alpha, linewidth=linewidth)
ax.fill(Ch4_long.wavelength,   Ch4_long.efficiency*ch4_boost,   color='red',              alpha=alpha/2)


MRSfilterLabels = 'y'
if MRSfilterLabels == 'y':
    xlab_off = 0.96
    y_labelplacement = 0.18   # 0.20 if ymax =0.35
    labelratio = 1.5
    plt.text( 5.35*xlab_off, y_labelplacement, r'CH1',    color ='darkviolet',       fontsize=fontsize/labelratio,     weight='bold')
    plt.text( 6.15*xlab_off, y_labelplacement, r'CH1',    color ='mediumorchid',     fontsize=fontsize/labelratio,     weight='bold')
    plt.text( 7.09*xlab_off, y_labelplacement, r'CH1',    color ='mediumpurple',     fontsize=fontsize/labelratio,     weight='bold')
    plt.text( 8.13*xlab_off, y_labelplacement, r'CH2',    color ='mediumslateblue',  fontsize=fontsize/labelratio,     weight='bold')
    plt.text( 9.40*xlab_off, y_labelplacement, r'CH2',    color ='cornflowerblue',   fontsize=fontsize/labelratio,     weight='bold')
    plt.text(10.85*xlab_off, y_labelplacement, r'CH2',    color ='dodgerblue',       fontsize=fontsize/labelratio,     weight='bold')
    plt.text(12.50*xlab_off, y_labelplacement, r'CH3',    color ='mediumaquamarine', fontsize=fontsize/labelratio,     weight='bold')
    plt.text(14.50*xlab_off, y_labelplacement, r'CH3',    color ='mediumseagreen',   fontsize=fontsize/labelratio,     weight='bold')
    plt.text(16.75*xlab_off, y_labelplacement, r'CH3',    color ='lightseagreen',    fontsize=fontsize/labelratio,     weight='bold')
    plt.text(19.29*xlab_off, y_labelplacement, r'CH4',    color ='orange',           fontsize=fontsize/labelratio,     weight='bold')
    plt.text(22.47*xlab_off, y_labelplacement, r'CH4',    color ='peru',             fontsize=fontsize/labelratio,     weight='bold')
    plt.text(26.20*xlab_off, y_labelplacement, r'CH4',    color ='red',              fontsize=fontsize/labelratio,     weight='bold')

    y_labelplacement = 0.17   # 0.18 if ymax =0.35
    plt.text( 5.35*xlab_off, y_labelplacement, r'SHORT',  color ='darkviolet',       fontsize=fontsize/labelratio,     weight='bold')
    plt.text( 6.15*xlab_off, y_labelplacement, r'MED', color ='mediumorchid',     fontsize=fontsize/labelratio,     weight='bold')
    plt.text( 7.09*xlab_off, y_labelplacement, r'LONG',   color ='mediumpurple',     fontsize=fontsize/labelratio,     weight='bold')
    plt.text( 8.13*xlab_off, y_labelplacement, r'SHORT',  color ='mediumslateblue',  fontsize=fontsize/labelratio,     weight='bold')
    plt.text( 9.40*xlab_off, y_labelplacement, r'MED', color ='cornflowerblue',   fontsize=fontsize/labelratio,     weight='bold')
    plt.text(10.85*xlab_off, y_labelplacement, r'LONG',   color ='dodgerblue',       fontsize=fontsize/labelratio,     weight='bold')
    plt.text(12.50*xlab_off, y_labelplacement, r'SHORT',  color ='mediumaquamarine', fontsize=fontsize/labelratio,     weight='bold')
    plt.text(14.50*xlab_off, y_labelplacement, r'MED', color ='mediumseagreen',   fontsize=fontsize/labelratio,     weight='bold')
    plt.text(16.75*xlab_off, y_labelplacement, r'LONG',   color ='lightseagreen',    fontsize=fontsize/labelratio,     weight='bold')
    
    plt.text(19.29*xlab_off, y_labelplacement, r'SHORT',  color ='orange',           fontsize=fontsize/labelratio,     weight='bold')
    plt.text(22.47*xlab_off, y_labelplacement, r'MED', color ='peru',             fontsize=fontsize/labelratio,     weight='bold')
    plt.text(26.20*xlab_off, y_labelplacement, r'LONG',   color ='red',              fontsize=fontsize/labelratio,     weight='bold')

    y_labelplacement = 0.16
    plt.text(19.29, y_labelplacement, r'x4',  color ='orange',           fontsize=fontsize/labelratio,     weight='bold')
    plt.text(22.47, y_labelplacement, r'x4',  color ='peru',             fontsize=fontsize/labelratio,     weight='bold')
    plt.text(26.20, y_labelplacement, r'x4',  color ='red',              fontsize=fontsize/labelratio,     weight='bold')

    
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
plot_quasar = 'n'
if plot_quasar == 'y':
    quasar_flux_damper = 2.3
    plt.plot((quasar_sed['wavelength']*(1.+redshift)), (quasar_sed['flux']/(quasar_sed['flux'].max()*quasar_flux_damper)), color='k')
    ## Label placement
    x_placement = 20.5      
    plt.text(x_placement, (ymax*0.72), r'$z$='+str(redshift)+' quasar', color='k',     weight='bold', size=fontsize)

plot_emissionlines = 'n'
## Putting in the emission lines..
if plot_emissionlines == 'y':
    for ll in range(len(linelist)):
        label = linelist['LineName'][ll]
        ## Need to convert from Ang to um; and then redshift...
        xylabel = (   ((linelist['Wavelength'][ll]/1e4)*(1.+redshift)), .30)
        ax.axvline(x= ((linelist['Wavelength'][ll]/1e4)*(1.+redshift)),    color='gray', linestyle='--', linewidth=linewidth/3.4)
        print(ll, xylabel, label)
        ax.annotate(label, xy=xylabel, ha='center', va='center', rotation=90, fontsize=fontsize/1.6 )

    

       
ls = 'solid'
lw = 1.0
ax.set_xlim((xmin, xmax))
ax.set_ylim((ymin, ymax))
ax.set_xlabel('xlabel', fontsize=fontsize)
ax.set_xlabel('xlabel', fontsize=fontsize)
ax.tick_params('x',which='major', top='on', direction='in', labelsize=labelsize,  length=majorticklength, width=tickwidth)
ax.tick_params('x',which='minor', top='on', direction='in', labelsize=labelsize,  length=majorticklength, width=tickwidth)
ax.tick_params('y', which='major',right='on', direction='in', labelsize=labelsize, length=majorticklength, width=tickwidth)
#ax.tick_params('y', which='minor',right='on', direction='in', labelsize=labelsize, length=majorticklength, width=tickwidth)


## Formatting the axes ticks
for axis in [ax.xaxis]:
    axis.set_major_formatter(ScalarFormatter())
    axis.set_minor_formatter(ScalarFormatter())
#for axis in [ax.yaxis]:
    #axis.set_major_formatter(ScalarFormatter())
    #axis.set_minor_formatter(ScalarFormatter())

plt.xlabel(r'Wavelength [$\mu$m]', fontsize=fontsize)
plt.ylabel('Photon-to-electron\nconversion efficiency',        fontsize=fontsize)
#ax.xaxis.label.set_size(32)
#ax.xtick.label.set_size(32)

#plt.show()
plt.savefig('MIRI_MRS_vs_QSO_temp.png', format='png')
#plt.savefig('MIRI_MRS_vs_QSO_temp.pdf', format='pdf')
plt.close(fig)
