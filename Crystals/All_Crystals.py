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
	namejsonOK = convert(name) 
		
	FullObject.append(namejsonOK)
	
FullObjectAsString = json.dumps( FullObject , indent=4) 
 
FileHandle = open('Hal9000.json', 'w')
FileHandle.write(FullObjectAsString)
FileHandle.close()

FileHandle = open('Hal9000.json', 'r')
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