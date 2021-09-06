from Game import Game

if __name__ == '__main__':
  game = Game()
  game.running = True

  while game.running:
    game.run()
