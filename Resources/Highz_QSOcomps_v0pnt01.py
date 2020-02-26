'''

Also!! 
https://www.aanda.org/articles/aa/abs/2016/01/aa27096-15/aa27096-15.html
https://github.com/jselsing/QuasarComposite

'''

import matplotlib.pyplot as plt
from astropy.io import ascii

#print(plt.style.available)
#plt.style.use('seaborn-poster')
#plt.style.use('seaborn-white')
#plt.style.use('dark_background')


## Banados et al. (2016) Pan-STARRS1 z>5.6 Composite paper
path = '/cos_pc19a_npr/data/highest_z_QSOs/Banados2016/'
file = 'Banados_2016_Table8.dat'
table = path+file
highz_comp = ascii.read(table)
highz_comp

## Vanden Berk et al. (2001) SDSS Composite paper
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


plt.rcParams.update({'font.size': 14})
fig, ax = plt.subplots(figsize=(12.0, 8.0))


cmap=plt.get_cmap('viridis')

## Tidy up the figure
xmin =   800.           
xmax =  1500.
ymin = -0.35  
ymax = 20.0    


ls = 'solid'
lw = 2.0
ms=20

ax.set_xlim((xmin, xmax))
ax.set_ylim((ymin, ymax))
ax.tick_params('x', direction='in')
ax.tick_params('y', direction='in')

## Plotting the Banados et al. (2016) QSO composite
plt.plot(highz_wave, (highz_flux_med*5), linewidth=lw)
plt.plot(highz_wave, (highz_flux_strong), linewidth=lw)
plt.plot(highz_wave, (highz_flux_weak*10), linewidth=lw)

plt.plot(VdB01_wave_LyA, VdB01_flux_LyA, linewidth=lw)

plt.legend(['PS1 Composite', 'Strong Lya', 'Weak Lya', 'Vanden Berk (2001)'],
           loc="upper left", ncol=1, shadow=True, fancybox=True,
           fontsize=22, frameon=True)


## Plotting the Vanden Berk et al. (2001) QSO composite
#plt.plot(VdB01_wave, VdB01_flux)

## Plotting the Glikman et al. (2006) QSO composite
#plt.plot(Glik_wave, Glik_flux)

#plt.xlabel('MJD')
#plt.ylabel(' W1 - W2 ')

plt.show()
