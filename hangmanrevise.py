#write code that accounts for space in a word
gameword = "taj mahal"
gamewordlist = list(gameword)
numberwrong = 0
correctcount = 0 
blanklist = ['_']*len(gamewordlist)
partialword = ''
if ' ' in gamewordlist:
	ind = gamewordlist.index()
	blanklist[ind] = ' '