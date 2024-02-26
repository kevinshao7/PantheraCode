import numpy as np
import matplotlib.pyplot as plt
from Classes import Fins, Body, Nosecone
from aero_coefficients import *
from forces import C_N_force, F_fin_N
from globalvariables import *
from FlightProfileDataRASAero import *


#####
start1 = 0   
end1 = 1700
step1 = 2
####

def fin_F_array(angle_attack_force_run:float,test_fins:Fins,test_body:Body, start1, end1, step1):  #indexes of excel sheet
  """
    Returns the fin forces

    Parameters
    ----------
    angle_attack_force_run : float
      angle of attack
    test_fins : Fin Object
      fin
    test_fins : Body Object
      body
    start1 : int
      start index of csv
    end1 : int
      end index of csv
    step1 : int
      step index of csv

    Returns t_trunc_array, f_trunc_array, max(f_list), cna, h_trunc_array, angles
    -------
    t_trunc_array : float array
      truncated time array
    f_trunc_array : float
      vertical distance from the leading edge at the top of the MAC to the top point of the fin
    max(f_list) : float
      maximum fin force 
    cna : float array
      normal coefficient array
    h_trunc_array : float array
      truncated altitude array
    angles : float array
      angle of attack array in degrees
  """
  f_list = []
  cna = []
  angles = []
  t_trunc_array = np.array(time_array[start1:end1:step1]) #truncated time array
  h_trunc_array = np.array(z_array[start1:end1:step1]) #truncated height array
  for i in range(start1, end1, step1):
      if i>5:
        angle_attack_wind = (180/np.pi)*np.arctan(5/vz_array[i]) #assume 5m/s crosswind at all altitudes
      else:
          angle_attack_wind = angle_attack_force_run #Angle of attack off of launch
      angles.append(angle_attack_wind)
      beta1 = np.sqrt(abs((mach_array[i])**2 - 1))
      if mach_array[i]<0.8:
          Normal_coeff1 = CNalphaN_subs(N_fins, test_fins.fin_span, test_body.Arearef(), test_fins.area(), beta1, test_fins.fin_gamma())
      elif 0.8 < mach_array[i] <1.2:
          Normal_coeff1 = CNalphaN_trans(N_fins, test_fins.fin_span, test_body.Arearef(), test_fins.area(), mach_array[i], test_fins.fin_gamma(), angle_attack_wind )
      elif mach_array[i] >= 1.2:
          Normal_coeff1 = CNalphaN_super(N_fins, test_body.Arearef(), test_fins.area(), beta1, angle_attack_wind) #FORCES ONLY VALID FOR SUPERSONIC HERE
      cna.append(Normal_coeff1)
      cn_force = C_N_force(Normal_coeff1, (angle_attack_wind * np.pi/180))
      fin_force1 = F_fin_N(cn_force, density_array[i] , test_fins.area(), vz_array[i])   #0 deg prelim flight used here so only vz to consider. #0.315
      f_list.append(fin_force1)
  f_trunc_array = np.array(f_list)
  return t_trunc_array, f_trunc_array, max(f_list), cna, h_trunc_array, angles

def mach_to_times(mach_array:np.array,time_array:np.array):
  """
  Identifies times associated with certain mach numbers

    Parameters
    ----------
    mach_array : numpy array
    mach numbers during flight
    time_array : numpy array
    times during flight

    Returns 
    -------
    2D array, left column mach numbers, right column time at which mach number achieved
  """
  run = True
  currentmach = 0.5
  mach_to_times_arr = [[0,0]]
  for i in range(len(mach_array)):
    for j in range(1,8):
        if abs(mach_array[i] -j*0.5) < 0.01 and j*0.5 != mach_to_times_arr[len(mach_to_times_arr)-1][0]:
          mach_to_times_arr.append([j*0.5,time_array[i]])
          break
  return np.array(mach_to_times_arr)    
    
      
    

