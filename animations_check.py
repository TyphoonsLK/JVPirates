import pygame
import os

#initialize pygame
pygame.init()

#game window
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 650
scale = 2.5
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('JVPrirate')

#define colors
RED = (255, 0, 0)
Background = (0, 150, 255)

# #define game variables
GRAVITY = 0.75
HEALTH = 100
TIME = 5
run = True

#define player action variables
## just to check animations
moving_left = False
moving_right = False
attack=False
jump = False 
dead = False 


#background and boundaries
def draw_bg():
    screen.fill(Background)
    pygame.draw.line(screen, RED, (0, 50), (SCREEN_WIDTH, 50))
    pygame.draw.line(screen, RED, (0, 600), (SCREEN_WIDTH, 600))

#Prirate class
class Character(pygame.sprite.Sprite):
    def __init__(self, char_type, x, y, scale, speed):
        pygame.sprite.Sprite.__init__(self)
        # Initialize character variables
        self.alive = True  # Flag indicating whether the soldier is alive
        self.char_type = char_type  # Type of character (player or enemy)
        self.speed = speed  # Movement speed of the soldier
        self.direction = 1  # Direction the soldier is facing (1 for right, -1 for left)
        self.vel_y = 0  # Vertical velocity for jumping and gravity
        self.jump = False  # Flag indicating whether the soldier is in a jump state
        self.in_air = True  # Flag indicating whether the soldier is currently in the air
        self.flip = False  # Flag indicating whether the soldier's image should be flipped horizontally
        self.animation_list = []  # List to store different animations (Idle, Run, Jump)
        self.frame_index = 0  # Index to keep track of the current frame in the animation
        self.action = 0  # Index to represent the current action (0 for Idle, 1 for Run, 2 for Jump)
        self.update_time = pygame.time.get_ticks()  # Record the time for animation updates

        #load all images for the players
        animation_types = ['idle','walk','jump','attack','death']  #,'jump','attack','death','walk'
        for animation in animation_types:
            #reset temporary list of images
            temp_list = []
            #count number of files in the folderC:\Users\Plutonix\Pictures\JVPirates-main\assets\img\character\Captain Cropped\idle\0.png
            num_of_frames = len(os.listdir(f'assets/img/character/Captain Cropped/{animation}'))
            for i in range(num_of_frames):
                img = pygame.image.load(f'assets/img/character/Captain Cropped/{animation}/{i}.png').convert_alpha()
                img = pygame.transform.scale(img, (int(img.get_width() * scale), int(img.get_height() * scale)))
                temp_list.append(img)
            self.animation_list.append(temp_list)  # Add the list of images for the current animation state to the main animation list

        # Set initial image and position
        self.image = self.animation_list[self.action][self.frame_index]  # Set the initial image based on the current action and frame
        self.rect = self.image.get_rect()  # Get the rectangular area of the image
        self.rect.center = (x, y)  # Set the center of the rectangle to the specified initial position (x, y)

    # Function to move the soldier
    def move(self, moving_left, moving_right):
        dx = 0  # Initialize the change in x-coordinate (horizontal movement) to 0
        dy = 0  # Initialize the change in y-coordinate (vertical movement) to 0

        # Check if the soldier is moving left and update movement variables accordingly
        if moving_left:
            dx = -self.speed  # Set horizontal movement to the left with the soldier's speed
            self.flip = True  # Flip the soldier's image to face left
            self.direction = -1  # Set the direction to -1, indicating movement to the left

        # Check if the soldier is moving right and update movement variables accordingly
        if moving_right:
            dx = self.speed  # Set horizontal movement to the right with the soldier's speed
            self.flip = False  # Do not flip the soldier's image (face right)
            self.direction = 1  # Set the direction to 1, indicating movement to the right

        # Check if the soldier is in a jump state and initiate a jump
        if self.jump == True and self.in_air == False:
            self.vel_y = -11  # Set vertical velocity for jumping
            self.jump = False  # Reset the jump flag
            self.in_air = True  # Set the in_air flag to True, indicating the soldier is in the air

        # Apply gravity to the soldier's vertical velocity
        self.vel_y += GRAVITY  # Increase the vertical velocity of the soldier, simulating the effect of gravity

        # Limit the vertical velocity to prevent excessive acceleration
        if self.vel_y > 10:
            self.vel_y = 10  # Cap the vertical velocity at a maximum value of 10 to avoid overly fast descent

        dy += self.vel_y  # Update the change in y-coordinate based on the modified vertical velocity


        # Check collision with the floor to prevent the soldier from falling through
        if self.rect.bottom + dy > 300:
            dy = 300 - self.rect.bottom  # Adjust dy to keep the soldier on the floor
            self.in_air = False  # Set in_air flag to False, indicating the soldier is on the floor

        # Update the soldier's rectangle position
        self.rect.x += dx  # Update the x-coordinate
        self.rect.y += dy  # Update the y-coordinate

    # Function to update the soldier's animation
    def update_animation(self):
        ANIMATION_COOLDOWN = 100
        # Update image depending on the current frame
        self.image = self.animation_list[self.action][self.frame_index]
        # Check if enough time has passed since the last update
        if pygame.time.get_ticks() - self.update_time > ANIMATION_COOLDOWN:
            self.update_time = pygame.time.get_ticks()
            self.frame_index += 1
        # If the animation has run out, reset back to the start
        if self.frame_index >= len(self.animation_list[self.action]):
            self.frame_index = 0

        # Function to update the soldier's action
    def update_action(self, new_action):
        # Check if the new action is different from the previous one
        if new_action != self.action:
            self.action = new_action  # Set the soldier's action to the new action
            # Reset animation settings to start from the beginning of the animation
            self.frame_index = 0  # Reset the frame index to the first frame
            self.update_time = pygame.time.get_ticks()  # Record the current time for animation updates

    # Function to draw the soldier on the screen
    def draw(self):
        # Flip the image horizontally if facing left
        screen.blit(pygame.transform.flip(self.image, self.flip, False), self.rect)

		
        


