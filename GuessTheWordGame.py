secretWord = raw_input("Player 1 enter a word: ")
guesses = 0

print("Hints: ")
print "The word is", len(secretWord), "letters long."

guess = raw_input("Player 2 guess a letter or word: ")

while guess != secretWord:
    if secretWord.find(guess) == -1:
        guesses = guesses + 1
        print("Guess is not within the word.")
        print "Number of guesses", guesses
        guess = raw_input("Guess a letter: ")
    else:
        guesses = guesses + 1
        print "Guess is within the word. It is in position ", secretWord.find(guess)+1
        print "Number of guesses", guesses
        guess = raw_input("Guess a letter: ")

guesses = guesses + 1
print "Congratulations, you guessed the word! It was", secretWord, "."
print "You guessed the word in", guesses, "guesses!"
