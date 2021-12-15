#import pygame modile

import pygame


#create a window
pygame.init()

   #window size
        #window width
SCREEN_WIDTH = 800
        #window height
SCREEN_HEIGHT = int(SCREEN_WIDTH *0.8)

   #set screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

   #coption of Window
pygame.display.set_caption('Window Caption')

   #close the screen when we click close button
run = True
while run:
    for event in pygame.event.get():
            #quit game
        if event.type == pygame.QUIT:
            run = False
pygame.quit()
