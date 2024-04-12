import matplotlib.pyplot as plt
import numpy as np
import math as math
#Purpose to show fin jig
version = "Panthera 0.6"

plt.title("Fin Jig "+version)
plt.fill([0,0,6,6,9,9,15,15],[0,10,30,3,3,40,60,0],label="jig profile")
plt.xlabel("Length (mm)")
plt.axis("equal")
plt.fill([6,6,7.5,9,9],[5,30,35,30,5],label="fin profile")

plt.ylabel("Length (mm)")
plt.legend()
plt.show()