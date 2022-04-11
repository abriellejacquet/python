'''
This outline will help solidify concepts from the Functions lesson.
Fill in this outline as the instructor goes through the lesson.
'''
from pickle import TRUE, FALSE

#1) Make a function that has two boolean parameters. If both booleans are
#true, return true. Else, return false. Then, call the function.
#Print what the function returns.

def bool_param(par1, par2):    
    if bool(par1) == True and bool(par2) == True:
        return 'True'
    else:
        return 'False'
 
par1 = False
par2 = True
print(bool_param(par1,par2))

#2) Make a function that takes one int parameter: gallons. Convert gallons
#to cups (do this by multiplying gallons by 16). Then return cups. Then,
#call the function.
#Print what the function returns.
def gal_to_cup(gal):
    answer =gal * 16
    return answer

gal = 2
print(gal_to_cup(gal))


#3) Make a function of any any kind with a common SYNTAX error. Then, call the
#function.
#Print what the function returns.

#dif gal_to_cup(gal) 
#key word should be spelled "def"

