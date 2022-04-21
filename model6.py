# -*- coding: utf-8 -*-
"""
Created on Mon Apr  4 17:08:33 2022

@author: clambert

model6 relateds to the "I/O" practical and should be used with 
the agentframework6 and the csvreader6 files.

in.txt is the input data for the csvreader6 file and should be stored in the same directory

Directions:
1. Save model6, agentframework6, in.txt and csvreader6 in the same directory location
2. Run model6

Expected outputs:
1. Scatter chart of agents, coloured individually and displayed on environment
background in a seperate window
2. print max and min distance between agents (maxd and mind)
2. "Finished" printed on closing the seperate window.

"""

#Imported modules
import random
import operator
import matplotlib.pyplot
import agentframework6 #link to agentframework6.py
import csvreader6 #link to csvreader6.py


# Set the seed for reproducinility
#random.seed(0) #testing reducability of model - when set, output should be the same each time
#random.seed(1)


#bring enviroment data in from csvreader6
environment = csvreader6.get_data()


a = agentframework6.Agent(environment)
#a. __init__()
a. move ()
#print(a.y, a.x) #test agentframework


#distance_between method - calcualtion used for distance at bottom of code
def distance_between(a, b):
    """
    Calculates and returns the 2D coordinate distance between a and b.

    Parameters
    ----------
    a : Agent
        Located in 2D space with an x and y cordinate values.
    b : Agent
        Located in 2D space with an x and y cordinate values.

    Returns
    -------
    Number
        The 2D coordinate distance bertween a and b.
    """
    return (((a.x - b.x)**2) + ((a.y - b.y)**2))**0.5



num_of_agents = 10 #changable value
num_of_iterations = 1 #changable value
agents = [] #Creates a new empty list for agents

# Make the agents.
for i in range(num_of_agents):
    agents.append(agentframework6.Agent(environment)) 

# Move the agents.
for j in range(num_of_iterations):
    for i in range(num_of_agents):
        agents[i].move()
        agents[i].eat()

#returns graphical results
matplotlib.pyplot.xlim(0, 99) #x axis
matplotlib.pyplot.ylim(0, 99) #y axis
matplotlib.pyplot.imshow(environment) #plots enviroment data from csvreader6
for i in range(num_of_agents): #created and moved agents based on number of agents
    matplotlib.pyplot.scatter(agents[i].x, agents[i].y) #plot scatter of agents
matplotlib.pyplot.show() #show window


# defining min and max dstance variables
maxd = distance_between(agents[0], agents[1])
mind = distance_between(agents[0], agents[1])

           
# Calculating the distance
for i in range(num_of_agents):
    for j in range(i + 1, num_of_agents, 1):
            #print(i, j)
            distance = distance_between(agents[i], agents[j])
            #print(distance)
            maxd = max(maxd, distance)
            mind = min(mind, distance)
print("maxd", maxd)
print("mind", mind)

# done marker
print ("finished")
