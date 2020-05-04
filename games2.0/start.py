import pygame

rtr = False
pygame.init()

display_width = 960
display_height = 540

usr_y = 279
usr_x = 0

usr_y_demon = 84
usr_x_demon = 400

make_jump = False
jump_counter = 10

forward = False
progress = 5

back = False
backward_movement = 5

make_jump_demon = False
jump_counter_demon = 10

back_demon = False
backward_movement_demon = 5

forward_demon = False
progress_demon = 5

climbing_stairs = False
down_stairs = False

clock = pygame.time.Clock()

display = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("Platform")

door = pygame.image.load('door.png')

img_movement_jinn = 0
jinn = [pygame.image.load('Idle1.png'), pygame.image.load('Flight1.png'), pygame.image.load('Flight2.png'),
        pygame.image.load('Flight3.png'), pygame.image.load('Flight4.png')
        ]

img_movement_back_demon = 5
demon = [
    pygame.image.load('baseRack.png'), pygame.image.load('movement1.png'),
    pygame.image.load('movement2.png'), pygame.image.load('movement3.png'),
    pygame.image.load('movement4.png')
]

platform = [
    pygame.image.load('tile1.png'), pygame.image.load('tile2.png'), pygame.image.load('tile3.png'),
    pygame.image.load('tile7.png'), pygame.image.load('tile8.png'), pygame.image.load('tile9.png'),
    pygame.image.load('tile27.png'), pygame.image.load('tile33.png'),
    pygame.image.load('tile34.png')
]

stairs = [pygame.image.load('stair1.png'), pygame.image.load('stair2.png'), pygame.image.load('stair3.png')]

img_star_counter = 0
star = [
    pygame.image.load('000_0019_star1.png'), pygame.image.load('000_0018_star2.png'),
    pygame.image.load('000_0017_star3.png'),
    pygame.image.load('000_0016_star4.png'), pygame.image.load('000_0015_star5.png'),
    pygame.image.load('000_0014_star6.png'),
    pygame.image.load('000_0013_star7.png'), pygame.image.load('000_0012_star8.png'),
    pygame.image.load('000_0011_star9.png'),
    pygame.image.load('000_0010_star10.png')
]
attac_demon_kl = False
img_attac_demon = 0
attac_demon = [pygame.image.load('Attack_demon1.png'), pygame.image.load('Attack_demon2.png'),
               pygame.image.load('Attack_demon3.png'), pygame.image.load('Attack_demon4.png')
               ]
attac_jinn_kl = False
img_attac_jinn = 0
attac_jinn = [pygame.image.load('Attack1.png'), pygame.image.load('Attack2.png'),
              pygame.image.load('Attack3.png'), pygame.image.load('Attack4.png'),
              pygame.image.load('Magic_Attack1.png'), pygame.image.load('Magic_Attack2.png'),
              pygame.image.load('Magic_Attack3.png'), pygame.image.load('Magic_Attack4.png'),
              pygame.image.load('Magic_Attack5.png'), pygame.image.load('Magic_Attack6.png'),
              pygame.image.load('Magic_Attack7.png'), pygame.image.load('Magic_Attack8.png'),
              pygame.image.load('Magic_Attack9.png'), pygame.image.load('Magic_Attack10.png'),
              pygame.image.load('Magic_Attack11.png'), pygame.image.load('Magic_Attack22.png'),
              pygame.image.load('Magic_Attack23.png')
              ]

health_demon = 100
health_jinn = 200

anim_derg_jinn = 0
img_deth_jinn = [
    pygame.image.load('Death1.png'), pygame.image.load('Death2.png'), pygame.image.load('Death3.png'),
    pygame.image.load('Death4.png'), pygame.image.load('Death5.png'), pygame.image.load('Death6.png')
]

anim_derg_demon = 0
img_deth_demon = [
    pygame.image.load('Death_demon1.png'), pygame.image.load('Death_demon2.png'), pygame.image.load('Death_demon3.png'),
    pygame.image.load('Death_demon4.png'), pygame.image.load('Death_demon5.png'), pygame.image.load('Death_demon6.png')
]


