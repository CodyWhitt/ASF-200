answer = 'PROFESSOR'
guessedLetters = []
wordBoard = ['_']* len(answer)
guessCountdown = int(5)

print("Can you guess the secret occupation?")

def showBoard():
    print(' '.join(wordBoard))

def checkGuess(guessedLetter):
    global guessedLetters
    global wordBoard
    guessedLetters.append(guessedLetter.upper())
    if int(guessedLetters.count(guessedLetter.upper())) == 1:
        if int(answer.count(guessedLetter.upper())) > 0:
            print("Yes there are " + str(answer.count(guessedLetter.upper())) + " " + guessedLetter.upper())
            for i, j in enumerate(answer):
                if j == guessedLetter.upper():
                    wordBoard[i] = j
        else:
            global guessCountdown 
            guessCountdown = guessCountdown -1
            print("I'm sorry but there is no letter " + guessedLetter.upper() + " in the word.")
            print("You have " + str(guessCountdown) + " chances left")
    else:
        print("You have already guessed the letter " + guessedLetter.upper() + " try again.")

while guessCountdown > 0:
    showBoard()
    if int(wordBoard.count('_')) != 0:
        guess = str(input("Guess a letter: "))
        checkGuess(guess)
    else:
        print('You Won!')
        break

print("You lose. The secret word was " + answer)
