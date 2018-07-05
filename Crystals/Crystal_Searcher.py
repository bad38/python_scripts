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
BeachBoyz = [] 
Backstreet= [] 
Backstreet_1= [] 
Backstreet_2= [] 
Backstreet_3= [] 
Backstreet_4= []
AllStar = []
AllStar_a = [] 
AllStar_b = [] 
AllStar_c = [] 
AllStar_d = [] 
Vida = []
C_d = [] 
Jimmy_Mack = [] 
Emil = [] 
Hal = [] 
Robbie = [] 
Lauren = [] 

#These lists will map crystals from Assembly numbering to DAQ numbering
Tower_Mapping = [0,6,19,5,14,9,7,13,10,18,3,1,8,16,17,15,5,11,12,2]
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




for parentId in db.sandbox.find({"name": "tower"}, {"parentId": ObjectId('5150c0057df19b0f09fb7686')}): 
	parentId = dict((k, v) for k, v in parentId.items() if v != a and v != b and v != c and v != d 
    and v != e and v != f and v != g and v != h and v != i and v != j and v != k and v != l and v != m)
	
	for k, v in parentId.items():
		#if v != ObjectId('51c2f550d1b74a2d56c21fca') and v != ObjectId('51c85601d1b74a059d0ae661'):
		for _id in db.sandbox.find({"_id": ObjectId(v)}):	
			for crystalFloors in _id["crystalFloors"]:
				Number = str(_id.get("number", "No Data"))
				#LIP = str(_id.get("locationInParent", "No Data")) 
				#print (LIP)	
				#print(locationInParent.split("."))
			
				value_of_intrest_a = str(crystalFloors.get("hearts", "No Data")) 
				value_of_intrest_b = str(crystalFloors.get("clubs", "No Data")) 
				value_of_intrest_c = str(crystalFloors.get("spades", "No Data")) 
				value_of_intrest_d = str(crystalFloors.get("diamonds", "No Data"))		
										
				if Number != "0":
					if value_of_intrest_a != "None" and value_of_intrest_b != "None" and value_of_intrest_c != "None" and value_of_intrest_d != "None":
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
									Te_batch_a = str(age_a.get("Te_acq_to_Xtal_storage", "No Data"))
									if Te_batch_a != "NAN":								 
										AllStar.append(w_str + " " + Te_batch_a)
								
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
									Te_batch_b = str(age_b.get("Te_acq_to_Xtal_storage", "No Data")) 
									if Te_batch_b != "NAN":								 
										AllStar.append(x_str + " " + Te_batch_b)

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
									Te_batch_c = str(age_c.get("Te_acq_to_Xtal_storage", "No Data")) 
									if Te_batch_c != "NAN":								 
										AllStar.append(y_str + " " + Te_batch_c)
				
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
									Te_batch_d = str(age_d.get("Te_acq_to_Xtal_storage", "No Data"))
									if Te_batch_d != "NAN":								 
										AllStar.append(z_str + " " + Te_batch_d)
										
										
print (len(AllStar))													
f = open("AllStar.txt", "w") 
f.write("\n".join(map(lambda x: str(x), AllStar))) 
f.close()
							
						
