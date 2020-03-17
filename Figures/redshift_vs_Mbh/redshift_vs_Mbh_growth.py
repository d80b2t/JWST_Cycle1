'''
WISE detections and colors of Very High redshift quasars
'''
import math
import numpy as np

from astropy.io import fits
from astropy.io import ascii
from astropy.table import Table
from astropy.table import Table

import astropy.units as u
import matplotlib
import matplotlib.pyplot as plt

from matplotlib import colors as mcolors
from matplotlib import gridspec

from astropy.cosmology import FlatLambdaCDM
from astropy.cosmology import z_at_value


## Setting up the cosmology...
cosmo    = FlatLambdaCDM(H0=67.7, Om0=0.307)  #Banados thesis
ages     = np.array([13, 10, 8, 6, 5, 4, 3, 2, 1.5, 1.2, 1, 0.8, 0.70, 0.50, 0.25, 0.10])*u.Gyr
ageticks = [z_at_value(cosmo.age, age) for age in ages]

redshifts     = np.array([6, 7, 8, 9, 10, 12, 15, 20])
redshiftticks = [cosmo.age(redshift).value for redshift in redshifts]

##
##  READ-IN THE   D A T A     F I L E (S)
##  Inayoshi, Visbal, Haiman   Annu. Rev. Astron. Astrophys. 2019. 58:1–79
filename = 'Inayoshi_2019_ARAA_203quasars.dat'
VHzQs    = ascii.read(filename, delimiter=r'\s', guess=False)

z_VHzQs       = VHzQs['redshift']
log_MBH_VHzQs = np.log10(VHzQs['Mbh'])
age_VHzQs     = cosmo.age(z_VHzQs).value


##  Trakhtenbrot et al. (2011) z=4.8 objects
##  name, redshift, L_bol, log_MBH, l_Edd
##  J143+0635	4.850	46.98		8.99	-0.19
path = '/cos_pc19a_npr/data/highest_z_QSOs/Trakhtenbrot2011/'
filename = 'Table2.dat'
Trak11 = ascii.read(path+filename, delimiter=r'\s', guess=False)

z_Trak11       = Trak11['redshift']
log_MBH_Trak11 = Trak11['log_MBH']
age_Trak11     = cosmo.age(z_Trak11).value


##  The 3 monsters in Banados et al, 2018, Nature, 553, 473
##  name, redshift, L_bol, log_MBH, l_Edd
##  J143+0635	4.850	46.98		8.99	-0.19
path      = '/cos_pc19a_npr/data/highest_z_QSOs/Mbh_values/'
filename  = 'Banados_2018_Fig2.dat'
Banados   = ascii.read(path+filename, delimiter=r'\s', guess=False)
log_MBH_Bana = np.log10(Banados['MBH'])
z_Bana       = Banados['redshift']

filename  = 'Gallerani_2017.dat'
Gallerani = ascii.read(path+filename, delimiter=r'\s', guess=False)
log_MBH_Gall = np.log10(Gallerani['M_BH'])
z_Gall       = Gallerani['redshift']

filename  = 'Top10.dat'
Top10 = ascii.read(path+filename, delimiter=r'\s', guess=False)
log_MBH_Top10 = np.log10(Top10['MBH'])
z_Top10       = Top10['redshift']



##
## Salpeter timescales,
##    basing this off Figure 2 of Banados et al. 2018, Nature
zrange = np.arange(3, 45, 0.1)
ee = [cosmo.age(zz).value for zz in zrange]
t_bana = np.array(ee)*1e9

## Some physical values...
Ledd = 1.0

## Hold M_seed constant, vary eta
M_seed = 1000.0

eta                  = [0.05, 0.10, 0.15,  0.20, 0.30]
eta                  = [0.10, 0.11, 0.125, 0.14, 0.15]
s = (len(t_bana),len(eta))
M_BH_grower_eta = np.zeros(s)
for ii in range(len(eta)):
    t_salpeter            = 4.5e7*(eta[ii]/0.1)*(Ledd**(-1))
    M_BH_grower_eta[:,ii] = (np.exp(t_bana/t_salpeter))*M_seed
    
