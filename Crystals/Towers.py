from pymongo import MongoClient 
from pprint import pprint 
from bson.objectid import ObjectId
import csv
import json 
import bson
import collections 
import Library_JsonLoad 
import matplotlib.pyplot as plt
import numpy as np

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
BeachBoyz = [] 
Backstreet= []
for Number in range(1,20):
	Tower_Number = 'Tower' + ' ' + str(Number) 
	for fullName in db.sandbox.find({"fullName": Tower_Number}):
		for crystalFloors in fullName["crystalFloors"]: 
			value_of_intrest_1 = str(crystalFloors.get("hearts", "No Data")) 
			value_of_intrest_2 = str(crystalFloors.get("clubs", "No Data")) 
			value_of_intrest_3 = str(crystalFloors.get("spades", "No Data")) 
			value_of_intrest_4 = str(crystalFloors.get("diamonds", "No Data")) 
	
			if value_of_intrest_1 != "None":
				for _id in db.sandbox.find({"_id": ObjectId(value_of_intrest_1)}): 
					crystal_age_1 = str(_id.get("crystal_age", "No Data"))
					Rank_1 = str(_id.get("rank", "No Data")) 
					Suit_1 = str(_id.get("suit", "No Data"))
					if Rank_1 == '1': 
						Rank_1 = 1 
					elif Rank_1 == '2':  
						Rank_a = 2
					elif Rank_1 == '3':
						Rank_a = 3
					elif Rank_1 == '4':
						Rank_a  = 4
					elif Rank_1 == '5':
						Rank_a = 5
					elif Rank_1 == '6':
						Rank_a = 6
					elif Rank_1 == '7':
						Rank_a = 7
					elif Rank_1 == '8':
						Rank_a = 8
					elif Rank_1 == '9':
						Rank_a = 9
					elif Rank_1 == '10':
						Rank_a = 10
					elif Rank_1 == 'J':
						Rank_a = 11
					elif Rank_1 == 'Q':
						Rank_a = 12
					elif Rank_1 == 'K':
						Rank_a = 13
					else:
						Rank_a = "0"	 
					if Suit_1 == 'diamonds':
						Suit_a = "4"
					elif Suit_1 == 'spades':
						Suit_a = "3"
					elif Suit_1 == 'hearts':
						Suit_a = "1"
					elif Suit_1 == 'clubs':
						Suit_a = "2" 
					else: 
						Suit_a = "0" 		
					
					for age_1 in db.sandbox.find({"_id": ObjectId(crystal_age_1)}):
						age_a = convert(age_1)
						FullObject.append(age_a)
						Xtal_current_age_1 = str(age_1.get("Xtal_current_age", "No Data")) 
						if Xtal_current_age_1 != "NAN":
							Channel_1 = (int(Number) - 1) * (52) + (int(Suit_a) - 1) * (13) + int(Rank_a)
							Xtal_1 = str(Channel_1) + ' ' + str(Xtal_current_age_1) 
							Backstreet.append(str(Channel_1)) 
							BeachBoyz.append(str(Xtal_current_age_1))
							#Backstreet.append(Xtal_1)
							#FullObject.append(Xtal_current_age_1)
			
			if value_of_intrest_2 != "None":
				for _id2 in db.sandbox.find({"_id": ObjectId(value_of_intrest_2)}): 
					crystal_age_2 = str(_id2.get("crystal_age", "No Data"))  
					Rank_2 = str(_id.get("rank", "No Data")) 
					Suit_2 = str(_id.get("suit", "No Data"))
					
					if Rank_2 == '1': 
						Rank_b = 1 
					elif Rank_2 == '2':  
						Rank_b = 2
					elif Rank_2 == '3':
						Rank_b = 3
					elif Rank_2 == '4':
						Rank_b  = 4
					elif Rank_2 == '5':
						Rank_b = 5
					elif Rank_2 == '6':
						Rank_b = 6
					elif Rank_2 == '7':
						Rank_b = 7
					elif Rank_2 == '8':
						Rank_b = 8
					elif Rank_2 == '9':
						Rank_b = 9
					elif Rank_2 == '10':
						Rank_b = 10
					elif Rank_2 == 'J':
						Rank_b = 11
					elif Rank_2 == 'Q':
						Rank_b = 12
					elif Rank_2 == 'K':
						Rank_b = 13
					else:
						Rank_b = "0"	 
					if Suit_2 == 'diamonds':
						Suit_b = "4"
					elif Suit_2 == 'spades':
						Suit_b = "3"
					elif Suit_2 == 'hearts':
						Suit_b = "1"
					elif Suit_2 == 'clubs':
						Suit_b = "2" 
					else: 
						Suit_b = "0" 
											
					for age_2 in db.sandbox.find({"_id": ObjectId(crystal_age_2)}):
						age_b = convert(age_2)
						FullObject.append(age_b)
						Xtal_current_age_2 = str(age_2.get("Xtal_current_age", "No Data")) 
						if Xtal_current_age_2 != "NAN":
							Channel_2 = (int(Number) - 1) * (52) + (int(Suit_b) - 1) * (13) + int(Rank_b)
							Xtal_2 = str(Channel_2) + ' ' + str(Xtal_current_age_2)
							#Backstreet.append(Xtal_2)
							Backstreet.append(str(Channel_2)) 
							BeachBoyz.append(str(Xtal_current_age_2))
			
			if value_of_intrest_3 != "None":
				for _id3 in db.sandbox.find({"_id": ObjectId(value_of_intrest_3)}):
					crystal_age_3 = str(_id3.get("crystal_age", "No Data"))
					Rank_3 = str(_id.get("rank", "No Data")) 
					Suit_3 = str(_id.get("suit", "No Data")) 
					
					if Rank_3 == '1': 
						Rank_c = 1 
					elif Rank_3 == '2':  
						Rank_c = 2
					elif Rank_3 == '3':
						Rank_c = 3
					elif Rank_3 == '4':
						Rank_c  = 4
					elif Rank_3 == '5':
						Rank_c = 5
					elif Rank_3 == '6':
						Rank_c = 6
					elif Rank_3 == '7':
						Rank_c = 7
					elif Rank_3 == '8':
						Rank_c = 8
					elif Rank_3 == '9':
						Rank_c = 9
					elif Rank_3 == '10':
						Rank_c = 10
					elif Rank_3 == 'J':
						Rank_c = 11
					elif Rank_3 == 'Q':
						Rank_c = 12
					elif Rank_3 == 'K':
						Rank_c = 13
					else:
						Rank_c = "0"	 
					if Suit_3 == 'diamonds':
						Suit_c = "4"
					elif Suit_3 == 'spades':
						Suit_c = "3"
					elif Suit_3 == 'hearts':
						Suit_c = "1"
					elif Suit_3 == 'clubs':
						Suit_c = "2" 
					else: 
						Suit_c = "0" 
										
					for age_3 in db.sandbox.find({"_id": ObjectId(crystal_age_3)}):
						age_c = convert(age_3)
						FullObject.append(age_c)
						Xtal_current_age_3 = str(age_3.get("Xtal_current_age", "No Data")) 
						if Xtal_current_age_3 != "NAN":
							Channel_3 = (int(Number) - 1) * (52) + (int(Suit_c) - 1) * (13) + int(Rank_c)
							Xtal_3 = str(Channel_3) + ' ' + str(Xtal_current_age_3)
							Backstreet.append(str(Channel_3))
							BeachBoyz.append(str(Xtal_current_age_3))
						#	Backstreet.append(Xtal_3)
						#	FullObject.append(Xtal_current_age_3)
			
			if value_of_intrest_4 != "None":
				for _id4 in db.sandbox.find({"_id": ObjectId(value_of_intrest_4)}):
					crystal_age_4 = str(_id4.get("crystal_age", "No Data"))
					Rank_4 = str(_id.get("rank", "No Data")) 
					Suit_4 = str(_id.get("suit", "No Data"))
					
					if Rank_4 == '1': 
						Rank_d = 1 
					elif Rank_4 == '2':  
						Rank_d = 2
					elif Rank_4 == '3':
						Rank_d = 3
					elif Rank_4 == '4':
						Rank_d  = 4
					elif Rank_4 == '5':
						Rank_d = 5
					elif Rank_4 == '6':
						Rank_d = 6
					elif Rank_4 == '7':
						Rank_d = 7
					elif Rank_4 == '8':
						Rank_d = 8
					elif Rank_4 == '9':
						Rank_d = 9
					elif Rank_4 == '10':
						Rank_d = 10
					elif Rank_4 == 'J':
						Rank_d = 11
					elif Rank_4 == 'Q':
						Rank_d = 12
					elif Rank_4 == 'K':
						Rank_d = 13
					else:
						Rank_d = "0"	 
					if Suit_4 == 'diamonds':
						Suit_d = "4"
					elif Suit_4 == 'spades':
						Suit_d = "3"
					elif Suit_4 == 'hearts':
						Suit_d = "1"
					elif Suit_4 == 'clubs':
						Suit_d = "2" 
					else: 
						Suit_d = "0" 
					
					for age_4 in db.sandbox.find({"_id": ObjectId(crystal_age_4)}):
						age_d = convert(age_4)
						FullObject.append(age_d)
						Xtal_current_age_4 = str(age_4.get("Xtal_current_age", "No Data")) 
						if Xtal_current_age_4 != "NAN":
							Channel_4 = (int(Number) - 1) * (52) + (int(Suit_d) - 1) * (13) + int(Rank_d)
							Xtal_4 = str(Channel_4) + ' ' + str(Xtal_current_age_4) 
							Backstreet.append(str(Channel_4)) 
							BeachBoyz.append(str(Xtal_current_age_4))
						#	Backstreet.append(Xtal_4)						
						#	FullObject.append(Xtal_current_age_4)
					

