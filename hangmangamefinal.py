#create a python script that simulates the hangman game
#how to get the partial word to show the updated word?
from random import *
wordpool = ["batman", "basketball","france", "lighter", "cactus","spur","banana","mountain","rifle","deer","walrus","beatle","dynamite","burrito","sombrero","football", "buccaneer","twinkie","taj mahal","mount everest","toothpick","grand teton national park","fly fishing","paris","porrentruy","swiss chocolate","christmas","turtle","count dracula","yellowstone","santa claus","jimi hendrix","charcuterie","chelsea","southampton", "leeds", "leicester city", "wolverhampton","tiger","annapurna","eleanor rigby","yosemite", "joshua tree", "red hot chili peppers","cascade canyon","lighthouse of alexandria"]
gameword = wordpool[int(uniform(1,len(wordpool)))]
gamewordlist = list(gameword)
numberwrong = 0
correctcount = 0 
blanklist = ['_']*len(gamewordlist)
partialword = ''
print("Let's play Hangman!")
if ' ' in gamewordlist:
	blankindlist = []
	for i in list(range(0,len(gamewordlist))):#goes through the indices of every word in the game word or game phrase
		if ' ' == gamewordlist[i]:
			[blankindlist.append(y) for y,n in enumerate(gamewordlist) if n == ' ']
			slicelist = []
			for i in blankindlist:
				blanklist[i] = ' '#replaces the underscore with a free space in the blanklist that is displayed to the player
print("Here's a look at your blank mystery word: " + str(''.join(blanklist)))	
print()
while numberwrong < 6 and partialword != gameword:
	if partialword != gameword:
		lettercount = 0
		if ' ' in gamewordlist:
			guess = input('Guess a letter contained in the mystery phrase!')
		else:
			guess = input("Guess a letter contained in the mystery word!")
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
				if partialword != gameword:
					if ' ' in gamewordlist:
						print("Great job! The letter '" + guess + "' appears once in the mystery phrase!")
						print("This is what your mystery phrase looks like now: " + partialword)
						print("Keep on guessing!")
					else:
						print("Great job! The letter '" + guess + "' appears once in the mystery word!")
						print("This is what your mystery word looks like now: " + partialword)
						print("Keep on guessing!")
			if lettercount > 1: #if the guessed letter appears once in the mystery word
				correctindex = []
				[correctindex.append(y) for y,n in enumerate(gamewordlist) if n ==guess]
				for i in list(range(0,len(gamewordlist))): #goes through every index number possible of the mystery word 
					if i in correctindex:
						blanklist[i] = guess
					partialword = ''.join(blanklist)
				if partialword != gameword:
					if ' ' in gamewordlist:
						print("Great job! The letter '" + guess + "' appears " + str(lettercount) + " times in the mystery phrase!")
						print("This is what your mystery phrase looks like now: " + partialword)
						print("Keep on guessing!")
					else:
						print("Great job! The letter '" + guess + "' appears " + str(lettercount) + " times in the mystery word!")
						print("This is what your mystery word looks like now: " + partialword)
						print("Keep on guessing!")
		else:
			numberwrong += 1
			if numberwrong < 6:
				if ' ' in gamewordlist:
					print("Woops! The letter '" + guess + "' is not in the mystery phrase! You have " + str(6-numberwrong) + " guesses remaining!")
				else:
					print("Woops! The letter '" + guess + "' is not in the mystery word! You have " + str(6-numberwrong) + " guesses remaining!")			
if numberwrong < 6:
	print("-----WINNER!-----")
	if ' ' in gamewordlist:
		print("Congratulations!! You guessed the mystery phrase correctly! The mystery phrase was " + '"' + partialword + '!"' + " Thanks for playing!")
	else:
		print("Congratulations!! You guessed the mystery word correctly! The mystery word was "  + '"'+ partialword + '!"' + " Thanks for playing!")
        
else:
	if ' ' in gamewordlist:
		print("Oh no! You have reached the maximum number of letter guesses! The mystery phrase was " + '"' + gameword + '."' + " Try again if you dare!")
	else:
		print("Oh no! You have reached the maximum number of letter guesses! The mystery word was " + '"' + gameword + '."' + " Try again if you dare!")
	print("-----GAME OVER-----")
