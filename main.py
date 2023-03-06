import random 

print("Guess a number between 1 and n ? ")
topNumber = input("Choose n: ")

if topNumber.isdigit():
    topNumber = int(topNumber)
    if topNumber < 1:
        print("Please choose a number higher than 0 next time")
        quit()
else:
    print("Please type a number next time!")
    quit()
    
randomNumber = random.randint(0, topNumber)
guessesTotal = 0

print("Let's guess a number between 1 and " + str(topNumber) + "!")
while True:
    guessesTotal += 1
    guess = input("Make a guess: ")
    if guess.isdigit():
        guess = int(guess)
        if guess == randomNumber:
            print("Well done!")
            print("You made it in" , guessesTotal , "guesses!")
            break
        elif guess < randomNumber:
            print("The number to guess is bigger")
        else:
            print("The number to guess is smaller")
    else:
        print("Please type a number next time")