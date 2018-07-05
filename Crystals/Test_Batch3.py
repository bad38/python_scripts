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
Fading = [] 
Tower_Mapping = [6,19,5,14,9,7,13,10,18,3,1,8,16,17,15,5,11,12,2]
Rank_Mapping = [1,2,3,4,5,6,7,8,9,10,11,12,13]

for Bagel in range(1,20):	
	TowerNumber = 'Tower' + ' ' + str(Bagel) 
	for fullName in db.sandbox.find({"fullName": TowerNumber}):
		if TowerNumber == "Tower 7":
			for _id in db.sandbox.find({"_id": ObjectId('524c6c4cd1b74a300f90ab0f')}):  
				value_of_intrest_a = str(crystalFloors.get("hearts", "No Data")) 
				value_of_intrest_b = str(crystalFloors.get("clubs", "No Data")) 
				value_of_intrest_c = str(crystalFloors.get("spades", "No Data")) 
				value_of_intrest_d = str(crystalFloors.get("diamonds", "No Data")) 
				
				if value_of_intrest_a != "None":
					for _id_a in db.sandbox.find({"_id": ObjectId(value_of_intrest_a)}): 
						crystal_age_a = str(_id_a.get("crystal_age", "No Data"))
						Rank_a = str(_id_a.get("rank", "No Data")) 
						Suit_a = str(_id_a.get("suit", "No Data"))						
						Number = Tower_Mapping[int(Bagel)]
				
						if Rank_a == 'A': 
							Rank_r = 1 
						elif Rank_a == 'J':
							Rank_r = 11
						elif Rank_a == 'Q':
							Rank_r = 12
						elif Rank_a == 'K':
							Rank_r = 13
						else:
							Rank_r = Rank_Mapping[int(Rank_a)]	 
						if Suit_a == 'diamonds':
							Suit_r = "4"
						elif Suit_a == 'spades':
							Suit_r = "3"
						elif Suit_a == 'hearts':
							Suit_r = "1"
						elif Suit_a == 'clubs':
							Suit_r = "2" 
						else: 
							Suit_r = "0" 		
						
						for age_a in db.sandbox.find({"_id": ObjectId(crystal_age_1)}):
							age_r = convert(age_a)
							Te_batch_a = str(age_a.get("Te_batch", "No Data")) 
							Channel_a = str((int(Number) - 1) * (52) + (1 - 1) * (13) + int(Rank_r))
							if Te_batch_a != "NAN":								 
								FullObject.append(Te_batch_a)								
								AllStar_a = str(Channel_a) + ' ' + str(Te_batch_a) 
								AllStar.append(AllStar_a)
				
				
				if value_of_intrest_b != "None":
					for _id_b in db.sandbox.find({"_id": ObjectId(value_of_intrest_b)}): 
						crystal_age_b = str(_id_b.get("crystal_age", "No Data"))
						Rank_b = str(_id_b.get("rank", "No Data")) 
						Suit_b = str(_id_b.get("suit", "No Data"))						
						Number = Tower_Mapping[int(Bagel)]
				
						if Rank_b == 'A': 
							Rank_s = 1 
						elif Rank_b == 'J':
							Rank_s = 11
						elif Rank_b == 'Q':
							Rank_s = 12
						elif Rank_b == 'K':
							Rank_s = 13
						else:
							Rank_s = Rank_Mapping[int(Rank_b)]	 
						if Suit_b == 'diamonds':
							Suit_s = "4"
						elif Suit_b == 'spades':
							Suit_s = "3"
						elif Suit_b == 'hearts':
							Suit_s = "1"
						elif Suit_b == 'clubs':
							Suit_s = "2" 
						else: 
							Suit_s = "0" 		
						
						for age_b in db.sandbox.find({"_id": ObjectId(crystal_age_b)}):
							age_s = convert(age_b)
							Te_batch_b = str(age_b.get("Te_batch", "No Data")) 
							Channel_b = str((int(Number) - 1) * (52) + (2 - 1) * (13) + int(Rank_s))
							if Te_batch_1 != "NAN":								 
								FullObject.append(Te_batch_b)								
								AllStar_b = str(Channel_b) + ' ' + str(Te_batch_b) 
								AllStar.append(AllStar_b) 

				if value_of_intrest_c != "None":
					for _id_c in db.sandbox.find({"_id": ObjectId(value_of_intrest_c)}): 
						crystal_age_c = str(_id_c.get("crystal_age", "No Data"))
						Rank_c = str(_id_c.get("rank", "No Data")) 
						Suit_c = str(_id_c.get("suit", "No Data"))						
						Number = Tower_Mapping[int(Bagel)]
				
						if Rank_c == 'A': 
							Rank_t = 1 
						elif Rank_c == 'J':
							Rank_t = 11
						elif Rank_c == 'Q':
							Rank_t = 12
						elif Rank_c == 'K':
							Rank_t = 13
						else:
							Rank_c = Rank_Mapping[int(Rank_c)]	 
						if Suit_c == 'diamonds':
							Suit_t = "4"
						elif Suit_c == 'spades':
							Suit_t = "3"
						elif Suit_c == 'hearts':
							Suit_t = "1"
						elif Suit_c == 'clubs':
							Suit_t = "2" 
						else: 
							Suit_t = "0" 		
						
						for age_c in db.sandbox.find({"_id": ObjectId(crystal_age_c)}):
							age_t = convert(age_c)
							Te_batch_c = str(age_c.get("Te_batch", "No Data")) 
							Channel_c = str((int(Number) - 1) * (52) + (3 - 1) * (13) + int(Rank_t))
							if Te_batch_c != "NAN":								 
								FullObject.append(Te_batch_c)								
								AllStar_c = str(Channel_c) + ' ' + str(Te_batch_c) 
								AllStar.append(AllStar_c) 

				if value_of_intrest_d != "None":
					for _id_d in db.sandbox.find({"_id": ObjectId(value_of_intrest_d)}): 
						crystal_age_d = str(_id_d.get("crystal_age", "No Data"))
						Rank_d = str(_id_d.get("rank", "No Data")) 
						Suit_d = str(_id_d.get("suit", "No Data"))						
						Number = Tower_Mapping[int(Bagel)]
				
						if Rank_d == 'A': 
							Rank_u = 1 
						elif Rank_d == 'J':
							Rank_u = 11
						elif Rank_d == 'Q':
							Rank_u = 12
						elif Rank_d == 'K':
							Rank_u = 13
						else:
							Rank_u = Rank_Mapping[int(Rank_d)]	  		
						
						for age_d in db.sandbox.find({"_id": ObjectId(crystal_age_d)}):
							age_u = convert(age_d)
							Te_batch_d = str(age_d.get("Te_batch", "No Data")) 
							Channel_d = str((int(Number) - 1) * (52) + (4 - 1) * (13) + int(Rank_u))
							if Te_batch_d != "NAN":								 
								FullObject.append(Te_batch_d)								
								AllStar_d = str(Channel_d) + ' ' + str(Te_batch_d) 
								AllStar.append(AllStar_d)								
				
				
		elif TowerNumber == "Tower 14": 
			for _id in db.sandbox.find({"_id": ObjectId('53c17877d1b74a36053434d1')}):  
				value_of_intrest_e = str(crystalFloors.get("hearts", "No Data")) 
				value_of_intrest_f = str(crystalFloors.get("clubs", "No Data")) 
				value_of_intrest_g = str(crystalFloors.get("spades", "No Data")) 
				value_of_intrest_h = str(crystalFloors.get("diamonds", "No Data"))  
				
				if value_of_intrest_e != "None":
					for _id_e in db.sandbox.find({"_id": ObjectId(value_of_intrest_e)}): 
						crystal_age_e = str(_id_e.get("crystal_age", "No Data"))
						Rank_e = str(_id_e.get("rank", "No Data")) 
						Suit_e = str(_id_e.get("suit", "No Data"))						
						Number = Tower_Mapping[int(Bagel)]
				
						if Rank_e == 'A': 
							Rank_v = 1 
						elif Rank_e == 'J':
							Rank_v = 11
						elif Rank_e == 'Q':
							Rank_v = 12
						elif Rank_e == 'K':
							Rank_v = 13
						else:
							Rank_v = Rank_Mapping[int(Rank_e)]	  		
						
						for age_e in db.sandbox.find({"_id": ObjectId(crystal_age_e)}):
							age_v = convert(age_e)
							Te_batch_e = str(age_e.get("Te_batch", "No Data")) 
							Channel_e = str((int(Number) - 1) * (52) + (1 - 1) * (13) + int(Rank_v))
							if Te_batch_e != "NAN":								 
								FullObject.append(Te_batch_e)								
								AllStar_e = str(Channel_e) + ' ' + str(Te_batch_e) 
								AllStar.append(AllStar_e) 
								
				if value_of_intrest_f != "None":
					for _id_f in db.sandbox.find({"_id": ObjectId(value_of_intrest_f)}): 
						crystal_age_f = str(_id_f.get("crystal_age", "No Data"))
						Rank_f = str(_id_f.get("rank", "No Data")) 
						Suit_f = str(_id_f.get("suit", "No Data"))						
						Number = Tower_Mapping[int(Bagel)]
				
						if Rank_f == 'A': 
							Rank_w = 1 
						elif Rank_f == 'J':
							Rank_w = 11
						elif Rank_f == 'Q':
							Rank_w = 12
						elif Rank_f == 'K':
							Rank_w = 13
						else:
							Rank_w = Rank_Mapping[int(Rank_f)]	  		
						
						for age_f in db.sandbox.find({"_id": ObjectId(crystal_age_f)}):
							age_w = convert(age_f)
							Te_batch_f = str(age_f.get("Te_batch", "No Data")) 
							Channel_f = str((int(Number) - 1) * (52) + (2 - 1) * (13) + int(Rank_w))
							if Te_batch_d != "NAN":								 
								FullObject.append(Te_batch_f)								
								AllStar_f = str(Channel_f) + ' ' + str(Te_batch_f) 
								AllStar.append(AllStar_f) 
								
				if value_of_intrest_g != "None":
					for _id_g in db.sandbox.find({"_id": ObjectId(value_of_intrest_g)}): 
						crystal_age_g = str(_id_g.get("crystal_age", "No Data"))
						Rank_g = str(_id_g.get("rank", "No Data")) 
						Suit_g = str(_id_g.get("suit", "No Data"))						
						Number = Tower_Mapping[int(Bagel)]
				
						if Rank_g == 'A': 
							Rank_x = 1 
						elif Rank_g == 'J':
							Rank_x = 11
						elif Rank_g == 'Q':
							Rank_x = 12
						elif Rank_g == 'K':
							Rank_x = 13
						else:
							Rank_x = Rank_Mapping[int(Rank_g)]	  		
						
						for age_g in db.sandbox.find({"_id": ObjectId(crystal_age_g)}):
							age_x = convert(age_g)
							Te_batch_g = str(age_g.get("Te_batch", "No Data")) 
							Channel_g = str((int(Number) - 1) * (52) + (3 - 1) * (13) + int(Rank_x))
							if Te_batch_g != "NAN":								 
								FullObject.append(Te_batch_g)								
								AllStar_g = str(Channel_g) + ' ' + str(Te_batch_g) 
								AllStar.append(AllStar_g) 
								
				if value_of_intrest_h != "None":
					for _id_h in db.sandbox.find({"_id": ObjectId(value_of_intrest_h)}): 
						crystal_age_h = str(_id_h.get("crystal_age", "No Data"))
						Rank_h = str(_id_h.get("rank", "No Data")) 
						Suit_h = str(_id_h.get("suit", "No Data"))						
						Number = Tower_Mapping[int(Bagel)]
				
						if Rank_h == 'A': 
							Rank_y = 1 
						elif Rank_h == 'J':
							Rank_y = 11
						elif Rank_h == 'Q':
							Rank_y = 12
						elif Rank_h == 'K':
							Rank_y = 13
						else:
							Rank_y = Rank_Mapping[int(Rank_h)]	  		
						
						for age_h in db.sandbox.find({"_id": ObjectId(crystal_age_h)}):
							age_y = convert(age_h)
							Te_batch_h = str(age_d.get("Te_batch", "No Data")) 
							Channel_h = str((int(Number) - 1) * (52) + (4 - 1) * (13) + int(Rank_y))
							if Te_batch_h != "NAN":								 
								FullObject.append(Te_batch_h)								
								AllStar_h = str(Channel_h) + ' ' + str(Te_batch_h) 
								AllStar.append(AllStar_h)
								
				
		else:
			for crystalFloors in fullName["crystalFloors"]: 
				value_of_intrest_1 = str(crystalFloors.get("hearts", "No Data")) 
				value_of_intrest_2 = str(crystalFloors.get("clubs", "No Data")) 
				value_of_intrest_3 = str(crystalFloors.get("spades", "No Data")) 
				value_of_intrest_4 = str(crystalFloors.get("diamonds", "No Data"))  
				
				#print(crystalFloors)

				
				if value_of_intrest_1 != "None":
					for _id in db.sandbox.find({"_id": ObjectId(value_of_intrest_1)}): 
						crystal_age_1 = str(_id.get("crystal_age", "No Data"))
						Rank_1 = str(_id.get("rank", "0")) 
						Suit_1 = str(_id.get("suit", "0"))						
						
						Number = Tower_Mapping[int(Bagel)]
				
						if Rank_1 == 'A': 
							Rank_a = 1 
						elif Rank_1 == 'J':
							Rank_a = 11
						elif Rank_1 == 'Q':
							Rank_a = 12
						elif Rank_1 == 'K':
							Rank_a = 13
						else:
							Rank_a = Rank_Mapping[int(Rank_1)]	 
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
							Te_batch_1 = str(age_1.get("Te_batch", "No Data")) 
							Channel_1 = str((int(Number) - 1) * (52) + (1 - 1) * (13) + int(Rank_a))
							if Te_batch_1 != "NAN":								 
								FullObject.append(Te_batch_1)								
								AllStar_1 = str(Channel_1) + ' ' + str(Te_batch_1) 
								AllStar.append(AllStar_1)
								
				if value_of_intrest_2 != "None":
					for _id2 in db.sandbox.find({"_id": ObjectId(value_of_intrest_2)}): 
						crystal_age_2 = str(_id2.get("crystal_age", "No Data"))  
						Rank_2 = str(_id2.get("rank", "0")) 
						Suit_2 = str(_id2.get("suit", "0"))
						
						Fading_2 = "Tower" + " " + str(Number) + ' ' + str(Rank_2) + ' ' + "clubs"
						Fading.append(Fading_2)
						
						Number = Tower_Mapping[int(Bagel)]
				
						if Rank_2 == 'A': 
							Rank_b = 1 
						elif Rank_2 == 'J':
							Rank_b = 11
						elif Rank_2 == 'Q':
							Rank_b = 12
						elif Rank_2 == 'K':
							Rank_b = 13
						else:
							Rank_b = Rank_Mapping[int(Rank_2)]	 
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
							#FullObject.append(age_b)
							Te_batch_2 = str(age_2.get("Te_batch", "No Data")) 
							Channel_2 = str((int(Number) - 1) * (52) + (2 - 1) * (13) + int(Rank_b))
							#Jimmy_Mack.append(Channel_2) 
							#Fading_2 = str(Number) + ' ' + str(Rank_2) + ' ' + Suit_2
							#Fading.append(Fading_2)
							if Te_batch_2 != "NAN":
								#Channel_2 = str((int(Number) - 1) * (52) + (2 - 1) * (13) + int(Rank_b))
								Xtal_2 = str(Channel_2) + ' ' + str(Te_batch_2)
								#print (Channel_2)
								
								a = {} 
								b = {}
								Jimmy_Mack.append(Channel_2)
								FullObject.append(Te_batch_2)
								
								#Fading_2 = str(Number) + ' ' + str(Rank_2) + ' ' + Suit_2
								#Fading.append(Fading_2)
								
								AllStar_2 = str(Channel_2) + ' ' + str(Te_batch_2) 
								AllStar.append(AllStar_2)

				if value_of_intrest_3 != "None":
					for _id3 in db.sandbox.find({"_id": ObjectId(value_of_intrest_3)}):
						crystal_age_3 = str(_id3.get("crystal_age", "No Data"))
						Rank_3 = str(_id3.get("rank", "0")) 
						Suit_3 = str(_id3.get("suit", "0")) 
						
						Fading_3 = "Tower" + " " + str(Number) + ' ' + str(Rank_3) + ' ' + "spades"
						Fading.append(Fading_3)
						
						Number = Tower_Mapping[int(Bagel)]
				
						if Rank_3 == 'A': 
							Rank_c = 1 
						elif Rank_3 == 'J':
							Rank_c = 11
						elif Rank_3 == 'Q':
							Rank_c = 12
						elif Rank_3 == 'K':
							Rank_c = 13
						else:
							Rank_c = Rank_Mapping[int(Rank_3)]	 
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
							#FullObject.append(age_c)
							Te_batch_3 = str(age_3.get("Te_batch", "No Data")) 
							Channel_3 = str((int(Number) - 1) * (52) + (3 - 1) * (13) + int(Rank_c))
							#Jimmy_Mack.append(Channel_3)
							#Fading_3 = str(Number) + ' ' + str(Rank_3) + ' ' + Suit_3
							#Fading.append(Fading_3)
							if Te_batch_3 != "NAN":
								#Channel_3 = str((int(Number) - 1) * (52) + (3 - 1) * (13) + int(Rank_c))
								Xtal_3 = str(Channel_3) + ' ' + str(Te_batch_3)
								#print (Channel_3)
								
								a = {} 
								b = {}
								
								Jimmy_Mack.append(Channel_3)
								FullObject.append(Te_batch_3) 
								
								#Fading_3 = str(Number) + ' ' + str(Rank_3) + ' ' + Suit_3
								#Fading.append(Fading_3)
								
								AllStar_3 = str(Channel_3) + ' ' + str(Te_batch_3) 
								AllStar.append(AllStar_3)

				if value_of_intrest_4 != "None":
					for _id4 in db.sandbox.find({"_id": ObjectId(value_of_intrest_4)}):
						crystal_age_4 = str(_id4.get("crystal_age", "No Data"))
						Rank_4 = str(_id4.get("rank", "0")) 
						Suit_4 = str(_id4.get("suit", "0")) 
						
						Fading_4 = "Tower" + " " + str(Number) + ' ' + str(Rank_4) + ' ' + "diamonds"
						Fading.append(Fading_4)
						

						Number = Tower_Mapping[int(Bagel)]
				
						if Rank_4 == 'A': 
							Rank_d = 1 
						elif Rank_4 == 'J':
							Rank_d = 11
						elif Rank_4 == 'Q':
							Rank_d = 12
						elif Rank_4 == 'K':
							Rank_d = 13
						else:
							Rank_d = Rank_Mapping[int(Rank_4)]	 
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
							#FullObject.append(age_d)
							Te_batch_4 = str(age_4.get("Te_batch", "No Data")) 
							Channel_4 = str((int(Number) - 1) * (52) + (4 - 1) * (13) + int(Rank_d)) 
							#Fading_4 = str(Number) + ' ' + str(Rank_4) + ' ' + Suit_4
							#Fading.append(Fading_4)
							
							#Jimmy_Mack.append(Channel_4)
							if Te_batch_4 != "NAN":
								Channel_4 = str((int(Number) - 1) * (52) + (4 - 1) * (13) + int(Rank_d))
								Xtal_4 = str(Channel_4) + ' ' + str(Te_batch_4) 		
								#print (Channel_4)
								a = {} 
								b = {} 
								Jimmy_Mack.append(Channel_4)
								FullObject.append(Te_batch_4) 
								
								#Fading_4 = str(Number) + ' ' + str(Rank_4) + ' ' + Suit_4
								#Fading.append(Fading_4)
								
								AllStar_4 = str(Channel_4) + ' ' + str(Te_batch_4) 
								AllStar.append(AllStar_4)
								

								
							
							
