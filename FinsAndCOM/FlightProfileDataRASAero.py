import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from ambiance import Atmosphere

df = pd.read_csv("FinsAndCOM\Flight_Test_RASAeroII.CSV")
#Time (sec),Stage,Stage Time (sec),Mach Number,Angle of Attack (deg),0-4
#CD,CL,Thrust (lb),Weight (lb),Drag (lb),5-9
#Lift (lb),CG (in),CP (in),Stability Margin (cal),Accel (ft/sec^2), 10-14
#Accel-V (ft/sec^2),Accel-H (ft/sec^2),Velocity (ft/sec),Vel-V (ft/sec),Vel-H (ft/sec), 15-19
#Pitch Attitude (deg),Flight Path Angle (deg),Altitude (ft),Distance (ft) #20-23

time_array = np.array(df.iloc[:, 0])
mach_array = np.array(df.iloc[:,3])
x_array = np.array(df.iloc[:, 23])*0.3048 #convet ft to m
y_array = np.zeros(len(x_array))
z_array = np.array(df.iloc[:, 22])*0.3048
vx_array = np.array(df.iloc[:, 19])*0.3048 #convert ft/s to m/s
vy_array = np.zeros(len(vx_array))
vz_array = np.array(df.iloc[:, 18])*0.3048
ax_array = np.array(df.iloc[:, 16])*0.3048 #convert ft/s^2 to m/s^2
ay_array = np.zeros(len(ax_array))
az_array = np.array(df.iloc[:, 15])*0.3048
# q_array = np.array(df.iloc[:, 15])


# e0_array = np.array(df.iloc[:, 10])
# e1_array = np.array(df.iloc[:, 11])
# e2_array = np.array(df.iloc[:, 12])
# e3_array = np.array(df.iloc[:, 13])

atmosphere = Atmosphere(z_array)
pressure_array = atmosphere.pressure
density_array = atmosphere.density
q_array = density_array*(np.array(df.iloc[:,17])**2)/2



# velocity_array = np.array([np.linalg.norm([vx_array[a], vy_array[a], vz_array[a]]) for a in range(len(vx_array))])
# plt.plot(time_array, vz_array)
# plt.show()
# accel_array = np.array(np.linalg.norm(ax_array[a], ay_array[a], az_array[a]))