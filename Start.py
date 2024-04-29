import pygame
import button
from pygame.locals import *
import sys
import random
import time
import main

pygame.init()
# oknienka (input)
font = pygame.font.Font(None, 32)
#1 okno
gracz1_name = ""
gracz1_input_rect = pygame.Rect(300, 200, 200, 50)
gracz1_text_surface = font.render(gracz1_name, True, (255, 255, 255))
gracz1_text_rect = gracz1_text_surface.get_rect()
gracz1_text_rect.midleft = gracz1_input_rect.midleft
#2 okno
gracz2_name = ""
gracz2_input_rect = pygame.Rect(800, 200, 200, 50)
gracz2_text_surface = font.render(gracz2_name, True, (255, 255, 255))
gracz2_text_rect = gracz2_text_surface.get_rect()
gracz2_text_rect.midleft = gracz2_input_rect.midleft

#muzyka
pygame.mixer.music.load('Inne/audio.mp3')
pygame.mixer.music.set_volume(12)
pygame.mixer.music.play()


game_state = "start_menu"
scr_width = 1280
scr_height = 720


screen = pygame.display.set_mode((scr_width, scr_height))
pygame.display.set_caption("Menu")
#buttons
X_img=pygame.image.load('Grafika/exit1.jpg').convert_alpha()
start_img = pygame.image.load('Grafika/start.jpg').convert_alpha()
exit_img = pygame.image.load('Grafika/exit1.jpg').convert_alpha()
ramka = pygame.image.load("Grafika/ramka1.png")
tekst = pygame.image.load("Grafika/tekst1.png")

x = button.Button(1230,0, X_img, 0.05)
start_button = button.Button(570, 350, start_img, 0.15)
exit_button = button.Button(570, 440, exit_img, 0.15)

#Game loop
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                if gracz1_name:
                    gracz1_name = gracz1_name[:-1]
                if gracz2_name:
                    gracz2_name = gracz2_name[:-1]
            else:
                if gracz1_input_rect.collidepoint(pygame.mouse.get_pos()):
                    gracz1_name += event.unicode
                elif gracz2_input_rect.collidepoint(pygame.mouse.get_pos()):
                    gracz2_name += event.unicode
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if gracz1_input_rect.collidepoint(event.pos):
                gracz1_name = ""
            elif gracz2_input_rect.collidepoint(event.pos):
                gracz2_name = ""

    screen.fill((0, 0, 0))
    screen.blit(ramka, (0, 0))
    screen.blit(tekst, (0, 0))
    if start_button.draw(screen):
        main.main(gracz1_name, gracz2_name)
        pygame.display.flip()
    if exit_button.draw(screen) == True:
        run = False
    if x.draw(screen) == True:
        run = False



    pygame.draw.rect(screen, (255, 255, 255), gracz1_input_rect, 2)
    pygame.draw.rect(screen, (255, 255, 255), gracz2_input_rect, 2)
    gracz1_text_surface = font.render(gracz1_name, True, (255, 255, 255))
    gracz2_text_surface = font.render(gracz2_name, True, (255, 255, 255))
    screen.blit(gracz1_text_surface, gracz1_text_rect)
    screen.blit(gracz2_text_surface, gracz2_text_rect)
    
    

    pygame.display.update()
pygame.quit()
