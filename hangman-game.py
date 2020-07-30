import random

# Intro to the hangman game, random output word from english2.txt
guesses = 0
print("Welcome to hangman my first game ever created\n\nYou will have to guess a word that I am thinking of\n\nLets start\n")
name = input("What is your name: ")
file = open("english2.txt", "r")
word = random.choice(file.readlines())
#print(word)

# Underlines per letter
count = 0
underlines = []
for x in word:
    count = count + 1
    underlines.append("_")
print("The word I am thinking of has", count, "letters")
print(" ".join(underlines))

print("_________")
print("|	 |")
print("|	  ")
print("|")
print("|")
print("|")
print("|________")

#Interaction with the user, guessing letters.
fails = 0
guesses = 0
guessletters = []

while fails <6:
    possitionletter = 0
    goodguess = 0
    letter = input(("Guess a letter in my word: "))
    letter = letter.lower()
    if letter == " ":
        print("Please enter a letter")
        goodguess = 1
    elif len(letter) > 1:
        print("Please one letter at a time")
        goodguess = 1
    elif letter in guessletters:
        print("You have already guessed that letter")
        goodguess = 1
    else:
        for x in word:
            if x == letter:
                underlines[possitionletter] = letter
                goodguess = 1
            possitionletter = possitionletter + 1
        guessletters.append(letter)

    if goodguess == 0:
        guesses = guesses + 1
        fails = fails + 1
        if (guesses == 1):
            print("_________")
            print("|	 |")
            print("|	 O")
            print("|")
            print("|")
            print("|")
            print("|________")
        elif (guesses == 2):
            print("_________")
            print("|	 |")
            print("|	 O")
            print("|	 |")
            print("|	 |")
            print("|")
            print("|________")
        elif (guesses == 3):
            print("_________")
            print("|	 |")
            print("|	 O")
            print("|	\|")
            print("|	 |")
            print("|")
            print("|________")
        elif (guesses == 4):
            print("_________")
            print("|	 |")
            print("|	 O")
            print("|	\|/")
            print("|	 |")
            print("|")
            print("|________")
        elif (guesses == 5):
            print("_________")
            print("|	 |")
            print("|	 O")
            print("|	\|/")
            print("|	 |")
            print("|	/ ")
            print("|________")
        elif (guesses == 6):
            print("_________")
            print("|	 |")
            print("|	 O")
            print("|	\|/")
            print("|	 |")
            print("|	/ \ ")
            print("|________")
            print("\n")
            print("You loose", name, "the word was", word)
            break

    print("Letters you have already try " + ", ".join(guessletters))
    print(" ".join(underlines))








