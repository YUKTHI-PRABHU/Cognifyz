

print("Welcome to the Guessing Game!")
print("I'm thinking of a number between 1 and 10.")
print("Can you guess what it is?")
print("You will be given 5 chances to check your luck\n")

import random

def start_game():
    secret_number = random.randint(1, 10)
    attempts = 0

   
    while True:
       
        if attempts>=5:
            print(" You are done with all 5 chances !!Try next time All the best") 
            break
        if attempts>=4:
            print("last chance do best...")
            
        guess = input("Enter your guess: ")
        try:
            guess = int(guess)
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue
            
      
        
    
        attempts += 1
        
        
        if attempts>4:
            print("Lost don't worry...")

        if guess >10:
            print("out of limit\n")
        elif guess < secret_number:
            print("Too low!Please guess high value\n")
        elif guess > secret_number:
            print("Too high! Please guess low value\n")
       
        else:
            print("Congratulations! You guessed the number in {} attempts.".format(attempts))
            print("Random number was:",secret_number)
            break

start_game()



