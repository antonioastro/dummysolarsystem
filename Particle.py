import numpy as np

'''
DO NOT CHANGE ANYTHING IN THIS FILE. 
'''
class Particle():
    position = np.array([0.,0.,0.])
    velocity = np.array([0.,0.,0.])
    acceleration = np.array([0.,0.,0.])
    Name = ''
    mass = 0.

    _particle = []

    def __init__(self,initialPosition,initialVelocity,initialAcceleration,Name,mass):
        self._particle.append(self) #this will automatically make a list of all instances of the class for later use
        self.position = np.array(initialPosition)
        self.velocity = np.array(initialVelocity)
        self.acceleration = np.array(initialAcceleration)
        self.Name = Name
        self.mass = mass

    def euler(self,deltaT):
        #self.acceleration = self.Gravity(other)
        self.position = self.position + (self.velocity*deltaT)
        self.velocity = self.velocity + (self.acceleration*deltaT) 

    def eulercramer(self,deltaT):
        self.velocity = self.velocity + (self.acceleration*deltaT)
        self.position = self.position + (self.velocity*deltaT)
        
    def __repr__(self):
        return 'Particle: %10s, Mass: %.5e, Position: %s, Velocity: %s, Acceleration:%s'%(self.Name,self.mass,self.position, self.velocity,self.acceleration)