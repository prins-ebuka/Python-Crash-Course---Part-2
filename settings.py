# Instead of doing all our setting in the game file which is the alien_invasion file
# we will save the settings here in this module.

class Settings:
    """A class to store all settings for Alien Invasion."""

    def __init__(self):
        """Initialize the game's settings."""
        self.screen_width = 800
        self.screen_height = 400
        self.bg_color = (230, 230, 230)

        # Ship settings - We are simply adjusting the ship's speed.
        self.ship_speed = 1.5