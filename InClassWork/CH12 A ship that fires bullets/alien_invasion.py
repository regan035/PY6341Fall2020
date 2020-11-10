import sys
import pygame
from settings import Settings
from ship import Ship
from bullet import Bullet

class AlienInvasion:
    """Overall class to manage game assets and behavior."""
    def __init__(self):
        """Initial the game, and create game resources."""
        pygame.init()
        self.settings = Settings()

        #Display in full screen
        # self.screen = pygame.display.set_mode((0,0),pygame.FULLSCREEN)
        # self.settings.screen_width = self.screen.get_rect().screen_width
        # self.settings.screen_height = self.screen.get_rect().screen_height

        #Display in window
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))

        pygame.display.set_caption("Alien Invasion")
        self.ship = Ship(self)
        self.bullets = pygame.spirite.Group()
        # Set the blackground color.
        #self.bg_color = (230, 230, 230)
        #Ship settings
        self.ship_speed = 1.5

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_events()
            self.ship.update()
            self._update_bullets()
            self._update_screen()
    
    def _check_events(self):
        """Respond to keypresses and mouse events"""
        #Watch fpr keyboard and mouse events.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                 sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)

            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

                    #Move the ship to right
                    #self.ship.rect.x += 1

    def _check_keydown_events(self, event):
        """Respond to keypresses"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
    
    def _check_keyup_events(self, event):
        """Respond to key releases"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _fire_bullet(self):
        """Create a new bullet and add it to the bullets group"""
        if len(self.bullets) < self.settings.bullet_allowd:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullets(self):
        """update postion of bullet and get rid of old bulltes"""
        #Update bullet positions
        self.bullets.update()
        # Get rid of bullets that have disappeared
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
            print(len(self.bullets))


    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""
        # Redraw the screen during each pass through the loop.
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        for bullet in self.bullets.spirites():
            bullet.draw_bullet()
        # Make the most recently draw screen visible.
        pygame.display.flip()
    
if __name__=='__main__':
    #Make a game instance, and run the game.
    ai = AlienInvasion()
    ai.run_game()
