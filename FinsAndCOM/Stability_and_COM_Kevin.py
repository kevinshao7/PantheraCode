import matplotlib.pyplot as plt
import numpy as np
class Section():
  def __init__(self, name, mass, start,length,uniform=True,COM=0,units="metric"):
    #mass, mass of part in grams/pounds
    #start, position from top of rocket of forwardmost surface of section
    #length, length of section
    #uniform variable indicates if radius of the section is the same (e.g. body tube is uniform but nosecone is not uniform)
    #if section not uniform, need to give center of mass in milimetres/inches
    self.name=name
    self.componenttype = "section"
    self.start = start
    self.length = length
    if units == "metric":
      self.mass = mass
      if uniform:
        self.COM = (2*start+length)/2
      else:
        self.COM = COM
    elif units == "imperial":
      self.mass = mass*453.592
      if uniform:
        self.COM = 25.4*(2*start+length)/2
      else:
        self.COM = COM*25.4
    else:
      print("Invalid units, choose \"metric\" (mm/kg) or \"imperial\" (in/lbs)")
    return

class Part():
  def __init__(self, name, mass,COM,units="metric"):
    #COM, distance from tip of nosecone along centerline to center of mass in milimetres/inches
    #mass, mass of part in grams/pounds
    self.name = name
    self.componenttype = "part"
    if units == "metric":
      self.mass = mass
      self.COM = COM
    elif units == "imperial":
      self.mass = mass*453.592
      self.COM = COM*25.4
    else:
      print("Invalid units, choose \"metric\" (mm/kg) or \"imperial\" (in/lbs)")
    return
