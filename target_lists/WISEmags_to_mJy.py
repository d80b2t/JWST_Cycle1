'''

http://wise2.ipac.caltech.edu/docs/release/allsky/expsup/sec4_4h.html
Table 1- Zero Magnitude Flux Density

Band    F_nu0     F^*_nu0
W1      309.540  306.6832 
W2      171.787  170.663
W3       31.674   29.045 
W4        8.363    8.283

'''

import numpy as np

##  Wright et al. (2010)
##  Table 1
##  Flux Corrections and Colors for Power Laws and Blackbodies
print()
print("Assuming F_nu ~ v^-2  power-law ")
print()

fc_W1 = 1.0000
fc_W2 = 1.0000
fc_W3 = 1.0000
fc_W4 = 1.0000

Fstar_nu0_W1 = 306.682
Fstar_nu0_W2 = 170.663
Fstar_nu0_W3 =  29.045
Fstar_nu0_W4 =   8.284


print()
direction = input("(1) Mags to Jy   or   (2) Jy to mags ?   ")
print()
which_band = input("Which band?   (1) WISE W1   (2) WISE W2   (3) WISE W3   (4) WISE W4  ")

print()
print(direction, which_band)


if direction == '1':
    print()
    print("Converting magnitude to Jy....")
    
    mag_system  = input(" (A) AB    or   (V) Vega ?")
    
    if mag_system == 'A':
        magnitude_AB = input(" AB magnitude? ")
        
        ## Converting AB to Vega
        ## (∆W1, ∆W2, ∆W3) = (2.673, 3.313, 5.148). For W4, we use the
        ##calibration of Brown et al. (2014), ∆W4= 6.66. These
        ## magnitudes are not Galactic extinction corrected.
        if which_band == '1': magnitude = float(magnitude_AB) - 2.673
        if which_band == '2': magnitude = float(magnitude_AB) - 3.313
        if which_band == '3': magnitude = float(magnitude_AB) - 5.148
        if which_band == '4': magnitude = float(magnitude_AB) - 6.66
            
    if mag_system == 'V':
        magnitude = input(" Vega magnitude? ")
        magnitude = float(magnitude)
        
    ##   O U T P U T S  ##
    print()
    if which_band == '1':
        F_in_Jy_W1 = (Fstar_nu0_W1 / fc_W1) * 10**(((-1.0)*(magnitude))/2.5)
        print("W1 Flux::   {:.4f} mJY ".format((F_in_Jy_W1*1000.0)))          
            
    if which_band == '2':
        F_in_Jy_W2 = (Fstar_nu0_W2 / fc_W2) * 10**(((-1.0)*(magnitude))/2.5)
        print("W2 Flux::   {:.4f} mJY ".format((F_in_Jy_W2*1000.0)))          

    if which_band == '2':
        F_in_Jy_W3 = (Fstar_nu0_W3 / fc_W3) * 10**(((-1.0)*(magnitude))/2.5)
        print("W3 Flux::   {:.4f} mJY ".format((F_in_Jy_W3*1000.0)))          

    if which_band == '4':
        F_in_Jy_W4 = (Fstar_nu0_W4/ fc_W4) * 10**(((-1.0)*(magnitude))/2.5)
        print("W4 Flux::   {:.4f} mJY ".format((F_in_Jy_W4*1000.0)))          

        

if direction == '2':
    print()
    print("Converting Jy to VEGA mags....")

    Flux_in    = input(" Flux in milliJanskys ?? ")
    Flux_in_Jy = float(Flux_in)/1e3
        
    ##   O U T P U T S  ##
    print()
    if which_band == '1':
        Vega_W1mag  = (-1.*2.5)* np.log10((Flux_in_Jy / (Fstar_nu0_W1 / fc_W1) ))
        AB_W1mag = Vega_W1mag + 2.673
        print("WISE W1 ::   {:.2f} mag Vega  ({:.2f} mag AB) ".format(Vega_W1mag, AB_W1mag))          
            
    if which_band == '2':
        Vega_W2mag  = (-1.*2.5)* np.log10((Flux_in_Jy / (Fstar_nu0_W2 / fc_W2) ))
        AB_W2mag = Vega_W2mag + 2.673
        print("WISE W2 ::   {:.2f} mag Vega  ({:.2f} mag AB) ".format(Vega_W2mag, AB_W2mag))          

    if which_band == '3':
        Vega_W1mag  = (-1.*2.5)* np.log10((Flux_in_Jy / (Fstar_nu0_W3 / fc_W3) ))
        AB_W3mag = Vega_W3mag + 2.673
        print("WISE W3 ::   {:.2f} mag Vega  ({:.2f} mag AB) ".format(Vega_W3mag, AB_W3mag))          
            
    if which_band == '4':
        Vega_W4mag  = (-1.*2.5)* np.log10((Flux_in_Jy / (Fstar_nu0_W4 / fc_W4) ))
        AB_W4mag = Vega_W4mag + 6.66
        print("WISE W4 ::   {:.2f} mag Vega  ({:.2f} mag AB) ".format(Vega_W4mag, AB_W4mag))          
