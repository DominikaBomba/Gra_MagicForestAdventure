import pygame
import sys
import random
import time
import game_over
pygame.init()

WIDTH = 1280
HEIGHT = 720
BACKGROUND = pygame.transform.scale(pygame.image.load("Grafika/propozycja4.png"), (1280, 720))

class Sprite(pygame.sprite.Sprite):
    def __init__(self, image, startx, starty):
        super().__init__()

        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()

        self.rect.center = [startx, starty]

    def update(self):
        pass

    def draw(self, screen):
        screen.blit(self.image, self.rect)
# gracz 1 - duszek - klasa
class Player(Sprite):
    def __init__(self, startx, starty):
        super().__init__("Grafika/gracz1_lewo.png", startx, starty)
        self.image =  pygame.image.load("Grafika/gracz1_lewo.png")
        self.min_jumpspeed = 3
        self.prev_key = pygame.key.get_pressed()
        self.speed = 5
        self.jumpspeed = 15
        self.standing_image = self.image
        self.predkosc_pion = 0 
        self.gravity = 1
        
    def update(self, platformy, podloga, nietoperz1_kolizja_true):
        predkosc_poziom = 0
        onground = pygame.sprite.spritecollideany(self, platformy)
        onpodloga = pygame.sprite.spritecollideany(self, podloga)
        key = pygame.key.get_pressed()
        if nietoperz1_kolizja_true == True:
            self.speed = 10
            self.jumpspeed = 20
        if key[pygame.K_a]:
            predkosc_poziom = -self.speed
            self.image =  pygame.image.load("Grafika/gracz1_lewo.png")
        elif key[pygame.K_d]:
            predkosc_poziom = self.speed
            self.image = pygame.image.load("Grafika/gracz1_prawo.png")
        if key[pygame.K_w] and (onground or onpodloga):
            self.predkosc_pion = -self.jumpspeed
            self.image = pygame.image.load("Grafika/gracz1_skok.png")
        if self.prev_key[pygame.K_w] and not key[pygame.K_w]:
            self.image = pygame.image.load("Grafika/gracz1_skok.png")
            if self.predkosc_pion < -self.min_jumpspeed:
                self.predkosc_pion = -self.min_jumpspeed
                
        self.prev_key = key
        
        if self.predkosc_pion < 20:
            self.predkosc_pion += self.gravity
            
        if self.predkosc_pion > 0 and (onground or onpodloga):
            self.predkosc_pion = 0
            
        self.move(predkosc_poziom, self.predkosc_pion)
    def move(self, x, y):
        self.rect.move_ip([x,y])
        self.rect.x = max(10, min(self.rect.x, 600))
        self.rect.y = max(0, min(self.rect.y, 720))
# gracz 2 - duszek - klasa
class Player2(Sprite):
    def __init__(self, startx, starty):
        super().__init__("Grafika/gracz1_lewo.png", startx, starty)
        self.min_jumpspeed = 3
        self.prev_key = pygame.key.get_pressed()
        self.speed = 5
        self.jumpspeed = 15
        self.standing_image = self.image
        self.predkosc_pion = 0 
        self.gravity = 1
    def update(self, platformy, podloga, nietoperz2_kolizja_true):
        predkosc_poziom = 0
        onground = pygame.sprite.spritecollideany(self, platformy)
        onpodloga = pygame.sprite.spritecollideany(self, podloga)
        key = pygame.key.get_pressed()
        if nietoperz2_kolizja_true == True:
            self.speed = 10
            self.jumpspeed = 20
        if key[pygame.K_LEFT]:
            predkosc_poziom = -self.speed
            self.image =  pygame.image.load("Grafika/gracz1_lewo.png")
        elif key[pygame.K_RIGHT]:
            predkosc_poziom = self.speed
            self.image =  pygame.image.load("Grafika/gracz1_prawo.png")
        if key[pygame.K_UP] and (onground or onpodloga):
            self.predkosc_pion = -self.jumpspeed
            self.image =  pygame.image.load("Grafika/gracz1_skok.png")
        if self.prev_key[pygame.K_UP] and not key[pygame.K_UP]:
            self.image =  pygame.image.load("Grafika/gracz1_skok.png")
            if self.predkosc_pion < -self.min_jumpspeed:
                self.predkosc_pion = -self.min_jumpspeed
                
        self.prev_key = key
        
        if self.predkosc_pion < 20:
            self.predkosc_pion += self.gravity
            
        if self.predkosc_pion > 0 and (onground or onpodloga):
            self.predkosc_pion = 0
            
        self.move(predkosc_poziom, self.predkosc_pion)
        
    def move(self, x, y):
        self.rect.move_ip([x,y])
        self.rect.x = max(650, min(self.rect.x, 1270))
        self.rect.y = max(0, min(self.rect.y, 720))

