'''
Created on Mar 11, 2022

@author: Abrielle Jacquet
'''
#The objective of this program is to quiz the user on basic high school
#trivia. 
#1)What is the powerhouse of the cell?
#2)How many states comprise the United States?
#3)In y=mx+b, what does m stand for?
#4)In English, a person, place or thing is called:
#The user will answer A, B, or C based on what answer they thing is correct
# If the answer is correct it will say correct and keep tract of your score
# If the answer is incorrect it will say inocrrect and state the correct
#answer. 
#At the end the user will recieve a score out of 4 and a percentage. 
from types import DynamicClassAttribute



score = 0

question1 = input("What is the powerhouse of the cell? A)mitochondria B)nucleus C) ribsome")

if (question1.upper() == "A"):
    print("Correct")
    score += 1;
    
else:
    print("Incorrect, the correct answer is A.")
#
question2 = input("How Many states comprise the United States? A)13 B)45 C)50")

if (question2.upper() == "C"):
    print("Correct")
    score += 1;
    
else:
    print("Incorrect, the correct answer is C.")

question3 = input("In y=mx+b, what does m stand for? A)slope B)output C)I don't understand math")

if (question3.upper() == "A"):
    print("Correct")
    score += 1;
    
else:
    print("Incorrect, the correct answer is A.")

question4 = input("In English, a person, place or things is called: A)verb B)adjective C)noun")

if (question4.upper() == "C"):
    print("Correct")
    score += 1;
    
else:
    print("Incorrect, the correct answer is C.")
p = score/4
str("You got a" +[score]/4 + "or a" + p +"%")
print(str)


