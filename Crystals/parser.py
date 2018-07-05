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
 


f = open("Im_Bad_Really_Really_Bad.json","r")
lines = f.readlines()
result = []
for x in lines: 
	
	A = x[5:29] 
	B = x[30:54] 
	C = x[55:79]
	D = x[80:104] 
	
	print (D)
f.close()



