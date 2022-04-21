# -*- coding: utf-8 -*-
"""
Created on Wed Apr  6 16:36:52 2022

@author: clambert

agentframework6 relateds to the "I/O" practical and should be used with 
the model6 and the csvreader6 files.

in.txt is the input data for the csvreader6 file and should be stored in the same directory

Directions:
1. Save model6, agentframework6, in.txt and csvreader6 in the same directory location
2. Run model6

"""

#Imported modules
import random


#Define "Agent" class
class Agent():

    #generate random x & y values        
    def __init__(self, environment):
        """
        Parameters
        ----------
        environment :
            __init__ creates random starting values for x & y between 0 and 99.

        Returns
        -------
        random starting values

        """
        self.environment = environment #defining environment
        self.store = 0
        self.x = random.randint (0,99) #random values for x
        self.y = random.randint (0,99) #random values for y
        #print (self.x) # test
        #print (self.y) # test

     #moves the agents   
    def move (self):
        """
        move takes the values generated in __init__ and moves them one step

        Returns
        -------
        Returns new values moved by one step

        """
        if random.random() < 0.5:
            self.x = (self.x + 1) % 100
        else:
            self.x = (self.x - 1) % 100

        if random.random() < 0.5:
            self.y = (self.y + 1) % 100
        else:       
            self.y = (self.y - 1) % 100
    
    
    # eats into enviroment based on values
    def eat(self): 
        """
        eats into enviroment if values are > 10
        
        Returns
        -------
        values in environment based on the subtraction assignment

        """
        if self.environment[self.y][self.x] > 10:
            self.environment[self.y][self.x] -= 10
            self.store += 10  

    pass

