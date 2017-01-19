# IF ELSE STATEMENT
#vScore = 75
#if vScore >= 50:
#    print("\nPass")
#else:
#    print("\nFail")

# IF IN STATEMENT
#vMonth = "September"
#vLetter = "e"

#if vLetter in vMonth:
#    print "There is a letter", vLetter, "in", vMonth
#else:
#    print "There is not a letter", vLetter, "in", vMonth

# FINDING LENGTH OF A WORD
#x = "September"
#print "There are", len(x), "letters in the word", x
#
# ELIF STATEMENTS
#vChoice = input("Enter number 1 to 3: ")
#print()
#
#if vChoice == 1:
#    print "Chosen item 1"
#
#elif vChoice == 2:
#    print "Chosen item 2"
#
#elif vChoice == 3:
#    print "Chosen item 3"
#
#else:
#    print "Sorry, but", vChoice, "isn't a valid number."
#
#input("\n\nPress the enter key to exit.")

# WORD SCORE GAME
vWord = raw_input("Enter a word: ")
vWord = vWord.lower()

score = 0

for letter in vWord:
    if letter == "a":
        score = score + 5
        print letter, " is worth 5. "
    elif letter == "e":
        score = score + 4
        print letter, " is worth 4. "
    elif letter == "i":
        score = score + 3
        print letter, " is worth 3. "
    elif letter == "o":
        score = score + 2
        print letter, " is worth 2. "
    elif letter == "u":
        score = score + 1
        print letter, " is worth 1. "
    else:
        print letter, " is worth 0. "

print "Total score is: ", score
