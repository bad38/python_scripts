from pymongo import MongoClient 
from pprint import pprint 
import json 
import bson
import collections 
import Library_JsonLoad

client = MongoClient() 
db = client.cdb 
collection = db.sandbox

#Number_of_Days = int(raw_input("(Number_of_Days+1): "))

def Search_by_Crystals_life_in_cavern(Number_of_Days):
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
	Day = str(Number_of_Days)

	for Days in range(Number_of_Days): 
		for life_in_cavern in db.sandbox.find({"life_in_cavern": Day}):
			life_in_cavernjsonOK = convert(life_in_cavern)
		

			FullObject.append(life_in_cavernjsonOK)

	FullObjectAsString = json.dumps( FullObject , indent=4) 
     
	FileHandle = open('json_files/Crystals_found_by_life_in_cavern.json', 'w')
	FileHandle.write(FullObjectAsString)
	FileHandle.close()

	FileHandle = open('json_files/Crystals_found_by_life_in_cavern.json', 'r')
	FullObjectAsStringFromFile = FileHandle.read()
	FileHandle.close()

	FullObjectFromFile = Library_JsonLoad.Main(
		FullObjectAsStringFromFile,
		ForceAscii = True,
	)

#Search_by_Crystals_life_in_cavern(Number_of_Days)