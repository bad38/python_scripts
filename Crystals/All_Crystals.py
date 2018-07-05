from pymongo import MongoClient 
from pprint import pprint 
import json 
import bson
import collections 
import Library_JsonLoad

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

for Number in range(100,1200):
	Crystal_Number = 'Crystal, Glued' + ' ' + str(Number) 

	for name in db.sandbox.find({"name": Crystal_Number}):
#for name in db.sandbox.find({"name": "Crystal, Glued"}, {"parentId": "5279067dd1b74a5a460b856f"}):
		namejsonOK = convert(name)
	
		FullObject.append(namejsonOK) 
		
for name in db.sandbox.find({"name": "Crystal, Glued"}): 
	
	value_of_intrest_1 = str(name.get("Xtal_birth_to_storage", "No Data")) 
	value_of_intrest_2 = str(name.get("Xtal_current_age", "No Data"))
	value_of_intrest_3 = str(name.get("Te_acq_to_Xtal_birth", "No Data"))
	value_of_intrest_4 = str(name.get("Te_acq_to_Xtal_storage", "No Data"))
	value_of_intrest_5 = str(name.get("life_in_canvern", "No Data"))
	
	Florance = str(value_of_intrest_1) + ' ' + str(value_of_intrest_2) + ' ' + str(value_of_intrest_3) + ' ' + str(value_of_intrest_4) 
	FullObject.append(Florance)
	
	pprint (FullObject)
	
FullObjectAsString = json.dumps( FullObject , indent=4) 
 
FileHandle = open('After_your_gone.json', 'w')
FileHandle.write(FullObjectAsString)
FileHandle.close()

FileHandle = open('After_your_gone.json', 'r')
FullObjectAsStringFromFile = FileHandle.read()
FileHandle.close()

FullObjectFromFile = Library_JsonLoad.Main(
	FullObjectAsStringFromFile,
	ForceAscii = True,
)

#pprint(FullObjectFromFile)

"""
Florence = []

for item in FullObjectFromFile: 
	for key, value in item.iteritems(): 
		Dwayne = convert(value) 
		
		Florence.append(Dwayne) 
		
FlorenceAsString = json.dumps( Florence , indent=4) 

FileHandle_2 = open('PennyLane.json', 'w') 
FileHandle_2.write(FlorenceAsString) 
FileHandle_2.close()	 

FileHandle_2 = open('PennyLane.json', 'r')
FlorenceAsStringFromFile = FileHandle_2.read()
FileHandle.close()

FlorenceFromFile = Library_JsonLoad.Main(
	FlorenceAsStringFromFile,
	ForceAscii = True,
)
	
for item in FlorenceFromFile: 
	#for key, value in item.iteritems(): 
	print key, value 
"""