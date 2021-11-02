from random import randint

print("You have 5 tries to guess the number correctly")
guessed = False
tries = 5
computer_gusse = randint(1,10)

while (guessed == False and tries > 0):
    # Checking the correctness of the input
    try:
        userin = int(input("Guess a number between 1 to 9 : "))
    except ValueError:
        print("Please use only integers ")
        continue
    # Check the guess
    if userin < 0 or userin > 9:
        print("Please guess between 1 and 9")
        tries = tries -1
        continue
    elif(computer_gusse == userin):
        print("WOW, you guessed it correctly")
    else:
        print("Oof, wrong number try again")
    tries = tries -1
if(guessed == False):
    print("Dang! You couldnt guess the number!")
else:
    print("Congrats!! You have guessed the number correctly!")
