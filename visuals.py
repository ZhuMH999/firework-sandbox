import pygame

class Visuals:
    def __init__(self, model, win):
        self.model = model
        self.win = win

    def draw(self):
        self.win.fill((0, 0, 0))

        for f in self.model.fireworks:
            if f.life <= 0:
                continue

            t = f.life / f.max_life
            alpha = int(255 * t)
            radius = max(1, f.radius)

            surf = pygame.Surface((radius * 2, radius * 2), pygame.SRCALPHA)
            pygame.draw.circle(
                surf,
                (*f.color, alpha),
                (radius, radius),
                radius
            )

            halo_radius = int(radius * 2.5)
            halo_surf = pygame.Surface((halo_radius*2, halo_radius*2), pygame.SRCALPHA)
            halo_color = (
                min(255, f.color[0] + 50),
                min(255, f.color[1] + 50),
                min(255, f.color[2] + 50)
            )

            pygame.draw.circle(
                halo_surf,
                (*halo_color, int(alpha*0.5)),
                (halo_radius, halo_radius),
                halo_radius
            )
            self.win.blit(halo_surf, (f.x - halo_radius, f.y - halo_radius))

            self.win.blit(surf, (f.x - radius, f.y - radius))
