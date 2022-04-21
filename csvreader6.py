# -*- coding: utf-8 -*-
"""
Created on Wed Apr  6 18:27:32 2022

@author: clambert

csvreader6 relateds to the "I/O" practical and should be used with 
the model6 and the agentframework6 files.

in.txt is the input data for this file and should be stored in the same directory

Directions:
1. Save model6, agentframework6, in.txt and csvreader6 in the same directory location
2. Run model6

"""
#Imported modules
import csv


#open, reads and appends in.txt input data to geneate envrionment
def get_data():
    """
    get_data() defines a function that allows connected code to get data from this reader

    Returns
    -------
    environment : list
        returns an appended envrionment list based on input data.

    """
    f = open('in.txt', newline='') #open in.txt data
    reader = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)
    
    environment = [] #define empty environment list
    for row in reader: # A list of rows
        rowlist = [] #define empty rowlist   
        for value in row: # A list of value
            rowlist.append(value) #append row data into rowlist 
            #print(value) # Floats
        environment.append(rowlist) #append data into environment
 
    f.close() 
    return environment

