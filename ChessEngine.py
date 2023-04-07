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

    def makeMove(self, move):
        #Take piece from starting location and move it to ending location
        self.board[move.startPOS[0]][move.startPOS[1]] = "--"
        self.board[move.endPOS[0]][move.endPOS[1]] = move.pieceMoved
        self.moveLog.append(move) #log the move

        #Switch the players turn
        self.whiteToMove = not self.whiteToMove 
        
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


    def chessNotation(self):
        #Can modify to make real chess notation
        return self.getRankFile(self.startPOS[0], self.startPOS[1]) + self.getRankFile(self.endPOS[0], self.endPOS[1])
    def getRankFile(self, x, y):
        #Gets file and ranks
        return self.colsToFiles[y] + self.rowsToRanks[x]
    

