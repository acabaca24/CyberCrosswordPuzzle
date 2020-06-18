tamanhoDaGrid = 14 # x * y of the grid
words =[]
grid = [[' '] * tamanhoDaGrid for _ in range(tamanhoDaGrid)]

class Word:
	def __init__(self, word, number, clue, posX, posY, isDown, isNumberLabelOnLeft):
		self.word = word # a palavra em si
		self.number = number # numero da palavra, apenas utilizado para as clues
		self.clue = clue # a dica associada à palavra
		self.posX = posX # coluna em que a palavra comeca
		self.posY = posY # linha em que a palavra comeca
		self.isDown = isDown # True se a palavra estiver escrita na vertical
		self.isRevealed = False # Iniciada a false para nao mostrar a palavra ao user
		self.isNumberLabelOnLeft = isNumberLabelOnLeft # True se o numero da palavra estiver a esquerda, false se acima
		self.PutWordInGrid()

	def PutWordInGrid(self):
		posX = self.posX
		posY = self.posY
		if(self.isNumberLabelOnLeft): #words that label will be on the left
			grid[self.posX - 1][self.posY] = self.number
		else: 					 # The rest, the label will be on the top
			grid[self.posX][self.posY - 1] = self.number
		for k in self.word:
			if(self.isRevealed):
				grid[posX][posY] = k
			else:
				grid[posX][posY] = '_'
			if self.isDown:
				posY += 1
			else:
				posX += 1

def PrintGrid():
	for y in range(0,13):
		for x in range(0,13):
			print(" " + grid[x][y], end = " ")
		print()

def Game():
	PrintGrid()
	print()
	print("Clues:")
	for word in words:
	 	print(word.number + ": " + word.clue)
	print("To quit, write 'quit'")

def Startup():
	# Here create the words with the rules aplied on the class Word
	words.append(Word('PENTEST', '1', 'Authorized simulated cyberattack', 3, 0, True, True))
	words.append(Word('CYBERSECURITY', '2', 'Practice of protecting systems, networks, and programs from digital attacks', 0, 4, False, False))
	words.append(Word('ENCRYPTION', '3', 'Process of encoding information',  6, 4, True, False))
	words.append(Word('FORENSICS', '4', 'Defined as the process of preservation, identification, extraction, and documentation of computer evidence', 4, 7, False, True))
	words.append(Word('HACKING', '5', 'Activities that seek to compromise digital devices',  2, 11, False, True))
	nWordsToFind = len(words)
	Game()

	while(nWordsToFind > 0):
		wordToGuess = input("Guess a word: ")
		wordToGuess = wordToGuess.upper()
		auxWordFound = False
		if(wordToGuess == 'QUIT'):
				if(input("Are you sure you want to quit(Y/n)? ") in ['y', 'Y']):
					return 0
		else:
			for word in words:
				if ((not word.isRevealed) and wordToGuess == word.word):
					auxWordFound = True
					word.isRevealed = True
					word.PutWordInGrid()
					break
				
			print(chr(27) + "[2J")
			Game()
			if(auxWordFound):
				nWordsToFind -= 1
				print("Nice! You got it!")
			else:
				print("Wrong word, try again :(")

	return 1

# Running program
if (Startup() == 1):
	print("CONGRATULATIONS!!! YOU'VE WON THE GAME!!!")
else:
	print("You're just sad :/")