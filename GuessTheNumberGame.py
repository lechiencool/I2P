from random import randint

x = randint(0,100)
y = input("Guess the Number!")
z = 0

while x!=y:
    if x<y:
        print("The number is lower than your guess. Try again.")
        z = z + 1
        print "Number of guesses:", z

    else:
        if x>y:
            print("The number is higher than your guess. Try again.")
            z = z + 1
            print "Number of guesses:", z


    y = input("Guess the Number!")

z = z + 1
print "You won in", z, "guesses! Now get back to work!"
