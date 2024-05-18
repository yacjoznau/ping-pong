from pygame import*

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, wight, height):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (wight, height)) #вместе 55,55 - параметры
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y


    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height - 80:
            self.rect.y += self.speed

    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_height - 80:
            self.rect.y += self.speed

back = (200, 255, 255)
win_width = 600
win_height = 500
window = display.set_mode((win_width, win_height))
window.fill(back)

game = True
finish = False
clock = time.Clock()
FPS = 60

speed_x = 3
speed_y = 3

RAKETKA1 = Player(player_image='racket.png', player_x=30, player_y=200, player_speed=4, wight=50, height=150)
RAKETKA2 = Player(player_image='racket.png', player_x=520, player_y=200, player_speed=4, wight=50, height=150)
ball = GameSprite(player_image='ball.png', player_x=200, player_y=200, player_speed=4, wight=50, height=50)

font.init()
font = font.Font(None, 35)
lose1 = font.render('PLAYER 1 LOSE!', True, (180, 0, 0))
lose2 = font.render('PLAYER 2 LOSE!', True, (180, 0, 0))

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    if finish != True:

        window.fill(back)
        RAKETKA1.update_l()
        RAKETKA2.update_r()
        ball.rect.x += speed_x
        ball.rect.y += speed_y

        if sprite.collide_rect(RAKETKA1, ball) or sprite.collide_rect(RAKETKA2, ball):
            speed_x *= -1
            speed_y *= 1
        
        if ball.rect.y > win_height-50 or ball.rect.y < 0:
            speed_y *= -1

        if ball.rect.x < 0:
            finish = True
            window.blit(lose1, (200, 200))

        if ball.rect.x > win_width:
            finish = True
            window.blit(lose2, (200, 200))

        RAKETKA1.reset()
        RAKETKA2.reset()
        ball.reset()

    display.update()
    clock.tick(FPS)