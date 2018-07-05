from pymongo import MongoClient 
from pprint import pprint 
import json 
import bson
import collections 
import Library_JsonLoad 
#import matplotlib.pyplot.hist
import matplotlib.pyplot as plt

FullObject = []
C_d = []
Sally = [] 
Tower_Mapping = [0,6,19,5,14,9,7,13,10,18,3,1,8,16,17,15,5,11,12,2]
Rank_Mapping = [1,2,3,4,5,6,7,8,9,10,11,12,13]
a = {} 
b = {} 
f = {}
g = {} 
h = {}

with open('Po210Rates2.txt') as f: 
	for line in f: 
		(key_1, val_1, val_2) = line.split() 
		a[int(key_1)] = val_1
		b[int(key_1)] = val_2 

		
		with open('AllStar.txt') as g_f: 
			for lane in g_f: 
				(val_f, val_g, val_h, batch) = lane.split() 
				Rank = Rank_Mapping[int(val_f)]
				Tower = Tower_Mapping[int(val_h)]
				if val_g == "hearts": 
					Channel = (str((int(Tower) - 1) * (52) + (1 - 1) * (13) + int(Rank))) 
					if key_1 == Channel: 
						C_d.append(str(key_1) + ' ' + str(Channel) + ' ' + str(val_2) + ' ' + str(batch))
				if val_g == "clubs":
					Channel = (str((int(Tower) - 1) * (52) + (2 - 1) * (13) + int(Rank))) 
					if key_1 == Channel: 
						C_d.append(str(key_1) + ' ' + str(Channel) + ' ' + str(val_2) + ' ' + str(batch))
				if val_g == "spades":
					Channel = (str((int(Tower) - 1) * (52) + (3 - 1) * (13) + int(Rank))) 
					if key_1 == Channel: 
						C_d.append(str(key_1) + ' ' + str(Channel) + ' ' + str(val_2) + ' ' + str(batch))
				if val_g == "diamonds": 
					Channel = (str((int(Tower) - 1) * (52) + (4 - 1) * (13) + int(Rank))) 
					if key_1 == Channel: 
						C_d.append(str(key_1) + ' ' + str(Channel) + ' ' + str(val_2) + ' ' + str(batch))


Jackson = set((C_d))

f = open("Rates_Batch.txt", "w") 
f.write("\n".join(map(lambda x: str(x), Jackson))) 
f.close()

with open('Rates_Batch.txt') as g_f: 
	for lane in g_f: 
		(key_4, key_5, val_5, Paul) = lane.split() 
		g[int(key_4)] = val_5
		
		Sally.append(str(Paul))
		FullObject.append(str(val_5))






Hal9000 = map(float, FullObject)
Hal9001 = map(int, Sally)
print (len(Hal9000))

fig = plt.figure()

ax1 = fig.add_subplot(111)

ax1.set_title("Crystal Age vs Rate")    
ax1.set_xlabel('Crystal Age [Days]')
ax1.set_ylabel("Rate [Events per Year]")
#plt.hist(Hal9000, bins=988, color='b', label='Crystals')
plt.scatter(Hal9001,Hal9000)
plt.axis([10007, 10009, 0, 7000])
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
"""