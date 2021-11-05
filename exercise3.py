from random import randint

number = randint(1,20)

while 1:
    
    guess = int(input("Guess a number between 1-20\n"))
    if guess <= 20 and guess >=1:
        if guess < number:
            print("Increase your number")
        elif guess > number:
            print("Decrease your number")
        else:
            print("You guessed correctly.")
            break
    else:
        print("Your guess is not between 1-20")

