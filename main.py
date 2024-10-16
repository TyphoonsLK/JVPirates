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

#background and boundaries
def draw_bg():
    screen.fill(Background)
    pygame.draw.line(screen, RED, (0, 50), (SCREEN_WIDTH, 50))
    pygame.draw.line(screen, RED, (0, 600), (SCREEN_WIDTH, 600))

#Prirate class
class Pirate(pygame.sprite.Sprite):
	
    #load all images for the players
		animation_types = ['Idle']
		for animation in animation_types:
			#reset temporary list of images
			temp_list = []
			#count number of files in the folder
			num_of_frames = len(os.listdir(f'assets/img/character/Captain{self.char_type}/{animation}'))
			for i in range(num_of_frames):
				img = pygame.image.load(f'img/{self.char_type}/{animation}/{i}.png').convert_alpha()
				img = pygame.transform.scale(img, (int(img.get_width() * scale), int(img.get_height() * scale)))
				temp_list.append(img)
		# 	self.animation_list.append(temp_list)

		# self.image = self.animation_list[self.action][self.frame_index]
		# self.rect = self.image.get_rect()
		# self.rect.center = (x, y)
		
        


    

# #define game variables
# GRAVITY = 0.75
# HEALTH = 100
# TIME = 5


run = True

while run:
    pygame.time.delay(100)
    
    draw_bg()



    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        # if event.type == pygame.KEYDOWN:
        #     if event.key == pygame.K_a
    pygame.display.update()

pygame.quit()