#Nietoperz gracz1
class Nietoperz1(Sprite):
    def __init__(self, startx, starty):
        super().__init__("Grafika/nietoperz1.png", startx, starty)
        self.speed = 4
    def update(self):
        self.rect.move_ip([self.speed, 0])
        if self.rect.left < 10:
            self.speed = -self.speed
            self.image = pygame.transform.flip(self.image, True, False)
        if self.rect.right > 630:
            self.speed = -self.speed
            self.image = pygame.transform.flip(self.image, True, False)

#Nietoperz gracz 2
class Nietoperz2(Sprite):
    def __init__(self, startx, starty):
        super().__init__("Grafika/nietoperz1.png", startx, starty)
        self.speed = 4
    def update(self):
        self.rect.move_ip([self.speed, 0])
        if self.rect.left < 650:
            self.image = pygame.transform.flip(self.image, True, False)
            self.speed = -self.speed
        if self.rect.right > 1270:
            self.image = pygame.transform.flip(self.image, True, False)
            self.speed = -self.speed
    
#Platforma - gracz 1 
class Platforma(Sprite):
    def __init__(self, startx, starty, speed):
        super().__init__("Grafika/trawka3.png", startx, starty)
        self.speed = speed
    def update(self):
        self.image =  pygame.image.load("Grafika/trawka3.png")
        self.rect.move_ip([self.speed, 0])
        if self.rect.left < 10:
            self.speed = -self.speed
        if self.rect.right > 630:
            self.speed = - self.speed
# Platforma - gracz 2
class Platforma2(Sprite):
    def __init__(self, startx, starty, speed):
        super().__init__("Grafika/trawka3.png", startx, starty)
        self.speed = speed
    def update(self):
        self.image =  pygame.image.load("Grafika/trawka3.png")
        self.rect.move_ip([self.speed, 0])
        if self.rect.left < 650:
            self.speed = -self.speed
        if self.rect.right > 1270:
            self.speed = -self.speed
            
#Nagrody
class Nagroda(Sprite):
    def __init__(self, startx, starty):
        super().__init__("Grafika/nagroda.png", startx, starty)

#drzwi
class Drzwi(Sprite):
    def __init__(self, startx, starty):
        super().__init__("Grafika/drzwi2.png", startx, starty)

    def handle_collision(self, gracz, score1,score2, clock2, gracz1_name, gracz2_name):
        if self.rect.colliderect(gracz.rect):
            self.image= pygame.image.load("Grafika/drzwi2.png")
        else:
            self.image= pygame.image.load("Grafika/dzrwi1.png")
            
        if self.rect.colliderect(gracz.rect) and (score1 >= 1 or score2 >= 11):
            game_over.main(score1, score2, clock2, gracz1_name, gracz2_name)

#podloga 
class Podloga(Sprite):
    def __init__(self, startx, starty):
        super().__init__("Grafika/podloga.png", startx, starty)
#paltforma koniec
class Platfroma_koniec(Sprite):
    def __init__(self, startx, starty):
        super().__init__("Grafika/trawka5.png", startx, starty)
