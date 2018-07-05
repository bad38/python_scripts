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
Backstreet_1= [] 
Backstreet_2= [] 
Backstreet_3= [] 
Backstreet_4= []
AllStar = []
Vida = []
C_d = [] 
Jimmy_Mack = [] 
a = {} 
b = {}
with open('Po210Rates2.txt') as f: 
	for line in f: 
		(key, val_1, val_2) = line.split() 
		a[int(key)] = val_1
		b[int(key)] = val_2 
			
		for key, val_1 in a.iteritems():  
			#for i in range(key):
				#if str(key) == Night[i]:
			
					#print (str(key) + ' ' + str(a[int(key)]) + ' ' + str(Night[int(i)])) 
			
					#C_d.append(str(val_1))
					#Backstreet_1.append(str(Channel_1)) 
					#BeachBoyz.append(str(Te_batch_1))

			for Bagel in range(1,20):
				TowerNumber = 'Tower' + ' ' + str(Bagel) 
				for fullName in db.sandbox.find({"fullName": TowerNumber}):
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
								
								if Bagel == 1: 
									Number = "6"
								elif Bagel == 2:  
									Number = "19"
								elif Bagel == 3:
									Number = "5"
								elif Bagel == 4:
									Number  = "14"
								elif Bagel == 5:
									Number = "9"
								elif Bagel == 6:
									Number = "7"
								elif Bagel == 7:
									Number = "13"
								elif Bagel == 8:
									Number = "10"
								elif Bagel == 9:
									Number = "18"
								elif Bagel == 10:
									Number = "3"
								elif Bagel == 11:
									Number = "1"
								elif Bagel == 12:
									Number = "8"
								elif Bagel == 13:
									Number = "16"
								elif Bagel == 14:
									Number = "17"	 
								elif Bagel == 15:
									Number = "15"
								elif Bagel == 16:
									Number = "5"
								elif Bagel == 17:
									Number = "11"
								elif Bagel == 18:
									Number = "12" 
								elif Bagel == 19: 
									Number = "2" 	
								else: 
									Number = "0"
								
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
									#FullObject.append(age_a)
									Te_batch_1 = str(age_1.get("Te_batch", "No Data")) 
									Channel_1 = str((int(Number) - 1) * (52) + (1 - 1) * (13) + int(Rank_a))
									Jimmy_Mack.append(Channel_1)
									if Te_batch_1 != "NAN":
										if val_1 == Channel_1:
											#Channel_1 = str((int(Number) - 1) * (52) + (int(Suit_a) - 1) * (13) + int(Rank_a))
											#ch_1 = set(Channel_1)
											Xtal_1 = str(Channel_1) + ' ' + str(Te_batch_1) 
											#Jimmy_Mack.append(Channel_1)
											a = {} 
											b = {}
											
											Jimmy_Mack.append(Channel_1) 
											FullObject.append(Te_batch_1)
											
											AllStar_1 = str(Channel_1) + ' ' + str(Te_batch_1) + ' ' + str(key) + ' ' + str(val_1)
											AllStar.append(AllStar_1)
										
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
												

								if Bagel == 1: 
									Number = "6"
								elif Bagel == 2:  
									Number = "19"
								elif Bagel == 3:
									Number = "5"
								elif Bagel == 4:
									Number  = "14"
								elif Bagel == 5:
									Number = "9"
								elif Bagel == 6:
									Number = "7"
								elif Bagel == 7:
									Number = "13"
								elif Bagel == 8:
									Number = "10"
								elif Bagel == 9:
									Number = "18"
								elif Bagel == 10:
									Number = "3"
								elif Bagel == 11:
									Number = "1"
								elif Bagel == 12:
									Number = "8"
								elif Bagel == 13:
									Number = "16"
								elif Bagel == 14:
									Number = "17"	 
								elif Bagel == 15:
									Number = "15"
								elif Bagel == 16:
									Number = "5"
								elif Bagel == 17:
									Number = "11"
								elif Bagel == 18:
									Number = "12" 
								elif Bagel == 19: 
									Number = "2"  
								else: 
									Number = "0"

								for age_2 in db.sandbox.find({"_id": ObjectId(crystal_age_2)}):
									age_b = convert(age_2)
									#FullObject.append(age_b)
									Te_batch_2 = str(age_2.get("Te_batch", "No Data")) 
									Channel_2 = str((int(Number) - 1) * (52) + (2 - 1) * (13) + int(Rank_b))
									Jimmy_Mack.append(Channel_2)
									if Te_batch_2 != "NAN":
										#Channel_2 = str((int(Number) - 1) * (52) + (2 - 1) * (13) + int(Rank_b))
										Xtal_2 = str(Channel_2) + ' ' + str(Te_batch_2)
										#print (Channel_2)
										
										a = {} 
										b = {}
										Jimmy_Mack.append(Channel_2)
										FullObject.append(Te_batch_2)
										
										AllStar_2 = str(Channel_2) + ' ' + str(Te_batch_2) 
										#AllStar.append(AllStar_2)

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
										
								if Bagel == 1: 
									Number = "6"
								elif Bagel == 2:  
									Number = "19"
								elif Bagel == 3:
									Number = "5"
								elif Bagel == 4:
									Number  = "14"
								elif Bagel == 5:
									Number = "9"
								elif Bagel == 6:
									Number = "7"
								elif Bagel == 7:
									Number = "13"
								elif Bagel == 8:
									Number = "10"
								elif Bagel == 9:
									Number = "18"
								elif Bagel == 10:
									Number = "3"
								elif Bagel == 11:
									Number = "1"
								elif Bagel == 12:
									Number = "8"
								elif Bagel == 13:
									Number = "16"
								elif Bagel == 14:
									Number = "17"	 
								elif Bagel == 15:
									Number = "15"
								elif Bagel == 16:
									Number = "5"
								elif Bagel == 17:
									Number = "11"
								elif Bagel == 18:
									Number = "12" 
								elif Bagel == 19: 
									Number = "2"  
								else: 
									Number = "0"				
													
								for age_3 in db.sandbox.find({"_id": ObjectId(crystal_age_3)}):
									age_c = convert(age_3)
									#FullObject.append(age_c)
									Te_batch_3 = str(age_3.get("Te_batch", "No Data")) 
									Channel_3 = str((int(Number) - 1) * (52) + (3 - 1) * (13) + int(Rank_c))
									Jimmy_Mack.append(Channel_3)
									if Te_batch_3 != "NAN":
										#Channel_3 = str((int(Number) - 1) * (52) + (3 - 1) * (13) + int(Rank_c))
										Xtal_3 = str(Channel_3) + ' ' + str(Te_batch_3)
										#print (Channel_3)
										
										a = {} 
										b = {}
										
										Jimmy_Mack.append(Channel_3)
										FullObject.append(Te_batch_3) 
										
										AllStar_3 = str(Channel_3) + ' ' + str(Te_batch_3) 
										#AllStar.append(AllStar_3)

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
								
								if Bagel == 1: 
									Number = "6"
								elif Bagel == 2:  
									Number = "19"
								elif Bagel == 3:
									Number = "5"
								elif Bagel == 4:
									Number  = "14"
								elif Bagel == 5:
									Number = "9"
								elif Bagel == 6:
									Number = "7"
								elif Bagel == 7:
									Number = "13"
								elif Bagel == 8:
									Number = "10"
								elif Bagel == 9:
									Number = "18"
								elif Bagel == 10:
									Number = "3"
								elif Bagel == 11:
									Number = "1"
								elif Bagel == 12:
									Number = "8"
								elif Bagel == 13:
									Number = "16"
								elif Bagel == 14:
									Number = "17"	 
								elif Bagel == 15:
									Number = "15"
								elif Bagel == 16:
									Number = "5"
								elif Bagel == 17:
									Number = "11"
								elif Bagel == 18:
									Number = "12" 
								elif Bagel == 19: 
									Number = "2"  
								else: 
									Number = "0"	
								for age_4 in db.sandbox.find({"_id": ObjectId(crystal_age_4)}):
									age_d = convert(age_4)
									#FullObject.append(age_d)
									Te_batch_4 = str(age_4.get("Te_batch", "No Data")) 
									Channel_4 = str((int(Number) - 1) * (52) + (4 - 1) * (13) + int(Rank_d)) 
									#Jimmy_Mack.append(Channel_4)
									if Te_batch_4 != "NAN":
										Channel_4 = str((int(Number) - 1) * (52) + (4 - 1) * (13) + int(Rank_d))
										Xtal_4 = str(Channel_4) + ' ' + str(Te_batch_4) 		
										#print (Channel_4)
										a = {} 
										b = {} 
										Jimmy_Mack.append(Channel_4)
										FullObject.append(Te_batch_4) 
										
										AllStar_4 = str(Channel_4) + ' ' + str(Te_batch_4) 
										#AllStar.append(AllStar_4)
									
