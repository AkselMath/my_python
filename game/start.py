import pygame

pygame.init()

display_width = 960
display_height = 540

display = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("Platform")

door = pygame.image.load('door.png')
platform = [pygame.image.load('tile1.png'), pygame.image.load('tile2.png'), pygame.image.load('tile3.png'), pygame.image.load('tile7.png'), pygame.image.load('tile8.png'), pygame.image.load('tile9.png'), pygame.image.load('tile27.png'), pygame.image.load('tile33.png'), pygame.image.load('tile34.png')]
stairs = [pygame.image.load('stair1.png'), pygame.image.load('stair2.png'), pygame.image.load('stair3.png')]
star =[pygame.image.load('000_0019_star1.png'), pygame.image.load('000_0018_star2.png'), pygame.image.load('000_0017_star3.png'), pygame.image.load('000_0016_star4.png'), pygame.image.load('000_0015_star5.png'), pygame.image.load('000_0014_star6.png'), pygame.image.load('000_0013_star7.png'), pygame.image.load('000_0012_star8.png'), pygame.image.load('000_0011_star9.png'), pygame.image.load('000_0010_star10.png'), ]
img_star_counter = 0
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

    display.blit(platform[7], (190, 444-190))
    k = 0
    y = 65
    while k < 6:
        k += 1
        display.blit(platform[6], (190 + y, 444-190))
        y += 64

    display.blit(platform[8], (190 + y, 444 - 190))
def run_game():
    game = True
    land = pygame.image.load('Background.png')

    while game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()


        display.blit(land, (0, 0))

        draw_platform()
        draw_stairs()
        draw_door()
        draw_star()

        pygame.display.update()

run_game()
