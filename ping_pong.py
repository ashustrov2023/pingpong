from pygame import *

# класс-родитель для других спрайтов
class GameSprite(sprite.Sprite):
 # конструктор класса
   def __init__(self, player_image, player_x, player_y, player_speed, wight, height):
       # Вызываем конструктор класса (Sprite):
       sprite.Sprite.__init__(self)

       # каждый спрайт должен хранить свойство image - изображение
       self.image = transform.scale(image.load(player_image), (wight, height))
       self.speed = player_speed

       # каждый спрайт должен хранить свойство rect - прямоугольник, в который он вписан

# класс главного игрока
class Player(GameSprite):
   # метод для управления спрайтом стрелками клавиатуры
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x < win_width - 80:
            self.rect.x += self.speed

    def update_l(self):
         keys = key.get_pressed()
         if keys[K_w] and self.rect.y > 5:
             self.rect.y -= self.speed
         if keys[K_s] and self.rect.y < win_width - 80:
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

racket1 = Player('racket1.png', 30, 200, 4, 50, 150)
racket2 = Player('racket2.png', 520, 200, 4, 50, 150)
ball = GameSprite('ball.png', 200, 200, 4, 50, 50)

font.init()
font = font.Font(None, 35)
lose1 = font.render('PLAYER 1 LOSE!', True, (180, 0, 0))
lose2 = font.render('PLAYER 2 LOSE!', True, (180, 0, 0))




