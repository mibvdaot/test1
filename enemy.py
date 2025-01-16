from game_sprite import GameSprite
from bullet import BossRocket
import random
import pygame

class Enemy(GameSprite):
    def update(self):
        self.rect.y += self.speed
        if self.rect.y > self.win_height:
            self.rect.y = -50
            self.rect.x = random.randint(0, self.win_width-50)
            return True
        else:
            return False
        
class Boss(Enemy):
    hp = 500
    direction = 0
    def update(self):
        if self.rect.x > (self.win_width - 120) or self.rect.x < 0:
            self.direction = 0 if self.direction else 1
        if random.randint(1, 1000) < 5:
            self.direction = 0 if self.direction else 1
        if self.direction:
            self.rect.x += self.speed
        else:
            self.rect.x -= self.speed
    
    def fire_rockets(self, player_rect):
        half = self.win_width//2 
        amount_rocket = (self.win_width//2)//50
        if player_rect.centerx < self.win_width // 2:
            rocket_x = 0  # Левая половина
        else:
            rocket_x = half  # Правая половина
        
        rocket_list = []

        x = 0

        # Создаём ракеты и добавляем их в группу
        for _ in range(amount_rocket):  # Генерируем 3 ракеты
            rocket = BossRocket(
                "bullet.png",  # Изображение ракеты
                rocket_x + x,  # Позиция ракеты по X
                self.rect.bottom,  # Позиция ракеты по Y (ниже босса)
                50,  # Ширина ракеты
                50,  # Высота ракеты
                5,  # Скорость ракеты
                (self.win_width, self.win_height)
            )
            rocket.image = pygame.transform.rotate(rocket.image, 180)
            rocket_list.append(rocket)
            x += 50
        
        return rocket_list