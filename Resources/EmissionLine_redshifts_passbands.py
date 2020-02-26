#!/usr/bin/env python
'''
Python code to figure out/state when various (quasar) emission lines 
move in and out of various SDSS/UKIDSS/WISE and JWST passbands
'''

import numpy as np

np.set_printoptions(precision=3)


## Table 9, Peth et al. (2011, AJ, 141, 105)
u = np.array([ 3005,  3551,  4000])
g = np.array([ 3720,  4686,  5680]) 
r = np.array([ 5370,  6166,  7120])
i = np.array([ 6770,  7480,  8380])
z = np.array([ 8000,  8932, 10620])
Y = np.array([ 9790, 10305, 10810])
J = np.array([11690, 12483, 13280])
H = np.array([14920, 16313, 17840])
K = np.array([20290, 22010, 23800])

## VdB01, Table 2, lambda_lab
Lya_lambda    = 1215.67
CIV_lambda    = 1549.06        
MgII_lambda   = 2798.75
Halpha_lambda = 6564.61


u_Lya = (u/Lya_lambda)-1
g_Lya = (g/Lya_lambda)-1
r_Lya = (r/Lya_lambda)-1
i_Lya = (i/Lya_lambda)-1
z_Lya = (z/Lya_lambda)-1
Y_Lya = (Y/Lya_lambda)-1
J_Lya = (J/Lya_lambda)-1
H_Lya = (H/Lya_lambda)-1
K_Lya = (K/Lya_lambda)-1

u_CIV = (u/CIV_lambda)-1
g_CIV = (g/CIV_lambda)-1
r_CIV = (r/CIV_lambda)-1
i_CIV = (i/CIV_lambda)-1
z_CIV = (z/CIV_lambda)-1
Y_CIV = (Y/CIV_lambda)-1
J_CIV = (J/CIV_lambda)-1
H_CIV = (H/CIV_lambda)-1
K_CIV = (K/CIV_lambda)-1
        
u_MgII = (u/MgII_lambda)-1
g_MgII = (g/MgII_lambda)-1
r_MgII = (r/MgII_lambda)-1
i_MgII = (i/MgII_lambda)-1
z_MgII = (z/MgII_lambda)-1
Y_MgII = (Y/MgII_lambda)-1
J_MgII = (J/MgII_lambda)-1
H_MgII = (H/MgII_lambda)-1
K_MgII = (K/MgII_lambda)-1

u_Halpha = (u/Halpha_lambda)-1
g_Halpha = (g/Halpha_lambda)-1
r_Halpha = (r/Halpha_lambda)-1
i_Halpha = (i/Halpha_lambda)-1
z_Halpha = (z/Halpha_lambda)-1
Y_Halpha = (Y/Halpha_lambda)-1
J_Halpha = (J/Halpha_lambda)-1
H_Halpha = (H/Halpha_lambda)-1
K_Halpha = (K/Halpha_lambda)-1

print('\n')
print('Lyman-alpha enters u-band at redshift' , "%6.3f" % u_Lya[0], 'and exits at ', "%6.3f" % u_Lya[-1])
print('Lyman-alpha enters g-band at redshift' , "%6.3f" % g_Lya[0], 'and exits at ', "%6.3f" % g_Lya[-1])
print('Lyman-alpha enters r-band at redshift' , "%6.3f" % r_Lya[0], 'and exits at ', "%6.3f" % r_Lya[-1])
print('Lyman-alpha enters i-band at redshift' , "%6.3f" % i_Lya[0], 'and exits at ', "%6.3f" % i_Lya[-1])
print('Lyman-alpha enters z-band at redshift' , "%6.3f" % z_Lya[0], 'and exits at ', "%6.3f" % z_Lya[-1])
print('Lyman-alpha enters Y-band at redshift' , "%6.3f" % Y_Lya[0], 'and exits at ', "%6.3f" % Y_Lya[-1])
print('Lyman-alpha enters J-band at redshift' , "%6.3f" % J_Lya[0], 'and exits at ', "%6.3f" % J_Lya[-1])
print('Lyman-alpha enters H-band at redshift' , "%6.3f" % H_Lya[0], 'and exits at ', "%6.3f" % H_Lya[-1])
print('Lyman-alpha enters K-band at redshift' , "%6.3f" % K_Lya[0], 'and exits at ', "%6.3f" % K_Lya[-1], '\n')

