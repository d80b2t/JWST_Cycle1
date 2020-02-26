import pyfits
import matplotlib
import matplotlib.pyplot as plt
from astropy.io import ascii

path = '/cos_pc19a_npr/data/SDSS/VdB01/'
file = 'Vanden_Berk_2001_Table1.dat'
table = path+file
VdB01_comp = ascii.read(table)
VdB01_comp

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

VdB01_wave = VdB01_comp['Wavelength']
VdB01_flux = VdB01_comp['Flux']
VdB01_wave_LyA = VdB01_comp['Wavelength'][200:700]
VdB01_flux_LyA = VdB01_comp['Flux'][200:700]

Glik_wave = Glikman_tab7['Wavelength']
Glik_flux = Glikman_tab7['Flux']


path = '/cos_pc19a_npr/data/filter_curves/JWST/MIRI/Ref_Files/'
f560w_filter = pyfits.open(path+'jwst_miri_f560w_filter.fits')
f560w_filter
f560w_filter[1].columns
f560w_data = f560w_filter[1].data

f560w_wave = f560w_data['WAVELENGTH'] 
f560w_trans = f560w_data['TRANSMISSION'] 







##
## Making the plot
##
## May fave new line ;-=)
#plt.style.use('dark_background')
matplotlib.rc('text', usetex=True)
matplotlib.rcParams['lines.linewidth'] = 22  #does this do anything??!!

plt.rcParams.update({'font.size': 14})
fig, ax1 = plt.subplots(figsize=(18.0, 8.0))
size_fac = 1.5

ls = 'solid'
lw = 2.0
ms_large = 250
ms = ms_large/3.

## redshift
redshift = 6.00

## Wavelength range
xmin =    800*(1+redshift)    
xmax =  30000*(1+redshift)     
## Flux range
ymin =   0.20
ymax = 25.00

ax1.set_xlim([xmin, xmax])
ax1.set_ylim([ymin, ymax])
ax1.set_xscale('log')
ax1.set_yscale('log')

cmap=plt.get_cmap('viridis')

#print(plt.style.available)
plt.style.use('seaborn-poster')
#plt.style.use('seaborn-dark-palette')

## Plotting the Vanden Berk et al. (2001) QSO composite
ax1.plot(VdB01_wave*(1+redshift), VdB01_flux, lw=lw)

## Plotting the Glikman et al. (2006) QSO composite
ratio=3.0
ax1.plot(Glik_wave*(1+redshift)    , (Glik_flux/ratio), lw=lw)

ax1.plot((f560w_wave*10000), (f560w_trans/4.))

ax1.set_xlabel('Wavelength \AA', fontsize=(38/size_fac))
ax1.set_ylabel('Flux (Arbitary units)', fontsize=(38/size_fac))
ax1.tick_params(axis='both', labelsize=(36/size_fac))


plt.show()
