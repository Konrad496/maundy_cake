class MaundyGame(object)

    def __init__(self, startWidth, startHeight):
        self.board = [(startWidth, startHeight)]
        self.left = HumanPlayer()
        self.right = AIPlayer()

    def cut(self, whichBoard, number, isLeft)
        desiredBoard = self.board[whichBoard]
        if((isLeft AND desiredBoard[0] % number != 0) OR
           (!isLeft AND desiredBoard[1] % number != 0))
            