def run_game():
    global make_jump, forward, back, forward_demon, back_demon, \
        make_jump_demon, img_movement_back_demon, img_demon, climbing_stairs, \
        down_stairs, rtr, attac_demon_kl, attac_jinn_kl, health_demon, health_jinn
    game = True
    land = pygame.image.load('Background.png')

    while game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        key = pygame.key.get_pressed()

        if key[pygame.K_SPACE]:
            make_jump = True
        if make_jump:
            jump_jinn()

        if key[pygame.K_d]:
            forward = True
        if forward:
            go_ahead_jinn()

        if key[pygame.K_a]:
            back = True
        if back:
            go_back_jinn()

        if key[pygame.K_RIGHT]:
            forward_demon = True
        if forward_demon:
            go_ahead_demon()

        if key[pygame.K_LEFT]:
            back_demon = True
        if back_demon:
            go_back_demon()

        if key[pygame.K_RCTRL]:
            make_jump_demon = True

        if make_jump_demon:
            jump_demon()

        if key[pygame.K_k]:
            attac_demon_kl = True

        if key[pygame.K_g]:
            attac_jinn_kl = True

        if 150 <= usr_x <= 180 and 165 <= usr_y <= 1000 and key[pygame.K_w]:
            climbing_stairs = True

        if climbing_stairs:
            climbing_stairs_w()

        if 150 <= usr_x <= 180 and 150 <= usr_y <= 269 and key[pygame.K_s]:
            down_stairs = True

        if (150 > usr_x or (usr_x > 180 and usr_y > 200)) and usr_y < 269:
            rtr = True

        if down_stairs:
            down_stairs_s()

        display.blit(land, (0, 0))

        if attac_jinn_kl:
            attac_jinn_fr()
            if usr_x - 50 <= usr_x_demon <= usr_x + 50 and usr_y - 100 <= usr_y_demon <= usr_y + 100:
                health_demon -= 100
            if health_demon <= 0:
                deth_demon()
        elif health_jinn > 0:
            draw_jinn()

        draw_platform()
        draw_stairs()
        draw_door()
        draw_star()

        if attac_demon_kl:
            attac_demon_fr()
            if usr_x_demon - 20 <= usr_x <= usr_x_demon + 50 and usr_y_demon - 100 <= usr_y <= usr_y_demon + 100:
                health_jinn -= 100
            if health_jinn <= 0:
                deth_jinn()
        elif health_demon > 0:
            movement_demon()

        pygame.display.update()
        clock.tick(60)


