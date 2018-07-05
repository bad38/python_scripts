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

"""
x = np.loadtxt("Po210Rates.txt", delimiter='  ', unpack=True)
print (x) 
"""
 


f = open("Po210Rates2.txt","r")
lines = f.readlines()
result = []
for x in lines: 
	
	A = x[0:3] 
	B = x[4:13] 
	C = x[13:24]
	#print (x.split(' ', 1))
	
	#y = np.array_split(x.split(), 3)
	print (A) 
	#print (B) 
	#print (C)
	#print (y)
	#print (x.split())
	
	
	#print (x)
	#result.append(x)
f.close()



#print (Hal9000)

"""
f = open("Po210Rates.txt","r")
lines = f.readlines()
result = []
for x in lines:
    result.append(x.split(' ')[3])
f.close()
print (result)
"""