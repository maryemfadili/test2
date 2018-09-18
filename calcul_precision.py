import numpy as np
import math as m

# This script aims to estimate the standart deviation of an XYZ coordinates for a maximum distance
# of 500m and a minimum angle of 0.3mgon which are the limit of the total station Leica TS06plus

# Measurements' value
Dmax = 300
#Amin = (0.3*0.001*m.pi)/200 # on radian
Amin = (0.3*m.pi)/200 # on radian

# Measurements' accuracy

# Distance's accuracy
## With prism
sigmaDP = 1.5 * 0.001 + 2*0.001*(Dmax/1000)  # 1.5mm + 2ppm

## Without prism
sigmaDWP = 2 * 0.001 + 2*0.001*(Dmax/1000)  # 2mm + 2ppm

# Angle's accuracy
sigmaA = (0.3*0.001*m.pi)/200

# Computing accuracy for XYZ coordinates 

# With prism
sigmaZP = m.sqrt((m.cos(Amin)*sigmaDP)**2 + ((Dmax/m.sin(Amin))*m.sin(Amin)*sigmaA)**2)

sigmaXP = m.sqrt((m.sin(Amin)*sigmaDP)**2 + (Dmax*m.cos(Amin)*sigmaA)**2)

sigmaYP = m.sqrt((m.cos(Amin)*sigmaDP)**2 + (Dmax*m.sin(Amin)*sigmaA)**2)

print'Accuracies of coordinates XYZ using prism are respectively : {} {} {}'.format(sigmaXP, sigmaYP, sigmaZP)


# Without prism
sigmaZWP = m.sqrt((m.cos(Amin)*sigmaDWP)**2 + ((Dmax/m.sin(Amin))*m.sin(Amin)*sigmaA)**2)

sigmaXWP = m.sqrt((m.sin(Amin)*sigmaDWP)**2 + (Dmax*m.cos(Amin)*sigmaA)**2)

sigmaYWP = m.sqrt((m.cos(Amin)*sigmaDWP)**2 + (Dmax*m.sin(Amin)*sigmaA)**2)

print'Accuracies of coordinates XYZ without prism are respectively : {} {} {}'.format(sigmaXWP, sigmaYWP, sigmaZWP)
