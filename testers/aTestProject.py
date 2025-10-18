import pygame, math
from sys import exit

pygame.init()

screen = pygame.display.set_mode((800, 800))
pygame.display.set_caption("Base code")
clock = pygame.time.Clock()

obj = pygame.image.load("testers/extension_icon.png").convert_alpha()
obj1 = pygame.transform.rotozoom(obj, 0, 0.25)
obj1_rect = obj1.get_rect(center = (400, 400))

dir = math.radians(1)
speed = 5

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.fill((50,50,50))

    # mousex = pygame.mouse.get_pos()[0]
    # mousey = pygame.mouse.get_pos()[1]
    # dir = (math.atan2(-(mousey - obj1_rect.centery), mousex - obj1_rect.centerx))

    if obj1_rect.right >= 800 or obj1_rect.left <= 0:
        dir = math.pi - dir
    if obj1_rect.top <= 0 or obj1_rect.bottom >= 800:
        dir = -dir

    obj1_rect.centerx += speed * math.cos(dir)
    obj1_rect.centery += -speed * math.sin(dir)

    screen.blit(obj1, obj1_rect)

    pygame.display.update()
    clock.tick(120)