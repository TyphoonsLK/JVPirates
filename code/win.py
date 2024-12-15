from settings import * 
from button import Button

class CongratulationsScreen:
    def __init__(self, screen, font, back_to_main_callback):
        self.screen = screen
        self.font = font
        self.small_font = font
        self.back_to_main = back_to_main_callback

        self.message = "Congratulations! You completed the game!"
        self.buttons = [
            Button("Back to Main Menu", self.font, (400, 400), "white", "blue", self.back_to_main),
        ]

    def update(self, event):
        for button in self.buttons:
            button.handle_event(event)

    def draw(self):
        self.screen.fill("black")
        title_surface = self.font.render("Congratulations!", True, "gold")
        self.screen.blit(title_surface, (WINDOW_WIDTH // 2 - title_surface.get_width() // 2, 150))

        message_surface = self.small_font.render(self.message, True, "white")
        self.screen.blit(message_surface, (400 - message_surface.get_width() // 2, 250))

        for button in self.buttons:
            button.draw(self.screen)