def fin_F_plotter(test_fins: Fins,test_body:Body):
  """
  Plots the fin forces

    Parameters
    ----------
    test_fins : Fin object
    test_body : Body object

    Returns 
    -------
    none, just plots
  """
  t_plot, f_plot, max_f, cna_plot, h_plot, ang_plot = fin_F_array(angle_attack_force_run,test_fins,test_body, start1, end1, step1)
  print(f'Max Fin Force is {max_f/1000} kN, Fin area of {test_fins.area()}m^2')
  #print(f'Chord_root, fin_span, Chord_tip, sweep_length, body_radius: {test_fins.Chord_root(), test_fins.fin_span(), test_fins.Chord_tip(), test_fins.sweep_length, test_fins.body_radius()}')
  #Print Normal Force on fins as function of time
  plt.plot(t_plot, f_plot/1000, label = 'Normal Force on Fin') #conversion to kN
  plt.xlabel('Time(s)')
  plt.ylabel('Total Fin force /kN')
  plt.title(f'Angle of Attack is {angle_attack_force_run} degrees')
  color_array=np.zeros(len(mach_array))
  for i in range(len(mach_array)):
      if mach_array[i]<0.8:
          color_array[i]=0
      elif mach_array[i]<1.2:
          color_array[i]=1
      elif mach_array[i]<5:
          color_array[i] = 2
      else:
          color_array[i] = 3
  colors = ['grey','green','orange','red']
  labels = ['Subsonic M<0.8','Transonic 0.8<M<1.2','Supersonic 1.2<M<5','Hypersonic M>5']
  for i in range(len(color_array)-1):
      if color_array[i] != color_array[i+1]:
          plt.axvline(time_array[i], color = colors[int(color_array[i])], label = labels[int(color_array[i])], linestyle = '-')
          plt.axvline(time_array[i+1], color = colors[int(color_array[i+1])], label = labels[int(color_array[i+1])], linestyle = '--')
  plt.ylim(0, (max_f+10)/1000)
  plt.legend()
  plt.show()
  #Plot Normal Force on Fin as function of time
  plt.plot(h_plot/1000, f_plot/1000, label = 'Normal Force on Fin') #conversion to kN
  plt.xlabel('Altitude (km)')
  plt.ylabel('Total Fin force /kN')
  plt.title(f'Angle of Attack is {angle_attack_force_run} degrees')
  plt.ylim(0, (max_f+10)/1000)
  plt.legend()
  plt.show()
  #Plot Normal Force Coefficient as function of time
  plt.plot(t_plot[0:end1:1], cna_plot[0:end1:1], label = 'CNalpha per rad')
  plt.title("Normal Coefficient CN")
  mach_to_timesarr=mach_to_times(mach_array)
  colors = ['blue','green','yellow','orange','red','purple','black']
  for i in range(len(mach_to_timesarr)):
    plt.axvline(mach_to_timesarr[i,1], color = colors[int(2*mach_to_timesarr[i,0])], label = f'Mach {mach_to_timesarr[i,0]}', linestyle = 'dotted')
  plt.legend()
  plt.show()
  #Plot angle of attack as function of time
  plt.xlabel('Time (s)')
  plt.ylabel('Angle of Attack')
  plt.title(f'Angle of Attack is {angle_attack_force_run} degrees')
  plt.plot(t_plot, ang_plot)
  plt.show()
    
def wind_lookup(alti): #Legacy code from Griffin, not yet modified for Panthera as of Feb 24, 2024
  """
  Finds crosswind as function of altitude

    Legacy code from Griffin, not yet modified for Panthera as of Feb 25, 2024
    ----------
  """
  #multiple datasets. seems to vary wind vs altitude so much over a year and location
  #max launch wind speed of 5.8m/s
  p = 7
  alts = [0, 2, 5, 7, 10, 12, 15, 17, 20, 25, 30, 35, 40]
  alt_windspeed=[5.8, 25, 35, 55, 65, 45, 35, 25, 20, 21, 30, 40, 50] #corresponding to Spokane, WA autumn
  alt_windspeed=[5.8, 11, 15, 21, 25, 15, 11, 9, 8, 10, 11, 15, 25] #NL avg
  coeffic=np.polyfit(alts, alt_windspeed, p)
  equ = np.poly1d(coeffic)
  #plt.plot(alts, alt_windspeed, label = 'Wind data')
  test_alts = np.array(np.linspace(0,40000,100))
  test_wind = [1.5*equ(a/1000) for a in test_alts ]
  #plt.plot(test_alts/1000, test_wind, label = 'Curve fitted data + safety factor')
  #plt.ylabel('Wind (m/s)')
  #plt.xlabel('Altitude (km)')
  #plt.legend()
  #plt.show()
  wind_s = 1.5*equ(alti/1000)
  #print(wind_s)
  return wind_s

if __name__ == "__main__":
  fin_F_plotter()