print('Carbon-IV enters u-band at redshift' , "%6.3f" % u_CIV[0], 'and exits at ', "%6.3f" % u_CIV[-1])
print('Carbon-IV enters g-band at redshift' , "%6.3f" % g_CIV[0], 'and exits at ', "%6.3f" % g_CIV[-1])
print('Carbon-IV enters r-band at redshift' , "%6.3f" % r_CIV[0], 'and exits at ', "%6.3f" % r_CIV[-1])
print('Carbon-IV enters i-band at redshift' , "%6.3f" % i_CIV[0], 'and exits at ', "%6.3f" % i_CIV[-1])
print('Carbon-IV enters z-band at redshift' , "%6.3f" % z_CIV[0], 'and exits at ', "%6.3f" % z_CIV[-1])
print('Carbon-IV enters Y-band at redshift' , "%6.3f" % Y_CIV[0], 'and exits at ', "%6.3f" % Y_CIV[-1])
print('Carbon-IV enters J-band at redshift' , "%6.3f" % J_CIV[0], 'and exits at ', "%6.3f" % J_CIV[-1])
print('Carbon-IV enters H-band at redshift' , "%6.3f" % H_CIV[0], 'and exits at ', "%6.3f" % H_CIV[-1])
print('Carbon-IV enters K-band at redshift' , "%6.3f" % K_CIV[0], 'and exits at ', "%6.3f" % K_CIV[-1], '\n')

print('Mg-II enters u-band at redshift' , "%6.3f" % u_MgII[0], 'and exits at ', "%6.3f" % u_MgII[-1])
print('Mg-II enters g-band at redshift' , "%6.3f" % g_MgII[0], 'and exits at ', "%6.3f" % g_MgII[-1])
print('Mg-II enters r-band at redshift' , "%6.3f" % r_MgII[0], 'and exits at ', "%6.3f" % r_MgII[-1])
print('Mg-II enters i-band at redshift' , "%6.3f" % i_MgII[0], 'and exits at ', "%6.3f" % i_MgII[-1])
print('Mg-II enters z-band at redshift' , "%6.3f" % z_MgII[0], 'and exits at ', "%6.3f" % z_MgII[-1])
print('Mg-II enters Y-band at redshift' , "%6.3f" % Y_MgII[0], 'and exits at ', "%6.3f" % Y_MgII[-1])
print('Mg-II enters J-band at redshift' , "%6.3f" % J_MgII[0], 'and exits at ', "%6.3f" % J_MgII[-1])
print('Mg-II enters H-band at redshift' , "%6.3f" % H_MgII[0], 'and exits at ', "%6.3f" % H_MgII[-1])
print('Mg-II enters K-band at redshift' , "%6.3f" % K_MgII[0], 'and exits at ', "%6.3f" % K_MgII[-1], '\n')

print('H-alpha enters u-band at redshift' , "%6.3f" % u_Halpha[0], 'and exits at ', "%6.3f" % u_Halpha[-1])
print('H-alpha enters g-band at redshift' , "%6.3f" % g_Halpha[0], 'and exits at ', "%6.3f" % g_Halpha[-1])
print('H-alpha enters r-band at redshift' , "%6.3f" % r_Halpha[0], 'and exits at ', "%6.3f" % r_Halpha[-1])
print('H-alpha enters i-band at redshift' , "%6.3f" % i_Halpha[0], 'and exits at ', "%6.3f" % i_Halpha[-1])
print('H-alpha enters z-band at redshift' , "%6.3f" % z_Halpha[0], 'and exits at ', "%6.3f" % z_Halpha[-1])
print('H-alpha enters Y-band at redshift' , "%6.3f" % Y_Halpha[0], 'and exits at ', "%6.3f" % Y_Halpha[-1])
print('H-alpha enters J-band at redshift' , "%6.3f" % J_Halpha[0], 'and exits at ', "%6.3f" % J_Halpha[-1])
print('H-alpha enters H-band at redshift' , "%6.3f" % H_Halpha[0], 'and exits at ', "%6.3f" % H_Halpha[-1])
print('H-alpha enters K-band at redshift' , "%6.3f" % K_Halpha[0], 'and exits at ', "%6.3f" % K_Halpha[-1], '\n')
