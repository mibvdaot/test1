import game_sprite
import pygame
import bullet

class Player(game_sprite.GameSprite):
    hp = 100

    def update(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        if key[pygame.K_RIGHT] and self.rect.x < self.win_width - 80:
            self.rect.x += self.speed
    
    def fire(self):
        return bullet.Bullet("bullet.png", 
                             self.rect.centerx,
                             self.rect.top,
                             15,
                             20,
                             -15,
                             (self.win_width, 
                              self.win_height)
                             )
    
    def ult(self):
        return bullet.AirDefense("bullet.png", 
                             self.win_width,
                             self.win_height,
                             15*3,
                             20*3,
                             -15,
                             (self.win_width, 
                              self.win_height)
                             )
    