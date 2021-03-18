import pygame
import sys
import random

FPS = 60
WIN_WIDTH = 700
WIN_HEIGHT = 500
WHITE = (255, 255, 255)
ORANGE = (255, 150, 100)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
pygame.init()
clock = pygame.time.Clock()
sc = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
pygame.display.set_caption('Dino')
ip = 'images/'
icon = pygame.image.load(ip + 'icon.png')
pygame.display.set_icon(icon)
z = 50
h = 80
x = WIN_WIDTH // 7
y = 345
a = 1
b = 1
c = random.randrange(1, 3)
d = 0
e = 0
ab = 0
r = 0
make_jump = False
jump_count = 30
dino_counter = 0
scores = 0
scores1 = 0
record = 0
error = 0
cactus1_x = WIN_WIDTH
cactus1_y = 350
cactus2_x = WIN_WIDTH
cactus2_y = 350
cactus3_x = WIN_WIDTH
cactus3_y = 350
cloud1_x = random.randrange(0, 700)
cloud1_y = random.randrange(0, 250)
cloud2_x = random.randrange(0, 700)
cloud2_y = random.randrange(0, 250)
cloud3_x = random.randrange(0, 700)
cloud3_y = random.randrange(0, 250)
cloud4_x = random.randrange(0, 700)
cloud4_y = random.randrange(0, 250)
dino_img = [pygame.image.load(ip + 'dino0.png'),
            pygame.image.load(ip + 'dino1.png'),
            pygame.image.load(ip + 'dino2.png'),
            pygame.image.load(ip + 'dino3.png'),
            pygame.image.load(ip + 'dino4.png'),
            pygame.image.load(ip + 'dino5.png'),
            pygame.image.load(ip + 'dino6.png'),
            pygame.image.load(ip + 'dino7.png'), ]


def clouds1():
    global cloud1_x, cloud1_y
    if cloud1_x >= -200:
        cloud1_x -= 2
        if cloud1_x <= - 200:
            cloud1_x = 700
            cloud1_y = random.randrange(0, 200)


def clouds2():
    global cloud2_x, cloud2_y
    if cloud2_x >= -200:
        cloud2_x -= 3
        if cloud2_x <= - 200:
            cloud2_x = 700
            cloud2_y = random.randrange(0, 200)


def clouds3():
    global cloud3_x, cloud3_y
    if cloud3_x >= -200:
        cloud3_x -= 4
        if cloud3_x <= - 200:
            cloud3_x = 700
            cloud3_y = random.randrange(0, 200)


def game_over():
    global x, y, cactus1_x, cactus1_y, cactus2_x, cactus2_y, cactus3_x, cactus3_y, ab, scores
    if (275 < y < 450 and 80 < cactus1_x < 120) or (275 < y < 450 and 50 < cactus2_x < 120) or (
            275 < y < 450 and 0 < cactus3_x < 120):
        pygame.mixer.music.load(ip + 'sound_die.mp3')
        pygame.mixer.music.play(1)
        over()


def over():
    global ab, scores, scores1
    ov = True
    while ov:
        for i in pygame.event.get():
            if i.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RETURN]:
            scores = 0
            scores1 = 0
            ab = 1
            y = 345
            ov = False
        print_text('Game Over, press ENTER to continue.', 35, 250)
        pygame.display.update()
        clock.tick(FPS)


def cactus1():
    global cactus1_y, cactus1_x, d, ab, r
    if cactus1_x >= -50:
        cactus1_x -= 8
        d = 0

        if ab == 1:
            cactus1_x = 700
        if cactus1_x <= -50:
            cactus1_x = 700
            d = 1
        ab = 0


def cactus2_a():
    global cactus2_y, cactus2_x, d, ab, r
    if cactus2_x >= -240:
        cactus2_x -= 8
        d = 0

        if ab == 1:
            cactus2_x = 700
        if cactus2_x <= -100:
            cactus2_x = 700
            d = 1
        ab = 0


def cactus3_a():
    global cactus3_y, cactus3_x, d, speed, ab, r
    if cactus3_x >= -300:
        cactus3_x -= 8
        d = 0

        if ab == 1:
            cactus3_x = 700
        if cactus3_x <= -240:
            cactus3_x = 700
            d = 1
        ab = 0


def print_text(message, ax, ay, font_color=BLACK, font_type=ip + '18959.ttf', font_size=30):
    font_type = pygame.font.Font(font_type, font_size)
    text = font_type.render(message, True, font_color)
    sc.blit(text, (ax, ay))


def jump():
    global y, a, b, make_jump, jump_count
    if jump_count >= -30:
        if jump_count == 30:
            pygame.mixer.music.load(ip + 'sound_jumper.mp3')
            pygame.mixer.music.play()
        y -= jump_count / 3
        jump_count -= 1
    else:
        jump_count = 30
        make_jump = False


def pause():
    paused = True
    while paused:
        for i in pygame.event.get():
            if i.type == pygame.QUIT or error == 1:
                pygame.quit()
                sys.exit()
        print_text('Paused, press ENTER to continue.', 80, 250)
        keys = pygame.key.get_pressed()

        if keys[pygame.K_RETURN]:
            paused = False
        pygame.display.update()
        clock.tick(FPS)


def scores_1():
    global scores, scores1
    print_text('Scores: ' + str(scores), 5, 5)
    scores1 += 1
    scores = scores1 // 5
    if scores % 100 == 0:
        pygame.mixer.music.load(ip + 'sound_100.mp3')
        pygame.mixer.music.play(1)


def record_time():
    global scores, record
    if scores > record:
        record = scores
    print_text('Record: ' + str(record), 5, 40)


def draw_dino():
    global dino_counter
    if dino_counter == 16:
        dino_counter = 0
    sc.blit(dino_img[dino_counter // 2], (x, y))
    dino_counter += 1


land = pygame.image.load(ip + 'Land.jpg')
cloud2 = pygame.image.load(ip + 'cloud2.png')
cloudA2 = pygame.image.load(ip + 'cloudA2.png')
cloudA3 = pygame.image.load(ip + 'cloudA3.png')
cactus = pygame.image.load(ip + 'cactus 10.png')
cactus2 = pygame.image.load(ip + 'cactus 20.png')
cactus3 = pygame.image.load(ip + 'cactus 30.png')
game = True
while game:
    sc.blit(land, (0, 0))
    sc.blit(cloud2, (cloud1_x, cloud1_y))
    sc.blit(cloudA2, (cloud2_x, cloud2_y))
    sc.blit(cloudA3, (cloud3_x, cloud3_y))
    sc.blit(cactus, (cactus1_x, cactus1_y))
    sc.blit(cactus2, (cactus2_x, cactus2_y))
    sc.blit(cactus3, (cactus3_x, cactus3_y))
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    if error == 1:
        pygame.quit()
        sys.exit()
    scores_1()
    record_time()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
        make_jump = True
    if make_jump:
        jump()
    if keys[pygame.K_ESCAPE]:
        pause()
    draw_dino()
    clouds1()
    clouds2()
    clouds3()
    game_over()
    if d == 1:
        c = random.randrange(1, 4)
    if c == 1:
        cactus1()
    if c == 2:
        cactus2_a()
    if c == 3:
        cactus3_a()
    pygame.display.update()
    clock.tick(FPS)