#print(Backstreet) 

Hal9000 = map(int, Backstreet)
Hal9001 = map(int, BeachBoyz)

#np.savetxt("FooDog.csv", Hal9000, delimiter=",")
#np.savetxt("FooDog2.csv", Hal9001, delimiter=",")

fig = plt.figure()

x_H = []

a = {} 
b = {}

with open('Po210Rates2.txt') as f: 
	for line in f: 
		(key, val_1, val_2) = line.split() 
		a[int(key)] = val_1
		b[int(key)] = val_2 
	
	
for key, val_1 in a.iteritems(): 
		print key, val_1	
#a_value = str(b.get("834", "No Data"))
		
#print (a_value)
"""
with open('Po210Rates2.txt') as f: 
	for line in f: 
		parts = line.split()
		if len(parts) > 1: 
			print parts[2]
			x = parts[2]
"""



"""
with open('Po210Rates2.txt') as f:
    lines = f.readlines()
    x = [line.split()[0] for line in lines]
    y = [line.split()[1] for line in lines] 
	#z = [line.split()[2] for line in lines] 
"""	
#x_a = str(x) + ' ' + str(y)
	#x_b = str(x) + ' ' + str(z) 
	
	
#np.savetxt("Critical.txt", x)	
	
#D = str(x) + str(y)
	
#x_H.append(D)

"""	
if Hal9000 = x:

	plt.plot(y, Hal9001, 'ro') 
	plt.axis([0, 988, 0, .1])
	plt.show()
"""
"""
np.savetxt("Book.txt", x, delimiter='')
np.savetxt("Book2.txt", x, delimiter='')

ax1 = fig.add_subplot(111)

ax1.set_title("Xtal Age vs. Channel")    
ax1.set_xlabel('Channel')
ax1.set_ylabel('Xtal_current_age')

#ax1.plot(data['x'], data['y'], color='r', label='the data')
plt.scatter(Hal9000,Hal9001)
plt.axis([0, 1000, 0, 2000])
plt.show()
"""



