import pygame

import Colors, WindowAttributes

class Paddle(pygame.sprite.Sprite):
  def __init__(self, color, width, height):
    super().__init__()

    self.image = pygame.Surface([width, height])
    self.image.fill(Colors.BLACK)
    self.image.set_colorkey(Colors.BLACK)
    
    pygame.draw.rect(self.image, color, [0,0,width,height])

    self.rect = self.image.get_rect()
  
  def moveUp(self, pixels):
    self.rect.y -= pixels
    # Don't go off screen to the top
    if self.rect.y < 0:
      self.rect.y = 0
  
  def moveDown(self, pixels):
    self.rect.y += pixels
    if self.rect.y > 400:
      self.rect.y = 400