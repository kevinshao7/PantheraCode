from Stability_and_COM_Kevin import stability_check
from FinForcePlotter import fin_F_plotter
from flutter import *
from Classes import Fins,Body,Nosecone
from globalvariables import *

############## INITIALIZE STRUCTURES ###################
Bodyone = Body(Body_dia, Body_len)
Cone = Nosecone(Nosecone_length)
Fin = Fins(0.207,0.066,0.036,0,Body_dia/2) 
#More parameters in file globalvariables

############## FIN FORCES ###################
fin_F_plotter(Fin,Bodyone)

############## STABILITY AND CENTRE OF PRESSURE ###################
#array length 11 of rasaero cops from mach 0,0.5....5 (in inches as given in software)
cops=[54.11,54.11,55.52,55.71,54.09,52.15,50.05,48,46.29,44.8,43.57]
t=32.8 #choose t to also find stability value at time t printed in terminal
p=4   #degree of polynomial to fit COPs to. needs to accurately extrapolate from mach 5 to 5.5
# stability_check(cops,t,p)

############## FIN FLUTTER ###################   
noncomp_switch = True
sf_switch = True    #Change to turn safety factor line plots on and off. edit fin dimensions and stuff in flutter file.
sf = 1.2              #safety factor for sim
sf2 = 0.8             #sf multiplier for crit
print(f'Skin Shear Modulus: {Gs/1e9}GPa, Root chord of {cr}m, Tip chord of {ct}m, Fin Span of {ss}m, Thickness of {th}m, Skin thickness of {ths}m, Core thickness of {thc}m, composite mass of {compm}, freqs are sol {solf} and comp {compf} Hz')
#flutt_plot(sf, sf2, sf_switch, noncomp_switch)
####