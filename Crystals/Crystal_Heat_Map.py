from pymongo import MongoClient 
from pprint import pprint 
import json 
import bson
import collections 
import Library_JsonLoad 
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm as CM
from matplotlib import mlab as ML

FullObject = []
C_d = []
Sally = [] 
Tower_Mapping = [0,6,19,5,14,9,7,13,10,18,3,1,8,16,17,15,4,11,12,2]
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
		(key_4, val_5, Paul, Alejandro) = lane.split() 
		g[int(key_4)] = val_5
		
		Sally.append(str(Paul))
		FullObject.append(str(Alejandro))

Hal9000 = map(float, FullObject)
Hal9001 = map(float, Sally)

heatmap, xedges, yedges = np.histogram2d(Hal9000, Hal9001, bins=(3,3))
extent = [xedges[0], xedges[-1], yedges[0], yedges[-1]]

plt.hexbin(Hal9000, Hal9001, gridsize=40, extent=extent, cmap=CM.jet, bins=None)
cb = plt.colorbar()
cb.set_label('Number of Crystals in each hexagon')
plt.title('Life in Cavern Vs. Rate [Gridsize = 40]')
plt.xlabel('life_in_cavern [Days]')
plt.ylabel('Rate [Events per Year]')
plt.show()  

