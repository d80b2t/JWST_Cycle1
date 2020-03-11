
# coding: utf-8

# In[60]:


import pyfits
import matplotlib.pyplot as plt


# In[61]:


path = '/cos_pc19a_npr/data/filter_curves/JWST/MIRI/Ref_Files/'
#file


# In[62]:


#jwst_miri_f560w_filter.fits
f560w_filter = pyfits.open(path+'jwst_miri_f560w_filter.fits')


# In[63]:


f560w_filter


# In[64]:


f560w_filter[1].columns


# In[65]:


data = f560w_filter[1].data


# In[66]:


f560w_wave = data['WAVELENGTH'] 
f560w_trans = data['TRANSMISSION'] 


# In[67]:


plt.plot(f560w_wave, f560w_trans)

