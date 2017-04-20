import random as rand
import math as math


	# def move(game):
	# 	number = findSmallestFactor
	# 	game.cut(board, number, )

def findAIMove(height):
	if(isPrime(height)):
		return height

	for i in range(height, 1, -1):
		if(isPrime(i) and height%i == 0):
			return i

def findSmallestFactor(number):

	h = int(math.floor(math.sqrt(number))+1)

	for i in xrange(2,h):
		if number%i == 0:
			return i
	return number

def isPrime(aNumber):
	h = int(math.floor(math.sqrt(aNumber))+1)
	
	for i in xrange(2, h):
		if aNumber%i == 0:
			return False
	return True

def getBoardValue(aPair):
	width = aPair[0]
	height = aPair[1]
	while(width != 1 and height != 1):
		width /= findSmallestFactor(width)
		height /= findSmallestFactor(height)
	if(width == 1 and height == 1):
		return 0
	isPositive = (height == 1)
	total = 0
	if(not(isPositive)):
		width = height
		height = 1
	while(width != 1):
		width = width/findSmallestFactor(width)
		total += width
	if (isPositive):
		return total
	else:
		return 0-total

class MaundyGame(object):

    def __init__(self, startWidth, startHeight):
        self.leftCurrent = (rand.randint(0,1) == 1)
        self.board = [(startWidth, startHeight)]

    # whichBoard is the index of list, gameboard to be cut

    def cut(self, whichBoard, number, isLeft):
        desiredBoard = self.board[whichBoard]

        if((isLeft and (desiredBoard[0] % number) != 0) or
        (not(isLeft) and (desiredBoard[1] % number) != 0)):
            print "error"
            return

        after = self.board[(whichBoard+1):]

        if(isLeft):
            self.board = self.board[:whichBoard] + [(self.board[whichBoard][0] / number, self.board[whichBoard][1])]
            for i in xrange(1, number):
                #print "self", self.board[whichBoard]
                self.board.append(self.board[whichBoard])
        else:
            self.board = self.board[:whichBoard] + [(self.board[whichBoard][0], self.board[whichBoard][1] / number)]
            for i in xrange(1, number):
                self.board.append(self.board[whichBoard])
        self.board += after

    def represent(self):
        for i in xrange(0,len(self.board)):
            print "Board " + str(i) + ": "
            for j in xrange(0, self.board[i][1]):
                for k in xrange(0, self.board[i][0]):
        	       print "x",
                print "\n",
            print "\n"

    def chooseAIBoard(self):
        for i in xrange(0, len(self.board)):
            if(getBoardValue(self.board[i]) < 0):
                return i
        for i in xrange(0, len(self.board)):
            if(self.board[i][1] > 1):
                return i
        print "ERROR :("
        return -1

    def checkFinish(self, isLeft):
        if(isLeft): 
            for i in xrange(0, len(self.board)):
                if self.board[i][0] > 1:
                    return False
            print "The game is finished! You lost!"
            return True
        else:
            for i in xrange(0, len(self.board)):
                if self.board[i][1] > 1: 
                    return False
        print "The game is finished! You won!"
        return True


if __name__ == '__main__':
	 
	# game.represent()
	# game.cut(0,3,False)
	# game.represent()


	print "Welcome to Maundy Cake!"
	width = int(raw_input('Please enter a width for the board: '))
	height = int(raw_input('Please enter a height for the board: '))

	print "The width for your board is " + str(width) + " and the height for your board is " + str(height) + "."

	game = MaundyGame(width,height)


	if(game.leftCurrent):
		print "Your move!"
	else:
		print "The computer will move first."

	while(not(game.checkFinish(game.leftCurrent))):

		game.represent()

		if(game.leftCurrent):

			boardNum = int(raw_input('Which board would you like to cut? '))
			while(boardNum >= len(game.board) or game.board[boardNum][0] <= 1):
				boardNum = int(raw_input('Oh no! Please try again. Which board would you like to cut? '))

			cutNum = int(raw_input('How many pieces would you like to cut the board into? '))
			while(game.board[boardNum][0]%cutNum != 0 or cutNum == 1):
				cutNum = int(raw_input('Oh no! Please try again. How many pieces would you like to cut the board into? '))

			game.cut(boardNum, cutNum, True)

		else:
			boardNum = game.chooseAIBoard()
			cutNum = findAIMove(game.board[boardNum][1])
			game.cut(boardNum, cutNum, False)
			print "The computer cuts board " + str(boardNum) + " into " + str(cutNum) + " pieces."


		game.leftCurrent = not(game.leftCurrent)