#M_BH_grower_etapnt05 = (np.exp(t_bana/t_salpeter))*M_seed
#eta                  = 0.10
#t_salpeter           = 4.5e7*(eta/0.1)*(Ledd**(-1))
#M_BH_grower_etapnt10 = (np.exp(t_bana/t_salpeter))*M_seed
#eta                  = 0.15
#t_salpeter           = 4.5e7*(eta/0.1)*(Ledd**(-1))
#M_BH_grower_etapnt15 = (np.exp(t_bana/t_salpeter))*M_seed
#eta                  = 0.2
#t_salpeter           = 4.5e7*(eta/0.1)*(Ledd**(-1))
#M_BH_grower_etapnt20 = (np.exp(t_bana/t_salpeter))*M_seed
#eta                  = 0.3
#t_salpeter           = 4.5e7*(eta/0.1)*(Ledd**(-1))
#M_BH_grower_etapnt30 = (np.exp(t_bana/t_salpeter))*M_seed

    
## Hold eta constant, vary M_seed    
eta        = 0.15
t_salpeter = 4.5e7*(eta/0.1)*(Ledd**(-1))
M_seed     = 100.0
M_BH_grower_hundred  = (np.exp(t_bana/t_salpeter))*M_seed
M_BH_grower_thousand = (np.exp(t_bana/t_salpeter))*M_seed*10
M_BH_grower_10k      = (np.exp(t_bana/t_salpeter))*M_seed*100
    
    
##
## Making the plot
##
fig, ax1 = plt.subplots(figsize=(14.0, 10.0))

## May fave new line ;-=)
plt.style.use('dark_background')
plt.rcParams.update({'font.size': 14})
matplotlib.rc('text', usetex=True)
matplotlib.rcParams['lines.linewidth'] = 22  #does this do anything??!!


## Adjusting the Whitespace for the plots
left   = 0.14   # the left side of the subplots of the figure
right  = 0.94   # the right side of the subplots of the figure
bottom = 0.16   # the bottom of the subplots of the figure
top    = 0.88   # the top of the subplots of the figure
wspace = 0.26   # the amount of width reserved for blank space between subplots
hspace = 0.06   # the amount of height reserved for white space between subplots
plt.subplots_adjust(left=left, bottom=bottom, right=right, top=top, wspace=wspace, hspace=hspace)

## Some NPR defaults
ls              = 'solid'
lw              = 1.0
ms_large        = 250
ms              = ms_large/3.
alpha           = 1.0
fontsize        = 36
labelsize       = fontsize
tickwidth       = 2.0
linewidth       = 2.4
tickwidth       = 2.0
ticklength      = 6.0
ticklabelsize   = labelsize
majorticklength = 12
minorticklength = 6


from matplotlib.ticker import MultipleLocator, FormatStrFormatter
minorLocator = MultipleLocator(5)

## define the colormap
cmap = plt.cm.jet ## great with 'dark_background'
cmap = plt.cm.viridis

## AGE RANGE
xmin =  0.20    # Gyr
xmax =  1.4 
## REDSHIFT RANGE
zmin =  5.8    ## 3.0    ## 4.3
zmax =  8.0    ## 16.0 ## z=45 in Banados 2018
##  Mass access
ymin =  6.5    # 2.8 good if redshift is z= 45. 
ymax = 10.5   


c = VHzQs['M1450']
#cmap = plt.cm.jet ## great with 'dark_background'
cmap = plt.cm.viridis_r

## Plotting the quasars...
ax1.scatter(z_VHzQs, log_MBH_VHzQs,    c=c, cmap=cmap, marker="P", s=(ms_large*1.2), label="$z>$6 QSOs", zorder=12)
#ax1.scatter(z_Top10, log_MBH_Top10,    c='b', marker="s", s=ms_large, label="Highest-$z$/most massive", zorder=10)
#ax1.scatter(z_Trak11, log_MBH_Trak11,  c='k', marker="d", s=ms_large, label="Trakhtenbrot (2011)", zorder=10)
#ax1.scatter(z_Trak11, log_MBH_Trak11,   c='silver', marker="d", s=ms_large, label="Trakhtenbrot+ (2011)", zorder=10)

