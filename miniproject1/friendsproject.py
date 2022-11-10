#!/usr/bin/env python3

""" Mini Project #1 -- Javier Duran
        While/IF - Friends Program """

def main():
    print("This program will test your Friends knowledge, let's see how much of a fan you are!")
    start = input("Are you ready to start? (Yes/No): ")
    start = start.capitalize()

    if start == "Yes":
        question1 = "What is the name of the cat that Phoebe says is her incarnated mother?  "
        answer1 = "JULIO"
        loop(question1, answer1)

        question2 = "Who is Chandler's TV guide addressed to? "
        answer2 = "MS CHANANDLER BONG"
        loop(question2, answer2)

        question3 = "What is the game show called that Joey was auditioning for? "
        answer3 = "BAMBOOZLED"
        loop(question3, answer3)

        question4 = "What is the name of Chandler's father's Las Vegas all male burlesque show? "
        answer4 = "VIVA LAS GAYGAS"
        loop(question4, answer4)

        question5 = "What is Monica's apartment number? "
        answer5 = "20"
        loop(question5, answer5)

        question6 = "Were Ross and Rachel on a break? (Yes/No)  "
        answer6 = "YES"
        loop(question6, answer6)

        print("\nThank you for playing")

    else:
        print("Come back when you are ready to play!")

def loop(question, answer):
    count = 0
    userInput = ""
    totalCorrect = 0

    # this while loop will run until all questions have been asked or there have been 5 incorrect answers
    while count < 3 and userInput != answer:
        userInput = input("\n" + question)
        userInput = userInput.upper()
        count += 1

        if userInput == answer:
            print("Correct!")
            totalCorrect += 1
            print("Total correct answers are: ", totalCorrect)
        elif count == 3:
            print("The correct answer is: " + answer)
        else:
            print("Try again")

main()
