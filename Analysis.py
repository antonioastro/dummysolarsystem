import numpy as np 
import math
import matplotlib.pyplot as plt

data=np.load('L:\-n\pythonA\simdata.npy')
bodieslist=np.load('L:\-n\python\listbodies.npy')


graphchoice = 4 

'''
A user must only change graphchoice to be one of the following values:
#1 for change in kinetic energy
#2 for total energies of each body
#3 for virial theorem test
#4 for total momentum of each body
#5 for angular momentum of each body

it is also important to note that a user must edit the directory to which files are saved to.
use ctrl+f and search 'L:\-n\python' to be replaced with the directory of your choice. during testing i have found the code to not function correctly if the directory is not precisely stated.
'''

if graphchoice == 1:
    f1=plt.figure()
    obj=0
    while obj < len(bodieslist):
        time=[]
        Kinchange=[]
        Kold=data[0][obj+1].mass*0.5*np.linalg.norm(data[0][obj+1].velocity)*np.linalg.norm(data[0][obj+1].velocity)
        for p in range(len(data)):
            K=data[p][obj+1].mass*0.5*np.linalg.norm(data[p][obj+1].velocity)*np.linalg.norm(data[p][obj+1].velocity)
            Kchange=K-Kold
            Kinchange.append(Kchange)
            time.append(data[p][0])
            Kold=K
        plt.plot(time,Kinchange,'-',label=(bodieslist[obj].Name))
        obj=obj +1
    plt.xlabel('time (s)')
    plt.ylabel('Change in kinetic energy (J)')
    plt.axis()
    plt.legend(loc=1)
    plt.savefig('L:\-n\python\changeinkineticenergy.png',bbox_inches='tight',dpi=100)
    plt.show() 

if graphchoice == 2:
    f1=plt.figure()
    obj=0
    while obj < len(bodieslist):
        time=[]
        energy=[]
        for p in range(len(data)):
            G=6.67e-11
            K=data[p][obj+1].mass*0.5*np.linalg.norm(data[p][obj+1].velocity)*np.linalg.norm(data[p][obj+1].velocity)
            u=0
            for n in range(len(bodieslist)):
                if data[p][obj+1].Name != data[p][n+1].Name:
                    u = u + (-G*data[p][obj+1].mass*data[p][n+1].mass)/np.linalg.norm(data[p][obj+1].position-data[p][n+1].position)
            energytot=K+u
            if p != 0:     
                energy.append(energytot)
                time.append(data[p][0])
        plt.plot(time,energy,'-',label=(bodieslist[obj].Name))
        obj=obj +1
    plt.xlabel('time (s)')
    plt.ylabel('Total energy (J)')
    plt.axis()
    plt.legend(loc=1)
    plt.savefig('L:\-n\python\-totalenergyeuler.png',bbox_inches='tight',dpi=100)
    plt.show() 

if graphchoice == 3:
    f1=plt.figure()
    obj=0
    while obj < len(bodieslist):
        time=[]
        virialt=[]
        for p in range(len(data)):
            G=6.67e-11
            K=data[p][obj+1].mass*0.5*np.linalg.norm(data[p][obj+1].velocity)*np.linalg.norm(data[p][obj+1].velocity)
            u=0
            for n in range(len(bodieslist)):
                if data[p][obj+1].Name != data[p][n+1].Name:
                    u = u + (-G*data[p][obj+1].mass*data[p][n+1].mass)/np.linalg.norm(data[p][obj+1].position-data[p][n+1].position)
            virial=2*K+u
            if p != 0:     
                virialt.append(virial)
                time.append(data[p][0])
        plt.plot(time,virialt,'-',label=(bodieslist[obj].Name))
        obj=obj +1
    plt.xlabel('time (s)')
    plt.ylabel('Energy (J)')
    plt.axis()
    plt.legend(loc=1)
    plt.savefig('L:\-n\python\-virialtheorem.png',bbox_inches='tight',dpi=100)
    plt.show() 

if graphchoice == 4:
    f1=plt.figure()
    obj=0
    while obj < len(bodieslist):
        time=[]
        MOmentum=[]
        for p in range(len(data)):
            momentum=data[p][obj+1].mass*np.linalg.norm(data[p][obj+1].velocity)
            MOmentum.append(momentum)
            time.append(data[p][0])
        plt.plot(time,MOmentum,'-',label=(bodieslist[obj].Name))
        obj=obj +1
    plt.xlabel('time (s)')
    plt.ylabel('momentum (kgm/s)')
    plt.axis()
    plt.legend(loc=1)
    plt.savefig('L:\-n\python\momentum.png',bbox_inches='tight',dpi=100)
    plt.show() 

if graphchoice == 5:
    f1=plt.figure()
    obj=0
    while obj < len(bodieslist):
        time=[]
        angMOmentum=[]
        for p in range(len(data)):
            angmomentum=np.linalg.norm(np.cross(data[p][obj+1].position,data[p][obj+1].mass*data[p][obj+1].velocity))
            angMOmentum.append(angmomentum)
            time.append(data[p][0])
        plt.plot(time,angMOmentum,'-',label=(bodieslist[obj].Name))
        obj=obj +1
    plt.xlabel('time (s)')
    plt.ylabel('angular momentum (kgm^2/s)')
    plt.axis()
    plt.legend(loc=1)
    plt.savefig('L:\-n\python\-angular momentum.png',bbox_inches='tight',dpi=100)
    plt.show() 