##
##   BH   Growth   tracks..
##
##   Varying   e t a 
##ax1.plot(zrange, (np.log10(M_BH_grower_etapnt05)), label ='$\eta=0.05$',  linewidth=8)
#ax1.plot(zrange, (np.log10(M_BH_grower_etapnt1)),  label ='$\;\; \eta=0.10$ (M$_{seed}=10^{4} M_{\odot}$)',  linewidth=8, linestyle='--', color='crimson')
#ax1.plot(zrange, (np.log10(M_BH_grower_etapnt05)),  label ='$\;\; \eta=0.10$',  linewidth=8, linestyle='--', color='crimson')
#ax1.plot(zrange, (np.log10(M_BH_grower_etapnt10)),  label ='$\;\; \eta=0.10$',  linewidth=8, linestyle='--', color='crimson')
#ax1.plot(zrange, (np.log10(M_BH_grower_etapnt15)), label = '$\; \eta=0.15$',  linewidth=8, linestyle='-')
#ax1.plot(zrange, (np.log10(M_BH_grower_etapnt20)),  label = '$\eta=0.20$',  linewidth=8,linestyle=':')  
#ax1.plot(zrange, (np.log10(M_BH_grower_etapnt30)),  label = '$\eta=0.30$',  linewidth=8)
#
ax1.plot(zrange, (np.log10( M_BH_grower_eta[:,0]   )),  label ='$\;\; \eta=0.10$',  linewidth=8, linestyle='--', color='crimson')
ax1.plot(zrange, (np.log10( M_BH_grower_eta[:,1]   )),  label ='$\;\; \eta=0.10$',  linewidth=8, linestyle='--', color='crimson')
ax1.plot(zrange, (np.log10( M_BH_grower_eta[:,2]   )), label = '$\; \eta=0.15$',  linewidth=8, linestyle='-')
ax1.plot(zrange, (np.log10( M_BH_grower_eta[:,3]   )),  label = '$\eta=0.20$',  linewidth=8,linestyle=':')  
ax1.plot(zrange, (np.log10( M_BH_grower_eta[:,4]   )),  label = '$\eta=0.30$',  linewidth=8)

##   Varying   seed  BH  mass
#ax1.plot(zrange, (np.log10(M_BH_grower_hundred)),  label ='$M_{seed}=10^{2} M_{\odot}$ ($\eta=0.15$)', linewidth=8, linestyle='--')
#ax1.plot(zrange, (np.log10(M_BH_grower_thousand)), label ='$M_{seed}=10^{3} M_{\odot}$',              linewidth=8, linestyle='-.')
#ax1.plot(zrange, (np.log10(M_BH_grower_10k)),      label ='$M_{seed}=10^{4} M_{\odot}$',              linewidth=8, linestyle=':')  


##   L E G E N D
ax1.legend(loc='lower right', fontsize=fontsize/1.3, frameon='True')


#ax1.set_xscale("log", nonposx='clip')
ax1.set_xlim((zmin, zmax))
ax1.set_ylim((ymin, ymax))
ax1.tick_params('x', direction='in', which='major', bottom='on', top='on', left='on', right='on', size=fontsize/1.6)
ax1.tick_params('x', direction='in', which='minor', bottom='on', top='on', left='on', right='on', size=fontsize/1.6)
ax1.tick_params('y', direction='in', which='major', bottom='on', top='on', left='on', right='on', size=fontsize/1.6)
ax1.tick_params('y', direction='in', which='minor', bottom='on', top='on', left='on', right='on', size=fontsize/1.6)
ax1.xaxis.set_minor_locator(minorLocator)

ax1.tick_params(axis='both',                    labelsize = fontsize/1.1)
ax1.set_xlabel('redshift, $z$',                 fontsize  = fontsize)
ax1.set_ylabel('log (M$_{BM}$) / M$_{\odot}$)', fontsize  = fontsize)
             
ax4 = ax1.twiny()
## If  AGE,  is the top x-axis
ax4.set_xticks(ageticks)
ax4.set_xticklabels(['{:g}'.format(age) for age in ages.value])
ax4.set_xlim(zmin, zmax)    ## the co-ordinate system is in "redshift units"
ax4.set_xlabel('Time since Big Bang (Gyr)', fontsize=fontsize)
ax4.tick_params(axis='both', labelsize=fontsize/1.1)
ax4.xaxis.set_label_coords(0.50, 1.10)

## if REDSHIFT is the top x-axis
#ax4.set_xlim(xmin, xmax)     ## The co-ordinate system is in "age units"
#ax4.set_xticks(redshiftticks)
#ax4.set_xticklabels(['{:g}'.format(redshifts) for redshifts in redshifts])
#ax4.tick_params(axis='both', labelsize=36)

#plt.show()
plt.savefig('redshift_vs_Mbh_growth_temp.png',format='png')
plt.close(fig)
