import pygame

class Ship:
    """A class to manage the ship"""

    def __init__(self, ai_game):
        """Initialise the ship and set its starting position"""
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        # load the ship image and get its rect
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        # start each new ship at the bottom centre of the screen
        self.rect.midbottom = self.screen_rect.midbottom

        # store a decimal value for the ship horizontal position
        self.x = float(self.rect.x)

        # movement flag
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """ update the ship's position based on the movement flags"""
        # update ship's x value, not the rect
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed

        # update rect object from self.x
        self.rect.x = self.x

    def blitme(self):
        """draw the ship at its current location"""
        self.screen.blit(self.image, self.rect)

    def centre_ship(self):
        """Centre ship on the screen"""
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)


