from pygame import *
from time import sleep

font.init()
mixer.init()

window = display.set_mode((900,500))
bg = transform.scale(image.load('Magic.jpeg'), (900,500))
FPS = 60
clock = time.Clock()
display.set_caption('Magic maze')

finish = False
collide_button = False

level = 1
door_open = 0
door = 0
get_key = 0
final_seconds = 60
seconds_of_final_text = 0
final_time = 0
tryvoha_seconds = 31
sound_tryvoha = 0
close_1 = 0
close_2 = 0
close_3 = 0
close_4 = 0

font_text = font.Font(None, 40)
number_lvl = font_text.render(f'{level}', True, (255, 215, 0))
font_level = font_text.render('Рівень:', True, (255, 215, 0))
number_final_seconds_yellow = font_text.render(f'{final_seconds}', True, (255, 215, 0))
number_final_seconds_red = font_text.render(f'{final_seconds}', True, (255, 215, 0))
font_control = font_text.render('Управління', True, (255, 215, 0))

font = font.Font(None, 120)
win = font.render('You Win!', True, (255, 215, 0))
lose = font.render('Game Over!', True, (255, 0, 0))
final_text_1 = font_text.render('Увага!', True, (255, 0, 0))
final_text_2 = font_text.render('Був активований отруйний газ!', True, (255, 0, 0))
final_text_3 = font_text.render('Через 60 секунд газ поширеться по всьому лабіринту!', True, (255, 0, 0))

key_number = font_text.render(f'{door}', True, (255, 215, 0))
font_key = font_text.render('Ключ:', True, (255, 215, 0))

mixer.music.load('magic_music.mp3')
mixer.music.play()

