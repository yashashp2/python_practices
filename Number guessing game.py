#Number guessing game

import random as rd

number = rd.randint(1,100)

guessed_number = 0 #initialising
while guessed_number != number: #loops through until the guessed number is correct
    guessed_number = int(input("Guess the number: ")) # asking user to guess a number
    
    if guessed_number > number +10:
        print(f"The guessed number {guessed_number} is too high!") #Guessed number is higher by at least 10 
    elif guessed_number > number:
        print(f"The guessed number {guessed_number} is higher than the number.") #Guessed number is higher not more than 10
    elif guessed_number < number -10:
        print(f"Guessed number {guessed_number} is too low!") #Guessed number is lower by at least 10
    elif guessed_number < number:
        print(f"Guessed number {guessed_number} is lower than the number.") #Guessed number is lower not more than 10
    elif guessed_number == number:
        print(f"You're right! The number is {number}")
