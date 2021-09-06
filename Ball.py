from random import randint
import pygame

class Ball(pygame.sprite.Sprite):
  def __init__(self, color, width, height):
    super().__init__()
    self.width = width
    self.height = height
    
    self.image = pygame.Surface([width, height])
    pygame.draw.rect(self.image, color, [0, 0, width, height])
    self.rect = self.image.get_rect()

    self.vX = randint(6, 8)
    self.vY = randint(-8, 8)
  
  def update(self):
    self.rect.x += self.vX
    self.rect.y += self.vY
  
  def bounce(self):
    self.vX = -self.vX
    self.vY = randint(-8, 8)
