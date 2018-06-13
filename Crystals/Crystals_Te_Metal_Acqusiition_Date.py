from pymongo import MongoClient 
from pprint import pprint 
import json 
import bson
import collections 
import Library_JsonLoad

client = MongoClient() 
db = client.cdb 
collection = db.sandbox 

#first = int(raw_input("(first_year_int): ")) 
#second = int(raw_input("(last_year_int+1): "))
#third = int(raw_input("(first_month_int): ")) 
#fourth = int(raw_input("(last_month_int+1): ")) 
#fifth = int(raw_input("(first_day_int): ")) 
#sixth = int(raw_input("(last_day_int+1): ")) 

def Search_by_Te_metal_acqusiition_date(first,second,third,fourth,fifth,sixth):
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

	for Year in range(first,second):
		for Month in range(third,fourth): 
			for Day in range(fifth,sixth):
				DateString = str(Year) + '-' + str(Month) + '-' + str(Day)
 
				for Te_metal_acqusiiton_date in db.sandbox.find({"Te_metal_acqusiiton_date": DateString}):
					Te_metal_acqusiiton_datejsonOK = convert(Te_metal_acqusiiton_date)
					
					FullObject.append(Te_metal_acqusiiton_datejsonOK)

	FullObjectAsString = json.dumps( FullObject , indent=4) 
      
	FileHandle = open('json_files/Crystals_found_by_Te_Metal_Acqusiition_Date.json', 'w')
	FileHandle.write(FullObjectAsString)
	FileHandle.close()

	FileHandle = open('json_files/Crystals_found_by_Te_Metal_Acqusiition_Date.json', 'r')
	FullObjectAsStringFromFile = FileHandle.read()
	FileHandle.close()

	FullObjectFromFile = Library_JsonLoad.Main(
		FullObjectAsStringFromFile,
		ForceAscii = True,
	)

#Search_by_Te_metal_acqusiition_date(first,second,third,fourth,fifth,sixth)