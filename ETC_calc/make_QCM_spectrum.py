import pyfits
import matplotlib
import matplotlib.pyplot as plt
from matplotlib import colors as mcolors
from astropy.io import ascii

factor = (1./1e4)  ## 1/1e4 to convert Ang to um

## Vanden Berk et al. 2001, Table1
path = '/cos_pc19a_npr/data/SDSS/VdB01/'
file = 'Vanden_Berk_2001_Table1.dat'
table = path+file
VdB01_comp = ascii.read(table)
VdB01_comp

VdB01_wave = VdB01_comp['Wavelength']  * factor
VdB01_flux = VdB01_comp['Flux']
VdB01_wave_LyA = VdB01_comp['Wavelength'][200:700]
VdB01_flux_LyA = VdB01_comp['Flux'][200:700]

## Glikman et al. 2006
path = '/cos_pc19a_npr/data/Glikman2006/'
file = 'Glikman_2006_ApJ_Table3.dat'
table = path+file
Glikman_tab3 = ascii.read(table)
print(Glikman_tab3)
path = '/cos_pc19a_npr/data/Glikman2006/'
file = 'Glikman_2006_ApJ_Table7.dat'
table = path+file
Glikman_tab7 = ascii.read(table)
print(Glikman_tab7)

Glik_wave = Glikman_tab7['Wavelength']* factor
Glik_flux = Glikman_tab7['Flux']

##
path = '/cos_pc19a_npr/data/SEDs/Kirkpatrick2012/'
#file = 'Kirkpatrick2012_featureless_AGN_SED.txt'
file = 'Kirkpatrick2012_z1_SF_SED.txt'
table = path+file
Kirkpatrick2012_AGN =  ascii.read(table)
KirkAGN_wave = Kirkpatrick2012_AGN['Wavelength_microns'] 
KirkAGN_flux = Kirkpatrick2012_AGN['Lnu'] / 1e23  ##  L_{\nu} in [W/Hz]

## redshift
redshift = 6.00

##
## Making the plot
##
## May fave new line ;-=)
#plt.style.use('dark_background')
matplotlib.rc('text', usetex=True)
plt.rcParams.update({'font.size': 14})
#print(plt.style.available)
plt.style.use('seaborn-poster')

fig, ax1 = plt.subplots(figsize=(12.0, 6.0))

size_fac = 1.5
ls = 'solid'
lw = 2.0
ms_large = 250
ms = ms_large/3.


## Wavelength range, in um
xmin =    5000. * factor #* (1+redshift)    
xmax =  310000. * factor #* (1+redshift)     

## Flux range
## if log
#ymin =    0.1  
#ymax =   60.00
ymin =    0.1   ## if linear
ymax =   50.00


ax1.set_xlim([xmin, xmax])
ax1.set_ylim([ymin, ymax])
ax1.set_xscale('log')
ax1.set_yscale('log')

cmap=plt.get_cmap('viridis')

ratio=1.5
## Plotting the Vanden Berk et al. (2001) QSO composite
ax1.plot(VdB01_wave*(1+redshift), (VdB01_flux*ratio), lw=lw)

## Plotting the Glikman et al. (2006) QSO composite
ratio=3.0
ax1.plot(Glik_wave*(1+redshift)    , (Glik_flux/ratio), lw=lw)

## Plotting the Kirkpatrick et al. (2012) composite
#ax1.plot(KirkAGN_wave*(1+redshift), (KirkAGN_flux/ratio), lw=lw)

ax1.set_xlabel('Wavelength [$\mu$m]', fontsize=(38/size_fac))
ax1.set_ylabel('Flux (Arbitary units)', fontsize=(38/size_fac))
ax1.tick_params(axis='both', labelsize=(36/size_fac))
plt.tick_params(which='both',  width=2)
plt.tick_params(which='major', length=10)
plt.tick_params(which='minor', length=5)

plt.tight_layout()

plt.show()
