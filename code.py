import pygame
import os

#initialize pygame
pygame.init()

#game window
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 675
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('JVPrirate')

## define game variables
gravity = 0.75
health = 100
time = 5
run = True
scale = 2.5

#colors (RGB)
Red = (255, 0, 0)
Background = (0, 150, 255)

#player action variables
moving_left = False
moving_right = False
attack=False
jump = False 
dead = False 

#background and boundaries
def draw_bg():
    screen.fill(Background)
    bg = pygame.image.load("assets/img/backgrounds/Ocean_2/fixed.png")
    screen.blit(bg, (0, 0))    
    pygame.draw.line(screen, Red, (0, 630), (SCREEN_WIDTH, 630)) 

#Characters  class
class Character(pygame.sprite.Sprite):
    def __init__(self, character, x, y, scale, speed):
        pygame.sprite.Sprite.__init__(self)
        # Initialize character variables
        self.alive = True 
        self.health=100 
        self.speed = speed  
        self.direction = 1 
        self.vel_y = 0  
        self.jump = False  
        self.in_air = True 
        self.flip = False  
        self.animation_list = []  
        self.frame_index = 0  
        self.action = 0  
        self.update_time = pygame.time.get_ticks()  

        #load all images for each player for each action
        animation_types = ['idle','walk','attack','death']
        if character=='Captain Cropped':
            animation_types = ['idle','walk','jump','attack','death']

        for animation in animation_types:
            #reset temporary list of images
            temp_list = []
            #count number of files in the folder
            num_of_frames = len(os.listdir(f'assets/img/character/{character}/{animation}'))
            for i in range(num_of_frames):
                img = pygame.image.load(f'assets/img/character/{character}/{animation}/{i}.png').convert_alpha()
                img = pygame.transform.scale(img, (int(img.get_width() * scale), int(img.get_height() * scale)))
                temp_list.append(img)
            self.animation_list.append(temp_list) 

        # Set initial image and position
        self.image = self.animation_list[self.action][self.frame_index]  
        self.rect = self.image.get_rect()  
        self.rect.center = (x, y)  

    # Character movements
    def move(self, moving_left, moving_right):
        dx = 0 
        dy = 0  

        if moving_left:
            dx = -self.speed  
            self.flip = True  
            self.direction = -1 

        if moving_right:
            dx = self.speed  
            self.flip = False  
            self.direction = 1 

        if self.jump == True and self.in_air == False:
            self.vel_y = -9  
            self.jump = False  
            self.in_air = True  

        # Apply gravity to the soldier's vertical velocity
        self.vel_y += gravity  

        # Limit the vertical velocity to prevent excessive acceleration
        if self.vel_y > 10:
            self.vel_y = 10  

        dy += self.vel_y  

        # prevent the character from falling through line
        if self.rect.bottom + dy > 300:
            dy = 300 - self.rect.bottom  
            self.in_air = False  

        # Update the character's rectangle position
        self.rect.x += dx  
        self.rect.y += dy  

    # Function to update the character's animation
    def update_animation(self):
        ANIMATION_COOLDOWN = 100
        self.image = self.animation_list[self.action][self.frame_index]
        if pygame.time.get_ticks() - self.update_time > ANIMATION_COOLDOWN:
            self.update_time = pygame.time.get_ticks()
            self.frame_index += 1

        if self.frame_index >= len(self.animation_list[self.action]):
            self.frame_index = 0

        # Function to update the character's action
    
    def update_action(self, new_action):
        if new_action != self.action:
            self.action = new_action  
            self.frame_index = 0  
            self.update_time = pygame.time.get_ticks()  
    
    def check_alive(self):  
        if self.health <= 0:  
            self.health = 0 
            self.speed = 0  
            self.alive = False  
            self.update_action(4)  # Update the action to death
    # draw the character on the screen
    def draw(self):
        screen.blit(pygame.transform.flip(self.image, self.flip, False), self.rect)
        
# Create captain
captian = Character('Captain Cropped', 600, 600, 3, 10)

while run:
    pygame.time.delay(100)    
    draw_bg()
    captian.update_animation()
    captian.draw()
    if captian.alive:
        if captian.in_air:
            captian.update_action(2)  # 2: jump
        elif moving_left or moving_right:
            captian.update_action(1)  # 1: run
        elif attack:
            captian.update_action(3)  # 1: run
        elif jump:
            captian.update_action(2)  # 2: jump    
        elif dead:
            captian.update_action(4)  # 2: jump
        else:
            captian.update_action(0)  # 0: idle

        captian.move(moving_left, moving_right) # Move the captian based on keyboard input

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        # handle key controls   
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a: # A
                moving_left = True  
            if event.key == pygame.K_d: # D
                moving_right = True  
            if event.key == pygame.K_f: # F
                attack=True                  
            if event.key == pygame.K_w and captian.alive : # W
                captian.jump = True  
            if event.key == pygame.K_s : # S
                dead = True                
            if event.key == pygame.K_ESCAPE:
                run = False  # If 'Esc' key is pressed, exiting the game loop

        # Handle key releases
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a: # A
                moving_left = False  
            if event.key == pygame.K_d: # D
                moving_right = False  
            if event.key == pygame.K_f: # F
                attack = False    
            if event.key == pygame.K_s: # S
                dead = False                                
    pygame.display.update()

pygame.quit()
