import pygame 
from sys import exit

class Slider:
    def __init__(self, xpos: int, ypos: int, max_value: int):
        self.x = xpos
        self.y = ypos
        self.max_value = max_value
        self.value = max_value
        self.old_mouse_pressed = False

        self.slider_button_width = 30
        self.slider_button_height = 10
        self.slider_button = pygame.Rect(self.x - (self.slider_button_width / 2 - 1), self.y - self.slider_button_height / 2, self.slider_button_width, self.slider_button_height)

    def detect(self, mx, my, mouse_pressed):
        mouse_pressed = mouse_pressed[0]
        if (mouse_pressed and self.slider_button.x <= mx <= self.slider_button.x + 30 and self.slider_button.y <= my <= self.slider_button.y + 10) or self.old_mouse_pressed:
                self.slider_button.y = max(self.y - self.slider_button_height / 2, min(my - self.slider_button_height / 2, ((self.y - self.slider_button_height / 2) + self.max_value * 3)))
                self.old_mouse_pressed = mouse_pressed

    def draw(self, screen):
        pygame.draw.line(screen, "white", (self.x, ((self.y + self.max_value * 3) + 10)), (self.x, (self.y - 10)), 40)
        pygame.draw.line(screen, "#4664fa", (self.x, (self.y + self.max_value * 3)), (self.x, self.slider_button.centery), 20)
        pygame.draw.rect(screen, "#3858fc", self.slider_button)

    def update(self):
         self.value = self.max_value - ((self.slider_button.centery - self.y) // 3)

    def get_value(self):
         return self.max_value - ((self.slider_button.centery - self.y) // 3)

def main():
    pygame.init()

    screen = pygame.display.set_mode((600, 600))
    pygame.display.set_caption("Sliders")
    clock = pygame.time.Clock()
    font = pygame.font.Font(None, 50)

    slider = Slider(100, 100, 100)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        screen.fill((50, 50, 50))
        
        slider.update()
        mouse = pygame.mouse.get_pressed()
        mouse_pos = pygame.mouse.get_pos()
        text = font.render(f"Value: {slider.value}", True, "white")
        text_rect = text.get_rect(topleft = (300, 10))
        screen.blit(text, text_rect)

        slider.detect(mouse_pos[0], mouse_pos[1], mouse)
        slider.draw(screen)

        pygame.display.update()
        clock.tick(60)

if __name__ == "__main__":
    main()