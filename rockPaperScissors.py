'''
Created on Apr 25, 2022

@author: Abrielle Jacquet
The Objective of this program is to make a Rock, Paper, Scissors game for the 
user to play against the computer. The tasks to complete are:
There should be a loop to repeat the game. And the game should go as follows:
Welcome the user with "Welcome to Rock Paper Scissors! Best two out of three. 
Press 'q' to quit"
Create variables to keep track of score
Begin a loop to repeat rounds until somebody wins. Someone wins when they have 
won 2 rounds. (Rounds are outlined below).
Once someone has won, print "Thanks for playing!", print out the final scores, 
and if the user wins: print "You win!"; if the cpu wins: print "CPU wins!"
Repeat the whole game once someone wins. And until the user chooses to quit.
A round should go as follows:
Have the user choose rock, paper, scissors, or q
Generate a random choice from the computer
Check the users input against the computers choice to see who won the round:
if the user won, add one to the users score, then print out the scores: "User:
 [#], Computer [#]”
else if the computer won, add one to the computer’s score, then print out the 
scores: "User: [#], Computer [#]"
else if it was a draw, print "DRAW", then print out the scores: "User: [#], 
Computer [#]"
else if the user entered "q", then end the round, and the game loop.
else the user didn't enter an accepted input, and prompt them to try again: 
"Not an option try again."
repeat the round until someone wins.

'''



#import random
import random 
#Make a boolean variable called keepPlaying to track whether they want to 
#keep playing and set it to True
keepPlaying = True
#LOOP: Make a game loop that continues while keepPlaying is True
while(keepPlaying):
    #print out a statement to welcome the user to the game
    print("Welcome to Rock, Paper, Scissors!")
    print("Best two out of three. press 'q' quit")
    #Make variables calleduserScore and cpuScore to track scores, set to 0
    cpuScore = 0
    userScore = 0
    #LOOP: Make a round loop that continues while the userScore or cpuScore is 
    #less than 2.
    while(userScore < 2 and cpuScore < 2):
        #Use input() to get a choice from the user (rock, paper, or scissors, "q")
        #store the choice in a variable.Use .lower() to make the users choice
        #all lower case.
        choice = input("Please choose(Rock, Paper, Scissors):")
        user = choice.lower
        
        #Make a list of choices, them use random.choice to get a random choice
        #for the CPU. store the choice in a variable. 
        choiceList = ["rock","paper", "scissors"]
        cpuchoice = random.choice(choiceList) 
        cpu = cpuchoice.lower
        #Make a if/elif/else statement to check the users input against he cpu's
        #choice.
        #Note: you will have to compare the users choice and the cpu's choice 
        #to "rock", "paper", and "scissors" separately and combine with logical 
        #operators. EXAMPLE of a tie:
        '''
        
        if((user == "rock" and cpu == "rock") or (user == "paper" and cpu =="paper")
        or the (user == "Scissors" and cpu == "scissors")):
        
            print("draw")
            print("User: " + str(userScore) + "CPU: " + str(cpuScore))
        '''
        
        #if the user won, add 1 to the users score.Then print out these scores
        #"user: [#], CPU [#]"
        if((user == "scissors" and cpu == "paper") or (user == "rock" and 
                    cpu == "scissors") or (user == "paper" and cpu == "rock")):
            userScore += 1
            print("User: " + str(userScore) + "CPU: " + str(cpuScore))
        #elif the computer won, add 1 to the computers score, then
        #print both of the scores.
        elif((user == "scissors" and cpu == "rock") or (user == "paper" and 
                cpu == "scissors") or (user == "rock" and cpu == "paper")):
            cpuScore += 1
            print("User: " + str(userScore) + "CPU: " + str(cpuScore))
        #elif it is a draw print("drow") then print out the scores
        elif((user == "scissors" and cpu == "scissors") or (user == "paper" 
                and cpu == "paper") or (user == "rock" and cpu == "rock")):
            print("DRAW")
            print("User: " + str(userScore) + "CPU: " + str(cpuScore))
        #elif the user entered "q" , then end the round and the game loop.
        #use the break statement to end the round. THen make keepPlaying
        #== "False"
        elif(choice.lower() == 'q'):
            keepPlaying = False
        #else if the user didn't enter an accepted input. print"not and option,
        #try again."
        else:
            print("Not an option, try again")
    #printout a thank you message 
    print("Thanks for playing!")
    #print out who won 
    
    # if the user score is 2. Then the user won
        #code
    if(userScore == 2):
        print("You won!")
    #elif the CPU score is 2. Then the CPU won. 
        #code
    elif(cpuScore == 2):
        print("CPU wins!")
    #print out the final scores.
    print("User: " + str(userScore) + "CPU: " + str(cpuScore))