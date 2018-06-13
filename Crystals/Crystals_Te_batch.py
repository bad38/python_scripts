from pymongo import MongoClient 
from pprint import pprint 
import json 
import bson
import collections 
import Library_JsonLoad

client = MongoClient() 
db = client.cdb 
collection = db.sandbox

#Number_of_Te_batch = int(raw_input("(Te_batch+1): "))

def Search_by_Crystals_Te_batch(Number_of_Te_batch):
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
	batch = str(Te_batch)

	for Te_batch in db.sandbox.find({"Te_batch": batch}):
		Te_batchjsonOK = convert(Te_batch)
	
		FullObject.append(Te_batchjsonOK)

	FullObjectAsString = json.dumps( FullObject , indent=4) 
     
	FileHandle = open('json_files/Crystals_found_by_Te_batch.json', 'w')
	FileHandle.write(FullObjectAsString)
	FileHandle.close()

	FileHandle = open('json_files/Crystals_found_by_Te_batch.json', 'r')
	FullObjectAsStringFromFile = FileHandle.read()
	FileHandle.close()

	FullObjectFromFile = Library_JsonLoad.Main(
		FullObjectAsStringFromFile,
		ForceAscii = True,
	)

#Search_by_Crystals_life_in_cavern(Number_of_Days)