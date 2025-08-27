import pygame 
from sys import exit

class Laser():
    def __init__(self, color, pos1, pos2, size, screen):
        self.color = color
        self.pos1 = pos1
        self.pos2 = pos2
        self.size = size

        self.trans_surf = pygame.Surface(screen.get_size(), pygame.SRCALPHA)

        self.color1 = self.color[:3] + (25,)
        self.color2 = self.color[:3] + (64,)
        self.color3 = self.color[:3] + (127,)

    def draw(self, screen):
        self.trans_surf.fill((0, 0, 0, 0))

        pygame.draw.line(self.trans_surf, self.color1, self.pos1, self.pos2, int(self.size * 20))
        pygame.draw.line(self.trans_surf, self.color2, self.pos1, self.pos2, int(self.size * 12))
        pygame.draw.line(self.trans_surf, self.color3, self.pos1, self.pos2, int(self.size * 4))

        screen.blit(self.trans_surf, (0, 0))

def main():
    pygame.init()

    screen = pygame.display.set_mode((600, 600))
    pygame.display.set_caption("Lasers")
    clock = pygame.time.Clock()

    laser1 = Laser((255, 0, 0, 255), (0,0), (600, 600), 1, screen)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
        
        screen.fill((230, 230, 230))

        laser1.draw(screen)

        pygame.display.update()
        clock.tick(60)

if __name__ == "__main__":
    main()