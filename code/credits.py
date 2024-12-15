from settings import * 
from button import Button

class CreditsMenu:
    def __init__(self, screen, font, back_to_main_callback):
        self.screen = screen
        self.font = font
        self.small_font = font
        self.back_to_main = back_to_main_callback

        self.credits = [
            "Game Developed by: Typhoons",
            "Art and Graphics: itch.io,craftpix.net",
            "Music: itch.io",
            "Special Thanks: CaftQuest & American Center",
        ]

        self.back_button = Button("Back", self.font, (400, 500), "white", "blue", self.back_to_main)

    def update(self, event):
        self.back_button.handle_event(event)

    def draw(self):
        self.screen.fill("black")
        title_surface = self.font.render("Credits", True, "white")
        self.screen.blit(title_surface, (WINDOW_WIDTH // 2 - title_surface.get_width() // 2, 50))

        for i, credit in enumerate(self.credits):
            credit_surface = self.small_font.render(credit, True, "white")
            self.screen.blit(credit_surface, (400 - credit_surface.get_width() // 2, 150 + i * 30))

        self.back_button.draw(self.screen)
