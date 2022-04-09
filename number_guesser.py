import random
print("You will guest a number from 0 to your input number")
max_range = input("Please type a positive number: ")

try:  #Check whether the input number is an integer and larger than 0 
    max_range = int(max_range)
    if max_range <= 0:
        print("Please type a number larger than 0 next time!")
        quit()
except ValueError:
    print("Please type a number next time!")    

random_number = random.randint(0, max_range) #Generate random number from 0 to input number
guesses = 0 

while True:
    guesses += 1 #Add 1 guess to the total guesses
    user_guess = input("Make a guess: ")
    if  user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("Please type a number next time!") 
        continue
    
    if user_guess == random_number:
        print("You got it right!")
        break
    elif user_guess > random_number: #Check if the user guess is below or above the random number
        print("You were above the number!")
    else: 
        print("You were below the number!")
if guesses == 1:
    print("You got it in 1 guess, so amazing!")
else: 
    print("You got it in", guesses, "guesses")