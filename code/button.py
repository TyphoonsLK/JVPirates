from settings import * 

class Button:
    def __init__(self, text, font, position, text_color, bg_color, callback):
        self.text = text
        self.font = font
        self.position = position
        self.text_color = text_color
        self.bg_color = bg_color
        self.callback = callback

        self.text_surface = self.font.render(self.text, True, self.text_color)
        self.rect = self.text_surface.get_rect(center=position)

    def draw(self, surface):
        pygame.draw.rect(surface, self.bg_color, self.rect.inflate(20, 10), border_radius=5)
        surface.blit(self.text_surface, self.rect)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and self.rect.collidepoint(event.pos):
            self.callback()
