from pymongo import MongoClient 
from pprint import pprint 
import json 
import bson
import collections 
import Library_JsonLoad 
import matplotlib.pyplot as plt 
import numpy as np
import matplotlib.pyplot as plt 
from mpl_toolkits.mplot3d import Axes3D

data = np.genfromtxt('FooDog.csv', delimiter=',', names=['x', 'y'])

fig = plt.figure()

ax1 = fig.add_subplot(111)

ax1.set_title("Mains power stability")    
ax1.set_xlabel('Channel')
ax1.set_ylabel('Xtal_current_age')

#ax1.plot(data['x'], data['y'], color='r', label='the data')
plt.scatter(data['x'],data['y'])
plt.show()

"""
with open('FooDog.csv') as f:
    lines = f.readlines()
    x = [line.split()[0] for line in lines]
    y = [line.split()[1] for line in lines] 
	#z = [line.split()[2] for line in lines]
	#print (y)


plt.plot(x, y, 'ro') 
plt.axis([0, 988, 0, 2000])
plt.show()
"""




"""
x = np.loadtxt("Po210Rates.txt", delimiter='  ', unpack=True)
print (x) 
"""
 

"""
f = open("Somebody.json","r")
lines = f.readlines()
result = []
for x in lines: 
	
	A = x[5:6]
	B = x[7:31] 
	C = x[36:37]
	D = x[34:58] 
	E = x[59:60]
	F =	x[61:85]
	G = x[86:87]
	H =	x[88:112] 
	
	print (C)
f.close()
"""