def calculate_COM(partlist,units="metric",printresults=True,plot=True):
  #Compute center of mass by weighted average
  rocketCOM = 0
  rocketmass = 0
  rocketradius= 79.375/2
  for i in range(len(partlist)):
    rocketCOM += partlist[i].mass*partlist[i].COM
    rocketmass += partlist[i].mass
  rocketCOM = rocketCOM/rocketmass
  if printresults:
    if units == "metric":
      print(rocketCOM)
      print("Rocket Center of Mass From Nosecone Tip: "+str(rocketCOM)+" mm")
      print("Rocket Mass: "+str(rocketmass)+" g")
    elif units == "imperial":
      rocketCOM = rocketCOM/25.4
      rocketmass = rocketmass/453.592
      print("Rocket Center of Mass From Nosecone Tip: "+str(rocketCOM)+" in")
      print("Rocket Mass: "+str(rocketmass)+" lb")
    else:
      print("Invalid units, choose \"metric\" (mm/kg) or \"imperial\" (in/lbs)")
  if plot:
    plt.figure(figsize=(10,4))
    colors = plt.rcParams["axes.prop_cycle"].by_key()["color"]
    colors.extend(colors)
    if units=="metric":
      plt.xlabel("Position (milimetres)")
      plt.xticks(np.arange(0, 1700, step=100))
      for i in range(len(partlist)):
        if partlist[i].componenttype == "section":
          x = [partlist[i].start,partlist[i].start,partlist[i].start+partlist[i].length,partlist[i].start+partlist[i].length,partlist[i].start]
          y = [-rocketradius+i,rocketradius-i,rocketradius-i,-rocketradius+i,-rocketradius+i]
          plt.plot(x,y,color=colors[i])
          plt.scatter(partlist[i].COM,0,color=colors[i])
          plt.annotate(partlist[i].name, (partlist[i].COM,0),
          xytext=(partlist[i].COM+1,(20*i+1.2*rocketradius)*(-1)**i), textcoords='data', color=colors[i],
          arrowprops=dict(color=colors[i],width=0.1,headwidth=0.1),
          fontsize=10,
          horizontalalignment='left', verticalalignment='top')
        if partlist[i].componenttype == "part":
          plt.scatter(partlist[i].COM,0,color=colors[i])
          plt.annotate(partlist[i].name, (partlist[i].COM,0),
          xytext=(partlist[i].COM+1,(20*i+1.2*rocketradius)*(-1)**i), textcoords='data', color=colors[i],
          arrowprops=dict(color=colors[i],width=0.1,headwidth=0.1),
          fontsize=10,
          horizontalalignment='left', verticalalignment='top')
      plt.title("Rocket Mass: "+str(rocketmass)[:5]+" g")
      plt.scatter(rocketCOM,0,marker="x",color="black")
      plt.scatter(rocketCOM+rocketradius*4,0,marker="x",color="red")
      plt.annotate("COM+2 Calibres "+str(rocketCOM+rocketradius*4)[:5]+" mm", (rocketCOM+rocketradius*4,0),
      xytext=(rocketCOM+rocketradius*4,70), textcoords='data', color="red",
      arrowprops=dict(color='red',width=0.1,headwidth=0.1),
      fontsize=10,
      horizontalalignment='left', verticalalignment='top')
      plt.annotate('Rocket COM '+str(rocketCOM)[:5]+" mm", (rocketCOM,0),
            xytext=(rocketCOM+1,-70), textcoords='data',
            arrowprops=dict(color='black',width=0.1,headwidth=0.1),
            fontsize=10,
            horizontalalignment='left', verticalalignment='top')
    if units == "imperial":
      plt.xlabel("Position (inches)")
      plt.xticks(np.arange(0, 70, step=2))
      for i in range(len(partlist)):
        if partlist[i].componenttype == "section":
          x = [partlist[i].start,partlist[i].start,partlist[i].start+partlist[i].length,partlist[i].start+partlist[i].length,partlist[i].start]
          imperialx = [k / 25.4 for k in x]
          y = [-rocketradius+i,rocketradius-i,rocketradius-i,-rocketradius+i,-rocketradius+i]
          imperialy = [k / 25.4 for k in y]
          plt.plot(imperialx,imperialy,color=colors[i])
          plt.scatter(partlist[i].COM/25.4,0,color=colors[i])
          plt.annotate(partlist[i].name, (partlist[i].COM/25.4,0),
            xytext=(partlist[i].COM/25.4+1,(0.6*i+1.2*rocketradius/25.4)*(-1)**i), textcoords='data', color=colors[i],
            arrowprops=dict(color=colors[i],width=0.1,headwidth=0.1),
            fontsize=10,
            horizontalalignment='left', verticalalignment='top')
        if partlist[i].componenttype == "part":
          plt.scatter(partlist[i].COM/25.4,0,color=colors[i])
          plt.annotate(partlist[i].name, (partlist[i].COM/25.4,0),
            xytext=(partlist[i].COM/25.4+1,(0.6*i+1.2*rocketradius/25.4)*(-1)**i), textcoords='data', color=colors[i],
            arrowprops=dict(color=colors[i],width=0.1,headwidth=0.1),
            fontsize=10,
            horizontalalignment='left', verticalalignment='top')
      plt.title("Rocket Mass: "+str(rocketmass)[:5]+" lb")
      plt.scatter(rocketCOM,0,marker="x",color="black")
      plt.scatter(rocketCOM+rocketradius*4/25.4,0,marker="x",color="red")
      plt.annotate("COM+2 Calibres "+str(rocketCOM+rocketradius*4/25.4)[:5]+" in", (rocketCOM+rocketradius*4/25.4,0),
      xytext=(rocketCOM+rocketradius*4/25.4,7), textcoords='data', color="red",
      arrowprops=dict(color='red',width=0.1,headwidth=0.1),
      fontsize=10,
      horizontalalignment='left', verticalalignment='top')
      plt.annotate('Rocket COM '+str(rocketCOM)[:5]+" in", (rocketCOM,0),
            xytext=(rocketCOM+1,-7), textcoords='data',
            arrowprops=dict(color='black',width=0.1,headwidth=0.1),
            fontsize=10,
            horizontalalignment='left', verticalalignment='top')
    plt.axis("equal")
    plt.show()
  return rocketCOM, rocketmass

##### MY FUNCTION: PLOTS STABILITY AND COP VS 2 CAL POINT AND PRINTS STABILITY AT TIME T #######

