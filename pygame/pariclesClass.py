import pygame
from sys import exit
from random import randint

class Particle:
    def __init__(self):
        self.particles = []

    def emit(self, screen):
        if self.particles:
            self.delete_particles() 
            for particle in self.particles:
                particle[3] += 1
                particle[1] += particle[3]
                particle[3] *= 0.98
                particle[0] += particle[2]
                pygame.draw.circle(screen, particle[4], (particle[0], particle[1]), particle[5])

    def create_particles(self, xpos, ypos):
        x = xpos
        y = ypos
        speedx = randint(-10, 10)
        speedy = randint(-18, -5)
        color = (randint(0, 255), randint(0, 255), randint(0, 255))
        radius = randint(8, 13)
        particle = [x, y, speedx, speedy, color, radius]
        self.particles.append(particle)

    def delete_particles(self):
        particle_copy = [particle for particle in self.particles if particle[1] < 790]
        self.particles = particle_copy

def main():
    pygame.init()

    screen = pygame.display.set_mode((800, 800))
    pygame.display.set_caption("Particles")
    clock = pygame.time.Clock()

    particle1 = Particle()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()


        screen.fill((240, 240, 240))

        if pygame.mouse.get_pressed()[0]:
            for i in range(1):
                particle1.create_particles(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])

        particle1.emit(screen)
        
        pygame.display.update()
        clock.tick(60)

if __name__ == "__main__" :
    main()