# Create captain
captian = Character('Captain Cropped', 200, 200, 3, 5)

while run:
    pygame.time.delay(100)    
    draw_bg()
    captian.update_animation()
    captian.draw()
    if captian.alive:
        # Check if the player is in the air
        if captian.in_air:
            captian.update_action(2)  # 2: jump
        # Check if the player is moving left or right
        elif moving_left or moving_right:
            captian.update_action(1)  # 1: run

        ## just to check animations
        elif attack:
            captian.update_action(3)  # 1: run
        elif jump:
            captian.update_action(2)  # 2: jump    
        elif dead:
            captian.update_action(4)  # 2: jump


        else:
            captian.update_action(0)  # 0: idle
        # Move the player based on keyboard input
        captian.move(moving_left, moving_right)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        # handle key controls   
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                moving_left = True  # If 'A' key is pressed, set the flag for moving left to True
            if event.key == pygame.K_d:
                moving_right = True  # If 'D' key is pressed, set the flag for moving right to True

            ## just to check animations
            if event.key == pygame.K_f:
                attack=True                  
            if event.key == pygame.K_w :
                jump = True  
            if event.key == pygame.K_s :
                dead = True                
            if event.key == pygame.K_ESCAPE:
                run = False  # If 'Esc' key is pressed, set the 'run' flag to False, exiting the game loop
        if event.type == pygame.KEYUP:
            # Handle key releases
            if event.key == pygame.K_a:
                moving_left = False  # If 'A' key is released, set the flag for moving left to False
            if event.key == pygame.K_d:
                moving_right = False  # If 'D' key is released, set the flag for moving right to False

            ## just to check animations    
            if event.key == pygame.K_f:
                attack = False  
            if event.key == pygame.K_w:
                jump = False   
            if event.key == pygame.K_s:
                dead = False                                
    pygame.display.update()

pygame.quit()