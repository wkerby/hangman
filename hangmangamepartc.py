#create a python script that simulates the hangman game
#how to get the partial word to show the updated word?
from random import *
wordpool = ["batman", "basketball","france", "lighter", "cactus","spur","banana","mountain","rifle","deer","walrus","beetle","dynamite","grand canyon","burrito","sombrero","football", "buccaneer","twinkie","taj mahal"]
gameword = wordpool[int(uniform(1,len(wordpool)))]
gamewordlist = list(gameword)
numberwrong = 0
correctcount = 0 
blanklist = ['_']*len(gamewordlist)
partialword = ''

while numberwrong <= 6:
	while partialword != gameword:
		lettercount = 0
		guess = input("guess a letter contained in the mystery word (must be lower case)")
		if guess in gamewordlist: #will this still work even if the letter appears multiple times in the word?
			correctcount += 1 
			for i in list(range(0,len(gamewordlist))): #goes through every index number possible for the mystery word
				if guess == gamewordlist[i]:
					lettercount += 1
				if lettercount == 1: #if the guessed letter appears once in mystery word
					correctindex = [] #this piece of code creates a list of the indexes of the correct lette guess in the word
					[correctindex.append(y) for y,n in enumerate(gamewordlist) if n == guess]
					for i in list(range(0,len(gamewordlist))): #goes through every index number possible of the mystery word
						if i in correctindex:
							blanklist[i] = guess
					partialword = ''.join(blanklist)
					print("Great job! The letter " + guess + " appears once in the mystery word!")
					print("This is what your mystery word looks like now: " + partialword) 
					print("Keep on guessing!")
				if lettercount > 1: #if the guessed letter appears once in the mystery word
					correctindex = []
					[correctindex.append(y) for y,n in enumerate(gamewordlist) if n ==guess]
					for i in list(range(0,len(gamewordlist))): #goes through every index number possible of the mystery word 
						if i in correctindex:
							blanklist[i] = guess
					partialword = ''.join(blanklist)
					print("Great job! The letter " + guess + " appears " + lettercount + " times in the mystery word!")
					print("This is what your mystery word looks like now: " + partialword)
					print("Keep on guessing!")
		else:
			numberwrong += 1
			print("Oops The letter " + guess + " is not in the mystery word! You have " + str(6-numberwrong)) + " guesses remaining!"
	print("Congratulations!! You guessed the mystery word correctly. The mystery word was "  + partialword + "! Thanks for playing!")
print('Oh no! You have surpassed the maximum number of letter guesses! **GAME OVER**')


