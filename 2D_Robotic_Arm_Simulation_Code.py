# Import library
import math
from pickletools import long4
import matplotlib.pyplot as plt

# Input Arm length
l1 = 1
l2 = 0.5
# Theta start and end values
theta_start = 0
theta_end = math.pi/2

# Number of theta values
n_theta = 10

# Define Angle variable
theta_1 = []
theta_2 = []

# Input Position of (x0,y0)
x0 = 0
y0 = 0

# Values of angle find out
for i in range(0,n_theta):
    theta_value = theta_start+i*(theta_end-theta_start)/(n_theta-1)
    theta_1.append(theta_value)
    theta_2.append(theta_value)


# A constant for getting movie frame.
k=1

# Calculate (x1,y1)   
for i in theta_1:
    # Calculating x2, y2 for corresponding theta2 by taking theta 1 value one by one
    for j in theta_2:
        # Calculate coordinates (x1, y1)
        x1= l1* math.cos(i)
        y1= l1* math.sin(i)

        # Calculate (x2,y2)
        x2= x1 + l2*math.cos(j)
        y2= y1 + l2*math.sin(j)
                
        # Define plot file name for generate animation
        filename = str(k) + '.png'
        k=k+1
        print(filename)
        
        # Plot of robotics arm
        plt.figure()
        plt.plot([x0,x1], [y0,y1],'r')
        plt.plot([x1,x2], [y1,y2],'b')

        
        # Plot axis limit
        plt.xlim([0,5])
        plt.ylim([0,5])
        
        # Save plot figure
        plt.savefig(filename)
