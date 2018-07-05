from pymongo import MongoClient 
from pprint import pprint 
import json 
import bson
import collections 
import Library_JsonLoad 
import numpy as np
#import matplotlib.pyplot.hist
import matplotlib.pyplot as plt

FullObject = []
C_d = []
Sally = []
a = {} 
b = {} 
g = {}

with open('Po210Rates2.txt') as f: 
	for line in f: 
		(key_1, val_1, val_2) = line.split() 
		a[int(key_1)] = val_1
		b[int(key_1)] = val_2 
		
		with open('AllStar.txt') as g_f: 
			for lane in g_f: 
				(key_2, val_3) = lane.split() 
				g[int(key_2)] = val_3
			 									
				#for key_2, val_3 in g.iteritems(): 
				if key_1 == key_2: 
				#print str(Channel_3) + ' ' + str(key) + ' ' + str(val_1)
					C_d.append(str(key_1) + ' ' + str(val_2) + ' ' + str(val_3))
				#print(Channel_3)
				#Backstreet.append(str(Channel_3))
				#BeachBoyz.append(str(Te_batch_3)) 
				#Pancake_King.append(str(Channel_3) + ' ' + str(val_1) + ' ' + (Te_batch_3))


Jackson = set((C_d))

f = open("Rates_Batch.txt", "w") 
f.write("\n".join(map(lambda x: str(x), Jackson))) 
f.close()

with open('Rates_Batch.txt') as g_f: 
	for lane in g_f: 
		(key_4, val_5, Paul) = lane.split() 
		g[int(key_4)] = val_5
		
		Sally.append(str(Paul))
		FullObject.append(str(val_5))






Hal9000 = map(float, FullObject)
Hal9001 = map(int, Sally)
#print (len(Hal9000)) 


heatmap, xedges, yedges = np.histogram2d(Hal9001, Hal9000, bins=(9,9))
extent = [xedges[0], xedges[-1], yedges[0], yedges[-1]]
 
# Plot heatmap
plt.clf()
plt.title('Pythonspot.com heatmap example')
plt.ylabel('y')
plt.xlabel('x')
plt.imshow(heatmap)
cax = plt.axis([0, 988, 0, 4000]) 
#plt.colorbar(heatmap)
#plt.imshow(heatmap, extent=extent)
#plt.figure(num=None, figsize=(8, 6), dpi=80, facecolor='w', edgecolor='k')
plt.show()








"""
fig = plt.figure()

ax1 = fig.add_subplot(111)

ax1.set_title("Te_Batch vs Rate")    
ax1.set_xlabel('Te_Batch Number')
ax1.set_ylabel("Rate [Events per Year]")
#plt.hist(Hal9000, bins=988, color='b', label='Crystals')
plt.scatter(Hal9001,Hal9000)
plt.axis([10000, 10013, 0, 7000])
plt.show()
"""






#import matplotlib.pyplot as plt 
#from numpy.random import normal, uniform 
#gaussian_numbers = normal(size=1000) 
#uniform_numbers = uniform(low=-3, high=3, size=1000)
#plt.hist(gaussian_numbers, bins=20, normed=True, cumulative=True) 
#plt.hist(Hal9000, bins=988, color='b', label='Crystals', cumulative=True) 
#plt.hist(Hal9000, bins=200, histtype='stepfilled', normed=True, color='b', label='Crystals') 
#plt.hist(uniform_numbers, bins=20, histtype='stepfilled', normed=True, color='r', alpha=0.5, label='Uniform')
#plt.title("Xtal Current Age") 
#plt.xlabel("Time [Days]") 
#plt.ylabel("Percentage of Total Crystals") 
#plt.legend()
#plt.show()
