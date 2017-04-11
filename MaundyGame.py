import random as rand

class MaundyGame(object):

    def __init__(self, startWidth, startHeight):
    	self.leftCurrent = (rand.randint(0,1) == 1)
        self.board = [(startWidth, startHeight)]
        #self.left = HumanPlayer()
        #self.right = AIPlayer()

    # whichBoard is the index of list, gameboard to be cut

    def cut(self, whichBoard, number, isLeft):
        desiredBoard = self.board[whichBoard]

        if((isLeft and desiredBoard[0] % number != 0) or
           (not(isLeft) and desiredBoard[1] % number != 0)):
        	print "error"
        	return

        after = self.board[whichBoard:]

        if(isLeft):
        	self.board = self.board[:whichBoard] + [(self.board[whichBoard][0] / number, self.board[whichBoard][1])]
        	for i in xrange(1, number):
        		self.board += self.board[whichBoard]
        else:
        	self.board = self.board[:whichBoard] + [(self.board[whichBoard][0], self.board[whichBoard][1] / number)]
        	for i in xrange(1, number):
        		self.board += self.board[whichBoard]

        self.board = self.board + after

    def represent(self):
    	print len(self.board)
    	for i in xrange(0, len(self.board)):
    		print self.board[i][1]
    		print self.board[i][0]
 		# for i in xrange(0,len(self.board)):
 		# 	for j in xrange(0, self.board[i][1]):
 		# 		for k in xrange(0, self.board[i][0]):
 		# 			print "x",
 		# 		print "\n",
 		# 	print "\n"



if __name__ == '__main__':
	 
	game = MaundyGame(6,8)
	game.represent()
	game.cut(0,2,True)
	# game.represent()