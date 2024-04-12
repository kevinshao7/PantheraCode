import numpy as np
import matplotlib.pyplot as plt
from Classes import *
from globalvariables import *

startf, endf, stepf = 0,np.argmin(np.abs(time_array-15)), 1

def flutterer(Gs, cr, ct, ss, th, ths, thc, startf, endf, stepf, solf, compf, solm, compm):
    #ss, cr, ct, th, ths, thc = ss*39.37, cr*39.37, ct*39.37, th*39.37, ths*39.37, thc*39.37
    #Ge = Gs #* 0.000145038 #effective shear modulus. Unsure how actually behaves with sandwich panel behaviour.
    area = 0.5 * (cr + ct) * ss
    AR = ss**2 / area #Aspect ratio
    lam = ct/cr #Lamda, taper ratio, tip chord/root chord
    critMJ = []
    critmach_noncomp = []
    critmach_noncomptaper = []
    mach_f_array = np.array(mach_array[startf:endf:stepf])
    t_f_array = np.array(time_array[startf:endf:stepf])
    for j in range(startf, endf, stepf): #Calculations from NACA Technical Note 4197 https://ntrs.nasa.gov/api/citations/19930085030/downloads/19930085030.pdf
        X_flut = (39.3*AR**3)/((th/cr)**3 * 1/(AR+2)) #"Nondimensional" geometric parameter, has units of psi
        X_flut = X_flut*6894.76 #Convert X_flut to pascals
        #Gs is shear modulus, convert to psi
        critmachnoncomp_toadd = np.sqrt(Gs/((pressure_array[j]/101325)*((lam+1)/2)*X_flut))
        critmach_noncomp.append(critmachnoncomp_toadd)
        f1 = 1+1.87*(1-lam)**(1.6)
        critmach_noncomptaper.append(critmachnoncomp_toadd*f1)
        #Below is composite material, not currently implemneted
    #     critMJ_toadd = np.sqrt(Gs*0.000145038/((pressure_array[j]/101325)*((lam+1)/2)*X_flut))*(compf/solf)*(np.sqrt(solm/compm))
    #     critMJ.append(critMJ_toadd)
    # critMJ_array = np.array(critMJ)
    critMJ_array = None
    return mach_f_array, t_f_array, critMJ_array, critmach_noncomp, critmach_noncomptaper

def flutt_plot(sf, sf2, sf_switch, noncomp_switch): #sf is safety factor
    mach_fplot, t_plotf, critMJ_plot, critmach_noncomp, critmach_noncomptaper = flutterer(Gs, cr, ct, ss, th, ths, thc, startf, endf, stepf, solf, compf, solm, compm)
    print(f'{mach_fplot[0::200]} read this to check mach values plot correctly')
    plt.plot(t_plotf, mach_fplot, label = 'Simulated actual Mach', color = 'red')
    if sf_switch == True:    
        plt.plot(t_plotf, mach_fplot*sf, label = f'Simulated with safety factor of {sf}', color = 'red', linestyle = 'dotted')
        #plt.plot(t_plotf, critMJ_plot*sf2, label = f'Simulated with sf of {sf2}', color = 'blue', linestyle = 'dotted')
    if noncomp_switch == True:
        plt.plot(t_plotf, critmach_noncomp, label = 'Critical Mach', color = 'black')
        #plt.plot(t_plotf, critmach_noncomptaper, label = 'Crit solid Mach, taper experiment', color = 'black', linestyle = 'dotted')
    #plt.plot(t_plotf, critMJ_plot, label = 'Critical Mach (NACA 4197)', color = 'blue')
    """ Finsim not currently implemented for Panthera as of February 25, 2024
    finsim_points = [2.25, 2.52, 2.83, 3.19, 3.62, 4.13, 4.75, 5.5] #flutter #difference in atmospheric model note.
    #finsim_points = [1.69, 1.89, 2.12, 2.39, 2.71, 3.1, 3.56, 4.12] # divergence
    finsim_ts = [0, 7.41, 11.52, 14.94, 17.77, 20.26, 22.45, 24.42 ] #this is to validate solid model analysis as a lower bound #naca 4197 composite correction is employed for other
    for i in range(0,len(finsim_points)):
        plt.plot(finsim_ts[i],finsim_points[i],marker='o',markeredgecolor="yellow", markerfacecolor="purple", label = f'{i*6000}ft altitude. Flutter V')
    print('Note that if fin design is changed, these points from FinSim need to be updated. This was just to ensure FinSim and code were in agreement for analysis on flutter')

    """
    plt.title("Fin Flutter Analysis")
    plt.xlabel('Time (s)')
    plt.ylabel('Mach number')
    plt.legend()
    plt.show()
    #Below is simulation for fin tapering, not relevant for Panthera
    # safety_plot = [critmach_noncomptaper[a]/mach_fplot[a] for a in range(len(critMJ_plot))]
    # plt.plot(t_plotf[startf+500:endf-600:stepf], safety_plot[startf+500:endf-600:stepf])
    # plt.title('Safety factor for taper simulating')
    # plt.xlabel("Time (s)")
    # plt.ylabel("Safety Factor")
    # plt.show()
    # print(f'Safety check: Max mach number in array is: {max(mach_fplot)}')

if __name__ == "__main__":
    from FlightProfileDataRASAero import *
    Gs = 30e9 #Shear Modulus Fibreglass, Pa https://www.azom.com/properties.aspx?ArticleID=764
    cr =  0.267
    ct = 0.0457
    ss =  0.086
    th = 7e-3
    ths = 0
    solf = None
    compf =None
    solm = None
    compm= None 
    thc = th - 2 * ths    # edit above as appropriate. 
    sf = 1.2
    sf2 = 2
    sf_switch = True
    noncomp_switch = True
    startf, endf, stepf = 0,4000, 1
    flutt_plot(sf, sf2, sf_switch, noncomp_switch)