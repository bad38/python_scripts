from pymongo import MongoClient 
from pprint import pprint 
from bson.objectid import ObjectId
import json 
import bson
import collections 
import Library_JsonLoad 
import matplotlib.pyplot as plt
import numpy as np

client = MongoClient() 
db = client.cdb 
collection = db.sandbox

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

FullObject = []
Beach_Boyz = []

for Number in range(1,20):
	Tower_Number = 'Tower' + ' ' + str(Number) 
	for fullName in db.sandbox.find({"fullName": Tower_Number}):
		for crystalFloors in fullName["crystalFloors"]: 
			value_of_intrest_1 = str(crystalFloors.get("hearts", "No Data")) 
			value_of_intrest_2 = str(crystalFloors.get("clubs", "No Data")) 
			value_of_intrest_3 = str(crystalFloors.get("spades", "No Data")) 
			value_of_intrest_4 = str(crystalFloors.get("diamonds", "No Data")) 
								
			if value_of_intrest_1 != "None":
				for _id in db.sandbox.find({"_id": ObjectId(value_of_intrest_1)}):  
					crystal_age_1 = str(_id.get("crystal_age", "No Data")) 
					for age_1 in db.sandbox.find({"_id": ObjectId(crystal_age_1)}): 
						#comments_1 = str(age_1.get("comment", "No Data"))
						#if comments_1 != "CUORE-0":
						age_a = convert(age_1)
						FullObject.append(age_a)
			
			if value_of_intrest_2 != "None":
				for _id2 in db.sandbox.find({"_id": ObjectId(value_of_intrest_2)}): 
					crystal_age_2 = str(_id2.get("crystal_age", "No Data"))  
					for age_2 in db.sandbox.find({"_id": ObjectId(crystal_age_2)}): 
						#comments_2 = str(age_2.get("comment", "No Data")) 
						#if comments_2 != "CUORE-0":
						age_b = convert(age_2)
						FullObject.append(age_b)

			
			if value_of_intrest_3 != "None":
				for _id3 in db.sandbox.find({"_id": ObjectId(value_of_intrest_3)}): 
					crystal_age_3 = str(_id3.get("crystal_age", "No Data"))
					for age_3 in db.sandbox.find({"_id": ObjectId(crystal_age_3)}): 
						#comments_3 = str(age_3.get("comment", "No Data"))
						#if comments_3 != "CUORE-0":
						age_c = convert(age_3)
						FullObject.append(age_c)
			
			if value_of_intrest_4 != "None":
				for _id4 in db.sandbox.find({"_id": ObjectId(value_of_intrest_4)}):	
					crystal_age_4 = str(_id4.get("crystal_age", "No Data"))
					for age_4 in db.sandbox.find({"_id": ObjectId(crystal_age_4)}): 
						#comments_4 = str(age_4.get("comment", "No Data")) 
						#if comments_4 != "CUORE-0":
						age_d = convert(age_4)
						FullObject.append(age_d)
					
FullObjectAsString = json.dumps( FullObject , indent=4) 

FileHandle = open('Loca.json', 'w')
FileHandle.write(FullObjectAsString)
FileHandle.close()

FileHandle = open('Loca.json', 'r')
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
 
 
 
 

Hal9000 = map(int, All_Items)



print (Hal9000)

"""
with open('Po210Rates2.txt') as f:
    lines = f.readlines()
    x = [line.split()[0] for line in lines]
    y = [line.split()[1] for line in lines] 
	#z = [line.split()[2] for line in lines]
	#print (y)

	
	

plt.plot(x, y, 'ro') 
plt.axis([0, 988, 0, .1])
#plt.hist(Hal9000, bins=988, color='b', label='Crystals', cumulative=True) 
plt.title("Xtal Current Age") 
plt.xlabel("Time [Days]") 
plt.ylabel("Total Crystals") 
#plt.legend()
plt.show()
"""