#cops from RASAero for mach 0,0.5,1.0 .... 5.0
def stability_check(cops,t,p):
    if len(cops) != 11:
        raise ValueError("cops input must be length 11, with cops from 0,0.5.... 5 mach from rasaero")
    #machs=[0,0.5,1,1.5,2,2.5,3,3.5,4,4.5] find from data sheet the approx time corresponding 5.5 will be extrapolated
    mach_to_times=[0.00,3.81,7.26,11.03,15.94,19.64,22.52,25.36,27.74,29.79,31.65] #corresponding
    coeffs=np.polyfit(mach_to_times,cops,p)
    eq=np.poly1d(coeffs)
    t_com=np.linspace(0,35,10*35)
    y_cop=eq(t_com)
    coms=[]
    cals2 = []
    for j in range(len(t_com)):
        coms.append((9.64-calcCentreOfMass(t_com[j]))*39.37) #cop must be 2 cals below com
        cals2.append((9.64-calcCentreOfMass(t_com[j])+2*0.375)*39.37)
    calibers=(y_cop-coms)/(0.375*39.37)
    figure,axes1=plt.subplots(1,2)
    plt.tight_layout()
    axes1[0].plot(t_com,coms,color='red',label='COM')
    axes1[0].legend(loc='upper right')
    axes1[0].set_xlabel('Time(s)')
    axes1[0].set_ylabel('Distance from nose tip (inches)')
    axes1[0].plot(t_com,y_cop,color='green',label='C.O.P - ONLY VALID TO BLACK LINE')
    axes1[0].plot(t_com, cals2, color = 'red', label = '2 cal point', linestyle = 'dotted')
    axes1[0].axvline(32.82, color='black', label='mach 5.5 timestamp', linestyle = 'dotted')
    for i in range(0,len(cops)):
      axes1[0].plot(mach_to_times[i],cops[i],marker='o',markeredgecolor="yellow", markerfacecolor="purple")
    axes1[0].legend(loc='lower left')
    axes1[0].set_title('COP vs COM')
    if not 0<=t<=33.6:
      raise ValueError("time must be in range 0 to 33.6s")
    t_finder=round(10*t)
    stability_point=calibers[t_finder]
    print(f'Stability at time {round(t)} seconds is {stability_point} calibers.')
    axes1[1].plot(t_com,calibers,label='calibers of stability')
    axes1[1].axvline(32.82, color='black', label='mach 5.5/max speed time', linestyle = 'dotted')
    axes1[1].axhline(2, color = 'red', label = '2 cal point', linestyle = 'dotted')
    axes1[1].set_xlabel('Time(s)')
    axes1[1].set_ylabel('Calibers of stability')
    axes1[1].legend(loc='upper right')
    plt.title(f'Stability Analysis',loc='center')
    plt.show()

if __name__ == "__main__":
  #Below should reflect most recent Panthera design as of February 24, 2024
  bodylength = 1066.8 #mm
  noseconelength = 231.1
  bodydensity = 1100/1524 #g/mm, from https://eurospacetechnology.eu/index.php?id_product=1685&id_product_attribute=338&rewrite=g12-bodytube-30-60-inch&controller=product#/94-length-60_inch
  #Motor Model: Cesaroni 4864L2375-P
  #Motor Data Sheet: http://www.pro38.com/products/pro75/motor/MotorData.php?prodid=4864L2375-P
  motorlength = 621 #mm
  unburnedmotordensity = 4161/621 #g/mm
  burnedmotordensity = 1840/621 #g/mm
  couplerdensity = 260/381
  couplerlength = 200
  burnfraction =0
  unburnedlength = (1-burnfraction)*motorlength
  burnedlength = burnfraction*motorlength
  partlist = [ #mass, position
  Section("Body",bodydensity*(bodylength),noseconelength,bodylength),
  Section("Nosecone",bodydensity*noseconelength,0,noseconelength+40.7,uniform=False,COM=noseconelength*0.666),
  Section("Unburned Motor",(1-burnfraction)*motorlength*unburnedmotordensity,noseconelength+bodylength-unburnedlength,unburnedlength),
  Section("Burned Motor",burnfraction*motorlength*burnedmotordensity,noseconelength+bodylength-unburnedlength-burnedlength,burnedlength),
  Section("Fins",1250,noseconelength+bodylength-170,150),
  Part("Parachute",550,330),
  Part("Plate1",60,300),
  Part("Plate3",60,noseconelength+bodylength-unburnedlength-burnedlength-5),
  Part("Electronics",400,420),
  Section("Coupler",couplerdensity*couplerlength,370,couplerlength)]
  rocketCOM,rocketmass = calculate_COM(partlist)
  calculate_COM(partlist,units="imperial")
