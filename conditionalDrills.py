'''
For this assignment you should read the task, then below the task do what it asks you to do.
'''
from pickle import FALSE

#1) Create a Variable called grade and set it to an integer. Make an 
#if/elif/else statement. If grade is equal to or above 80, then print "passing".
#Elif grade is lower than 80 and greater than or equal to 60, then print
#"probation". Else, print "failing". 
grade = 95
if grade>=80: 
    print("passing")
    
elif grade<80>=60:
    print("probation")
else:
    print("failing")
    
    


#2) Make a int variable named a. Now make an if/elif statment, and if a is more
#than/equal too 100 or less than/equal too -100, print "a is a three digit 
#number". Elif a is between 100 and -100, print "a is not a three digit number".

a=87
if -100>=a>=100:
    print("a is a three digit number")
elif -100<a<100:
    print("a is not a three digit number")

#3)Create a variable called age. Make an if/else statement. If age is older
#than 18, print "You can vote". Else, print "You cannot vote".

age = 16
if age>18:
    print("You can vote")
else:
    print("You cannot vote")

#4)Make a string variable called answer, and set it to the letter a, b, c, or d.
#Make an if/elif statement. If answer is a, b, or d, print "Wrong". Elif answer
#is c, print "Correct".

answer ="a"
if answer =="a" or "b" or "d":
    print("wrong")
elif answer == "c":
    print("Correct")

#5)Make two boolean variables. Make an if/elif/else statement. If both booleans 
#are true, print "Both". Elif only one of the booleans is true, print "Only 
#one". Else, print "Neither".

apples = True
Oranges= False 

if apples and Oranges == True:
    print("Both")
elif apples or Oranges == True:
    print("Only one")
else:
    print("Neither")