def deth_demon():
    global img_deth_demon, anim_derg_demon, attac_demon_kl
    if anim_derg_demon == 216:
        anim_derg_demon = 0
    else:
        display.blit(img_deth_demon[anim_derg_demon // 36], (usr_x_demon, usr_y_demon))
        anim_derg_demon += 1
    if anim_derg_demon == 36:
        attac_demon_kl = False


def attac_jinn_fr():
    global img_attac_jinn, attac_jinn_kl
    if img_attac_jinn == 169:
        img_attac_jinn = 0
    else:
        if (img_attac_jinn // 13) < 4:
            display.blit(attac_jinn[img_attac_jinn // 13], (usr_x, usr_y))

        if (img_attac_jinn // 13) == 4:
            display.blit(attac_jinn[img_attac_jinn // 13], (usr_x + 50, usr_y - 60))
            draw_jinn()
        if (img_attac_jinn // 13) > 4:
            display.blit(attac_jinn[img_attac_jinn // 13], (usr_x + 50, usr_y - 60))
            draw_jinn()
        img_attac_jinn += 1
    if img_attac_jinn == 169:
        attac_jinn_kl = False


def deth_jinn():
    global img_deth_jinn, anim_derg_jinn, attac_jinn_kl
    if anim_derg_jinn == 36:
        anim_derg_jinn = 0
    else:
        display.blit(img_deth_jinn[anim_derg_jinn // 6], (usr_x, usr_y))
        anim_derg_jinn += 1
    if img_attac_demon == 36:
        attac_jinn_kl = False


def attac_demon_fr():
    global img_attac_demon, attac_demon_kl
    if img_attac_demon == 20:
        img_attac_demon = 0
    else:
        display.blit(attac_demon[img_attac_demon // 5], (usr_x_demon, usr_y_demon))
        img_attac_demon += 1
    if img_attac_demon == 16:
        attac_demon_kl = False


def draw_jinn():
    global img_movement_jinn, rtr, usr_y
    if rtr:
        if img_movement_jinn == 25:
            img_movement_jinn = 0
        else:
            display.blit(jinn[img_movement_jinn // 5], (usr_x, usr_y))
            img_movement_jinn += 1
        usr_y += 1
        if usr_y >= 269:
            rtr = False
    else:
        if img_movement_jinn == 25:
            img_movement_jinn = 0
        else:
            display.blit(jinn[img_movement_jinn // 5], (usr_x, usr_y))
            img_movement_jinn += 1


def climbing_stairs_w():
    global climbing_stairs, usr_y
    usr_y -= 5
    climbing_stairs = False


def down_stairs_s():
    global down_stairs, usr_y
    usr_y += 5
    down_stairs = False


def draw_star():
    global img_star_counter
    if img_star_counter == 100:
        img_star_counter = 0
    display.blit(star[img_star_counter // 10], (370, 365))
    img_star_counter += 1


def draw_door():
    display.blit(door, (595, 165))


def draw_stairs():
    display.blit(stairs[1], (200, 365))
    k = 0
    y = 33
    while k < 2:
        k += 1
        display.blit(stairs[2], (200, 365 - y))
        y += 32
    display.blit(stairs[0], (200, 365 - y))


def draw_platform():
    k = 0
    y = 65
    display.blit(platform[0], (5, 380))
    while k < 5:
        k += 1
        display.blit(platform[1], (y, 380))
        y += 64
    display.blit(platform[2], (y, 380))
    display.blit(platform[5], (5, 444))
    k = 0
    y = 65
    while k < 5:
        k += 1
        display.blit(platform[4], (y, 444))
        y += 64
    display.blit(platform[3], (y, 444))

    display.blit(platform[7], (190, 444 - 190))
    k = 0
    y = 65
    while k < 6:
        k += 1
        display.blit(platform[6], (190 + y, 444 - 190))
        y += 64

    display.blit(platform[8], (190 + y, 444 - 190))


def jump_jinn():
    global make_jump, usr_y, jump_counter
    if jump_counter >= -10:
        usr_y -= jump_counter
        jump_counter -= 1
    else:
        jump_counter = 10
        make_jump = False


def go_ahead_jinn():
    global usr_x, progress, forward
    usr_x += progress
    forward = False


def go_back_jinn():
    global usr_x, backward_movement, back
    usr_x -= backward_movement
    back = False


def go_back_demon():
    global usr_x_demon, backward_movement_demon, back_demon, img_movement_back_demon
    usr_x_demon -= backward_movement_demon
    back_demon = False


def go_ahead_demon():
    global usr_x_demon, progress_demon, forward_demon
    usr_x_demon += progress_demon
    forward_demon = False


def jump_demon():
    global make_jump_demon, usr_y_demon, jump_counter_demon
    if jump_counter_demon >= -10:
        usr_y_demon -= jump_counter_demon
        jump_counter_demon -= 1
    else:
        jump_counter_demon = 10
        make_jump_demon = False


def movement_demon():
    global img_movement_back_demon
    if img_movement_back_demon == 25:
        img_movement_back_demon = 0
    else:
        display.blit(demon[img_movement_back_demon // 5], (usr_x_demon, usr_y_demon))
        img_movement_back_demon += 1


run_game()
