import pygame

import Colors, WindowAttributes
from Ball import Ball
from Paddle import Paddle

class Game:
  def __init__(self):
    pygame.init()
    pygame.display.set_caption('Pong')

    self._screen = pygame.display.set_mode(WindowAttributes.SIZE)
    self._clock = pygame.time.Clock()

    self._createSprites()
    self._initScores()

    self.running = False
    
  def run(self):
    self._ball.update()
    self._processUserInputs()
    self._checkCollisions()
    self._updateScores()

    self._sprites.draw(self._screen)
    pygame.display.flip() # Update the entire screen
    self._clock.tick(60) # Limit game speed to 60 fps

  def _awaitUserQuit(self, keys):
    if keys[pygame.K_ESCAPE]:
      self.running = False
    
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        self.running = False

  def _checkCollisions(self):
    # Ball hits right wall
    if self._ball.rect.x >= WindowAttributes.WIDTH - self._ball.width:
      self._score1 += 1
      self._ball.vX = -self._ball.vX
    
    # Ball hits left wall
    if self._ball.rect.x <= 0:
      self._score2 += 1
      self._ball.vX = -self._ball.vX
    
    # Ball reaches ground
    if self._ball.rect.y > WindowAttributes.HEIGHT - self._ball.height:
      self._ball.vY = -self._ball.vY
    
    # Ball reaches ceiling
    if self._ball.rect.y < 0:
      self._ball.vY = -self._ball.vY

    # Ball collides with paddle
    if pygame.sprite.collide_rect(self._ball, self._paddle1) or pygame.sprite.collide_rect(self._ball, self._paddle2):
      self._ball.bounce()

  def _createSprites(self):
    self._paddle1 = Paddle(Colors.WHITE, width=10, height=100)
    self._paddle1.rect.x = 20
    self._paddle1.rect.y = WindowAttributes.HEIGHT // 2 - self._paddle1.height // 2

    self._paddle2 = Paddle(Colors.WHITE, width=10, height=100)
    self._paddle2.rect.x = WindowAttributes.WIDTH - self._paddle2.width - self._paddle1.rect.x
    self._paddle2.rect.y = WindowAttributes.HEIGHT // 2 - self._paddle1.height // 2

    self._ball = Ball(Colors.WHITE, 10, 10)
    self._ball.rect.x = WindowAttributes.WIDTH // 2 - self._ball.width // 2
    self._ball.rect.y = WindowAttributes.HEIGHT // 2 - self._ball.height // 2

    self._sprites = pygame.sprite.Group()
    self._sprites.add(self._paddle1)
    self._sprites.add(self._paddle2)
    self._sprites.add(self._ball)

  def _initScores(self):
    self._font = pygame.font.Font(None, 74)
    self._score1 = 0
    self._score2 = 0

  def _processUserInputs(self):
    keys = pygame.key.get_pressed()
    self._processUserMovement(keys)

    self._awaitUserQuit(keys)

  def _processUserMovement(self, keys):
    if keys[pygame.K_w]:
      self._paddle1.moveUp(5)
    if keys[pygame.K_s]:
      self._paddle1.moveDown(5)
    if keys[pygame.K_UP]:
      self._paddle2.moveUp(5)
    if keys[pygame.K_DOWN]:
      self._paddle2.moveDown(5)
    
    # Hide the old white paddle pixels
    self._screen.fill(Colors.BLACK)

  def _updateScores(self):
    text = self._font.render(str(self._score1), True, Colors.WHITE)
    self._screen.blit(text, (250, 10))
    text = self._font.render(str(self._score2), True, Colors.WHITE)
    self._screen.blit(text, (420, 10))
