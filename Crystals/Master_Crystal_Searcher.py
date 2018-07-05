#This script was written in order to find all crystals that meet a certain criteria and to print 
#the location of the crystals that meet that particular citeria.

from pymongo import MongoClient 
from pprint import pprint 
from bson.objectid import ObjectId
import csv
import json 
import bson
import collections 
import Library_JsonLoad 
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import cm as CM
from matplotlib import mlab as ML

#Setting up the Mongo Database
client = MongoClient() 
db = client.cdb 
collection = db.sandbox

#Defining function that turns unicode objects into strings
def convert(data):
	if isinstance(data, basestring):
		return str(data)
	elif isinstance(data, bson.objectid.ObjectId): 
		return str(data)
	elif isinstance(data, collections.Mapping):
		return dict(map(convert, data.iteritems()))
	elif isinstance(data, collections.Iterable):
		return type(data)(map(convert, data))
	else:
		return data 

		
#Defining the arrays that we will be printing data into...
FullObject = []
Found_Crystals = []
Data_from_Data_base = []
C_d = []
Data_from_Decay_file = []
Data_base_float = [] 
Decay_file_float = []
Jackson = []
dict_a = {} 
dict_b = {} 
dict_c = {}
dict_d = {} 
dict_e = {} 

#These lists will map crystals from Assembly numbering to DAQ numbering
Tower_Mapping = [0,6,19,5,14,9,7,13,10,18,3,1,8,16,17,15,4,11,12,2]
Rank_Mapping = [1,2,3,4,5,6,7,8,9,10,11,12,13]


#These are items that are located in the trash. They are meant to be excluded
a = ObjectId('53c177f2d1b74a3605342f0e')
b = ObjectId('524c6bf2d1b74a300f90a832')
c = ObjectId('524c6c42d1b74a300f90a993')
d = ObjectId('524c6c42d1b74a300f90a9aa')
e = ObjectId("5150c0047df19b0f09fb7677")
f = ObjectId('53c177fbd1b74a3605342f25')
g = ObjectId('53c1780bd1b74a3605342fa2')
h = ObjectId('53c17810d1b74a3605342fdd')
i = ObjectId('53c17849d1b74a36053432b2')
j = ObjectId('53c17858d1b74a360534336d')
k = ObjectId('53c1786cd1b74a3605343458') 
l = ObjectId('53c1786cd1b74a3605343458')
m = ObjectId('5150c0057df19b0f09fb7686')


#These are the prompts that the script will show you when you run it
criteria = str(raw_input("What are searching by: ")) 
title = str(raw_input("What is the title for your plot: ")) 
x_label = str(raw_input("What is the label for your x axis: ")) 
y_label = str(raw_input("What is the label for your y axis: "))
output = str(raw_input("What do you want to call your output file: "))  
isotope = str(raw_input("What isotope data are you using: "))

#The four outer most for loops search the data base for all Towers that were installed and not put into the trash
for parentId in db.sandbox.find({"name": "tower"}, {"parentId": ObjectId('5150c0057df19b0f09fb7686')}): 
	parentId = dict((k, v) for k, v in parentId.items() if v != a and v != b and v != c and v != d 
    and v != e and v != f and v != g and v != h and v != i and v != j and v != k and v != l and v != m)
	
	for k, v in parentId.items():
		for _id in db.sandbox.find({"_id": ObjectId(v)}):	
			for crystalFloors in _id["crystalFloors"]:
				Number = str(_id.get("number", "No Data"))

#extracting all of the crystals that fall into a certain suit from the towers
				value_of_intrest_a = str(crystalFloors.get("hearts", "No Data")) 
				value_of_intrest_b = str(crystalFloors.get("clubs", "No Data")) 
				value_of_intrest_c = str(crystalFloors.get("spades", "No Data")) 
				value_of_intrest_d = str(crystalFloors.get("diamonds", "No Data"))		
										
				if Number != "0":
					if value_of_intrest_a != "None" and value_of_intrest_b != "None" and value_of_intrest_c != "None" and value_of_intrest_d != "None":

#Searching all of the hearts suit crystals in each tower for the specified criteria
						for _id_a in db.sandbox.find({"_id": ObjectId(value_of_intrest_a)}): 
							LIP_w = str(_id_a.get("locationInParent", "No Data")) 
							w = LIP_w.split(".")
							del w[0]
							w.append(Number) 
							w_str = ' '.join(w)
							crystal_age_a = str(_id_a.get("crystal_age", "No Data"))
							
							if crystal_age_a != "No Data":
								for age_a in db.sandbox.find({"_id": ObjectId(crystal_age_a)}):
									age_r = convert(age_a)
									Te_batch_a = str(age_a.get(criteria, "No Data"))
									if Te_batch_a != "NAN":								 
										Found_Crystals.append(w_str + " " + Te_batch_a)

