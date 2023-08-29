# 1. Import Modules
from pygame import *
from random import *
from time import time as daGreat


# 2. CONSTANT Variables
WIDTH = 600
HEIGHT = 400
FPS = 60
score = 0
lost = 0
lives = 3

# 3. Game Setups
scr = display.set_mode((WIDTH, HEIGHT))
display.set_caption("Tireur de l'espace 69.0")
background = transform.scale(image.load("farlands_n.jpg"), (WIDTH, HEIGHT))
clock = time.Clock()

# 4. Activate Music
mixer.init()
mixer.music.load("otherside.mp3")
mixer.music.play()

# shoot_sound = mixer.Sound("fireballse.mp3")

# Classes
class Principale(sprite.Sprite): # Main
    def __init__(self, img, x, y, w, h, speed):
        super().__init__()
        self.image = transform.scale(image.load(img),(w,h))
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    
    def reset(self):
        scr.blit(self.image,(self.rect.x, self.rect.y))



class Joueuse(Principale): # Player
    def controls(self):
        keys = key.get_pressed()
        # if keys[K_w] and self.rect.y > 0:
        #     self.rect.y -= self.speed

        if keys[K_d] and self.rect.x < WIDTH - 50:
            self.rect.x += self.speed

        if keys[K_a] and self.rect.x > 0:
            self.rect.x -= self.speed

        # if keys[K_s] and self.rect.y < HEIGHT-100:
        #     self.rect.y += self.speed

    def shoot(self):
        bullet = Bullet("fireballmc.png", self.rect.centerx, self.rect.top, 30, 30, 8)
        bullets.add(bullet)


class Ennemie(Principale):
    def update(self):
        global lost, lives
        self.rect.y += self.speed


        if self.rect.y > HEIGHT:
            self.rect.x = randint(0,WIDTH-75)
            self.rect.y = 0
            lost += 1
            lives -=1
    def update_rock(self):
        global lost
        self.rect.y += self.speed


        if self.rect.y > HEIGHT:
            self.rect.x = randint(0,WIDTH-75)
            self.rect.y = 0


class Bullet(Principale):
    def update(self):
        self.rect.y -= self.speed
        if self.rect.y < 0:
            self.kill()
    


bateau = Joueuse("dispenser.png", 300, 300, 50, 50, 20) # Rocket

bullets = sprite.Group()
monsters = sprite.Group()
asteroids = sprite.Group()

for i in range(1,6):
    enemy = Ennemie("tnt.png", randint(0,550), -50, 50, 50, randint(1,3))
    monsters.add(enemy)

for i in range(2,5):
    asteroid = Ennemie("bedrock_block.png", randint(0,550), -50, 50, 50, randint(1,3))
    asteroids.add(asteroid)



font.init()
style = font.SysFont(None, 36)
style2 = font.SysFont(None, 50)
style3 = font.SysFont(None, 25)

num_shots = 0
reload_bul = False

# 5.Game Loop
end = False
run = True
while run:

    # 6. Event Loop
    for e in event.get():
        if e.type == QUIT:
            run = False
            quit()
        if e.type == KEYDOWN:
            if e.key == K_SPACE:
                if num_shots < 10 and reload_bul == False:
                    num_shots += 1
                    bateau.shoot()
                    # shoot_sound.play()
                if num_shots >= 10 and reload_bul == False:
                    final = daGreat()
                    reload_bul = True


    # 7. Blit BG
    if end != True:
        scr.blit(background,(0, 0))
        bateau.reset()
        bateau.controls()

        monsters.update()
        asteroid.update_rock()
        bullets.update()

        text_lose = style.render("Missed: " + str(lost), 1, (255, 255, 255))
        text_score = style.render("Score: " + str(score), 1, (255, 255, 255))
        jeff = "jeff.jpg"

        scr.blit(text_lose, (10,20))
        scr.blit(text_score, (10,50))


        monsters.draw(scr)
        asteroids.draw(scr)
        bullets.draw(scr)


        if reload_bul:
            current = daGreat()
            if current - final < 3:
                reload_text = style3.render("Reloading", 1, (255, 0, 0))
                scr.blit(reload_text, (300, 300))
            else:
                num_shots = 0
                reload_bul = False


        collides = sprite.groupcollide(bullets, monsters, True, True)
        for c in collides:
            score += 1
            enemy = Ennemie("tnt.png", randint(0,550), -50, 50, 50, randint(1,3))
            monsters.add(enemy)

        if sprite.spritecollide(bateau, monsters, True) or sprite.spritecollide(bateau, asteroids, True):
            lives = 0
            

        if lost >= 3:
            end = True


        if sprite.spritecollide(bateau, monsters, True) or sprite.spritecollide(bateau, asteroids, True):
            lives -= 3
            end = True

        if lives == 0:
            end = True

        if lives == 3:
            life_color = (10,250,10)
        if lives == 2:
            life_color = (250,250,10)
        if lives == 1:
            life_color = (250,100,10)
        if lives == 0:
            life_color = (75, 0, 0)

        text_lives = style2.render(str(lives), 1, life_color)
        scr.blit(text_lives,(550,350))
        











        display.update()
    else:
        end = False
        score = 0
        lives = 3
        for m in monsters:
            m.kill()
        for b in bullets:
            b.kill()
        for a in asteroids:
            a.kill()
        lost = 0
        bateau = Joueuse("dispenser.png", 300, 300, 50, 50, 20)
        for i in range(1,6):
            enemy = Ennemie("tnt.png", randint(0,550), -50, 50, 50, randint(1,3))
            monsters.add(enemy)

        for i in range(2,5):
            asteroid = Ennemie("bedrock_block.png", randint(0,550), -50, 50, 50, randint(1,3))
            asteroids.add(asteroid)
        time.delay(2000)
        









    # 8. Update Loop
    time.delay(30)


















