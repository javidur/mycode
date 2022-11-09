#!/usr/bin/env python3

round = 0
answer = ""

## add shrubbery as another answer and allow to provide lowercase or uppercase
while round < 3 and (answer != "Brian" and answer != "Shrubbery"):
    round +=1 # increase the round counter
    answer = input('Finish the movie title, "Monty Python\'s The Life of _____": ')
    answer = answer.capitalize()

    if answer == "Brian":
        print("Correct")
    elif answer == "Shrubbery":
        print("That's the other answer")
    elif round == 3:
        print("Sorry, the anser was Brian")
    else:
        print("Sorry, try again!")
