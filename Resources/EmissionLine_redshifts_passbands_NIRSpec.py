#!/usr/bin/env python
'''
Python code to figure out/state when various (quasar) emission lines 
move in and out of various SDSS/UKIDSS/WISE and JWST passbands
'''

import numpy as np

np.set_printoptions(precision=3)

## https://jwst-docs.stsci.edu/display/JTI/NIRSpec+Dispersers+and+Filters
G140H_F070LP = np.array([0.81,  1.00,  1.27])
G140H_F100LP = np.array([0.97,  1.20,  1.82])
G235H_F170LP = np.array([1.66,  2.00,  3.05])
G395H_F290LP = np.array([2.87,  1.00,  5.14])

## VdB01, Table 2, lambda_lab
Lya_lambda    = 0.121567
CIV_lambda    = 0.154906        
MgII_lambda   = 0.279875
Halpha_lambda = 0.656461

G140H_F070LP_Lya = (G140H_F070LP/Lya_lambda)-1
G140H_F100LP_Lya = (G140H_F100LP/Lya_lambda)-1
G235H_F170LP_Lya = (G235H_F170LP/Lya_lambda)-1
G395H_F290LP_Lya = (G395H_F290LP/Lya_lambda)-1

G140H_F070LP_CIV = (G140H_F070LP/CIV_lambda)-1
G140H_F100LP_CIV = (G140H_F100LP/CIV_lambda)-1
G235H_F170LP_CIV = (G235H_F170LP/CIV_lambda)-1
G395H_F290LP_CIV = (G395H_F290LP/CIV_lambda)-1
        
G140H_F070LP_MgII = (G140H_F070LP/MgII_lambda)-1
G140H_F100LP_MgII = (G140H_F100LP/MgII_lambda)-1
G235H_F170LP_MgII = (G235H_F170LP/MgII_lambda)-1
G395H_F290LP_MgII = (G395H_F290LP/MgII_lambda)-1

G140H_F070LP_Halpha = (G140H_F070LP/Halpha_lambda)-1
G140H_F100LP_Halpha = (G140H_F100LP/Halpha_lambda)-1
G235H_F170LP_Halpha = (G235H_F170LP/Halpha_lambda)-1
G395H_F290LP_Halpha = (G395H_F290LP/Halpha_lambda)-1

print('\n')
print('Lyman-alpha enters G140H/F070LP at redshift' , "%6.3f" % G140H_F070LP_Lya[0], 'and exits at ', "%6.3f" % G140H_F070LP_Lya[-1])
print('Lyman-alpha enters G140H/F100LP at redshift' , "%6.3f" % G140H_F100LP_Lya[0], 'and exits at ', "%6.3f" % G140H_F100LP_Lya[-1])
print('Lyman-alpha enters G235H/F170LP at redshift' , "%6.3f" % G235H_F170LP_Lya[0], 'and exits at ', "%6.3f" % G235H_F170LP_Lya[-1])
print('Lyman-alpha enters G395H/F290LP at redshift' , "%6.3f" % G395H_F290LP_Lya[0], 'and exits at ', "%6.3f" % G395H_F290LP_Lya[-1])

print('Carbon-IV enters G140H/F070LP at redshift' , "%6.3f" % G140H_F070LP_CIV[0], 'and exits at ', "%6.3f" % G140H_F070LP_CIV[-1])
print('Carbon-IV enters G140H/F100LP at redshift' , "%6.3f" % G140H_F100LP_CIV[0], 'and exits at ', "%6.3f" % G140H_F100LP_CIV[-1])
print('Carbon-IV enters G235H/F170LP at redshift' , "%6.3f" % G235H_F170LP_CIV[0], 'and exits at ', "%6.3f" % G235H_F170LP_CIV[-1])
print('Carbon-IV enters G395H/F290LP at redshift' , "%6.3f" % G395H_F290LP_CIV[0], 'and exits at ', "%6.3f" % G395H_F290LP_CIV[-1])

print('Mg-II enters G140H/F070LP at redshift' , "%6.3f" % G140H_F070LP_MgII[0], 'and exits at ', "%6.3f" % G140H_F070LP_MgII[-1])
print('Mg-II enters G140H/F100LP at redshift' , "%6.3f" % G140H_F100LP_MgII[0], 'and exits at ', "%6.3f" % G140H_F100LP_MgII[-1])
print('Mg-II enters G235H/F170LP at redshift' , "%6.3f" % G235H_F170LP_MgII[0], 'and exits at ', "%6.3f" % G235H_F170LP_MgII[-1])
print('Mg-II enters G395H/F290LP at redshift' , "%6.3f" % G395H_F290LP_MgII[0], 'and exits at ', "%6.3f" % G395H_F290LP_MgII[-1])

print('H-alpha enters G140H/F070LP at redshift' , "%6.3f" % G140H_F070LP_Halpha[0], 'and exits at ', "%6.3f" % G140H_F070LP_Halpha[-1])
print('H-alpha enters G140H/F100LP at redshift' , "%6.3f" % G140H_F100LP_Halpha[0], 'and exits at ', "%6.3f" % G140H_F100LP_Halpha[-1])
print('H-alpha enters G235H/F170LP at redshift' , "%6.3f" % G235H_F170LP_Halpha[0], 'and exits at ', "%6.3f" % G235H_F170LP_Halpha[-1])
print('H-alpha enters G395H/F290LP at redshift' , "%6.3f" % G395H_F290LP_Halpha[0], 'and exits at ', "%6.3f" % G395H_F290LP_Halpha[-1])
