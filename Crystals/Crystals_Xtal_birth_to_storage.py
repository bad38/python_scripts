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

def Search_by_Crystals_Xtal_birth_to_storage(Number_of_Days):
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
		for Xtal_birth_to_storage in db.sandbox.find({"Xtal_birth_to_storage": Day}):
			Xtal_birth_to_storagejsonOK = convert(Xtal_birth_to_storage)

			FullObject.append(Te_aqc_to_Xtal_storagejsonOK)

	FullObjectAsString = json.dumps( FullObject , indent=4) 
     
	FileHandle = open('json_files/Crystals_found_by_Xtal_birth_to_storage.json', 'w')
	FileHandle.write(FullObjectAsString)
	FileHandle.close()

	FileHandle = open('json_files/Crystals_found_by_Xtal_birth_to_storage.json', 'r')
	FullObjectAsStringFromFile = FileHandle.read()
	FileHandle.close()

	FullObjectFromFile = Library_JsonLoad.Main(
		FullObjectAsStringFromFile,
		ForceAscii = True,
	)

#Search_by_Crystals_Xtal_birth_to_storage(Number_of_Days)