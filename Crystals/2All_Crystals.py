from pymongo import MongoClient 
from pprint import pprint 
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
			#FullObject.append(value_of_intrest_1) 
			Florance = str(Number) + ' ' + str(value_of_intrest_1) + ' ' +  str(Number) + ' ' + str(value_of_intrest_2) + ' ' + str(Number) + ' ' + str(value_of_intrest_3) + ' ' + str(Number) + ' ' + str(value_of_intrest_4)  
			#FullObject.append(value_of_intrest_1) 
			#FullObject.append(value_of_intrest_2) 
			#FullObject.append(value_of_intrest_3) 
			#FullObject.append(value_of_intrest_4)
			FullObject.append(Florance)
"""
			ID_1 = str(Tower_Number) + ' suit: " +  
			ID_2 =
			ID_3 =
			ID_4 =
"""
"""
			ID_1 = 'ObjectId(' + value_of_intrest_1 + ')' 
			ID_2 = 'ObjectId(' + value_of_intrest_2 + ')' 
			ID_3 = 'ObjectId(' + value_of_intrest_3 + ')' 
			ID_4 = 'ObjectId(' + value_of_intrest_4 + ')'
"""				
			
		
		 
"""
			print (ID_1) 
			print (ID_2) 
			print (ID_3) 
			print (ID_4)

"""
			
"""
			for hearts in crystalFloors"hearts"]: 
				heartsjsonOK = convert(hearts) 
				FullObject.append(heartssjsonOK)
			for clubs in crystalFloors["clubs"]: 
				clubsjsonOK = convert(clubs) 
				FullObject.append(clubsjsonOK)
			for spades in crystalFloors["spades"]: 
				spadesjsonOK = convert(spades) 
				FullObject.append(spadesjsonOK)
			for diamonds in crystalFloors["diamonds"]: 
				diamondsjsonOK = convert(diamonds)
				FullObject.append(diamondsjsonOK) 

		
"""		
			
"""
			+ ' ' + value_of_intrest_2 + ' ' + value_of_intrest_3 + ' ' + value_of_intrest_4
"""
			
"""        
		
for name in db.sandbox.find({"name": "Crystal, Glued"}): 
	namejsonOK = convert(name) 
		
	FullObject.append(namejsonOK)
"""
	
FullObjectAsString = json.dumps( FullObject , indent=4) 

FileHandle = open('Somebody.json', 'w')
FileHandle.write(FullObjectAsString)
FileHandle.close()

FileHandle = open('Somebody.json', 'r')
FullObjectAsStringFromFile = FileHandle.read()
FileHandle.close()

FullObjectFromFile = Library_JsonLoad.Main(
	FullObjectAsStringFromFile,
	ForceAscii = True,
) 


"""
All_Items = []  
for Sally in FullObjectFromFile: 	
	value_of_intrest_1 = Sally.get("crystalFloors", "No Data")

	All_Items.append(value_of_intrest_1) 

#pprint (All_Items) 
print (All_Items.sort())

All_ItemsAsString = json.dumps( All_Items , indent=4) 

FileHandle = open('Test3_ID.json', 'w')
FileHandle.write(All_ItemsAsString)
FileHandle.close() 

FileHandle = open('Test3_ID.json', 'r')
All_ItemsAsStringFromFile = FileHandle.read()
FileHandle.close()


All_ItemsFromFile = Library_JsonLoad.Main(
	All_ItemsAsStringFromFile,
	ForceAscii = True,
) 

Violet = []

#for Robbie_chan in All_ItemsFromFile: 
	#value_of_intrest_2 = Robbie_chan("hearts") 
#	print (Robbie_chan.sort())
"""