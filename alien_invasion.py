import sys

import pygame

from settings import Settings
from ship import Ship

class AlienInvasion:
    """Overall class to manage game assets and behaviour."""

    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()
        self.settings = Settings()

        #Running the game in fullscreen mode. Since I do not enjoy the fullscreen I will comment this section
        #self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        #self.settings.screen_width = self.screen.get_rect().width
        #self.settings.screen_height = self.screen.get_rect().height

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")
        
        self.ship = Ship(self)


    def run_game(self):
        """Start the main loop for the game."""
        while True:
            # to call a method within a class we use the dot notation with the variable self and the name of the method.
            self._check_events()
            self.ship.update()
            self._update_screen()
            # Watch for keyboard and mouse events.
            
    def _check_events(self):
        """Respond to keypresses and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            # My comment: Please refer to the Piloting Ship section below.
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
                if event.type == pygame.K_RIGHT:
                    self.ship.moving_right = True
                elif event.key == pygame.K_LEFT:
                    self.ship.moving_left = True

            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
                if event.key == pygame.K_RIGHT:
                    self.ship.moving_right = False
                elif event.key == pygame.K_LEFT:
                    self.ship.moving_left = False
                    # Move the ship to the right.
                    self.ship.rect.x +=1

    def _check_keydown_events(self, event):
        """Respond to keypresses."""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        # Pressing Q to Quit
        elif event.key == pygame.K_q:
            sys.exit

    def _check_keyup_events(self, event):
        """Respond to key releases."""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""
        # Redraw the screen during each pass through the loop.
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()

        # Make the most recently drawn screen visible.
        pygame.display.flip()

if __name__ == '__main__':
    # Make a game instance, and run the game.
    ai = AlienInvasion()
    ai.run_game()

# my notes
# first we imported sys and pygame modules. The Pygame module contains the functionally to make a game.
# we use the sys module to exit the game when the player quits.
# at some point, we create a class Settings to hold the settings of the game and imported it 
# into the game (alien_invasion) class.

# Since it has been long and this is the first time doing this project, I need to revise all I have done so far.
# 3 things that look quite strange are the way we first initialised the pygame.init() and
# modules like display etc..

# Page 236, I am in "Refactoring the _check events() and _update_screen() Methods."
# In this section, we'll break the run-game() method, which is getting lengthy, into two "helper methods."
# A "helper method" does work inside a class but isn't meant to be called through an instance. 
# In Python, a single leading undescore indicates a helper nethod.

# Piloting the Ship
# Responding to a Keypress: Whenever the player presses a key, that key-press is registered in Pygame as an event.
# Each event is picked up by the pygame.event.get() method.
# Each keypress is registered as a KEYDOWN event.

# With all the complications I am seeing here, I need to comeback to this to try and capture the main points.