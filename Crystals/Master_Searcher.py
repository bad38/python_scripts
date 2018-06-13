from pymongo import MongoClient 
from pprint import pprint 
import json 
import bson
import collections 
import Library_JsonLoad
from Crystals_Arrive_Time import Search_by_Crystals_arrival_date 
from Crystals_Birth_Date import Search_by_Crystals_birth_date 
from Crystals_Shipping_Date import Search_by_Crystals_shipping_date 
from Crystals_Vacuum_Packed_Date import Search_by_Crystals_vacuum_packed_date 
from Crystals_Te_Metal_Acqusiition_Date import Search_by_Te_metal_acqusiition_date 
from Crystals_Te_acq_to_Xtal_birth import Search_by_Crystals_Te_acq_to_Xtal_birth 
from Crystals_Xtal_birth_to_storage import Search_by_Crystals_Xtal_birth_to_storage 
from Crystals_life_in_cavern import Search_by_Crystals_life_in_cavern 
from Crystals_Xtal_current_age import Search_by_Crystals_Xtal_current_age 
from Crystals_Te_acq_to_Xtal_storage import Search_by_Crystals_Te_acq_to_Xtal_storage
from Crystals_Te_batch import Search_by_Crystals_Te_batch

client = MongoClient() 
db = client.cdb 
collection = db.sandbox 

			#Time relating searching

first = int(raw_input("(first_year_int): ")) 
second = int(raw_input("(last_year_int+1): "))
third = int(raw_input("(first_month_int): ")) 
fourth = int(raw_input("(last_month_int+1): ")) 
fifth = int(raw_input("(first_day_int): ")) 
sixth = int(raw_input("(last_day_int+1): "))  

#Search_by_Te_metal_acqusiition_date(first,second,third,fourth,fifth,sixth) 
Search_by_Crystals_birth_date(first,second,third,fourth,fifth,sixth) 
#Search_by_Crystals_vacuum_packed_date(first,second,third,fourth,fifth,sixth) 
#Search_by_Crystals_arrival_date(first,second,third,fourth,fifth,sixth) 
#Search_by_Crystals_shipping_date(first,second,third,fourth,fifth,sixth)  

			#Timespan related searching 

#Number_of_Days = int(raw_input("(Number_of_Days+1): "))

#Search_by_Crystals_Te_acq_to_Xtal_birth(Number_of_Days)
#Search_by_Crystals_Xtal_birth_to_storage(Number_of_Days)
#Search_by_Crystals_life_in_cavern(Number_of_Days)
#Search_by_Crystals_Xtal_current_age(Number_of_Days)
#Search_by_Crystals_Te_acq_to_Xtal_storage(Number_of_Days) 

			#Misc 

#Number_of_Te_batch = int(raw_input("(number_of_Te_batch_int): "))
#Search_by_Crystals_Te_batch(Number_of_Te_batch)
