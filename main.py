import random
number = -65
print("Welcome to the Guess the Number game!")
print("I'm thinking of a number between 1 and 100. Can you guess what it is?")
guesses = 0
guess = 0
while True:
    choice = input('What range do you want? '
                   '\n Press "A" for 0 to 1 '
                   '\n Press "B" for 1 to 10'
                   '\n Press "C" for 1 to 100'
                   '\n Enter your choice: ')
    if choice == "A".lower():
        number = random.randint(0, 1)
    elif choice == "B".lower():
        number = random.randint(0, 10)
    elif choice == "C".lower():
        number = random.randint(0, 100)
    else:
        print("PLEASE ENTER A VALID CHOICE!")
        continue
    break
while guess != number:
    guess = int(input("Guess the number : "))
    guesses += 1
    if guess < number:
        print("Your guess is too low. Guess again.")
    elif guess > number:
        print("Your guess is too high. Guess again.")
    else:
        print("Congratulations! You guessed the number correctly after", guesses, "guesses!")