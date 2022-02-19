'''
Created on Feb 19, 2022

The objective is to make a program that can complete different conversions.
Miles to yards.
Miles to feet.
Miles to inches. 

@author: Abrielle Jacquet
'''


miles = input("How many miles do you have?")
miles = int(miles)

yards= int(miles) * 1760
print(str(miles) + " miles converts to " + str(yards) + " yards")

feet = int(miles) * 5280
print(str(miles) + " miles converts to " + str(feet) + " feet")

inches = int(miles) * 63360
print(str(miles) + " miles converts to " + str(inches) + " inches")
