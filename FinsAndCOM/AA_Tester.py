from Stability_and_COMs import stability_check
from FinForcePlotter import fin_F_plotter
from flutter import *

####FIN NORMAL FORCE
fin_F_plotter()

####STABILITY, center of pressure
cops=[294.25,294.25,297.69,307.6,303.52,295.8,287.78,279.91,272.21,264.68,257.52]#array length 11 of rasaero cops from mach 0,0.5....5 (in inches as given in software)

t=32.8           #choose t to also find stability value at time t printed in terminal
p=3              #degree of polynomial to fit COPs to. needs to accurately extrapolate from mach 5 to 5.5

stability_check(cops,t,p)
####

####FLUTTER    
noncomp_switch = True
sf_switch = True    #Change to turn safety factor line plots on and off. edit fin dimensions and stuff in flutter file.
sf = 1.2              #safety factor for sim
sf2 = 0.8             #sf multiplier for crit

print(f'Skin Shear Modulus: {Gs/1e9}GPa, Root chord of {cr}m, Tip chord of {ct}m, Fin Span of {ss}m, Thickness of {th}m, Skin thickness of {ths}m, Core thickness of {thc}m, composite mass of {compm}, freqs are sol {solf} and comp {compf} Hz')
flutt_plot(sf, sf2, sf_switch, noncomp_switch)
####