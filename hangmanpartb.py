gameword = 'banana'
gamewordlist = list(gameword)
guess = input('Guess a letter contained in the mystery word.')
count = 0
if guess in gamewordlist:
    for i in list(range(0,len(gamewordlist))):
        if guess == gamewordlist[i]:
            count += 1
correctindex = []
remainingindex = []
[correctindex.append(y) for y,n in enumerate(gamewordlist) if n == guess]
#print(correctindex)
[remainingindex.append(y) for y,n in enumerate(gamewordlist) if n != guess]
#print(remainingindex)
blanklist = ['_']*5
print(blanklist)
