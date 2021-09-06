import pygame

import Colors, WindowAttributes
from Ball import Ball
from Paddle import Paddle

class Game:
  def __init__(self):
    pygame.init()
    pygame.display.set_caption('Pong')

    self.screen = pygame.display.set_mode(WindowAttributes.SIZE)
    self.clock = pygame.time.Clock()

    self._createSprites()

    self.running = False

    self._initScores()
    
  def run(self):
    self._processUserInputs()
    self._checkCollisions()
    self._updateScores()

    self.sprites.draw(self.screen)
    self.sprites.update()
    pygame.display.flip()

    # Limit game speed to 60 fps
    self.clock.tick(60)

  def _awaitUserQuit(self):
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        self.running = False

  def _checkCollisions(self):
    if self.ball.rect.x >= 690:
      self.score1 += 1
      self.ball.velocity[0] = -self.ball.velocity[0]
    if self.ball.rect.x <= 0:
      self.score2 += 1
      self.ball.velocity[0] = -self.ball.velocity[0]
    if self.ball.rect.y > 490:
      self.ball.velocity[1] = -self.ball.velocity[1]
    if self.ball.rect.y < 0:
      self.ball.velocity[1] = -self.ball.velocity[1]

    if pygame.sprite.collide_mask(self.ball, self.paddle1) or pygame.sprite.collide_mask(self.ball, self.paddle2):
      self.ball.bounce()

  def _createSprites(self):
    self.paddle1 = Paddle(Colors.WHITE, width=10, height=100)
    self.paddle1.rect.x = 20
    self.paddle1.rect.y = 200

    self.paddle2 = Paddle(Colors.WHITE, width=10, height=100)
    self.paddle2.rect.x = 670
    self.paddle2.rect.y = 200

    self.ball = Ball(Colors.WHITE, 10, 10)
    self.ball.rect.x = 345
    self.ball.rect.y = 195

    self.sprites = pygame.sprite.Group()
    self.sprites.add(self.paddle1)
    self.sprites.add(self.paddle2)
    self.sprites.add(self.ball)

  def _initScores(self):
    self.font = pygame.font.Font(None, 74)
    self.score1 = 0
    self.score2 = 0

  def _processUserInputs(self):
    keys = pygame.key.get_pressed()
    self._processUserMovement(keys)

    self._awaitUserQuit()

  def _processUserMovement(self, keys):
    if keys[pygame.K_w]:
      self.paddle1.moveUp(5)
    if keys[pygame.K_s]:
      self.paddle1.moveDown(5)
    if keys[pygame.K_UP]:
      self.paddle2.moveUp(5)
    if keys[pygame.K_DOWN]:
      self.paddle2.moveDown(5)
    
    # Hide the old white paddle pixels
    self.screen.fill(Colors.BLACK)

  def _updateScores(self):
    text = self.font.render(str(self.score1), True, Colors.WHITE)
    self.screen.blit(text, (250, 10))
    text = self.font.render(str(self.score2), True, Colors.WHITE)
    self.screen.blit(text, (420, 10))
