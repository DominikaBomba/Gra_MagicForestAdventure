import pygame
import sys
import random
import time

BLACK = (0, 0, 0)

pygame.init()
pygame.display.set_caption("Game Over")

scr_width = 1280
scr_height = 720

screen = pygame.display.set_mode((scr_width, scr_height))
ramka = pygame.image.load("Grafika/ramka2.png")
tekst = pygame.image.load("Grafika/tekst1.png")
gameover = pygame.image.load("Grafika/gameover.png")



def main(score1, score2, clock2, gracz1_name, gracz2_name):

    plik = open("test.txt", "a")
    zawartosc = ["Czas gry: ", str(clock2), "\n", "Gracz 1: ", str(score1), "\n",  "Gracz 2: " , str(score2),  "\n", "---------------------", "\n"]
    plik.writelines(zawartosc)
    plik.close()
    pygame.init()
    run = True
    screen = pygame.display.set_mode((1280, 720))
    while run:
        screen.blit(ramka, (0, 0))
        screen.blit(tekst, (0, -50))
        screen.blit(gameover, (0, -10))
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT: 
                run = False
        if score1 > score2:
            wygrana = pygame.font.Font.render(pygame.font.Font("Inne/Eina01-SemiBold.ttf",45), f"WYGRAŁ/A: {str(gracz1_name)}", True, (100, 227 ,124))
        else:
             wygrana = pygame.font.Font.render(pygame.font.Font("Inne/Eina01-SemiBold.ttf",45), f"WYGRAŁ/A: {str(gracz2_name)}", True, (100, 227 ,124))
             
        podsumowanie_czas = pygame.font.Font.render(pygame.font.Font("Inne/Eina01-SemiBold.ttf",40), f"CZAS GRY: {int(clock2)}", True, (49, 54 ,48))
        podsumowanie = pygame.font.Font.render(pygame.font.Font("Inne/Eina01-SemiBold.ttf",40), f"WYNIK GRACZA 1: {int(score1)}", True, (49, 54 ,48))
        podsumowanie1 = pygame.font.Font.render(pygame.font.Font("Inne/Eina01-SemiBold.ttf",40), f"WYNIK GRACZA 2:{int(score2)}", True, (49, 54 ,48))
        screen.blit(wygrana, (410,330))
        screen.blit(podsumowanie, (420,380))
        screen.blit(podsumowanie1, (425,430))
        screen.blit(podsumowanie_czas, (465,480))
        pygame.display.flip()
    
    pygame.quit()
if __name__ == "__main__":
    main()