#print(Backstreet) 

#Hal9000 = map(int, FullObject)
#Hal9001 = map(int, Jimmy_Mack)

#print (len(list(set(Backstreet))))
#print (len(FullObject))
#print (len(Jimmy_Mack))
print (AllStar)
#print (len(set(Jimmy_Mack)))
#Day = set(Jimmy_Mack)
#Night = (sorted(Day, key=int))
#Day_2 = set(AllStar) 
#Night_2 = (sorted(Day_2, key=int))
#print (sorted(Day, key=int))
#print len(Day)
#print (len(set((Jimmy_Mack)))) 
#print (Night_2)
#print (len(Night_2)) 


	
"""
fig = plt.figure()

ax1 = fig.add_subplot(111)

ax1.set_title("Te_batch")    
ax1.set_xlabel('Te_batch [Number]')
ax1.set_ylabel("Number of Bolometers")
#plt.hist(Hal9000, bins=988, color='b', label='Crystals')
plt.scatter(Hal9000,Hal9001)
#plt.axis([10001, 10013, 0, 150])
plt.show()
"""




"""
with open('Po210Rates2.txt') as f: 
	for line in f: 
	(key, val_1, val_2) = line.split() 
	a[int(key)] = val_1
	b[int(key)] = val_2 
									
		for key, val_1 in a.iteritems():  
			#print str(Channel_3) + ' ' + str(key) + ' ' + str(val_1)
			C_d.append(str(val_1))
			#print (Channel_1)
			Backstreet_1.append(str(Channel_1)) 
			BeachBoyz.append(str(Te_batch_1))
"""











"""
fig = plt.figure()

ax1 = fig.add_subplot(111)

ax1.set_title("Te_batch vs. Livetime")    
ax1.set_xlabel('Te_batch [Number]')
ax1.set_ylabel('Livetime')
plt.hist(Hal9000, bins=988, color='b', label='Crystals')
#plt.scatter(Hal9000,Hal9001)
plt.show()

"""