import pygame

import WindowAttributes

class Paddle(pygame.sprite.Sprite):
  def __init__(self, color, width, height):
    super().__init__()
    self.height = height
    self.width = width

    self.image = pygame.Surface([width, height])
    pygame.draw.rect(self.image, color, [0,0, width, height])
    self.rect = self.image.get_rect()
  
  def moveUp(self, pixels):
    self.rect.y -= pixels
    if self.rect.y < 0:
      self.rect.y = 0
  
  def moveDown(self, pixels):
    self.rect.y += pixels
    if self.rect.y >= WindowAttributes.HEIGHT - self.height:
      self.rect.y = WindowAttributes.HEIGHT - self.height
