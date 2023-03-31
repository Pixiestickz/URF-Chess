import pygame
from flask import Flask

app = Flask(__name__)

@app.route('/')

def index():
    return "hello world!"

# We can disable debug mode in production environments to disable security issues
if __name__ == "__main__":
    app.run(debug = True)


