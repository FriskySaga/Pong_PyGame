import pygame

import Colors, WindowAttributes
from Ball import Ball
from Paddle import Paddle


pygame.init()
screen = pygame.display.set_mode(WindowAttributes.SIZE)
pygame.display.set_caption('Pong')
clock = pygame.time.Clock()

paddle1 = Paddle(Colors.WHITE, width=10, height=100)
paddle1.rect.x = 20
paddle1.rect.y = 200
paddle2 = Paddle(Colors.WHITE, width=10, height=100)
paddle2.rect.x = 670
paddle2.rect.y = 200

ball = Ball(Colors.WHITE, 10, 10)
ball.rect.x = 345
ball.rect.y = 195

sprites = pygame.sprite.Group()
sprites.add(paddle1)
sprites.add(paddle2)
sprites.add(ball)

score1 = 0
score2 = 0

gameIsRunning = True

while gameIsRunning:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      gameIsRunning = False
    elif event.type == pygame.KEYDOWN:
      if event.key == pygame.K_ESCAPE:
        gameIsRunning = False
  
  keys = pygame.key.get_pressed()
  if keys[pygame.K_w]:
    paddle1.moveUp(5)
  if keys[pygame.K_s]:
    paddle1.moveDown(5)
  if keys[pygame.K_UP]:
    paddle2.moveUp(5)
  if keys[pygame.K_DOWN]:
    paddle2.moveDown(5)
  
  sprites.update()

  if ball.rect.x >= 690:
    score1 += 1
    ball.velocity[0] = -ball.velocity[0]
  if ball.rect.x <= 0:
    score2 += 1
    ball.velocity[0] = -ball.velocity[0]
  if ball.rect.y > 490:
    ball.velocity[1] = -ball.velocity[1]
  if ball.rect.y < 0:
    ball.velocity[1] = -ball.velocity[1]
  
  if pygame.sprite.collide_mask(ball, paddle1) or pygame.sprite.collide_mask(ball, paddle2):
    ball.bounce()

  screen.fill(Colors.BLACK)

  # Draw the net
  pygame.draw.line(surface=screen,
                   color=Colors.WHITE,
                   start_pos=[WindowAttributes.WIDTH // 2, 0],
                   end_pos=[WindowAttributes.WIDTH // 2, WindowAttributes.HEIGHT],
                   width=5)

  sprites.draw(screen)

  font = pygame.font.Font(None, 74)
  text = font.render(str(score1), 1, Colors.WHITE)
  screen.blit(text, (250,10))
  text = font.render(str(score2), 1, Colors.WHITE)
  screen.blit(text, (420, 10))

  # Update screen
  pygame.display.flip()

  # Limit game speed to 60 fps
  clock.tick(60)
