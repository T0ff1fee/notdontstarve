from time import*
from pygame import*
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (65, 65))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x < win_width - 80:
            self.rect.x += self.speed
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height - 80:
            self.rect.y += self.speed

class Enemy(GameSprite):

    direction = 'left'

    def update(self):
        if self.rect.x <= 470:
            self.direction = 'right'
        if self.rect.x >= win_width - 85:
            self.direction = 'left'
        if self.direction == 'left':
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed

class Wall(sprite.Sprite):
    def __init__(self, color_1, color_2, color_3, wall_x, wall_y, wall_width, wall_height):
        super().__init__()
        self.color_1 = color_1
        self.color_2 = color_2
        self.color_3 = color_3
        self.width = wall_width
        self.height = wall_height
        self.image = Surface((self.width, self.height))
        self.image.fill((color_1, color_2, color_3))
        self.rect = self.image.get_rect()
        self.rect.x = wall_x
        self.rect.y = wall_y

    def draw_wall(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
        #draw.rect(window, (self.color_1, self.color_2, self.color_3))


class Enemy2(GameSprite):

    direction = 'up'

    def update(self):
        if self.rect.y <= 20:
            self.direction = 'down'
        if self.rect.y >= win_height - 85:
            self.direction = 'up'
        if self.direction == 'up':
            self.rect.y -= self.speed
        else:
            self.rect.y += self.speed

class Enemy3(GameSprite):

    direction = 'left'

    def update(self):
        if self.rect.x <= 20:
            self.direction = 'right'
        if self.rect.x >= 165:
            self.direction = 'left'
        if self.direction == 'left':
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed

class Enemy4(GameSprite):

    direction = 'left'

    def update(self):
        if self.rect.x <= 20:
            self.direction = 'right'
        if self.rect.x >= win_width - 85:
            self.direction = 'left'
        if self.direction == 'left':
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed


win_width = 700
win_height = 500
window = display.set_mode((win_width, win_height))
display.set_caption('Maze')
background = transform.scale(image.load('back.jpg'), (win_width, win_height))
 
player = Player('wilson.png', 5, win_height - 80, 4)
monster = Enemy('drevnistraj.png', win_width - 80, 280, 2)
final = GameSprite('tulicit.png', win_width- 120, win_height - 80, 0)
w1 = Wall(95, 158, 160, 110, 450, 370, 10)
w2 = Wall(95, 158, 160, 10, 10, 10, 370)
w3 = Wall(95, 158, 160, 10, 10, 680, 10)
w4 = Wall(95, 158, 160, 680, 10, 10, 370)
w5 = Wall(95, 158, 160, 110, 100, 10, 350)
w6 = Wall(95, 158, 160, 200, 250, 200, 10)
w7 = Wall(95, 158, 160, 200, 10, 10, 350)
w8 = Wall(95, 158, 160, 480, 150, 10, 300)



monster2 = Enemy2('spider.png', 320, 50, 2)
#monster3 = Enemy3('spider.png', 100, 50, 2)
monster4 = Enemy4('spider.png', win_width - 80, 200, 2)


game = True
finish = False
clock = time.Clock()
FPS = 60

font.init()
font = font.Font(None, 70)
win = font.render('YOU WIN!', True, (255, 215, 0))
lose = font.render('YOU LOSE!', True, (180, 0, 0))

mixer.init()
mixer.music.load('Dawn.mp3')
mixer.music.play()

money = mixer.Sound('money.ogg')
kick = mixer.Sound('kick.ogg')

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if finish != True:
        window.blit(background, (0,0))
        player.update()
        monster.update()
        monster.reset()
        w1.draw_wall()
        w2.draw_wall()
        w3.draw_wall()
        w4.draw_wall()
        w5.draw_wall()
        w6.draw_wall()
        w7.draw_wall()
        w8.draw_wall()

        player.reset()
        
        monster2.reset()
        monster4.reset()
        #monster3.reset()
        monster2.update()
        #monster3.update()
        monster4.update()

        final.reset()
    if sprite.collide_rect(player,monster) or sprite.collide_rect(player, w1) or sprite.collide_rect(player, w2) or sprite.collide_rect(player, w3) or sprite.collide_rect(player, w4) or sprite.collide_rect(player, w5) or sprite.collide_rect(player, w6) or sprite.collide_rect(player, w7) or sprite.collide_rect(player, w8) or sprite.collide_rect(player,monster2) or sprite.collide_rect(player,monster4):
        finish = True
        window.blit(lose, (200, 200))
        kick.play()
    if sprite.collide_rect(player, final):
        finish = True
        window.blit(win, (200, 200))
        money.play()



    
    
    display.update()
    clock.tick(FPS)