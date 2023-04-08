"""
Handles user input and displaying the current GameState object
"""
import sys
sys.path.append('/path/to/Chess')
import pygame as p
import ChessEngine

#Initialize pygame
p.init()

#Constants
WIDTH = HEIGHT = 512 #400 is another good option ratio wise
DIMENSION = 8 
SQ_SIZE = HEIGHT // DIMENSION #512 is a power of 2 (easily divisible by 8)
MAX_FPS = 15 #For animations
IMAGES = {}

'''
Only want to load images into memory one time
Save them and reuse them
'''
#Initialize global dictionary of images
def loadImages():
    #Initialize a list of strings that has all the pieces
    pieces = ['wP', 'wR', 'wN', 'wB', 'wK', 'wQ', 'bP', 'bR', 'bN', 'bB', 'bK', 'bQ']

    #Loop each piece and load in it's image (scaling it)
    #Note we can access an image by saying 'IMAGES['wp']'
    for piece in pieces:
        IMAGES[piece] = p.transform.scale(p.image.load("images/" + piece + ".png"), (SQ_SIZE, SQ_SIZE))


'''
Handles all graphics within current game state
'''
def drawGameState(screen, gs):
    '''
    Order matters, must draw the board first before pieces
    '''
    drawBoard(screen) #draw squares on the board
    #Add in piece highlighting or move suggestion (later)
    drawPieces(screen, gs.board) #Draw pieces on top of those squares

'''
Draws the squares on the board

Top left square is always light!
'''
def drawBoard(screen):
    #Select colors for board
    colors = [p.Color("white"), p.Color("gray")]

    """
    If we add up coordinates, we can determine it's parity
    All evens are white
    All odds are black
    """
    for row in range(DIMENSION):
        for col in range(DIMENSION):
            #picks the color based on parity
            # 0 is even (white), and 1 is odd (gray)
            color = colors[((row + col) % 2)]

            #Draw it 
            p.draw.rect(screen, color, p.Rect(col*SQ_SIZE, row*SQ_SIZE, SQ_SIZE, SQ_SIZE))

'''
Draw pieces on the board
Uses current GameState.board
'''
def drawPieces(screen, board):
    """
    Setting it up the same way as last time
    """
    for row in range(DIMENSION):
        for col in range (DIMENSION):
            piece = board[row][col]

            #Check to make sure piece is in an empty square and blit it to the proper location
            if piece != "--":
                screen.blit(IMAGES[piece], p.Rect(col*SQ_SIZE, row*SQ_SIZE, SQ_SIZE, SQ_SIZE))


'''
Main Driver
Handles input and updating the graphics
'''
def main():
    #Setup screen variable
    screen = p.display.set_mode((WIDTH, HEIGHT))
    clock = p.time.Clock()
    screen.fill(p.Color("white"))

    #Grabs GameState constructor and loads in images
    gs = ChessEngine.GameState()
    loadImages()

    #tuple variable to store user clicked location (row, col)
    sqSelected = ()  
    #History of player clicks; contains two tuples 
    playerClicks = [] #Ex: [(6,4), (4,4)] v

    #While loop
    running = True
    while running:
        for e in p.event.get():
            if e.type == p.QUIT:
                running = False
            
            #Event for mouse clicks
            elif (e.type == p.MOUSEBUTTONDOWN):
                #keeps track of coords (x,y)
                location = p.mouse.get_pos()
                col = location[0] // SQ_SIZE #round down for integers
                row = location[1] // SQ_SIZE #round down for integers

                #Handles whether a tile is selected before selecting
                if sqSelected == (row, col):
                    #If a square is already selected
                    sqSelected = () #we clear it out, essentially "unselecting" the tile
                    playerClicks = [] #clear player clicks as well

                else:
                    #Store the selected tile and append it to our history of clicks
                    sqSelected = (row, col)
                    playerClicks.append(sqSelected)

                #Determine if this was the second click; "moving a piece"
                if (len(playerClicks) == 2):
                    '''
                    Create move object 
                        calls ChessEngine's Move class
                            passes in initial click square and second click square
                            passes in current game state of the board 
                    '''
                    move = ChessEngine.Move(playerClicks[0], playerClicks[1], gs.board)
                    print(move.chessNotation()) #prints chess notation
                    gs.makeMove(move) #creates the move

                    #Clear our selected squares and clicks for next move
                    sqSelected = () 
                    playerClicks = []

            #Check if we're going to undo the move
            elif e.type == p.KEYDOWN:
                #Undoes the move if the user presses "z"
                if e.key == p.K_z: 
                    gs.undoMove()
                    

        #Lock in our max FPS 
        drawGameState(screen, gs)
        clock.tick(MAX_FPS)
        p.display.flip()

'''
Call main
'''
if __name__ == "__main__":
    main()