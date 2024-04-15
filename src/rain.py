import pygame
import random

class Particle():
    def __init__(self, pos=(0,0), size=15, life= 500):
        self.pos = pos
        self.size = size
        self.color = pygame.Color(0,255,0)
        self.surface = self.update_surface()
        self.age = 0
        self.life = life
        self.dead = False
        self.alpha = 255

    def update(self, dt):
        self.age += dt
        if self.age > self.life:
            self.dead = True
        self.alpha = 255 * (1-(self.age/self.life))

    def update_surface(self):
        surf = pygame.Surface((self.size*.8,self.size*.8))
        surf.fill(self.color)
        return surf
    
    def draw(self, surface):
        if self.dead:
            return
        self.surface.set_alpha(self.alpha)
        surface.blit(self.surface, self.pos)
class Rain():
    """Function creates particles that fall down from the top of the screen at randomly generated 
    locations along the x axis."""
    def __init__(self, res):
        self.res = res
        self.particle_size = 15
        self.rate = 1
        self.trails = []

    def update(self, dt):
      self.new_trail()
      self.update_trails(dt)

    def update_trails(self, dt):
        for idx, trail in enumerate(self.trails):
            trail.update(dt)
            if self.offscreen(trail):
                del self.trails[idx]

    def offscreen(self, trail):
        offscreen = trail.particles[-1].pos[1] > self.res[1]
        return offscreen
    
    def new_trail(self):
        for count in range(self.rate):
            width = self.res[0]
            x = random.randrange(0, width, self.particle_size)
            pos = (x, 0)
            life = random.randrange(500, 1500)
            trail = particle_trails(pos, self.particle_size, life)
            self.trails.insert(0, trail)

    def draw(self, surface):
        for trail in self.trails:
            trail.draw(surface)

class particle_trails():
    """Function makes it so that each particle leaves a trail of fading paricles that randomly vary
    in length."""

    def __init__(self, pos, size, life):
        self.pos= pos
        self.size = size
        self.life = life
        self.particles = []

    def update(self, dt):
        particle = Particle(self.pos, size=self.size, life=self.life)
        self.particles.insert(0, particle)
        self.update_particles(dt)
        self.position(dt)

    def update_particles(self, dt):
        for idx, particle in enumerate(self.particles):
            particle.update(dt)
            if particle.dead:
                del self.particles[idx]

    def position(self, dt):
        x, y = self.pos
        y += self.size
        self.pos = (x, y)

    def draw(self, surface):
        for particle in self.particles:
            particle.draw(surface)   

def main():
    """Function creates a 800x600 pixel window with a title."""
    pygame.init()
    pygame.display.set_caption("Digital Rain")
    clock = pygame.time.Clock()
    dt = 0
    resolution = (800, 600)
    screen = pygame.display.set_mode(resolution)
    rain = Rain(resolution)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
    
        rain.update(dt)

        black = pygame.Color(0, 0, 0)
        screen.fill(black)
        rain.draw(screen)
        pygame.display.flip()
        dt = clock.tick(12)
    pygame.quit()

if __name__ == "__main__":
    main()