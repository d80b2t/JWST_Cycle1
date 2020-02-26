'''

Also!! 
https://www.aanda.org/articles/aa/abs/2016/01/aa27096-15/aa27096-15.html
https://github.com/jselsing/QuasarComposite

http://svo2.cab.inta-csic.es/svo/theory/fps3/index.php
http://svo2.cab.inta-csic.es/svo/theory/fps3/index.php?id=JWST/MIRI.F560W&&mode=browse&gname=JWST&gname2=MIRI#filter

'''

import matplotlib.pyplot as plt
from astropy.io import ascii

#print(plt.style.available)
#plt.style.use('seaborn-poster')
#plt.style.use('seaborn-white')
#plt.style.use('dark_background')

redshift = 9.5
#redshift = input("What redshift are we working at??   ")
print()
print("Working at redshift = ", redshift, '\n')


## JWST FILTERS
G140M_F100LP = ascii.read('NIRSpec_throughput_G140M_F100LP.dat')


## Banados et al. (2016) Pan-STARRS1 z>5.6 Composite paper
path = '/cos_pc19a_npr/data/highest_z_QSOs/Banados2016/'
file = 'Banados_2016_Table8.dat'
table = path+file
highz_comp = ascii.read(table)
#highz_comp

## Vanden Berk et al. (2001) SDSS Composite paper
path = '/cos_pc19a_npr/data/SDSS/VdB01/'
file = 'Vanden_Berk_2001_Table1.dat'
table = path+file
VdB01_comp = ascii.read(table)
#VdB01_comp

## Glikman et al. (2006) NIR Quasar Composite
path = '/cos_pc19a_npr/data/Glikman2006/'
file = 'Glikman_2006_ApJ_Table3.dat'
table = path+file
Glikman_tab3 = ascii.read(table)
#print(Glikman_tab3)
path = '/cos_pc19a_npr/data/Glikman2006/'
file = 'Glikman_2006_ApJ_Table7.dat'
table = path+file
Glikman_tab7 = ascii.read(table)
#print(Glikman_tab7)

## Making all the variables a bit more user friendly..
G140M_F100LP_wave = G140M_F100LP['wavelength']*10000
G140M_F100LP_thru = G140M_F100LP['thoughput']

highz_wave = highz_comp['Wavelength']
highz_flux_med = highz_comp['Flux_comp']
highz_flux_strong = highz_comp['Flux_strong']
highz_flux_weak = highz_comp['Flux_weak']

VdB01_wave = VdB01_comp['Wavelength']
VdB01_flux = VdB01_comp['Flux']
VdB01_wave_LyA = VdB01_comp['Wavelength'][200:700]
VdB01_flux_LyA = VdB01_comp['Flux'][200:700]

Glik_wave = Glikman_tab7['Wavelength']
Glik_flux = Glikman_tab7['Flux']

## PLOTTING IT ALL UP
plt.rcParams.update({'font.size': 14})
fig, ax = plt.subplots(figsize=(12.0, 8.0))

cmap=plt.get_cmap('viridis')

## Tidy up the figure
xmin =    800.*redshift           
xmax =   2100.*redshift
ymin =  -0.05  
ymax =   1.8    

ls = 'solid'
lw = 2.0
ms=20

ax.set_xlim((xmin, xmax))
ax.set_ylim((ymin, ymax))
ax.tick_params('x', direction='in')
ax.tick_params('y', direction='in')

overall_norm = 12.0
## Plotting the Banados et al. (2016) QSO composite
#plt.plot(highz_wave*redshift, ((highz_flux_med*5)/overall_norm), linewidth=lw)
#plt.plot(highz_wave*redshift, ((highz_flux_strong)/overall_norm), linewidth=lw)
#plt.plot(highz_wave*redshift, ((highz_flux_weak*10)/overall_norm), linewidth=lw)

#plt.plot(VdB01_wave_LyA*redshift, (VdB01_flux_LyA/overall_norm), linewidth=lw, color='m')
plt.plot(VdB01_wave*redshift, (VdB01_flux/overall_norm), linewidth=lw, color='m')

plt.plot(G140M_F100LP_wave, G140M_F100LP_thru, linewidth=lw, color='r')
plt.fill(G140M_F100LP_wave, G140M_F100LP_thru, alpha=0.20,   color='r')

plt.legend(
#    ['PS1 Composite', 'Strong Lya', 'Weak Lya','Vanden Berk (2001)','G140M/F100LP'],
    ['Vanden Berk (2001)','G140M/F100LP'],
           loc="upper right", ncol=1, shadow=True, fancybox=True,
           fontsize=22, frameon=True)

## Plotting the Vanden Berk et al. (2001) QSO composite
#plt.plot(VdB01_wave, VdB01_flux)

## Plotting the Glikman et al. (2006) QSO composite
#plt.plot(Glik_wave, Glik_flux)

plt.title(r'QSO at $z=9.5$', fontsize=28)
plt.xlabel('Observed Wavelenght (Ang)')
plt.ylabel('Norm. Flux')

plt.show()
