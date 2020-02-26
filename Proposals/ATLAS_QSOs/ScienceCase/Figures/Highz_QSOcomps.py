
# coding: utf-8

# In[19]:


''' 
Also!! 
https://www.aanda.org/articles/aa/abs/2016/01/aa27096-15/aa27096-15.html
https://github.com/jselsing/QuasarComposite
'''


# In[20]:


import matplotlib.pyplot as plt
from astropy.io import ascii


# In[21]:


#print(plt.style.available)
plt.style.use('seaborn-poster')
#plt.style.use('seaborn-dark-palette')


# In[22]:


path = '/cos_pc19a_npr/data/highest_z_QSOs/Banados2016/'
file = 'Banados_2016_Table8.dat'
table = path+file
highz_comp = ascii.read(table)
highz_comp


# In[31]:


path = '/cos_pc19a_npr/data/SDSS/VdB01/'
file = 'Vanden_Berk_2001_Table1.dat'
table = path+file
VdB01_comp = ascii.read(table)
VdB01_comp


# In[24]:


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


# In[25]:


highz_wave = highz_comp['Wavelength']
highz_flux_med = highz_comp['Flux_comp']
highz_flux_strong = highz_comp['Flux_strong']
highz_flux_weak = highz_comp['Flux_weak']


# In[46]:


VdB01_wave = VdB01_comp['Wavelength']
VdB01_flux = VdB01_comp['Flux']
VdB01_wave_LyA = VdB01_comp['Wavelength'][200:700]
VdB01_flux_LyA = VdB01_comp['Flux'][200:700]


# In[47]:


Glik_wave = Glikman_tab7['Wavelength']
Glik_flux = Glikman_tab7['Flux']


# In[48]:


cmap=plt.get_cmap('viridis')


# In[54]:


## Plotting the Banados et al. (2016) QSO composite
plt.plot(highz_wave, (highz_flux_med*10))
plt.plot(highz_wave, (highz_flux_strong))
plt.plot(highz_wave, (highz_flux_weak*10))

plt.plot(VdB01_wave_LyA, VdB01_flux_LyA)

plt.legend(['PS1 Composite', 'Strong Lya', 'Weak Lya', 
            'Vanden Berk (2001)'],
#           loc="lower left", ncol=3, shadow=True, fancybox=True,
           loc="upper left", ncol=1, shadow=True, fancybox=True,
           fontsize=22, frameon=True)


# In[39]:


## Plotting the Vanden Berk et al. (2001) QSO composite
plt.plot(VdB01_wave, VdB01_flux)

## Plotting the Glikman et al. (2006) QSO composite
plt.plot(Glik_wave, Glik_flux)


# In[ ]:


plt.rcParams.update({'font.size': 14})
fig, ax = plt.subplots(figsize=(12.0, 8.0))

## Tidy up the figure
xmin =   100           
xmax = 40000.
#ymin = -0.35  
#ymax = 1.0    

ls = 'solid'
lw = 1.0
ax.set_xlim((xmin, xmax))
ax.set_ylim((ymin, ymax))
ax.tick_params('x', direction='in')
ax.tick_params('y', direction='in')

plt.xlabel('MJD')
plt.ylabel(' W1 - W2 ')

