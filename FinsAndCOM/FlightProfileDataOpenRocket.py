import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from ambiance import Atmosphere

df = pd.read_csv("FinsAndCOM\Flight_Test_OpenRocket_Panthera0.6.csv",comment="#")

# Time (s),Altitude (m),Vertical velocity (m/s),Vertical acceleration (m/s²),Total velocity (m/s),
#Total acceleration (m/s²),Position East of launch (m),Position North of launch (m),Lateral distance (m),Lateral direction (°),
#Lateral velocity (m/s),Lateral acceleration (m/s²),Latitude (°),Longitude (°),Gravitational acceleration (m/s²),
#Angle of attack (°),Roll rate (°/s),Pitch rate (°/s),Yaw rate (°/s),Mass (g),
#Motor mass (g),Longitudinal moment of inertia (kg·m²),Rotational moment of inertia (kg·m²),CP location (cm),CG location (cm),
#Stability margin calibers (​),Mach number (​),Reynolds number (​),Thrust (N),Drag force (N),
#Drag coefficient (​),Axial drag coefficient (​),Friction drag coefficient (​),Pressure drag coefficient (​),Base drag coefficient (​),
#Normal force coefficient (​),Pitch moment coefficient (​),Yaw moment coefficient (​),Side force coefficient (​),Roll moment coefficient (​),
#Roll forcing coefficient (​),Roll damping coefficient (​),Pitch damping coefficient (​),Coriolis acceleration (m/s²),Reference length (cm),
#Reference area (cm²),Vertical orientation (zenith) (°),Lateral orientation (azimuth) (°),Wind velocity (m/s),Air temperature (°C),
#Air pressure (mbar),Speed of sound (m/s),Simulation time step (s),Computation time (s)

###All in SI Units
time_array = np.array(df.iloc[:, 0])
z_array = np.array(df.iloc[:, 1])
vz_array = np.array(df.iloc[:, 2])
az_array = np.array(df.iloc[:, 3])
v_array = np.array(df.iloc[:, 4])
a_array = np.array(df.iloc[:, 5])
x_array = np.array(df.iloc[:, 6])
y_array = np.array(df.iloc[:, 7])
l_array = np.array(df.iloc[:, 8]) #lateral position
vl_array = np.array(df.iloc[:, 10])
al_array = np.array(df.iloc[:, 11])
mass_array = np.array(df.iloc[:,19])
mach_array = np.array(df.iloc[:, 26])
area_array = np.array(df.iloc[:, 45])/1e4 #Convert cm2 to m2
pressure_array = np.array(df.iloc[:, 50])*100 #Convert mbar to Pa
atmosphere = Atmosphere(z_array)
density_array = atmosphere.density
q_array = density_array*(np.array(v_array)**2)/2
angleattack_array = np.array(df.iloc[:, 15])

# ax_array = np.array(df.iloc[:, 7])
# ay_array = np.array(df.iloc[:, 8])
if __name__ == "__main__":
    plt.figure()
    plt.plot(time_array,angleattack_array)
    plt.xlabel("Time After Ignition (s)")
    plt.ylabel("Angle of Attack (Degrees)")
    plt.title("Angle of Attack vs Time")
    plt.show()
#plot angle of attack
#take angle of attack from openrocket data