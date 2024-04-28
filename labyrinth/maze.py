from pygame  import *

window =  display.set_mode ((700, 500))
display.set_caption('Maze')
background = transform.scale(image.load('background.jpg'), (700, 500))

mixer.init()
mixer.music.load('jungles.ogg')
mixer.music.set_volume(0.6)
mixer.music.play()

font.init()
font = font.Font(None, 70)
win = font.render('YOU WIN!', True, (255, 215, 0))
lose = font.render('YOU LOSE!', True, (180, 0, 0))

class Gamesprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, speed):
        self.image = transform.scale(image.load(player_image), (50, 50))
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x =  player_x
        self.rect.y = player_y
    def draw(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Hero(Gamesprite):
    def movement(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 0:
            self.rect.x -=  self.speed
        if keys[K_RIGHT] and self.rect.x < 635:
            self.rect.x +=  self.speed
        if keys[K_UP] and self.rect.y > 0:
            self.rect.y -=  self.speed
        if keys[K_DOWN] and self.rect.y < 435:
            self.rect.y +=  self.speed

class Cyborg1(Gamesprite):
    def movement(self):
        self.rect.x += self.speed
        if self.rect.x > 700 or self.rect.x < 400:
            self.speed = self.speed * (-1)

class Cyborg2(Gamesprite):
    def movement(self):
        self.rect.x += self.speed
        if self.rect.x < 1 or self.rect.x > 400:
            self.speed = self.speed * (-1)
        


class Wall(sprite.Sprite):
    def __init__(self, r, g, b, wall_x, wall_y, wall_width, wall_height):
        self.image = Surface((wall_width, wall_height))
        self.image.fill((r, g, b))
        self.rect = self.image.get_rect()
        self.rect.x = wall_x
        self.rect.y = wall_y
    def draw(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

hero = Hero('hero.png', 10, 420, 5)
cyborg1 = Cyborg1('cyborg.png', 620, 300, 5)
cyborg2 = Cyborg2('cyborg.png', 10, 90, 5)
treasure = Gamesprite('treasure.png', 570, 420, 0)

wall1 = Wall(154, 205, 50, 100, 20, 460, 10)
wall2 = Wall(154, 205, 50, 100, 20, 10, 370)
wall3 = Wall(154, 205, 50, 100, 480, 450, 10)
wall4 = Wall(154, 205, 50, 550, 110, 10, 380)
wall5 = Wall(154, 205, 50, 210, 110, 340, 10)
wall6 = Wall(154, 205, 50, 100, 380, 340, 10)
wall7 = Wall(154, 205, 50, 210, 110, 10, 200)
wall8 = Wall(154, 205, 50, 440, 190, 10, 200)
wall9 = Wall(154, 205, 50, 320, 190, 100, 10)

clock = time.Clock()
FPS = 60
game= True
finish = False
while game:
    window.blit(background, (0, 0))
    for e in event.get():
        if e.type == QUIT:
            game = False   
    hero.draw()
    cyborg1.draw()
    cyborg2.draw()
    treasure.draw()
    wall1.draw()
    wall2.draw()
    wall3.draw()
    wall4.draw()
    wall5.draw()
    wall6.draw()
    wall7.draw()
    wall8.draw()
    wall9.draw()
    
    if finish == False:
        cyborg2.movement()
        cyborg1.movement()
        hero.movement()
    
    if sprite.collide_rect(hero, cyborg1) or sprite.collide_rect(hero, cyborg2) or  sprite.collide_rect(hero, wall1) or sprite.collide_rect(hero, wall2) or sprite.collide_rect(hero, wall3) or sprite.collide_rect(hero, wall4) or sprite.collide_rect(hero, wall5) or sprite.collide_rect(hero, wall6) or sprite.collide_rect(hero, wall7) or sprite.collide_rect(hero, wall8) or sprite.collide_rect(hero, wall9):
        finish = True
        window.blit(lose, (300, 200))

    if sprite.collide_rect(hero, treasure):
        finish = True
        window.blit(win, (300, 200))
        
    clock.tick(FPS)
    display.update()