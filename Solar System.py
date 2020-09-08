import numpy as np 
import math
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d

data=np.load('L:\-n\python\simdata.npy')
bodieslist=np.load('L:\-n\python\listbodies.npy')

GraphType= 1 

'''
A user must only change GraphType to be one of the following values:
#1 for an x-y plot
#2 for an x-z plot
#3 for a 3-d plot, though this has been found to not always work correctly

it is also important to note that a user must edit the directory to which files are saved to or loaded from.
use ctrl+f and search 'L:\-n\python' to be replaced with the directory of your choice. during testing i have found the code to not function correctly if the directory is not precisely stated.
'''

if GraphType ==1   :
    f1=plt.figure('Top View')
    obj=0
    while obj < len(bodieslist):
        xpos=[]
        ypos=[]
        for line in data:
            xpos.append(line[obj+1].position[0])
            ypos.append(line[obj+1].position[1])
        plt.plot(xpos,ypos,'-',label=bodieslist[obj].Name)
        obj=obj+1
    plt.xlabel('x-position (m)')
    plt.ylabel('y-position (m)')
    plt.axis('equal')
    plt.legend(loc=1)
    plt.savefig('L:\-n\python\top view.png',bbox_inches='tight',dpi=1000)
    plt.show('Top View') 

if GraphType ==2 :
    f2=plt.figure('Ecliptic Plane View')
    obj=0
    while obj < len(bodieslist):
        xpos=[]
        zpos=[]
        for line in data:
            xpos.append(line[obj+1].position[0])
            zpos.append(line[obj+1].position[2])
        plt.plot(xpos,zpos,'-',label=bodieslist[obj].Name)
        obj+=1
    plt.xlabel('x-position (m)')
    plt.ylabel('z-position (m)')
    plt.axis('equal')
    plt.legend(loc=1)
    plt.savefig('L:\-n\python\Ecliptic View.png',bbox_inches='tight',dpi=100)
    plt.show() 
    

if GraphType ==3:
    f3=plt.figure('3D view')
    ax = plt.axes(projection='3d')
    obj=0
    while obj < len(bodieslist):
        xpos=[]
        ypos=[]
        zpos=[]
        for line in data:
            xpos.append(line[obj+1].position[0])
            ypos.append(line[obj+1].position[1])
            zpos.append(line[obj+1].position[2])
        ax.plot3D(xpos,ypos,zpos,'-',label=bodieslist[obj].Name)
        obj+=1
    ax.set_aspect('equal')
    ax.set_xlabel('x-position (m)')
    ax.set_ylabel('y-position (m)')
    ax.set_zlabel('z-position (m)')
    plt.legend(loc=1)
    plt.show() 
    plt.savefig('L:\-n\python\-3D view.png',bbox_inches='tight',dpi=100)