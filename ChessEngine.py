"""
Stores information about current state
Determines valid moves at the current state
Maintaines move log 
"""

class GameState():
    
    def __init__(self):

        """
        2d array
        White's perspective
        """
        self.board = [
            ["bR", "bN", "bB", "bQ", "bK", "bB", "bN", "bR"],
            ["bP", "bP", "bP", "bP", "bP", "bP", "bP", "bP"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["wP", "wP", "wP", "wP", "wP", "wP", "wP", "wP"],
            ["wR", "wN", "wB", "wQ", "wK", "wB", "wN", "wR"]
        ]


        self.whiteToMove = True
        self.moveLog = []

    '''
    takes move as a parameter and executes it
        Doesn't take into account: castling, pawn promotion, en-passant
    '''
    def makeMove(self, move):
        #Take piece from starting location and move it to ending location
        self.board[move.startPOS[0]][move.startPOS[1]] = "--"
        self.board[move.endPOS[0]][move.endPOS[1]] = move.pieceMoved
        self.moveLog.append(move) #log the move

        #Switch the players turn
        self.whiteToMove = not self.whiteToMove 

    '''
    Undo the last move made
    ''' 
    def undoMove(self):
        #Ensure that there's a move to undo
        if len(self.moveLog) != 0:
            #remove the most recent move from the move log; popping since we're ammending
            move = self.moveLog.pop()

            #After the most recent move was removed, we want to revert any changes
            self.board[move.startPOS[0]][move.startPOS[1]] = move.pieceMoved
            self.board[move.endPOS[0]][move.endPOS[1]] = move.pieceCaptured

            #Revert who's turn it is
            self.whiteToMove = not self.whiteToMove

    '''
    All moves not considering checks
    '''
    def getAllPossibleMoves(self):
        #Empty list of moves
        moves = []

        #search entire board
        for r in range(len(self.board)):
            for c in range(len(self.board[r])):
                #Generates current turn using the first character 
                #Example: bK -> "b" | wQ -> "w"
                turn = self.board[r][c][0]
                
                #Check for proper turns
                if (turn == 'w' and self.whiteToMove) and (turn == 'b' and not self.whiteToMove):
                    #Grab the piece using the second character
                    #Example: bK -> "K" | wQ -> "Q"
                    piece = self.borard[r][c][1]

                    '''
                    Sort logic by piece
                    '''
                    #Pawn moves
                    if piece == 'p':
                        self.getAllPossibleMoves(r,c,moves)
                    
                    #rook moves
                    elif piece == 'R':
                        self.getRookMoves(r,c,moves)

        return moves

    '''
    Pawn moves
    '''
    def getPawnMoves(self, r, c, moves):
        pass

    '''
    Rook moves
    '''
    def getRookMoves(self, r, c, moves):
        pass

    '''
    All moves considering checks
    '''
    def getValidMoves(self):
        #Take into consideration valid moves first
        return self.getAllPossibleMoves()

class Move():
    """
    Converts to chess notation and vice versa
    """
    #Constructor class
    #Maps keys to values
    #Key : Value
    ranksToRows = {"8" : 0, "7" : 1, "6" : 2, "5" : 3,
                    "4" : 4, "3" : 5, "2" : 6, "1" : 7}
    rowsToRanks = {v: k for k, v in ranksToRows.items()} #for loop to reverse a dictionary

    filesToCols = {"a" : 0, "b" : 1, "c" : 2, "d" : 3,
                    "e" : 4, "f" : 5, "g" : 6, "h" : 7}
    colsToFiles = {v: k for k, v in filesToCols.items()}#for loop to reverse a dictionary


    #constructor class
    """
    Passing in the start position, end position, and the current state of the board
    """
    def __init__(self, startPOS, endPOS, board):
        
        #Keep track of moved pieces and captured pieces
        #recall that startPOS and endPOS are: [row,col] ~ [0,1]
        self.startPOS = startPOS
        self.endPOS = endPOS
        self.pieceMoved = board[startPOS[0]][startPOS[1]]
        self.pieceCaptured = board[endPOS[0]][endPOS[1]]

        '''
        Unique ID for each move:
            1000 (starting row)
            100 (starting col)
            10 (ending row)
            1 (ending col)
        
            EX:
                7543
                    Starting row = 7
                    Starting col = 5
                    ending row = 4
                    ending col = 3
        '''
        self.moveID = (1000* self.startPOS[0]) + (100 * self.startPOS[1]) + (10 * self.endPOS[0]) + self.endPOS[1]
        print(self.moveID)

    '''
    Overriding the equals method in order to properly compare objects
    '''
    def __eq__(self, other):
        if isinstance(other, Move):
            #Only need to compare moveIDs
            return self.moveID == other.moveID
        
        return False
    


    def chessNotation(self):
        #Can modify to make real chess notation
        return self.getRankFile(self.startPOS[0], self.startPOS[1]) + self.getRankFile(self.endPOS[0], self.endPOS[1])
    def getRankFile(self, x, y):
        #Gets file and ranks
        return self.colsToFiles[y] + self.rowsToRanks[x]
    

