// Import the Pygame.js library
import Pygame from "./static/js/pygame.js";

// Set the size of the window
const WINDOW_SIZE = [600, 600];

// Initialize Pygame.js
Pygame.init();

// Create the Pygame window
const screen = Pygame.display.set_mode(WINDOW_SIZE);

// Set the caption of the window
Pygame.display.set_caption("Chess Game");

// Main game loop
function gameLoop() {
    // Handle Pygame events
    for (const event of Pygame.event.get()) {
        if (event.type === Pygame.QUIT) {
            // Quit the game if the user closes the window
            Pygame.quit();
            return;
        }
    }
    
    // Update the display
    Pygame.display.update();

    // Request animation frame
    requestAnimationFrame(gameLoop);
}

// Start the game loop
requestAnimationFrame(gameLoop);
