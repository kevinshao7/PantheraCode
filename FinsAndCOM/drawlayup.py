import matplotlib.pyplot as plt
import numpy as np
import math as math
#Purpose to show fin profile for tip to tip fibreglassing
#For Panthera 0.6
cr = 26.7 #root chord, all in cm
ct = 4.57 #tip chord
ss = 8.6 #fin span
sl = 21.1 #sweep length
sr = cr-sl-ct #rear sweep length
lang = math.atan(ss/sl) #leading angle
rang = math.atan(ss/sr) #trailing angle
print(lang)
d = 7.94 #outer diameter of body tube
taper = 0.5
th = "3mm"
version = "Panthera 0.6"
plt.title("Profile of Fin "+version)
plt.fill([0,sl,sl+ct,cr],[0,ss,ss,0],color="brown",label="taper plywood 5mm gap")
plt.fill([taper/math.sin(lang),sl+(taper/math.tan((math.pi-lang)/2)),sl+ct-(taper/math.tan((math.pi-rang)/2)),cr-(taper*math.sin(rang))],[0,ss-taper,ss-taper,0],color="tan",label="flat plywood")
taper = 0.7
plt.fill([taper/math.sin(lang),sl+(taper/math.tan((math.pi-lang)/2)),sl+ct-(taper/math.tan((math.pi-rang)/2)),cr-(taper*math.sin(rang))],[0,ss-taper,ss-taper,0],color="red",label="1st layer 7mm gap"+th)
taper=0.9
plt.fill([taper/math.sin(lang),sl+(taper/math.tan((math.pi-lang)/2)),sl+ct-(taper/math.tan((math.pi-rang)/2)),cr-(taper*math.sin(rang))],[0,ss-taper,ss-taper,0],color="green",label="2nd layer 9mm gap"+th)
taper=1.1
plt.fill([taper/math.sin(lang),sl+(taper/math.tan((math.pi-lang)/2)),sl+ct-(taper/math.tan((math.pi-rang)/2)),cr-(taper*math.sin(rang))],[0,ss-taper,ss-taper,0],color="blue",label="3rd layer 11mm gap "+th)

plt.xlabel("Length (cm)")
plt.ylim((-1,ss+1))
plt.axis("equal")

plt.ylabel("Length (cm)")
plt.legend()
plt.show()