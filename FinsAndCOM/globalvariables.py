import numpy as np
from ambiance import Atmosphere
##### LAST UPDATE OF VARIABLES AND DESIGN ####
#February 25, 2024

############## CONSTANTS ##################
speed_sound = 343 #speed of sound, m/s shouldn't this be 343?

############## FLIGHT CHARACHTERISTICS ###################
start_mass = 7.5 #Wet mass, kg
end_mass = 5.2 #Recovery Mass, kg
v_burnout = 585 #Burnout velocity, m/s
max_q_velo = 580.03 #Velocity at Max-Q, m/s
#MaxQ occurs at 2095 feet
max_q_alt = 638.6 #m
max_q_atmosphere = Atmosphere(np.array([max_q_alt]))
max_q_rho = max_q_atmosphere.density[0]
max_q_staticp = max_q_atmosphere.pressure[0]
p_atm = 94321.68 #Static pressure at launch, Pa
max_q_Mach = max_q_velo/speed_sound
max_q_beta = np.sqrt(abs(max_q_Mach**2 - 1))

############## ROCKET GEOMETRY ###################
Nosecone_length = 0.231 #Nosecone length
Body_dia = 0.0794 #body diameter
Body_len = 1.0668 #body tube length
CoM = 0.842 #for Panthera
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
angle_attack = 0 #angle of attack for simulation of stability
angle_attack_force = 3 #angle of attack for simulation of stability, cannot be equal to zero
desired_stability = 2.5
angle_attack_force_run = 0.1 #Angle of attack right after launch