def main(gracz1_name, gracz2_name):
    nietoperz_true = True
    nietoperz1_kolizja_true = False
    nietoperz2_kolizja_true = False
    koniec = False
    pygame.init()
    run = True
    score1 = 0
    score2 = 0
    ilosc_nagrod1 = 0
    ilosc_nagrod2 = 0
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock_gracz1 = 1
    clock_gracz2 = 1
    clock2 = 0
    gracz1 = Player(540, 600)
    gracz2 = Player2(1000, 600)
    drzwi1 = Drzwi(50, 60)
    drzwi2 = Drzwi(1230, 60)
    nietoperze = pygame.sprite.Group()
    platformy = pygame.sprite.Group()
    podloga = pygame.sprite.Group()
    nagrody1 = pygame.sprite.Group()
    nagrody2 = pygame.sprite.Group()
    #platformy
    for py in range(140,720, 120):
        x_platformy = random.randint(60,320)
        speed_p = random.randint(-2, 2)
        platformy.add(Platforma(x_platformy, py, speed_p))
        platformy.add(Platforma2(x_platformy + 640, py, speed_p))
        
    for py in range(180,720, 120):
        x_platformy = random.randint(60,600)
        platformy.add(Platforma(x_platformy, py, 0))
        platformy.add(Platforma2(x_platformy + 640, py, 0))
        
    for py in range(220,720, 120):
        x_platformy = random.randint(320,600)
        speed_p = random.randint(-1, 1)
        platformy.add(Platforma(x_platformy, py, speed_p))
        platformy.add(Platforma2(x_platformy + 640, py, speed_p))

    
    podloga.add(Podloga(640,720))
    podloga.add(Platfroma_koniec(60, 100))
    podloga.add(Platfroma_koniec(1210, 100))
    while run:

        pygame.event.pump()
        clock_gracz1 += pygame.time.Clock().tick(60)/1000
        clock_gracz2 += pygame.time.Clock().tick(60)/1000
        clock2 += pygame.time.Clock().tick(60)/333
        czas_wys = pygame.font.Font.render(pygame.font.Font("Inne/czcionka.ttf",48), f"{int(clock2)}", True, (255,255 ,255))
        score1_wys = pygame.font.Font.render(pygame.font.Font("Inne/czcionka.ttf",20), f"{str(gracz1_name)}", True, (255,255 ,255))
        gracz1_wys = pygame.font.Font.render(pygame.font.Font("Inne/czcionka.ttf",20), f"{int(score1)}", True, (255,255 ,255))
        score2_wys = pygame.font.Font.render(pygame.font.Font("Inne/czcionka.ttf",20), f" {str(gracz2_name)}", True, (255,255 ,255))
        gracz2_wys = pygame.font.Font.render(pygame.font.Font("Inne/czcionka.ttf",20), f"{int(score2)}", True, (255,255 ,255))

        nagrody1_hit_list = pygame.sprite.spritecollide(gracz1, nagrody1, True)
        nagrody2_hit_list = pygame.sprite.spritecollide(gracz2, nagrody2, True)
        if nagrody1_hit_list:
            score1 += 1
            ilosc_nagrod1 -= 1
            print(ilosc_nagrod1)
        if nagrody2_hit_list:
            score2 += 1
            ilosc_nagrod2 -= 1
                
        if clock_gracz1 >= 1 and ilosc_nagrod1 < 4:
            clock_gracz1 = 0
            ilosc_nagrod1 += 1
            x_nagrody = random.randint(30,610)
            y_nagrody = random.randint(100,650)
            nagrody1.add(Nagroda(x_nagrody, y_nagrody))
        if clock_gracz2 >= 1 and ilosc_nagrod2 < 4:
            clock_gracz2 = 0
            ilosc_nagrod2 += 1
            x_nagrody = random.randint(660,1260)
            y_nagrody = random.randint(100,720)
            nagrody2.add(Nagroda(x_nagrody, y_nagrody))

        pygame.time.Clock().tick(60)
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT: 
                run = False
        #nietoperz
                
        czas_nietoperz = random.randint(2, 8)
        if clock2 >= czas_nietoperz and nietoperz_true == True:
            wysokosc = random.randint(100, 600)
            nietoperze.add(Nietoperz1(200, wysokosc))
            wysokosc = random.randint(100, 900)
            nietoperze.add(Nietoperz2(800, wysokosc))
            nietoperz_true = False
        nietoperz1_kolizja = pygame.sprite.spritecollide(gracz1, nietoperze, True)
        nietoperz2_kolizja = pygame.sprite.spritecollide(gracz2, nietoperze, True)
        if nietoperz1_kolizja:
            nietoperz1_kolizja_true = True
        if nietoperz2_kolizja:
            nietoperz2_kolizja_true = True
        
        drzwi1.handle_collision(gracz1, score1, score2, clock2, gracz1_name, gracz2_name)
        drzwi2.handle_collision(gracz2, score1, score2, clock2, gracz1_name, gracz2_name)
        
        platformy.update()

        
        gracz1.update(platformy, podloga, nietoperz1_kolizja_true)
        gracz2.update(platformy, podloga, nietoperz2_kolizja_true)
        nietoperze.update()
        screen.blit(BACKGROUND,(0,0))
        

        podloga.draw(screen)
        platformy.draw(screen)
        drzwi1.draw(screen)
        drzwi2.draw(screen)
        nietoperze.draw(screen)
        nagrody1.draw(screen)
        nagrody2.draw(screen)
        gracz1.draw(screen)
        gracz2.draw(screen)
        screen.blit(czas_wys,(620,20))
        screen.blit(score1_wys,(300,20))
        screen.blit(gracz1_wys,(320,50))
        screen.blit(score2_wys,(900,20))
        screen.blit(gracz2_wys,(920,50))
        pygame.display.flip()
    pygame.quit()


if __name__ == "__main__":
    main()
