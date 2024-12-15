from settings import * 
from button import Button

class MainMenu:
    def __init__(self, screen, font, start_game_callback, options_callback, credits_callback, quit_callback):
        self.screen = screen
        self.background = pygame.image.load("graphics/backgrounds/main_menu_bg.png").convert_alpha()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
        self.background = pygame.transform.scale(self.background, (WINDOW_WIDTH, WINDOW_HEIGHT))
        
        self.logo = pygame.image.load("graphics/backgrounds/logo.png").convert_alpha()
        self.font = font

        self.start_game = start_game_callback
        self.show_options = options_callback
        self.show_credits = credits_callback
        self.quit_game = quit_callback

        self.buttons = [
            Button("Start Game", self.font, (400, 250), "white", "blue", self.start_game),
            Button("Options", self.font, (400, 320), "white", "blue", self.show_options),
            Button("Credits", self.font, (400, 390), "white", "blue", self.show_credits),
            Button("Quit", self.font, (400, 460), "white", "blue", self.quit_game)
        ]

    def reset(self):
        """Reset any animations or states for the main menu."""
        pass

    def update(self, event):
        for button in self.buttons:
            button.handle_event(event)

    def draw(self):
        self.screen.blit(self.background, (0, 0))
        title_surface = self.font.render("Main Menu", True, "white")
        self.screen.blit(title_surface, (320, 110)) 
        self.screen.blit(self.logo, (600, 40))

        for button in self.buttons:
            button.draw(self.screen)
