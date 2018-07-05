from pymongo import MongoClient 
from pprint import pprint 
from bson.objectid import ObjectId
import json 
import bson
import collections 
import Library_JsonLoad 
import matplotlib.pyplot as plt

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

for Number in range(20):
	Tower_Number = 'Tower' + ' ' + str(Number) 
	for fullName in db.sandbox.find({"fullName": Tower_Number}):
		for crystalFloors in fullName["crystalFloors"]: 
			value_of_intrest_1 = str(crystalFloors.get("hearts", "No Data")) 
			value_of_intrest_2 = str(crystalFloors.get("clubs", "No Data")) 
			value_of_intrest_3 = str(crystalFloors.get("spades", "No Data")) 
			value_of_intrest_4 = str(crystalFloors.get("diamonds", "No Data"))
			Str_1 = 'ObjectId(' + value_of_intrest_1 + ')'
			#print (Str_1)
			#print (value_of_intrest_1) 
			if value_of_intrest_1 != "None":
				for _id in db.sandbox.find({"_id": ObjectId(value_of_intrest_1)}): 
					crystal_age_1 = str(_id.get("crystal_age", "No Data")) 
					#print (crystal_age_1)
					for age_1 in db.sandbox.find({"_id": ObjectId(crystal_age_1)}): 
						Xtal_current_age_1 = str(age_1.get("Xtal_current_age", "No Data")) 
						FullObject.append(Xtal_current_age_1)
			
			if value_of_intrest_2 != "None":
				for _id2 in db.sandbox.find({"_id": ObjectId(value_of_intrest_2)}): 
					crystal_age_2 = str(_id2.get("crystal_age", "No Data"))  
					for age_2 in db.sandbox.find({"_id": ObjectId(crystal_age_2)}): 
						Xtal_current_age_2 = str(age_2.get("Xtal_current_age", "No Data")) 
						FullObject.append(Xtal_current_age_2)
			
			if value_of_intrest_3 != "None":
				for _id3 in db.sandbox.find({"_id": ObjectId(value_of_intrest_3)}): 
					crystal_age_3 = str(_id3.get("crystal_age", "No Data"))
					for age_3 in db.sandbox.find({"_id": ObjectId(crystal_age_3)}): 
						Xtal_current_age_3 = str(age_3.get("Xtal_current_age", "No Data")) 
						FullObject.append(Xtal_current_age_3)
			
			if value_of_intrest_4 != "None":
				for _id4 in db.sandbox.find({"_id": ObjectId(value_of_intrest_4)}):
					crystal_age_4 = str(_id4.get("crystal_age", "No Data"))
					for age_4 in db.sandbox.find({"_id": ObjectId(crystal_age_4)}): 
						Xtal_current_age_4 = str(age_4.get("Xtal_current_age", "No Data")) 
						FullObject.append(Xtal_current_age_4)
					
FullObjectAsString = json.dumps( FullObject , indent=4) 

FileHandle = open('Amano.json', 'w')
FileHandle.write(FullObjectAsString)
FileHandle.close()

FileHandle = open('Amano.json', 'r')
FullObjectAsStringFromFile = FileHandle.read()
FileHandle.close()

FullObjectFromFile = Library_JsonLoad.Main(
	FullObjectAsStringFromFile,
	ForceAscii = True,
) 
