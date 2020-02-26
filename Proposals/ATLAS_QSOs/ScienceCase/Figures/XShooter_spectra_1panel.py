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

## Emission Lines e.g.
## ~/data/SDSS/VdB01/List_of_lines_byRelativeFlux.dat
Lyb_wave    = 1025.72 * factor
OVI_wave    = 1033.83 * factor
Lya_wave    = 1215.67 * factor
NV_wave     = 1240.14 * factor
SiIV_wave   = 1396.76 * factor
OIV_wave    = 1402.06 * factor
CIV_wave    = 1546.15 * factor
CIII_wave   = 1908.73 * factor
MgII_wave   = 2800.26 * factor
Hbeta_wave  = 4862.68 * factor
Hgamma_wave = 4341.68 * factor
OIII_wave   = 5008.22 * factor
Halpha_wave = 6564.93 * factor


##
## JWST FILTERS
##
## NIRSpec
#path = '/cos_pc19a_npr/data/filter_curves/JWST/NIRSpec/Ref_Files/'
path = '/cos_pc19a_npr/LaTeX/proposals/JWST/JWST_Cycle1/pandeia_data-1.2.2/jwst/nirspec/filters/'
nirspec_f070lp = pyfits.open(path+'jwst_nirspec_f070lp_trans_20160902193401.fits')
nirspec_f070lp_data  = nirspec_f070lp[1].data
nirspec_f070lp_wave  = nirspec_f070lp_data['WAVELENGTH'] ## in um
nirspec_f070lp_trans = nirspec_f070lp_data['THROUGHPUT'] 

path = '/cos_pc19a_npr/LaTeX/proposals/JWST/JWST_Cycle1/pandeia_data-1.2.2/jwst/nirspec/blaze/'
nirspec_g140h = pyfits.open(path+'jwst_nirspec_g140h_speceff_20160902193401.fits')
nirspec_g140h_data  = nirspec_g140h[1].data
##nirspec_g140h_data.columns 
nirspec_g140h_wave  = nirspec_g140h_data['WAVELENGTH'] ## in um
nirspec_g140h_trans = nirspec_g140h_data['THROUGHPUT'] 


## MIRI
## Imaging
## https://jwst-docs.stsci.edu/display/JTI/MIRI+Imaging?preview=/16220172/16220180/MIRI_IMAGING2.png
path = '/cos_pc19a_npr/data/filter_curves/JWST/MIRI/Ref_Files/'
f560w_filter = pyfits.open(path+'jwst_miri_f560w_filter.fits')
f560w_filter[1].columns
f560w_data  = f560w_filter[1].data
f560w_wave  = f560w_data['WAVELENGTH'] 
f560w_trans = f560w_data['TRANSMISSION'] 

f770w_filter = pyfits.open(path+'jwst_miri_f770w_filter.fits')
f770w_data   = f770w_filter[1].data
f770w_wave   = f770w_data['WAVELENGTH'] 
f770w_trans  = f770w_data['TRANSMISSION'] 

f1000w_filter = pyfits.open(path+'jwst_miri_f1000w_filter.fits')
f1000w_data   = f1000w_filter[1].data
f1000w_wave   = f1000w_data['WAVELENGTH'] 
f1000w_trans  = f1000w_data['TRANSMISSION'] 

path = '/cos_pc19a_npr/LaTeX/proposals/JWST/JWST_Cycle1/pandeia_data-1.2.2/jwst/miri/dispersion/'
miri_ch1_short = pyfits.open(path+'jwst_miri_ch1_short_disp_20170404135013.fits')
miri_ch1_short_data = miri_ch1_short[1].data
'''
miri_ch1_short_data.columns
ColDefs(
    name = 'WAVELENGTH'; format = 'D'; unit = 'MICRONS'
    name = 'DLDS'; format = 'D'; unit = 'MICRON/PIXEL'
    name = 'R'; format = 'D'; unit = 'RESOLUTION'
)
'''
#miri_ch1_short_wave = tbdata.field('WAVELENGTH')
#miri_ch1_short_thru = tbdata.field('THROUGHPUT')

path = '/cos_pc19a_npr/LaTeX/proposals/JWST/JWST_Cycle1/pandeia_data-1.2.2/jwst/miri/qe/'
miri_mrs_sw = pyfits.open(path+'jwst_miri_mrs_sw_qe_20170404135013.fits')
tbdata = miri_mrs_sw[1].data
mrs_sw_wave = tbdata.field('WAVELENGTH')
mrs_sw_thru = tbdata.field('THROUGHPUT')


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

## Wavelength range, in um
xmin =     800. * factor*(1+redshift)    
xmax =  100000. * factor*(1+redshift)     
## Flux range
ymin =    0.1
ymax =   60.00

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

## Plotting the Kirkpatrick et al. (2012) composite
ax1.plot(KirkAGN_wave*(1+redshift), (KirkAGN_flux/ratio), lw=lw)


## Plotting the Emission Lines wavelengths as vertical lines
lw = 1.0
plt.axvline(x=(Lyb_wave*(1+redshift)), linewidth=lw, color='k', linestyle='dotted')
#plt.axvline(x=(OVI_wave*(1+redshift)), linewidth=lw, color='k', linestyle='dotted')
plt.axvline(x=(Lya_wave*(1+redshift)), linewidth=lw, color='k', linestyle='dotted')
plt.axvline(x=(NV_wave*(1+redshift)), linewidth=lw, color='k', linestyle='dotted')
plt.axvline(x=(SiIV_wave*(1+redshift)), linewidth=lw, color='k', linestyle='dotted')
plt.axvline(x=(OIV_wave*(1+redshift)), linewidth=lw, color='k', linestyle='dotted')
plt.axvline(x=(CIV_wave*(1+redshift)), linewidth=lw, color='k', linestyle='dotted')
plt.axvline(x=(CIII_wave*(1+redshift)), linewidth=lw, color='k', linestyle='dotted')
plt.axvline(x=(MgII_wave*(1+redshift)), linewidth=lw, color='k', linestyle='dotted')
plt.axvline(x=(Hbeta_wave*(1+redshift)), linewidth=lw, color='k', linestyle='dotted')
plt.axvline(x=(OIII_wave*(1+redshift)), linewidth=lw, color='k', linestyle='dotted')
plt.axvline(x=(Halpha_wave*(1+redshift)), linewidth=lw, color='k', linestyle='dotted')

## JWST Filters to plot
## NIRSpec
ax1.plot(nirspec_f070lp_wave, nirspec_f070lp_trans, color='red')
ax1.plot(nirspec_g140h_wave, nirspec_g140h_trans, color='red')

## MIRI
ax1.plot(f560w_wave, (f560w_trans/4.), color='darkorchid')

#darkorchid, blueviolet, mediumpurple
#slateblue, dodgerblue, cornflowerblue
#lightseagreen, mediumaquamarine, darkseagreen
#khaki, sandybrown, salmon


ax1.set_xlabel('Wavelength \AA', fontsize=(38/size_fac))
ax1.set_ylabel('Flux (Arbitary units)', fontsize=(38/size_fac))
ax1.tick_params(axis='both', labelsize=(36/size_fac))


plt.show()
