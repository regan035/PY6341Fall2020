import pygame
class Settings:
    """A class to store all settings for Alien Invasion."""


    def __init__(self):
        """Initealize the game's settings."""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230,230,230)
        bg_img_path = '/Users/genli/Desktop/PY6341Fall2020/Gen Li GitRepo/FinalProject/images/space.png'
        self.bg_img = pygame.image.load(bg_img_path)
        # Ship settings
        self.ship_speed = 1.5

        # Bullet settings
        self.bullet_speed = 2.5
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (255,69,0)
        self.bullet_allowed = 3