#print (Jimmy_Mack)						
							
							
f = open("AllStar.txt", "w") 
f.write("\n".join(map(lambda x: str(x), AllStar))) 
f.close()
							
							
							
#print set(AllStar)						
#print len(set(AllStar))							
#print(Backstreet) 

Hal9000 = map(int, FullObject)
#Hal9001 = map(int, Jimmy_Mack)

#print (len(list(set(Backstreet))))
#print (len(FullObject))
#print (len(Jimmy_Mack))
#print (len(Vida))
#print (AllStar)
#print (len(set(Jimmy_Mack)))
#Day = set(Fading)
Night = sorted(Fading)
#Day_2 = set(AllStar) 
#Night_2 = (sorted(Day_2, key=int))
#print (sorted(Day, key=int))
#print len(Day)
#pprint (Night) 

f = open("Speaker.txt", "w") 
f.write("\n".join(map(lambda x: str(x), Night))) 
f.close()




fig = plt.figure()

ax1 = fig.add_subplot(111)

ax1.set_title("Bolometers in each Te_batch")    
ax1.set_xlabel('Te_batch [Number]')
ax1.set_ylabel("Number of Bolometers")
plt.hist(Hal9000, bins=988, color='b', label='Crystals')
#plt.scatter(Hal9000,Hal9001)
plt.axis([10001, 10013, 0, 150])
plt.show()
