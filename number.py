import random 
number = random.randint(1,9)
chances=0
while chances<5:
    guess=int(input("Enter a number between 1 to 9 :"))
    if guess == number:
        print("Congrats your guess is correct")
    elif guess < number:
        print("Your Guess is too low guess a higher number")
    else:
        print("Your Guess Was too high guess a lower number")
    chances += 1
if not chances < 5:
    print("All your chances are exhausted")