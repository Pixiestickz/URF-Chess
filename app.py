from flask import Flask, render_template
import pygame

#initialize flask object named app
app = Flask(__name__)

#Set the size of the window
WINDOW_SIZE = (600,600)

#Initialize pygame
pygame.init()

#Create a pygame window
screen = pygame.display.set_mode(WINDOW_SIZE)

#Set the caption of the window
pygame.display.set_caption("URF Chess")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/game")
def game():
    return render_template("game.html")

if __name__ == "__main__":
    app.run(debug=True)
