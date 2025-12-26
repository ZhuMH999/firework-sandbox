from constants import FRICTION, GRAVITY, WIND
import random

class Firework:
    def __init__(self, x_origin, y_origin, x_vel, y_vel):
        self.x = x_origin
        self.y = y_origin
        self.x_vel = x_vel
        self.y_vel = y_vel

        self.color = random.choice([
            (0, 179, 44),
            (220, 61, 42),
        ])

        self.life = random.uniform(150, 170)
        self.max_life = self.life
        self.radius = 5

    def update_pos(self):
        # move particle
        self.x += self.x_vel + WIND
        self.y += self.y_vel

        # friction slows both axes slightly
        self.x_vel /= FRICTION
        self.y_vel /= FRICTION

        # gravity always applies
        self.y_vel += GRAVITY

        # decay
        self.life -= 1
        self.radius = max(1, int(5 * (self.life / self.max_life)))

