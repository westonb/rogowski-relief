import numpy as np
import matplotlib.pyplot as plt
import control



FSTART = 100E3
FEND = 50E6

freq_range = np.geomspace(FSTART, FEND, 1000) * 2*np.pi


#generate plant transfer function
R1 = 470.0
R2 = 470.0 
R3 = 1.1E3 

C1 = 47E-12

G0 = (R1 + R2) / R2

Wp1 = 1/(R3*C1)

Wz1 = (R1+R2)/(C1*(R1*R2 + R1*R3 + R2*R3))


plant_TF = control.tf([1/Wz1, 1], [1/Wp1, 1]) * G0

print(Wp1)
print(Wz1)

mag,phase,omega = control.bode(plant_TF, freq_range, Hz=True, dB=True, initial_phase=0)
plt.show()
