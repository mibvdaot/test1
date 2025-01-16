import pygame

class GameSprite(pygame.sprite.Sprite):
    def __init__(self, image, pos_x, pos_y, size_x, size_y, speed, win_size):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load(image), (size_x, size_y))
        self.speed = speed
        
        self.win_width, self.win_height = win_size

        self.rect = self.image.get_rect()
        self.rect.x = pos_x
        self.rect.y = pos_y
    
    def draw(self):
        return self.image, (self.rect.x, self.rect.y)