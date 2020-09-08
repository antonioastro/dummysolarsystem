from Particle import Particle
import matplotlib.pyplot as plt 
import math
import copy
import numpy as np
import Bodies

deltaT = 5000 
runtime = 40e6 
method = 2 
datatosave = 500 

'''
a user should only change: 
deltaT - this is the time step in seconds. a lower time step is more accurate but may take longer to compute
runtime - this is how long the simulation is simulating in seconds. for ease of reference 1 month = 2.4e6 seconds and 1 year is 32e6 seconds.
method - the update method. #1 for Euler and #2 for Euler-Cromer
datatosave - changing this will reduce the amount of data saved by a factor of n, making the data file smaller, though the plot more polygonal than circular

it is also important to note that a user must edit the directory to which files are saved to or loaded from.
use ctrl+f and search 'L:\-n\python' to be replaced with the directory of your choice. during testing i have found the code to not function correctly if the directory is not precisely stated.
'''

data = [] 
time=0

def Gravity(ob1,ob2):
    G=6.67e-11
    radius = ob2.position-ob1.position
    accGrav = -(G*ob1.mass*radius)/(np.linalg.norm(radius)*np.linalg.norm(radius)*np.linalg.norm(radius))
    return accGrav

def GravTot(ob2):
    total=np.array([0,0,0])
    for x in Bodies.bodies:
        if ob2 == x:
            continue
        total = total+Gravity(x,ob2)
    return total

while (time<runtime):
    temp1 = []
    time = time + deltaT
    for obj in Bodies.bodies:
        obj.acceleration=GravTot(obj)
    for obj in Bodies.bodies:    
        if method == 1:
            obj.euler(deltaT)
    for obj in Bodies.bodies:        
        if method == 2:
            obj.eulercramer(deltaT)
    for obj in Bodies.bodies:
        temp1.append(copy.deepcopy(obj))
    item=[time]
    item=item+temp1
    if time % datatosave==0:
        data.append(item)

print('Simulation Ran. Saving Data...')
np.save('L:\-n\python\zindata.npy',data)
np.save('L:\-n\python\listbodies.npy',Bodies.bodies)
print('Simulation Data saved. Please run the Solar System and/or Analysis File')