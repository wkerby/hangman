#Create python script that simulates the hangman game
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

        if correctcount == 0:

            lettercount = 0
            guess = input("guess a letter contained in the mystery word")

            if guess in gamewordlist:
                correctcount += 1

                for i in list(range(0,len(gamewordlist))):
                          if guess == gamewordlist[i]:
                            lettercount +=1
                          
                if lettercount == 1:
                    correctindex = []
                    [correctindex.append(y) for y,n in enumerate(gamewordlist) if n == guess]
                      

                

                    for i in list(range(0,len(gamewordlist))):
                                if i in correctindex:
                                    blanklist[i] = guess
                    partialword = ''.join(blanklist)
            
                      
                    print("Great job! The letter " + guess + " appears once in the mystery word!")
                    print("This is what your mystery word looks like now: " + partialword)
                    print("Keep guessing!")

                elif lettercount > 1:
            
                    correctindex = []
                    [correctindex.append(y) for y,n in enumerate(gamewordlist) if n == guess]
                
                    blanklist = ['_']*len(gamewordlist)
                
                    for i in list(range(0,len(gamewordlist))):
                                if i in correctindex:
                                    blanklist[i] = guess
                            
                    partialword = ''.join(blanklist)
        
                    print("Great job! The letter " + guess + " appears " + lettercount + " times in the mystery word! Keep guessing!") 
                    print("This is what your mystery word looks like now: " + partialword)
                    print("Keep guessing!")
              
            else:
                numberwrong += 1
                print("Oops! The letter " + guess + " is not in the mystery word! You have " + str(6 - numberwrong) + "guesses remaining!"

#________________________________________________________________________________
#--------------------------------------------------------------------------------

        if correctcount > 0:
            lettercount = 0
            guess = input("guess a letter contained in the mystery word")
        
            if guess in gamewordlist:
                correctcount += 1

                for i in list(range(0,len(gamewordlist)):
                          if guess == gamewordlist[i]:
                                lettercount +=1
                if lettercount == 1:
                    correctindex = []
                    [correctindex.append(y) for y,n in enumerate(gamewordlist) if n == guess]

                    for i in list(range(0,len(gamewordlist))):
                        if i in correctindex:
                            blanklist[i] = guess
            
                      
                    print("Great job! The letter " + guess + " appears once in the mystery word!")
                    print("This is what your mystery word looks like now: " + partialword)
                    print("Keep guessing!")

                elif lettercount > 1:
            
                    correctindex = []
                    [correctindex.append(y) for y,n in enumerate(gamewordlist) if n == guess]



                    for i in list(range(0,len(gamewordlist))):
                            if i in correctindex:
                                blanklist[i] = guess
                            
                    partialword = ''.join(blanklist)
        
                    print("Great job! The letter " + guess + " appears " + lettercount + " times in the mystery word! Keep guessing!") 
                    print("This is what your mystery word looks like now: " + partialword)
                    print("Keep guessing!")
            
              
            else:
                numberwrong += 1
                print("Oops! The letter " + guess + " is not in the mystery word! You have " + str(6 - numberwrong) + "guesses remaining!"

    print('Congratulations! You guessed the mystery word correctly. The mystery word was ' + partialword + '!')
print('Oh no! You have surpassed the maximum number of letter guesses! **GAME OVER**')



    
            
