from firework import Firework
from constants import generate_text_velocities

class Model:
    def __init__(self):
        self.fireworks = []
        self.text_vel = generate_text_velocities('MERRY CHRISTMAS!', 0.06)

    def spawn_fireworks(self, x, y):
        for vx, vy in self.text_vel:
            self.fireworks.append(Firework(x, y, vx, vy))

    def manage_fireworks(self):
        for f in self.fireworks[:]:
            f.update_pos()
            if f.life <= 0:
                self.fireworks.remove(f)

    def check_where_interact(self, x, y, button):
        if button == 1:
            self.spawn_fireworks(x, y)