kick = mixer.Sound('kick.mp3')

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, width, height):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (width, height))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
        self.direction = ""

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Wall(sprite.Sprite):
    def __init__(self, color_r, color_g, color_b, wall_x, wall_y, wall_width, wall_height):
        super().__init__()
        self.color_r = color_r
        self.color_g = color_g
        self.color_b = color_b
        self.width = wall_width
        self.height = wall_height
        self.image = Surface((self.width, self.height))
        self.image.fill((color_r, color_g, color_b))
        self.rect = self.image.get_rect()
        self.rect.x = wall_x
        self.rect.y = wall_y

    def draw_wall(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update(self):
        keys_pressed = key.get_pressed()

        if keys_pressed[K_LEFT] or keys_pressed[K_a] and self.rect.x > 5:
            self.rect.x -= self.speed

        if keys_pressed[K_RIGHT] or keys_pressed[K_d] and self.rect.x < 895:
            self.rect.x += self.speed

        if keys_pressed[K_DOWN] or keys_pressed[K_s] and self.rect.y > 5:
            self.rect.y += self.speed

        if keys_pressed[K_UP] or keys_pressed[K_w] and self.rect.y < 495:
            self.rect.y -= self.speed

    def update_1(self):
        if sprite.collide_rect(player_1, wall_1):
            kick.play()
            self.rect.y = 50
            self.rect.x = 55

        if sprite.collide_rect(player_1, wall_2):
            kick.play()
            self.rect.y = 50
            self.rect.x = 55

        if sprite.collide_rect(player_1, wall_3):
            kick.play()
            self.rect.y = 50
            self.rect.x = 55

        if sprite.collide_rect(player_1, wall_4):
            kick.play()
            self.rect.y = 50
            self.rect.x = 55

        if sprite.collide_rect(player_1, wall_5):
            kick.play()
            self.rect.y = 50
            self.rect.x = 55

        if sprite.collide_rect(player_1, wall_6):
            kick.play()
            self.rect.y = 50
            self.rect.x = 55

        if sprite.collide_rect(player_1, wall_7):
            kick.play()
            self.rect.y = 50
            self.rect.x = 55

        if sprite.collide_rect(player_1, wall_8):
            kick.play()
            self.rect.y = 50
            self.rect.x = 55

        if sprite.collide_rect(player_1, wall_9):
            kick.play()
            self.rect.y = 50
            self.rect.x = 55

        if sprite.collide_rect(player_1, wall_10):
            kick.play()
            self.rect.y = 50
            self.rect.x = 55

        if sprite.collide_rect(player_1, wall_11):
            kick.play()
            self.rect.y = 50
            self.rect.x = 55

        if sprite.collide_rect(player_1, wall_12):
            kick.play()
            self.rect.y = 50
            self.rect.x = 55

        if sprite.collide_rect(player_1, wall_13):
            kick.play()
            self.rect.y = 50
            self.rect.x = 55

    def update_2(self):
        if sprite.collide_rect(player_2, wall_1):
            kick.play()
            self.rect.y = 395
            self.rect.x = 785
        
        if sprite.collide_rect(player_2, wall_2):
            kick.play()
            self.rect.y = 395
            self.rect.x = 785

        if sprite.collide_rect(player_2, wall_3):
            kick.play()
            self.rect.y = 395
            self.rect.x = 785

        if sprite.collide_rect(player_2, wall_4):
            kick.play()
            self.rect.y = 395
            self.rect.x = 785

        if sprite.collide_rect(player_2, wall_14):
            kick.play()
            self.rect.y = 395
            self.rect.x = 785

        if sprite.collide_rect(player_2, wall_15):
            kick.play()
            self.rect.y = 395
            self.rect.x = 785

        if sprite.collide_rect(player_2, wall_16):
            kick.play()
            self.rect.y = 395
            self.rect.x = 785

        if sprite.collide_rect(player_2, wall_17):
            kick.play()
            self.rect.y = 395
            self.rect.x = 785
        
        if sprite.collide_rect(player_2, wall_18):
            kick.play()
            self.rect.y = 395
            self.rect.x = 785

        if sprite.collide_rect(player_2, wall_19):
            kick.play()
            self.rect.y = 395
            self.rect.x = 785

        if sprite.collide_rect(player_2, wall_20):
            kick.play()
            self.rect.y = 395
            self.rect.x = 785

        if sprite.collide_rect(player_2, wall_21):
            kick.play()
            self.rect.y = 395
            self.rect.x = 785

        if sprite.collide_rect(player_2, wall_22):
            kick.play()
            self.rect.y = 395
            self.rect.x = 785

        if sprite.collide_rect(player_2, wall_23):
            kick.play()
            self.rect.y = 395
            self.rect.x = 785

        if sprite.collide_rect(player_2, wall_24):
            kick.play()
            self.rect.y = 395
            self.rect.x = 785

        if sprite.collide_rect(player_2, wall_25):
            kick.play()
            self.rect.y = 395
            self.rect.x = 785

        if sprite.collide_rect(player_2, wall_26):
            kick.play()
            self.rect.y = 395
            self.rect.x = 785

        if sprite.collide_rect(player_2, wall_27):
            kick.play()
            self.rect.y = 395
            self.rect.x = 785

    def update_3(self):
        if sprite.collide_rect(player_3, wall_28):
            kick.play()
            self.rect.y = 45
            self.rect.x = 805
        
        if sprite.collide_rect(player_3, wall_29):
            kick.play()
            self.rect.y = 45
            self.rect.x = 805

        if sprite.collide_rect(player_3, wall_30):
            kick.play()
            self.rect.y = 45
            self.rect.x = 805

        if sprite.collide_rect(player_3, wall_31):
            kick.play()
            self.rect.y = 45
            self.rect.x = 805

        if sprite.collide_rect(player_3, wall_32):
            kick.play()
            self.rect.y = 45
            self.rect.x = 805

        if sprite.collide_rect(player_3, wall_33):
            kick.play()
            self.rect.y = 45
            self.rect.x = 805

        if sprite.collide_rect(player_3, wall_34):
            kick.play()
            self.rect.y = 45
            self.rect.x = 805

        if sprite.collide_rect(player_3, wall_35):
            kick.play()
            self.rect.y = 45
            self.rect.x = 805

        if sprite.collide_rect(player_3, wall_36):
            kick.play()
            self.rect.y = 45
            self.rect.x = 805
        
        if sprite.collide_rect(player_3, wall_37):
            kick.play()
            self.rect.y = 45
            self.rect.x = 805

        if sprite.collide_rect(player_3, wall_38):
            kick.play()
            self.rect.y = 45
            self.rect.x = 805

        if sprite.collide_rect(player_3, wall_39):
            kick.play()
            self.rect.y = 45
            self.rect.x = 805

        if sprite.collide_rect(player_3, wall_40):
            kick.play()
            self.rect.y = 45
            self.rect.x = 805

        if sprite.collide_rect(player_3, wall_41):
            kick.play()
            self.rect.y = 45
            self.rect.x = 805

        if sprite.collide_rect(player_3, wall_42):
            kick.play()
            self.rect.y = 45
            self.rect.x = 805

        if sprite.collide_rect(player_3, wall_1):
            kick.play()
            self.rect.y = 45
            self.rect.x = 805

        if sprite.collide_rect(player_3, wall_2):
            kick.play()
            self.rect.y = 45
            self.rect.x = 805

        if sprite.collide_rect(player_3, wall_3):
            kick.play()
            self.rect.y = 45
            self.rect.x = 805

        if sprite.collide_rect(player_3, wall_4):
            kick.play()
            self.rect.y = 45
            self.rect.x = 805

        if sprite.collide_rect(player_3, portal_1):
            self.rect.x = 65
            self.rect.y = 130

        if sprite.collide_rect(player_3, portal_2):
            self.rect.x = 600
            self.rect.y = 405

    def update_4(self):
        if sprite.collide_rect(player_4, wall_43):
            kick.play()
            self.rect.y = 50
            self.rect.x = 50

        if sprite.collide_rect(player_4, wall_44):
            kick.play()
            self.rect.y = 50
            self.rect.x = 50

        if sprite.collide_rect(player_4, wall_45):
            kick.play()
            self.rect.y = 50
            self.rect.x = 50

        if sprite.collide_rect(player_4, wall_46):
            kick.play()
            self.rect.y = 50
            self.rect.x = 50

        if sprite.collide_rect(player_4, wall_47):
            kick.play()
            self.rect.y = 50
            self.rect.x = 50

        if sprite.collide_rect(player_4, wall_48):
            kick.play()
            self.rect.y = 50
            self.rect.x = 50

        if sprite.collide_rect(player_4, wall_49):
            kick.play()
            self.rect.y = 50
            self.rect.x = 50

        if sprite.collide_rect(player_4, wall_50):
            kick.play()
            self.rect.y = 50
            self.rect.x = 50

        if sprite.collide_rect(player_4, wall_51):
            kick.play()
            self.rect.y = 50
            self.rect.x = 50

        if sprite.collide_rect(player_4, wall_52):
            kick.play()
            self.rect.y = 50
            self.rect.x = 50

        if sprite.collide_rect(player_4, wall_1):
            kick.play()
            self.rect.y = 50
            self.rect.x = 50

        if sprite.collide_rect(player_4, wall_2):
            kick.play()
            self.rect.y = 50
            self.rect.x = 50

        if sprite.collide_rect(player_4, wall_3):
            kick.play()
            self.rect.y = 50
            self.rect.x = 50

        if sprite.collide_rect(player_4, wall_4):
            kick.play()
            self.rect.y = 50
            self.rect.x = 50

        if sprite.collide_rect(player_4, portal_3):
            self.rect.x = 830
            self.rect.y = 280

        if sprite.collide_rect(player_4, portal_4):
            self.rect.x = 450
            self.rect.y = 50

        if door == 0 and sprite.collide_rect(player_4, door_2) and door_open == 0:
            self.rect.y -= 4
        
        if door == 0 and sprite.collide_rect(player_4, door_1) and door_open == 1:
            self.rect.x -= 4

    def update_5(self):
        if sprite.collide_rect(player_5, wall_1):
            kick.play()
            self.rect.y = 430
            self.rect.x = 440

        if sprite.collide_rect(player_5, wall_2):
            kick.play()
            self.rect.y = 430
            self.rect.x = 440

        if sprite.collide_rect(player_5, wall_3):
            kick.play()
            self.rect.y = 430
            self.rect.x = 440

        if sprite.collide_rect(player_5, wall_4):
            kick.play()
            self.rect.y = 430
            self.rect.x = 440

        if sprite.collide_rect(player_5, wall_53):
            kick.play()
            self.rect.y = 430
            self.rect.x = 440

        if sprite.collide_rect(player_5, wall_54):
            kick.play()
            self.rect.y = 430
            self.rect.x = 440

        if sprite.collide_rect(player_5, wall_55):
            kick.play()
            self.rect.y = 430
            self.rect.x = 440

        if sprite.collide_rect(player_5, wall_56):
            kick.play()
            self.rect.y = 430
            self.rect.x = 440
        
        if sprite.collide_rect(player_5, wall_57):
            kick.play()
            self.rect.y = 430
            self.rect.x = 440

        if sprite.collide_rect(player_5, wall_58):
            kick.play()
            self.rect.y = 430
            self.rect.x = 440

        if sprite.collide_rect(player_5, wall_59):
            kick.play()
            self.rect.y = 430
            self.rect.x = 440

        if sprite.collide_rect(player_5, wall_60):
            kick.play()
            self.rect.y = 430
            self.rect.x = 440

        if sprite.collide_rect(player_5, wall_61):
            kick.play()
            self.rect.y = 430
            self.rect.x = 440

        if sprite.collide_rect(player_5, wall_62):
            kick.play()
            self.rect.y = 430
            self.rect.x = 440

        if sprite.collide_rect(player_5, wall_63):
            kick.play()
            self.rect.y = 430
            self.rect.x = 440

        if sprite.collide_rect(player_5, wall_64):
            kick.play()
            self.rect.y = 430
            self.rect.x = 440

        if sprite.collide_rect(player_5, wall_65):
            kick.play()
            self.rect.y = 430
            self.rect.x = 440

        if sprite.collide_rect(player_5, wall_66):
            kick.play()
            self.rect.y = 430
            self.rect.x = 440

        if sprite.collide_rect(player_5, wall_67):
            kick.play()
            self.rect.y = 430
            self.rect.x = 440

        if sprite.collide_rect(player_5, wall_68):
            kick.play()
            self.rect.y = 430
            self.rect.x = 440

        if sprite.collide_rect(player_5, wall_69):
            kick.play()
            self.rect.y = 430
            self.rect.x = 440

        if sprite.collide_rect(player_5, wall_70):
            kick.play()
            self.rect.y = 430
            self.rect.x = 440

        if sprite.collide_rect(player_5, wall_71):
            kick.play()
            self.rect.y = 430
            self.rect.x = 440

        if sprite.collide_rect(player_5, wall_72):
            kick.play()
            self.rect.y = 430
            self.rect.x = 440

        if sprite.collide_rect(player_5, wall_73):
            kick.play()
            self.rect.y = 430
            self.rect.x = 440

        if sprite.collide_rect(player_5, wall_74):
            kick.play()
            self.rect.y = 430
            self.rect.x = 440

        if sprite.collide_rect(player_5, portal_5):
            self.rect.x = 840
            self.rect.y = 300

        if sprite.collide_rect(player_5, portal_6):
            self.rect.x = 95
            self.rect.y = 32

        if sprite.collide_rect(player_5, portal_7):
            self.rect.x = 600
            self.rect.y = 210

        if sprite.collide_rect(player_5, portal_8):
            self.rect.x = 840
            self.rect.y = 90

        if sprite.collide_rect(player_5, portal_9):
            self.rect.x = 275
            self.rect.y = 280

        if sprite.collide_rect(player_5, portal_10):
            self.rect.x = 620
            self.rect.y = 280

        if door == 0 and sprite.collide_rect(player_5, door_3) and door_open == 4:
            self.rect.y += 4
        
        if door == 0 and sprite.collide_rect(player_5, door_4) and door_open == 3:
            self.rect.y += 4

        if door == 0 and sprite.collide_rect(player_5, door_5) and door_open == 2:
            self.rect.y += 4

class Enemy(GameSprite):
    def update_1(self):
        if self.rect.x <= 200:
            self.direction = "right"

        if self.rect.x >= 800:
            self.direction = "left"
        
        if self.direction == 'left':
            self.rect.x -= self.speed

        else:
            self.rect.x += self.speed

    def update_2_1(self):
        if self.rect.x <= 160:
            self.direction = "right"

        if self.rect.x >= 700:
            self.direction = "left"
        
        if self.direction == 'left':
            self.rect.x -= self.speed

        else:
            self.rect.x += self.speed

    def update_2_2(self):
        if self.rect.y <= 150:
            self.direction = "down"

        if self.rect.y >= 400:
            self.direction = "up"
    
        if self.direction == "down":
            self.rect.y += self.speed

        else:
            self.rect.y -= self.speed

    def update_3_1(self):
        if self.rect.y <= 40:
            self.direction = "down"

        if self.rect.y >= 200:
            self.direction = "up"
    
        if self.direction == "down":
            self.rect.y += self.speed

        else:
            self.rect.y -= self.speed

    def update_3_2(self):
        if self.rect.y <= 50:
            self.direction = "up"

        if self.rect.y >= 200:
            self.direction = "down"
    
        if self.direction == "up":
            self.rect.y += self.speed

        else:
            self.rect.y -= self.speed

    def update_4_1(self):
        if self.rect.x <= 150:
            self.direction = "right"

        if self.rect.x >= 820:
            self.direction = "left"
    
        if self.direction == "right":
            self.rect.x += self.speed

        else:
            self.rect.x -= self.speed

    def update_4_2(self):
        if self.rect.y >= 430:
            self.direction = "up"

        if self.rect.y <= 190:
            self.direction = "down"
    
        if self.direction == "up":
            self.rect.y -= self.speed

        else:
            self.rect.y += self.speed

    def update_5_1(self):
        if self.rect.x <= 140:
            self.direction = "right"

        if self.rect.x >= 320:
            self.direction = "left"
    
        if self.direction == "right":
            self.rect.x += self.speed

        else:
            self.rect.x -= self.speed

    def update_5_2(self):
        if self.rect.y >= 430:
            self.direction = "up"

        if self.rect.y <= 100:
            self.direction = "down"
    
        if self.direction == "up":
            self.rect.y -= self.speed

        else:
            self.rect.y += self.speed

arrows_control = GameSprite('arrows_control.png', 620, 250, 1, 100, 70)
wasd_control = GameSprite('wasd_control.png', 470, 228, 1, 130, 110)

player_1 = Player('hero.png', 55, 50, 4, 40, 70)
player_2 = Player('hero.png', 785, 395, 4, 40, 70)
player_3 = Player('hero.png', 805, 45, 4, 35, 60)
player_4 = Player('hero.png', 50, 50, 4, 25, 50)
player_5 = Player('hero.png', 440, 430, 3, 20, 35)

enemy_1 = Enemy('goblin.png', 800, 50, 3, 50, 50)
enemy_2_1 = Enemy('goblin.png', 600, 47.5, 4, 50, 50)
enemy_2_2 = Enemy('goblin.png', 575, 300, 3, 50, 50)
enemy_3_1 = Enemy('goblin.png', 390, 120, 2.5, 45, 45)
enemy_3_2 = Enemy('goblin.png', 605, 40, 2.5, 45, 45)
enemy_4_1 = Enemy('goblin.png', 850, 415, 2, 40, 40)
enemy_4_2 = Enemy('goblin.png', 50, 415, 2, 40, 40)
enemy_5_1 = Enemy('goblin.png', 140, 210, 2, 35, 35)
enemy_5_2 = Enemy('goblin.png', 47.5, 430, 3, 35, 35)

portal_main_1 = GameSprite('portal_main.png', 27.5, 270, 1, 110, 110)
portal_main_2 = GameSprite('portal_main.png', 25, 20, 1, 110, 110)
portal_main_3 = GameSprite('portal_main.png', 250, 272.5, 1, 100, 100)
portal_main_4 = GameSprite('portal_main.png', 125, 197, 1, 100, 100)

portal_1 = GameSprite('portal_1.png', 500, 400, 1, 55, 55)
portal_2 = GameSprite('portal_1.png', 47, 45, 1, 55, 55)
portal_3 = GameSprite('portal_1.png', 370, 40, 1, 50, 50)
portal_4 = GameSprite('portal_1.png', 800, 215, 1, 50, 50)
portal_5 = GameSprite('portal_1.png', 40, 31, 1, 45, 45)
portal_6 = GameSprite('portal_1.png', 807.5, 340, 1, 45, 45)
portal_7 = GameSprite('portal_2.png', 807.5, 35, 1, 45, 45)
portal_8 = GameSprite('portal_2.png', 547.5, 187.5, 1, 45, 45)
portal_9 = GameSprite('portal_3.png', 647.5, 273, 1, 45, 45)
portal_10 = GameSprite('portal_3.png', 225, 272.5, 1, 45, 45)

door_1 = GameSprite('door.png', 180, 305, 1, 70, 70)
door_2 = GameSprite('door.png', 30, 100, 1, 80, 80)
door_3 = GameSprite('door.png', 410, 250, 1, 80, 50)
door_4 = GameSprite('door.png', 410, 305, 1, 80, 50)
door_5 = GameSprite('door.png', 410, 360, 1, 80, 50)

key_1 = GameSprite('key.png', 25, 370, 1, 110, 110)
key_2 = GameSprite('key.png', 235, 370, 1, 110, 110)
key_3 = GameSprite('key.png', 125, 320, 1, 90, 85)
key_4 = GameSprite('key.png', 795, 85, 1, 90, 85)
key_5 = GameSprite('key.png', 505, 245, 1, 90, 85)

exit_1 = GameSprite('exit.png', 25, 150, 1, 40, 60)
exit_2 = GameSprite('exit.png', 500, 30, 1, 50, 30)
exit_3 = GameSprite('exit.png', 835, 200, 1, 40, 60)
exit_4 = GameSprite('exit.png', 835, 410, 1, 40, 60)

closed_1 = GameSprite('closed.png', 25, 150, 1, 40, 60)
closed_2 = GameSprite('closed.png', 500, 30, 1, 50, 30)
closed_3 = GameSprite('closed.png', 835, 200, 1, 40, 60)
closed_4 = GameSprite('closed.png', 835, 410, 1, 40, 60)


red_button = GameSprite('red_button.png', 410, 180, 1, 70, 55)

wall_1 = Wall(80, 0, 100, 0, 0, 30, 500)
wall_2 = Wall(80, 0, 100, 0, 0, 900, 30)
wall_3 = Wall(80, 0, 100, 870, 30, 30, 470)
wall_4 = Wall(80, 0, 100, 0, 470, 900, 30)
wall_5 = Wall(80, 0, 100, 150, 120, 160, 30)
wall_6 = Wall(80, 0, 100, 150, 0, 30, 140)
wall_7 = Wall(80, 0, 100, 280, 130, 30, 110)
wall_8 = Wall(80, 0, 100, 0, 250, 140, 30)
wall_9 = Wall(80, 0, 100, 140, 250, 30, 120)
wall_10 = Wall(80, 0, 100, 150, 340, 615, 30)
wall_11 = Wall(80, 0, 100, 420, 120, 30, 250)
wall_12 = Wall(80, 0, 100, 420, 120, 345, 30)
wall_13 = Wall(80, 0, 100, 740, 120, 30, 250)
wall_14 = Wall(80, 0, 100, 770, 355, 100, 25)
wall_15 = Wall(80, 0, 100, 770, 5, 25, 370)
wall_16 = Wall(80, 0, 100, 270, 120, 140, 25)
wall_17 = Wall(80, 0, 100, 645, 120, 25, 350)
wall_18 = Wall(80, 0, 100, 530, 120, 140, 25)
wall_19 = Wall(80, 0, 100, 385, 120, 25, 130)
wall_20 = Wall(80, 0, 100, 385, 235, 150, 25)
wall_21 = Wall(80, 0, 100, 525, 120, 25, 140)
wall_22 = Wall(80, 0, 100, 130, 30, 25, 230)
wall_23 = Wall(80, 0, 100, 130, 235, 140, 25)
wall_24 = Wall(80, 0, 100, 245, 250, 25, 115)
wall_25 = Wall(80, 0, 100, 245, 350, 305, 25)
wall_26 = Wall(80, 0, 100, 25, 350, 105, 25)
wall_27 = Wall(80, 0, 100, 115, 350, 25, 120)
wall_28 = Wall(80, 0, 100, 765, 30, 20, 355)
wall_29 = Wall(80, 0, 100, 465, 365, 300, 20)
wall_30 = Wall(80, 0, 100, 465, 385, 20, 90)
wall_31 = Wall(80, 0, 100, 120, 30, 20, 335)
wall_32 = Wall(80, 0, 100, 120, 365, 250, 20)
wall_33 = Wall(80, 0, 100, 350, 260, 20, 110)
wall_34 = Wall(80, 0, 100, 350, 260, 320, 20)
wall_35 = Wall(80, 0, 100, 669, 150, 100, 20)
wall_36 = Wall(80, 0, 100, 669, 30, 20, 120)
wall_37 = Wall(80, 0, 100, 565, 30, 20, 140)
wall_38 = Wall(80, 0, 100, 350, 120, 20, 140)
wall_39 = Wall(80, 0, 100, 460, 120, 20, 140)
wall_40 = Wall(80, 0, 100, 240, 120, 130, 20)
wall_41 = Wall(80, 0, 100, 240, 260, 115, 20)
wall_42 = Wall(80, 0, 100, 240, 140, 20, 120)
wall_43 = Wall(80, 0, 100, 110, 190, 150, 20)
wall_44 = Wall(80, 0, 100, 230, 100, 20, 110)
wall_45 = Wall(80, 0, 100, 260, 190, 610, 20)
wall_46 = Wall(80, 0, 100, 340, 30, 20, 90)
wall_47 = Wall(80, 0, 100, 355, 100, 435, 20)
wall_48 = Wall(80, 0, 100, 765, 200, 20, 195)
wall_49 = Wall(80, 0, 100, 110, 375, 660, 20)
wall_50 = Wall(80, 0, 100, 110, 100, 20, 185)
wall_51 = Wall(80, 0, 100, 110, 395, 20, 80)
wall_52 = Wall(80, 0, 100, 110, 285, 570, 20)
wall_53 = Wall(80, 0, 100, 240, 250, 170, 20)
wall_54 = Wall(80, 0, 100, 490, 250, 220, 20)
wall_55 = Wall(80, 0, 100, 280, 150, 515, 20)
wall_56 = Wall(80, 0, 100, 360, 150, 20, 120)
wall_57 = Wall(80, 0, 100, 520, 150, 20, 120)
wall_58 = Wall(80, 0, 100, 390, 270, 20, 140)
wall_59 = Wall(80, 0, 100, 490, 270, 20, 140)
wall_60 = Wall(80, 0, 100, 100, 390, 300, 20)
wall_61 = Wall(80, 0, 100, 100, 320, 20, 70)
wall_62 = Wall(80, 0, 100, 100, 320, 230, 20)
wall_63 = Wall(80, 0, 100, 100, 250, 170, 20)
wall_64 = Wall(80, 0, 100, 100, 150, 20, 120)
wall_65 = Wall(80, 0, 100, 30, 77, 680, 20)
wall_66 = Wall(80, 0, 100, 200, 270, 20, 50)
wall_67 = Wall(80, 0, 100, 190, 95, 20, 105)
wall_68 = Wall(80, 0, 100, 280, 170, 20, 30)
wall_69 = Wall(80, 0, 100, 490, 390, 385, 20)
wall_70 = Wall(80, 0, 100, 775, 150, 20, 250)
wall_71 = Wall(80, 0, 100, 100, 320, 230, 20)
wall_72 = Wall(80, 0, 100, 775, 30, 20, 120)
wall_73 = Wall(80, 0, 100, 570, 320, 150, 20)
wall_74 = Wall(80, 0, 100, 700, 250, 20, 70)

start_button = GameSprite('start_button.png', 335, 205, 1, 250, 100)
exit_button = GameSprite('exit_button.png', -22, -10, 1, 200, 100)
music_button = GameSprite('music_btn.png', 790, 15, 1, 100, 100)

music = True
menu = True
game = True

while game:

    if menu == True:
        for e in event.get():
            if e.type == QUIT:
                game = False

            elif e.type == MOUSEBUTTONDOWN:
                if exit_button.rect.collidepoint(e.pos):
                    game = False
                
                if music_button.rect.collidepoint(e.pos):
                    if music == True:
                        mixer.music.pause()
                        music_button = GameSprite('unmusic_btn.png', 780, 5, 1, 120, 120)
                        music = False
                    else:
                        mixer.music.unpause()
                        music_button = GameSprite('music_btn.png', 790, 15, 1, 100, 100)
                        music = True

                if start_button.rect.collidepoint(e.pos):
                    menu = False
        
        window.blit(bg, (0,0))
        start_button.reset()
        exit_button.reset()
        music_button.reset()

    if finish != True and menu == False:
        for e in event.get():
            if e.type == QUIT:
                game = False
                
        if level == 1:
            window.blit(bg, (0,0))

            player_1.reset()
            player_1.update()
            player_1.update_1()

            enemy_1.update_1()
            enemy_1.reset()

            wall_5.draw_wall()
            wall_6.draw_wall()
            wall_7.draw_wall()
            wall_8.draw_wall()
            wall_9.draw_wall()
            wall_10.draw_wall()
            wall_11.draw_wall()
            wall_12.draw_wall()
            wall_13.draw_wall()

            portal_main_1.reset()

            arrows_control.reset()
            wasd_control.reset()

            window.blit(font_control, (520, 180))

            if sprite.collide_rect(player_1, portal_main_1):
                window.blit(bg, (0,0))
                level += 1
                number_lvl = font_text.render(f'{level}', True, (255, 215, 0))

        if level == 2:
            window.blit(bg, (0,0))

            player_2.reset()
            player_2.update()
            player_2.update_2()

            enemy_2_1.update_2_1()
            enemy_2_1.reset()
            enemy_2_2.update_2_2()
            enemy_2_2.reset()

            wall_14.draw_wall()
            wall_15.draw_wall()
            wall_16.draw_wall()
            wall_17.draw_wall()
            wall_18.draw_wall()
            wall_19.draw_wall()
            wall_20.draw_wall()
            wall_21.draw_wall()
            wall_22.draw_wall()
            wall_23.draw_wall()
            wall_24.draw_wall()
            wall_25.draw_wall()
            wall_26.draw_wall()
            wall_27.draw_wall()

            portal_main_2.reset()

            if sprite.collide_rect(player_2, portal_main_2):
                window.blit(bg, (0,0))
                level += 1
                number_lvl = font_text.render(f'{level}', True, (255, 215, 0))

        if level == 3:
            window.blit(bg, (0,0))

            player_3.reset()
            player_3.update()
            player_3.update_3()

            enemy_3_1.update_3_1()
            enemy_3_1.reset()
            enemy_3_2.update_3_2()
            enemy_3_2.reset()

            portal_1.reset()
            portal_2.reset()

            wall_28.draw_wall()
            wall_29.draw_wall()
            wall_30.draw_wall()
            wall_31.draw_wall()
            wall_32.draw_wall()
            wall_33.draw_wall()
            wall_34.draw_wall()
            wall_35.draw_wall()
            wall_36.draw_wall()
            wall_37.draw_wall()
            wall_38.draw_wall()
            wall_39.draw_wall()
            wall_40.draw_wall()
            wall_41.draw_wall()
            wall_42.draw_wall()

            portal_main_3.reset()

            if sprite.collide_rect(player_3, portal_main_3):
                window.blit(bg, (0,0))
                level += 1
                number_lvl = font_text.render(f'{level}', True, (255, 215, 0))

        if level == 4:
            window.blit(bg, (0,0))

            player_4.reset()
            player_4.update()
            player_4.update_4()

            enemy_4_1.update_4_1()
            enemy_4_1.reset()
            enemy_4_2.update_4_2()
            enemy_4_2.reset()

            portal_3.reset()
            portal_4.reset()

            if door_open < 1:
                door_2.reset()

            if door_open < 2:
                door_1.reset()

            if get_key == 0:
                key_2.reset()

            if get_key != 2:
                key_1.reset()

            wall_43.draw_wall()
            wall_44.draw_wall()
            wall_45.draw_wall()
            wall_46.draw_wall()
            wall_47.draw_wall()
            wall_48.draw_wall()
            wall_49.draw_wall()
            wall_50.draw_wall()
            wall_51.draw_wall()
            wall_52.draw_wall()

            portal_main_4.reset()

            if sprite.collide_rect(player_4, portal_main_4):
                window.blit(bg, (0,0))
                level += 1
                number_lvl = font_text.render(f'{level}', True, (255, 215, 0))
        
        if level == 5:
            window.blit(bg, (0,0))

            if seconds_of_final_text == 300 and final_seconds > 0:

                if close_1 == 1:
                    closed_1.reset()
                if close_2 == 1:
                    closed_2.reset()
                if close_3 == 1:
                    closed_3.reset()
                if close_4 == 1:
                    closed_4.reset()

                if close_1 == 0:
                    exit_1.reset()
                if close_2 == 0:
                    exit_2.reset()
                if close_3 == 0:
                    exit_3.reset()
                if close_4 == 0:
                    exit_4.reset()

                final_time += 0.015

                if final_time > 0.9:
                    final_seconds -= 1
                    final_time = 0

                if sprite.collide_rect(player_5, exit_1):
                    close_1 = 1

                if sprite.collide_rect(player_5, exit_2):
                    close_2 = 1

                if sprite.collide_rect(player_5, exit_3):
                    close_3 = 1
                
                if sprite.collide_rect(player_5, exit_4):
                    close_4 = 1

            player_5.reset()
            player_5.update()
            player_5.update_5()

            enemy_5_1.reset()
            enemy_5_2.reset()
            enemy_5_1.update_5_1()
            enemy_5_2.update_5_2()

            portal_5.reset()
            portal_6.reset()
            portal_7.reset()
            portal_8.reset()
            portal_9.reset()
            portal_10.reset()

            if door_open < 5:
                door_3.reset()

            if door_open < 4:
                door_4.reset()

            if door_open < 3:
                door_5.reset()

            if get_key < 5:
                key_3.reset()

            if get_key < 3:
                key_4.reset()

            if get_key < 4:
                key_5.reset()

            wall_53.draw_wall()
            wall_54.draw_wall()
            wall_55.draw_wall()
            wall_56.draw_wall()
            wall_57.draw_wall()
            wall_58.draw_wall()
            wall_59.draw_wall()
            wall_60.draw_wall()
            wall_61.draw_wall()
            wall_62.draw_wall()
            wall_63.draw_wall()
            wall_64.draw_wall()
            wall_65.draw_wall()
            wall_66.draw_wall()
            wall_67.draw_wall()
            wall_68.draw_wall()
            wall_69.draw_wall()
            wall_70.draw_wall()
            wall_71.draw_wall()
            wall_72.draw_wall()
            wall_73.draw_wall()
            wall_74.draw_wall()

        wall_1.draw_wall()
        wall_2.draw_wall()
        wall_3.draw_wall()
        wall_4.draw_wall()

        if final_seconds > 10 and seconds_of_final_text == 300:
            number_final_seconds_yellow = font_text.render(f'{final_seconds}', True, (255, 215, 0))
            window.blit(number_final_seconds_yellow, (430, 5))
        elif final_seconds < 11 and seconds_of_final_text == 300:
            number_final_seconds_red = font_text.render(f'{final_seconds}', True, (255, 0, 0))
            window.blit(number_final_seconds_red, (430, 5))

        if collide_button == False and level == 5:
            red_button.reset()

        elif collide_button == True and seconds_of_final_text < 300:
            window.blit(final_text_1, (390, 110))
            window.blit(final_text_2, (240, 170))
            window.blit(final_text_3, (90, 230))
            seconds_of_final_text += 0.75

        window.blit(font_level, (5,4))
        window.blit(number_lvl, (105,4))
        if level > 3:
            window.blit(font_key, (125,4))
            window.blit(key_number, (215,4))
        clock.tick(FPS)

        if sprite.collide_rect(player_4, key_1) and get_key == 1:
            get_key += 1
            door += 1
            key_number = font_text.render(f'{door}', True, (255, 215, 0))

        if sprite.collide_rect(player_4, key_2) and get_key == 0:
            get_key += 1
            door += 1
            key_number = font_text.render(f'{door}', True, (255, 215, 0))

        if sprite.collide_rect(player_5, key_3) and get_key == 4:
            get_key += 1
            door += 1
            key_number = font_text.render(f'{door}', True, (255, 215, 0))

        if sprite.collide_rect(player_5, key_4) and get_key == 2:
            get_key += 1
            door += 1
            key_number = font_text.render(f'{door}', True, (255, 215, 0))

        if sprite.collide_rect(player_5, key_5) and get_key == 3:
            get_key += 1
            door += 1
            key_number = font_text.render(f'{door}', True, (255, 215, 0))      

        if sprite.collide_rect(player_1, enemy_1):
            finish = True
            window.blit(bg, (0,0))
            window.blit(lose, (220,210))

        if sprite.collide_rect(player_2, enemy_2_2) or sprite.collide_rect(player_2, enemy_2_1):
            finish = True
            window.blit(bg, (0,0))
            window.blit(lose, (220,210))

        if sprite.collide_rect(player_3, enemy_3_2) or sprite.collide_rect(player_3, enemy_3_1):
            finish = True
            window.blit(bg, (0,0))
            window.blit(lose, (220,210))

        if sprite.collide_rect(player_4, enemy_4_2) or sprite.collide_rect(player_4, enemy_4_1):
            finish = True
            window.blit(bg, (0,0))
            window.blit(lose, (220,210))

        if sprite.collide_rect(player_5, enemy_5_2) or sprite.collide_rect(player_5, enemy_5_1):
            finish = True
            window.blit(bg, (0,0))
            window.blit(lose, (220,210))

        if final_seconds < 1:
            finish = True
            window.blit(bg, (0,0))
            window.blit(lose, (220,210))

        if door > 0 and sprite.collide_rect(player_4, door_2) and door_open == 0:
            door_open += 1
            door -= 1
            key_number = font_text.render(f'{door}', True, (255, 215, 0))

        if door > 0 and sprite.collide_rect(player_4, door_1) and door_open == 1:
            door_open += 1
            door -= 1
            key_number = font_text.render(f'{door}', True, (255, 215, 0))

        if door > 0 and sprite.collide_rect(player_5, door_3) and door_open == 4:
            door_open += 1
            door -= 1
            key_number = font_text.render(f'{door}', True, (255, 215, 0))

        if door > 0 and sprite.collide_rect(player_5, door_4) and door_open == 3:
            door_open += 1
            door -= 1
            key_number = font_text.render(f'{door}', True, (255, 215, 0))

        if door > 0 and sprite.collide_rect(player_5, door_5) and door_open == 2:
            door_open += 1
            door -= 1
            key_number = font_text.render(f'{door}', True, (255, 215, 0))

        if sprite.collide_rect(player_5, exit_1) and close_2 == 1 and close_3 == 1 and close_4 == 1:
            level += 1
            finish = True

        if sprite.collide_rect(player_5, exit_2) and close_1 == 1 and close_3 == 1 and close_4 == 1:
            level += 1
            finish = True

        if sprite.collide_rect(player_5, exit_3) and close_1 == 1 and close_2 == 1 and close_4 == 1:
            level += 1
            finish = True

        if sprite.collide_rect(player_5, exit_4) and close_1 == 1 and close_2 == 1 and close_3 == 1:
            level += 1
            finish = True

        if sprite.collide_rect(player_5, red_button):
            collide_button = True
            sound_tryvoha = 2

        if tryvoha_seconds < 32 and sound_tryvoha > 0:
            tryvoha_seconds += 0.0168
        elif tryvoha_seconds > 32:
            tryvoha_seconds = 0
            sound_tryvoha -= 1

            if music == True:
                mixer.music.load('tryvoha.mp3')
                mixer.music.play()

        if level == 6 and finish == True:
            for e in event.get():
                if e.type == QUIT:
                    game = False

            if music == True:
                mixer.music.load('magic_music.mp3')
                mixer.music.play()

            window.blit(bg, (0,0))
            window.blit(win, (280,210))
              
    display.flip()