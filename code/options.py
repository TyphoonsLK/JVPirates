from settings import * 
from button import Button

class OptionsMenu:
    def __init__(self, screen, font, back_to_main_callback):
        self.screen = screen
        self.font = font
        self.small_font = font
        self.back_to_main = back_to_main_callback

        self.buttons = [
            Button("Video Settings", self.font, (400, 250), "white", "blue", self.show_video_settings),
            Button("Keyboard Settings", self.font, (400, 320), "white", "blue", self.show_keyboard_settings),
            Button("Volume Settings", self.font, (400, 390), "white", "blue", self.show_volume_settings),
            Button("Back", self.font, (400, 460), "white", "blue", self.back_to_main),
        ]

        # Settings states
        self.fullscreen = False
        self.volume = 50
        self.key_bindings = {"Move Left": "A", "Move Right": "D", "Jump": "Space"}

    def show_video_settings(self):
        self.fullscreen = not self.fullscreen  # Toggle fullscreen
        print(f"Fullscreen is now {'ON' if self.fullscreen else 'OFF'}")

    def show_keyboard_settings(self):
        print("Current Key Bindings:")
        for action, key in self.key_bindings.items():
            print(f"{action}: {key}")
        # Add logic to rebind keys if necessary

    def show_volume_settings(self):
        print(f"Current Volume: {self.volume}")
        # Add volume adjustment logic (e.g., increase or decrease using buttons)

    def update(self, event):
        for button in self.buttons:
            button.handle_event(event)

    def draw(self):
        self.screen.fill("black")
        title_surface = self.font.render("Options Menu", True, "white")
        self.screen.blit(title_surface, (WINDOW_WIDTH // 2 - title_surface.get_width() // 2, 100))

        for button in self.buttons:
            button.draw(self.screen)
