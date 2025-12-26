import pygame
from constants import WIDTH, HEIGHT
from visuals import Visuals
from model import Model

pygame.init()

class Controller:
    def __init__(self):
        self.win = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()

        self.model = Model()
        self.visuals = Visuals(self.model, self.win)

        pygame.display.set_caption('Fireworks Sandbox')

    def run(self):
        running = True

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = pygame.mouse.get_pos()
                    self.model.check_where_interact(x, y, event.button)

            self.visuals.draw()
            self.model.manage_fireworks()

            pygame.display.update()
            self.clock.tick(60)

        pygame.quit()

if __name__ == '__main__':
    c = Controller()
    c.run()