#Searching all of the clubs suit crystals in each tower for the specified criteria										
						for _id_b in db.sandbox.find({"_id": ObjectId(value_of_intrest_b)}): 
							crystal_age_b = str(_id_b.get("crystal_age", "No Data"))
							LIP_x = str(_id_b.get("locationInParent", "No Data")) 
							x = LIP_x.split(".")
							del x[0]
							x.append(Number) 
							x_str = ' '.join(x)
							
							if crystal_age_b != "No Data":
								for age_b in db.sandbox.find({"_id": ObjectId(crystal_age_b)}):
									age_s = convert(age_b)
									Te_batch_b = str(age_b.get(criteria, "No Data")) 
									if Te_batch_b != "NAN":								 
										Found_Crystals.append(x_str + " " + Te_batch_b)

#Searching all of the spades suit crystals in each tower for the specified criteria
						for _id_c in db.sandbox.find({"_id": ObjectId(value_of_intrest_c)}): 
							crystal_age_c = str(_id_c.get("crystal_age", "No Data"))
							LIP_y = str(_id_c.get("locationInParent", "No Data")) 
							y = LIP_y.split(".")
							del y[0] 
							y.append(Number) 
							y_str = ' '.join(y)
							
							if crystal_age_c != "No Data":
								for age_c in db.sandbox.find({"_id": ObjectId(crystal_age_c)}):
									age_t = convert(age_c)
									Te_batch_c = str(age_c.get(criteria, "No Data")) 
									if Te_batch_c != "NAN":								 
										Found_Crystals.append(y_str + " " + Te_batch_c) 
										
										
#Searching all of the diamonds suit crystals in each tower for the specified criteria			
						for _id_d in db.sandbox.find({"_id": ObjectId(value_of_intrest_d)}): 
							crystal_age_d = str(_id_d.get("crystal_age", "No Data"))
							LIP_z = str(_id_d.get("locationInParent", "No Data")) 
							z = LIP_z.split(".")
							del z[0]
							z.append(Number) 
							z_str = ' '.join(z)
							
							if crystal_age_d != "No Data":
								for age_d in db.sandbox.find({"_id": ObjectId(crystal_age_d)}):
									age_u = convert(age_d)
									Te_batch_d = str(age_d.get(criteria, "No Data"))
									if Te_batch_d != "NAN":								 
										Found_Crystals.append(z_str + " " + Te_batch_d)
										
										

#Printing all of the relevant crystals to the textfile specified by the user the length of the containing the data is also printed 
#for trouble shooting purposes (e.g. if one searches for crystals from any batch 984 should be returned
print (len(Found_Crystals))													
f = open(output, "w") 
f.write("\n".join(map(lambda x: str(x), Found_Crystals))) 
f.close()


#The next half of this script compares the data from the searched crystals to their DAQ data							
with open(isotope) as h_f: 
	for line in h_f: 
		(key_1, val_1, val_2) = line.split() 
		dict_a[int(key_1)] = val_1
		dict_b[int(key_1)] = val_2 
		
		with open(output) as g_f: 
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

f_h = open("Rates_Batch.txt", "w") 
f_h.write("\n".join(map(lambda x: str(x), Jackson))) 
f_h.close()

with open('Rates_Batch.txt') as v_f: 
	for lane in v_f: 
		(key_4, val_5, val_6, val_7) = lane.split() 
		dict_c[int(key_4)] = val_5
		
		Data_from_Decay_file.append(str(val_6))
		Data_from_Data_base.append(str(val_7))

Data_base_float = map(float, Data_from_Data_base)
Decay_file_float = map(float, Data_from_Decay_file)

#heatmap, xedges, yedges = np.histogram2d(Data_base_float, Decay_file_float, bins=(3,3))
#extent = [xedges[0], xedges[-1], yedges[0], yedges[-1]]

#plt.hexbin(Data_base_float, Decay_file_float, gridsize=40, extent=extent, cmap=CM.jet, bins=None)
#cb = plt.colorbar()
#cb.set_label('Number of Crystals in each hexagon')
plt.hist(Decay_file_float, bins=988, color='b', label='Crystals')
plt.title(title)
plt.xlabel(x_label)
plt.ylabel(y_label)
plt.show()  
						
