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
## The MIRI MRS Filters
## From:: 
##   http://ircamera.as.arizona.edu/MIRI/pces.htm
##   MRSPCE_TN-00072-ATC-Iss1
##
path = 'filter_curves/MIRI/'
df   = pandas.read_csv(path+'MRSPCE_TN-00072-ATC-Iss1.csv')       

## Setting up the channels 
Ch1_short  = df[df.Band == 0]
Ch1_medium = df[df.Band == 1]
Ch1_long   = df[df.Band == 2]
Ch2_short  = df[df.Band == 3]
Ch2_medium = df[df.Band == 4]
Ch2_long   = df[df.Band == 5]
Ch3_short  = df[df.Band == 6]
Ch3_medium = df[df.Band == 7]
Ch3_long   = df[df.Band == 8]
Ch4_short  = df[df.Band == 9]
Ch4_medium = df[df.Band == 10]
Ch4_long   = df[df.Band == 11]


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


##  R E D S H I F T  !!!!
#redshift =  7.54
redshift = 6.7
#redshift = float(input("What redshift are we at??   "))


## Some NPR plotting defaults 
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

## Plotting things up...
plt.rcParams.update({'font.size': 24})
fig, ax = plt.subplots(figsize=(22.0, 8.0))

## Setting the limits.
## If log
xmin = 4.85           ## .400 if log;  0.1um = 1e-7 = 100e-9 = 1000Ang
xmax = 30.           ## 60.  if log;  30.0um
ax.set_xscale("log", nonposx='clip')
ymin = 0.00  
ymax = 0.22   


## Plotting the QSO composites
#plt.plot((VdB01_wave              *(1.+redshift)), (VdB01_flux/VdB01_flux.max()),                 color='k', linestyle='-')
plt.plot((quasar_sed['wavelength']*(1.+redshift)), (quasar_sed['flux']/(quasar_sed['flux'].max()*2)), color='k')


##
## MIRI Imaging filters
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

ax.plot(Ch4_short.wavelength,  Ch4_short.efficiency,  color='orange',           alpha=alpha, linewidth=linewidth)
ax.fill(Ch4_short.wavelength,  Ch4_short.efficiency,  color='orange',           alpha=alpha/2)
ax.plot(Ch4_medium.wavelength, Ch4_medium.efficiency, color='peru',             alpha=alpha, linewidth=linewidth)
ax.fill(Ch4_medium.wavelength, Ch4_medium.efficiency, color='peru',             alpha=alpha/2)
ax.plot(Ch4_long.wavelength,   Ch4_long.efficiency,   color='red',              alpha=alpha, linewidth=linewidth)
ax.fill(Ch4_long.wavelength,   Ch4_long.efficiency,   color='red',              alpha=alpha/2)


plot_filterLabels = 'y'
y_labelplacement = 0.18
if plot_filterLabels == 'y':
    plt.text( 5.35, y_labelplacement, r'CH1 SHORT',  color ='darkviolet',       fontsize=fontsize,     weight='bold')
    plt.text( 6.15, y_labelplacement, r'CH1 MEDIUM', color ='mediumorchid',     fontsize=fontsize,     weight='bold')
    plt.text( 7.09, y_labelplacement, r'CH1 LONG',   color ='mediumpurple',     fontsize=fontsize,     weight='bold')
    
    plt.text( 8.13, y_labelplacement, r'CH2 SHORT',  color ='mediumslateblue',  fontsize=fontsize,     weight='bold')
    plt.text( 9.40, y_labelplacement, r'CH2 MEDIUM', color ='cornflowerblue',   fontsize=fontsize,     weight='bold')
    plt.text(10.85, y_labelplacement, r'CH2 LONG',   color ='dodgerblue',       fontsize=fontsize,     weight='bold')
    
    plt.text(12.50, y_labelplacement, r'CH3 SHORT',  color ='mediumaquamarine', fontsize=fontsize,     weight='bold')
    plt.text(14.50, y_labelplacement, r'CH3 MEDIUM', color ='mediumseagreen',   fontsize=fontsize,     weight='bold')
    plt.text(16.75, y_labelplacement, r'CH3 LONG',   color ='lightseagreen',    fontsize=fontsize,     weight='bold')
    
    plt.text(19.29, y_labelplacement, r'CH4 SHORT',  color ='orange',           fontsize=fontsize,     weight='bold')
    plt.text(22.47, y_labelplacement, r'CH4 MEDIUM', color ='peru',             fontsize=fontsize,     weight='bold')
    plt.text(26.20, y_labelplacement, r'CH4 LONG',   color ='red',              fontsize=fontsize,     weight='bold')




x_placement = 20.5      
#plt.text(x_placement, (ymax*0.72), r'$z$='+str(redshift)+' quasar', color='k',     weight='bold', size=size)
plt.text(x_placement, (ymax*0.72), r'$z$='+str(redshift)+' quasar', color='k',     weight='bold', size=fontsize)

#plt.legend([
#             'Quasar SED Glikman (2006)',
      #     loc="upper right", ncol=1, shadow=True, fancybox=True,
       #   fontsize=22, frameon=True)

       
ls = 'solid'
lw = 1.0
ax.set_xlim((xmin, xmax))
ax.set_ylim((ymin, ymax))
ax.set_xlabel('xlabel', fontsize=fontsize)
ax.set_xlabel('xlabel', fontsize=fontsize)
ax.tick_params('x',which='major', top='on', direction='in', labelsize=labelsize,  length=majorticklength, width=tickwidth)
ax.tick_params('x',which='minor', top='on', direction='in', labelsize=labelsize,  length=majorticklength, width=tickwidth)
#ax.tick_params('x',which='minor', top='on', direction='in', labelsize=labelsize,  length=minorticklength, width=tickwidth)
ax.tick_params('y', which='major',right='on', direction='in', labelsize=labelsize, length=majorticklength, width=tickwidth)
ax.tick_params('y', which='major',right='on', direction='in', labelsize=labelsize, length=majorticklength, width=tickwidth)
#ax.tick_params('y', which='minor', right='on', direction='in', labelsize=labelsize, length=minorticklength, width=tickwidth)

##ax.ticklabel_format(style='plain', axis='x')

## https://matplotlib.org/gallery/ticks_and_spines/scalarformatter.html
## https://stackoverflow.com/questions/21920233/matplotlib-log-scale-tick-label-number-formatting

for axis in [ax.xaxis, ax.yaxis]:
    axis.set_major_formatter(ScalarFormatter())
    axis.set_minor_formatter(ScalarFormatter())

plt.xlabel(r'Wavelength [$\mu$m]', fontsize=fontsize)
plt.ylabel('Photon-to-electron\nconversion efficiency',        fontsize=fontsize)
#ax.xaxis.label.set_size(32)
#ax.xtick.label.set_size(32)

#plt.show()
plt.savefig('MIRI_MRS_vs_QSO_temp.png', format='png')
plt.savefig('MIRI_MRS_vs_QSO_temp.pdf', format='pdf')
plt.close(fig)
