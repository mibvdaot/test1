from game_sprite import GameSprite
import pygame
import math


class Bullet(GameSprite):
    def update(self):
        self.rect.y += self.speed
        if self.rect.y < 0:
            self.kill()


class AirDefense(GameSprite):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.original_image = self.image  # Сохраняем оригинальное изображение

    def update(self, target):
        # Координаты центра цели
        target_x, target_y = target.center
        
        # Вычисление вектора движения
        dx, dy = target_x - self.rect.centerx, target_y - self.rect.centery
        distance = math.hypot(dx, dy)  # Расстояние до цели

        # Проверка на достижение цели
        if distance <= 5.0:  # Снаряд достигает цели
            self.kill()
            return "dist"

        # Нормализация вектора движения
        dx, dy = dx / distance, dy / distance

        # Перемещение снаряда
        self.rect.x += -(dx * self.speed)
        self.rect.y += -(dy * self.speed)

        # Вычисление угла поворота
        angle = math.degrees(math.atan2(-dy, -dx))  # Убедитесь, что ось Y инвертирована
        # Поворот изображения и коррекция центра
        original_center = self.rect.center
        self.image = pygame.transform.rotate(self.original_image, angle)
        self.rect = self.image.get_rect(center=original_center)
        return "live"
    
class BossRocket(GameSprite):
    def update(self):
        self.rect.y += self.speed  # Ракета летит вниз
        if self.rect.top > self.win_height:  # Если ракета вышла за экран, удаляем её
            self.kill()
    