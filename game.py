"""A number-guessing game."""


#process
#ask for users {name}
#print {name}, I'm thinkning of a number between 1 and 100. Try to guess my number.
#run a loop if guess is === number go to congrats
# if number is < say too low
#increase number of guesses
#if number is > say too high
#else:
#congratulate player




import random
n = random.randint(1, 100)
name = input("What is your name? ")
print("Hello" + " "  + name )
guess = int(raw_input("Enter an integer from 1 to 100: "))
while n != "guess":
    print
    if guess < n:
        print ("guess is low")
        guess = int(raw_input("Enter an integer from 1 to 100: "))
    elif guess > n:
        print ("guess is high")
        guess = int(raw_input("Enter an integer from 1 to 100: "))
    else:
        print ("Congratulations! You guessed it!")
        break
    print


#you have to enter your name in " " for it to not call an undefined in the terminal.
