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

for Number in range(100,1200):
	Crystal_Number = 'Crystal, Glued' + ' ' + str(Number) 

	for name in db.sandbox.find({"name": Crystal_Number}, {"locationInParent": True}):
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

All_Items = [] 
Violet = [] 
for Sally in FullObjectFromFile: 	
	value_of_intrest_1 = Sally.get("rank", "No Data")
	value_of_intrest_2 = Sally.get("parentId", "No Data") 
	value_of_intrest_3 = Sally.get("suit", "No Data") 
	
	if value_of_intrest_2 == '5279067dd1b74a5a460b856f': 
		Tower = 0 
	elif value_of_intrest_2 == '51c2d8bfd1b74a2d56c21dd7':  
		Tower =	6
	elif value_of_intrest_2 == '51c2f550d1b74a2d56c21fca':
		Tower = 19
	elif value_of_intrest_2 == '51c2f8abd1b74a2d56c22181':
		Tower = 5
	elif value_of_intrest_2 == '51c85601d1b74a059d0ae661':
		Tower = 14
	elif value_of_intrest_2 == '51c85cfbd1b74a059d0ae7a4':
		Tower = 9
	elif value_of_intrest_2 == '524d4b81d1b74a300f90addf':
		Tower = 7
	elif value_of_intrest_2 == '524c6c4cd1b74a300f90ab0f':
		Tower = 13
	elif value_of_intrest_2 == '524da3a6d1b74a300f90af24':
		Tower = 10
	elif value_of_intrest_2 == '524dbc4fd1b74a300f90b061':
		Tower = 18
	elif value_of_intrest_2 == '52937966d1b74a5171f4b253':
		Tower = 3
	elif value_of_intrest_2 == '529c9d06d1b74a056e760ba3':
		Tower = 1
	elif value_of_intrest_2 == '52a5acead1b74a1b758491c8':
		Tower = 6
	elif value_of_intrest_2 == '537c832dd1b74a1f1e8c7d9e':
		Tower = 16
	elif value_of_intrest_2 == '53c17877d1b74a36053434d1':
		Tower = 17
	elif value_of_intrest_2 == '5379dc3fd1b74a1f1e8c7c49':
		Tower = 15
	elif value_of_intrest_2 == '53d79a78d1b74a3605343a5e':
		Tower = 4
	elif value_of_intrest_2 == '53d7d0d2d1b74a3605343bac':
		Tower = 11
	elif value_of_intrest_2 == '53d7f7ecd1b74a3605343ca4':
		Tower = 12
	elif value_of_intrest_2 == '53e273c8d1b74a2a75e889fd':
		Tower = 2 
	else: 
		Tower = "Fernando"  
	if value_of_intrest_1 == '1': 
		Rank = 1 
	elif value_of_intrest_1 == '2':  
		Rank =	2
	elif value_of_intrest_1 == '3':
		Rank = 3
	elif value_of_intrest_1 == '4':
		Rank = 4
	elif value_of_intrest_1 == '5':
		Rank = 5
	elif value_of_intrest_1 == '6':
		Rank = 6
	elif value_of_intrest_1 == '7':
		Rank = 7
	elif value_of_intrest_1 == '8':
		Rank = 8
	elif value_of_intrest_1 == '9':
		Rank = 9
	elif value_of_intrest_1 == '10':
		Rank = 10
	elif value_of_intrest_1 == 'J':
		Rank = 11
	elif value_of_intrest_1 == 'Q':
		Rank = 12
	elif value_of_intrest_1 == 'K':
		Rank = 13
	else:
		Rank = "0"	 
	if value_of_intrest_3 == 'diamonds':
		Suit = "4"
	elif value_of_intrest_3 == 'spades':
		Suit = "3"
	elif value_of_intrest_3 == 'hearts':
		Suit = "1"
	elif value_of_intrest_3 == 'clubs':
		Suit = "2" 
	else: 
		Suit = "0" 
		
	Channel = (int(Tower) - 1) * (52) + (int(Suit - 1) * (13) + int(Rank)	

	Vera ='Tower : ' + str(Tower) + ' rank: ' + str(Rank) + ' suit: ' + str(Suit)
	#	Vera = 'ObjectId(' + str(value_of_intrest) + ')'
	All_Items.append(Vera) 

pprint (All_Items) 

All_ItemsAsString = json.dumps( All_Items , indent=4) 

FileHandle = open('Test_ID.json', 'w')
FileHandle.write(All_ItemsAsString)
FileHandle.close()



	
	
"""	
	for Alejandro in db.sandbox.find({"_id": Vera}): 
		idjsonOK = convert(id) 
		
		Violet.append(idjsonOK)
"""
	
		
"""
VioletAsString = json.dumps( Violet , indent=4) 

FileHandle = open('Violet.json', 'w')
FileHandle.write(VioletAsString)
FileHandle.close()

FileHandle = open('Violet.json', 'r')
VioletAsStringFromFile = FileHandle.read()
FileHandle.close()

FullObjectFromFile = Library_JsonLoad.Main(
	VioletAsStringFromFile,
	ForceAscii = True,
) 

"""



"""

FileHandle = open('ID.json', 'w')
FileHandle.write(str(All_Items))
FileHandle.close()	
	
for Emil in db.sandbox.find({"_id": value_of_intrest_1}):
	value_of_intrest_2 = Emil["shipped"]
	if value_of_intrest_2 != "NAN": 
			All_Items.append(value_of_intrest) 
			print (value_of_intrest_2)
""" 
	 

"""
       if value_of_intrest != "NAN": 
               All_Items.append(value_of_intrest) 
						
				
				
	Fernando = value_of_intrest_2 - value_of_intrest_1 

	a = datetime.strptime(value_of_intrest_1, "%Y-%m-%d")
	b = datetime.strptime(value_of_intrest_2, "%Y-%m-%d")
	Fernando = abs((b - a).days
		
"""
		
		
		
		
		
		
		
		
		
		
		
		
		
"""
FileHandle = open('Hal9000', 'r')
FullObjectAsStringFromFile = FileHandle.read()
FileHandle.close()

FullObjectFromFile = Library_JsonLoad.Main(
	FullObjectAsStringFromFile,
	ForceAscii = True,
)  

"""
"""
All_Items = [] 
for Sally in FullObjectFromFile: 
	value_of_intrest = Sally["_id"] 
	
        if value_of_intrest != "NAN": 
                All_Items.append(value_of_intrest) 
	
	

Hal9000 = map(int, All_Items)

print (Hal9000)

plt.hist(Hal9000, bins=200, histtype='stepfilled', normed=True, color='b', label='Crystals') 
plt.title("Xtal Current Age") 
plt.xlabel("Time [Days]") 
plt.ylabel("Percentage of Total Crystals") 
plt.legend()
plt.show()
"""