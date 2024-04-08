import matplotlib.pyplot as plt
import numpy as np
import math as math
#Purpose to show cloth shape for fine layers
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
plt.fill([0,0,(ct)*math.cos(0.5*math.pi-lang),(cr+2)*math.cos(0.5*math.pi-lang)],[0,ss/math.sin(lang)+2,ss/math.sin(lang)+(ct+2)*math.sin(0.5*math.pi-lang),(cr+2)*math.sin(0.5*math.pi-lang)],color="red",label="intentional overhang")
plt.fill([0,0,-ct*math.cos(0.5*math.pi-lang),-(cr+2)*math.cos(0.5*math.pi-lang)],[0,ss/math.sin(lang)+2,ss/math.sin(lang)+(ct+2)*math.sin(0.5*math.pi-lang),(cr+2)*math.sin(0.5*math.pi-lang)],color="red")
plt.fill([0,0,ct*math.cos(0.5*math.pi-lang),cr*math.cos(0.5*math.pi-lang)],[0,ss/math.sin(lang),ss/math.sin(lang)+ct*math.sin(0.5*math.pi-lang),cr*math.sin(0.5*math.pi-lang)],color="blue",label="fin profile")
plt.fill([0,0,-ct*math.cos(0.5*math.pi-lang),-cr*math.cos(0.5*math.pi-lang)],[0,ss/math.sin(lang),ss/math.sin(lang)+ct*math.sin(0.5*math.pi-lang),cr*math.sin(0.5*math.pi-lang)],color="blue")
plt.plot([0,0],[0,ss/math.sin(lang)+2],color="black",linestyle="--")
plt.xlabel("Length (cm)")
plt.ylim((-1,ss+1))
plt.axis("equal")

plt.ylabel("Length (cm)")
plt.legend()
plt.show()