import numpy as np
from ambiance import Atmosphere
##### LAST UPDATE OF VARIABLES AND DESIGN ####
#March 11, 2024

############## CONSTANTS ##################
speed_sound = 343 #speed of sound, m/s shouldn't this be 343?

############## FLIGHT PROFILE DATA SOURCE ############
#RASAero:
#from FlightProfileDataRASAero import *
#flightdatasource = "RASAero"

#Open Rocket
#Open Rocket allows for variable angle of attack
from FlightProfileDataOpenRocket import *
flightdatasource="OpenRocket"
############## FLIGHT CHARACHTERISTICS ###################
start_mass = mass_array[0] #Wet mass, kg
end_mass = mass_array[-1] #Recovery Mass, kg
v_burnout = np.max(v_array) #Burnout velocity, m/s
max_q_velo = v_array[np.argmax(q_array)] #Velocity at Max-Q, m/s
max_q_alt = z_array[np.argmax(q_array)] #m
max_q_atmosphere = Atmosphere(np.array([max_q_alt]))
max_q_rho = max_q_atmosphere.density[0]
max_q_staticp = max_q_atmosphere.pressure[0]
p_atm = 94321.68 #Static pressure at launch, Pa
max_q_Mach = max_q_velo/speed_sound
max_q_beta = np.sqrt(abs(max_q_Mach**2 - 1))

############## ROCKET GEOMETRY ###################
Nosecone_length = 0.40 #Nosecone length
Body_dia = 0.0794 #body diameter in metres
Body_len = 1.36 #body tube length
CoM = 1.24 #for Panthera
total_length = Body_len+Nosecone_length
fineness = total_length/Body_dia

############## Material Properties ###################
#G_alu = 24E9 #Shear Modulus Aluminium, Pa
#G_alu_psi = 3.7e6 #Shear Modulus Aluminium, Psi
#density_alu = 2710 #Density Aluminium, kg/m3
G_alu = 79.3E9 #Shear Modulus Aluminium, Pa
G_alu_psi = 11.5e6 #Shear Modulus Aluminium, Psi
density_alu = 7850 #Density Aluminium, kg/m3 (already edited for steel here)

############## FIN PROPERTIES ###################
Roughness =3e-6 #body surface roughness - corresponding to a painted surface
N_fins = 4 #number of rocket fins
angle_attack = 3 #angle of attack for simulation of stability
angle_attack_force = 3 #angle of attack for simulation of stability, cannot be equal to zero
desired_stability = 2.5
angle_attack_force_run = 3 #Angle of attack right after launch
"""
Skin Shear Modulus: {Gs} Pa
Root chord of {cr}m
Tip chord of {ct}m
Fin Span of {ss}m
Thickness of {th}m
Skin thickness of {ths}m
Core thickness of {thc}m
composite mass of {compm}
freqs are sol {solf} and comp {compf} Hz'
Composites not implemented for Panthera
"""
Gs = 18e9
cr =  0.267
ct = 0.0457
ss =  0.0889
th = 5e-3
ths = 1e-3
solf = 588
compf =None
solm = 15.36
compm= None #torsion freqs (edited for Al here)
thc = th - 2 * ths
############## Centre of Pressure ###################
#array length 11 of rasaero cops from mach 0,0.5....3 (in inches as given in software)
cops=[49.21,54.11,55.52,55.71,54.09,52.15,50.05]


#Constant angle of attack
#Solidworks model