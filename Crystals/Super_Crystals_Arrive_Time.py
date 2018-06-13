from pymongo import MongoClient 
from pprint import pprint 
import json 
import bson
import collections 
import Library_JsonLoad

client = MongoClient() 
db = client.cdb 
collection = db.sandbox 

first = int(raw_input("(first_year_int): ")) 
second = int(raw_input("(last_year_int+1): "))
third = int(raw_input("(first_month_int): ")) 
fourth = int(raw_input("(last_month_int+1): ")) 
fifth = int(raw_input("(first_day_int): ")) 
sixth = int(raw_input("(last_day_int+1): "))

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

				for Number in range(100,1200):
					Crystal_Number = 'Crystal, Glued' + ' ' + str(Number) 

					for name in db.sandbox.find({"name": Crystal_Number}, {"arrived_at_LNGS": DateString}):
						namejsonOK = convert(name)
	
						FullObject.append(namejsonOK) 
		
				for name in db.sandbox.find({"name": "Crystal, Glued"}, {"arrived_at_LNGS": DateString}): 
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

for item in FullObjectFromFile: 
	for key, value in item.iteritems(): 
		print key, value 

