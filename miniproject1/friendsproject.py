#!/usr/bin/env python3

""" Mini Project #1 -- Javier Duran
        While/IF - Friends Program """

def main():
    print("This program will test your Friends knowledge, let's see how much of a fan you are!")
    start = input("Are you ready to start? (Yes/No): ")
    start = start.capitalize()
    totalCorrect = 0

    if start == "Yes":
        question1 = "What is the name of the cat that Phoebe says is her incarnated mother?  "
        answer1 = "JULIO"
        totalCorrect = loop(question1, answer1, totalCorrect)

        question2 = "Who is Chandler's TV guide addressed to? "
        answer2 = "MS CHANANDLER BONG"
        totalCorrect = loop(question2, answer2, totalCorrect)

        question3 = "What is the game show called that Joey was auditioning for? "
        answer3 = "BAMBOOZLED"
        totalCorrect = loop(question3, answer3, totalCorrect)

        question4 = "What is the name of Chandler's father's Las Vegas all male burlesque show? "
        answer4 = "VIVA LAS GAYGAS"
        totalCorrect = loop(question4, answer4, totalCorrect)

        question5 = "What is Monica's apartment number? "
        answer5 = "20"
        totalCorrect = loop(question5, answer5, totalCorrect)

        question6 = "Were Ross and Rachel on a break? (Yes/No)  "
        answer6 = "YES"
        totalCorrect = loop(question6, answer6, totalCorrect)
        
        question7 = "What is the phrase Ross repeats on his double date with Charlie, Joey, and Rachel? "
        answer7 = "I'M FINE"
        totalCorrect = loop(question7, answer7, totalCorrect)

        question8 = "What is the name of the diner that Phoebe's twin sister works at? "
        answer8 = "RIFF'S"
        totalCorrect = loop(question8, answer8, totalCorrect)

        question9 = "What is the name of the show Mr Waltham gives Rachel and Emily tickets to? "
        answer9 = "DIE FLEDERMAUS"
        totalCorrect = loop(question9, answer9, totalCorrect)

        question10 = "What movie does Chandler announce he is watching, to get Joey away, when he wants to come into his hotel room? "
        answer10 = "MY GIANT"
        totalCorrect = loop(question10, answer10, totalCorrect)

        question11 = "What does Monica's neighbor describe her Christmas candy as? "
        answer11= "LITTLE DROPS OF HEAVEN"
        totalCorrect = loop(question11, answer11, totalCorrect)

        print("\nThank you for playing")

    else:
        print("Come back when you are ready to play!")

def loop(question, answer, totalCorrect):
    count = 0
    userInput = ""

    # this while loop will run until all questions have been asked or there have been 5 incorrect answers
    while count < 3 and userInput != answer:
        userInput = input("\n" + question)
        userInput = userInput.upper()
        count += 1

        if userInput == answer:
            print("Correct!")
            totalCorrect += 1
            print("Total correct answers are: ", totalCorrect)
            return totalCorrect
        elif count == 3:
            print("The correct answer is: " + answer)
            return totalCorrect
        else:
            print("Try again")
     
main()
