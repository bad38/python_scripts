from pymongo import MongoClient 
from pprint import pprint 
import json 
import bson
import collections 
import Library_JsonLoad 
#import matplotlib.pyplot.hist
import matplotlib.pyplot as plt

"""
filename = "PennyLane.json" 
with open(filename, 'r') as f: 
	objects = json.items(f, 'logId') 
	columns = list(objects) 
	
	print(columns[0]) 
"""	
	
	
FileHandle = open('Repeat_After_Me.json', 'r')
FullObjectAsStringFromFile = FileHandle.read()
FileHandle.close()

FullObjectFromFile = Library_JsonLoad.Main(
	FullObjectAsStringFromFile,
	ForceAscii = True,
) 

All_Items = [] 
for Sally in FullObjectFromFile: 
	value_of_intrest = Sally["Xtal_current_age"] 
	
        if value_of_intrest != "NAN": 
                All_Items.append(value_of_intrest) 
	
	
##pprint (All_Items)  

Hal9000 = map(int, All_Items)

print (Hal9000)

"""
plt.plot(Hal9000) 
plt.show
""" 

#import matplotlib.pyplot as plt 
#from numpy.random import normal, uniform 
#gaussian_numbers = normal(size=1000) 
#uniform_numbers = uniform(low=-3, high=3, size=1000)
#plt.hist(gaussian_numbers, bins=20, normed=True, cumulative=True) 
plt.hist(Hal9000, bins=988, color='b', label='Crystals', cumulative=True) 
#plt.hist(Hal9000, bins=200, histtype='stepfilled', normed=True, color='b', label='Crystals') 
#plt.hist(uniform_numbers, bins=20, histtype='stepfilled', normed=True, color='r', alpha=0.5, label='Uniform')
plt.title("Xtal Current Age") 
plt.xlabel("Time [Days]") 
plt.ylabel("Percentage of Total Crystals") 
plt.legend()
plt.show()
