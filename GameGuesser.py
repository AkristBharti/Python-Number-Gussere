import random
print("You have 5 tries to guess the number correctly")
guessed = False
tries = 5
n = random.randint(1,10)
while (guessed == False and tries > 0):
    userin = int(input("Guess a number between 1 to 9 : "))
    if(n == userin):
        print("WOW, you guessed it correctly")
    else:
        print("Oof, wrong number try again")
    tries = tries -1
if(guessed == False):
    print("Dang! You couldnt guess the number!")
else:
    print("Congrats!! You have guessed the number correctly!")
