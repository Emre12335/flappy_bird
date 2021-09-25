# Kuşun çizimi
# Kuşu normal bir şekilde rectangle kullanarak çizeceğiz.
# Ardından gravity i diğer gravityden farklı yapacağız.
# Bunun için 2 tane variable kullanacağız.
# Gravity yer çekimini temsil edecek ve sürekli artacak.
# Ve bu artan gravity bird movement a eklenecek
# tuşa basıldığında gravity 0 olacak ve bird movement negatif bir değer olacak bu sayede yükselecek
import pygame

pygame.init()
screen = pygame.display.set_mode((567, 800))
clock = pygame.time.Clock()
pygame.display.set_caption("Flappy Bird")

# Surfaces
bg_surface = pygame.image.load("assets/background-day.png").convert()
bg_surface = pygame.transform.scale(bg_surface, (567, 800))
ground_surface = pygame.image.load("assets/base.png")
ground_surface = pygame.transform.scale(ground_surface, (567, 150))

main_bird = pygame.image.load("assets/bluebird-midflap.png").convert()
main_bird = pygame.transform.scale(main_bird,(50,40))
main_bird_r = main_bird.get_rect(center = (100,400))
# Variable of floor
floor_x1_pos = 0

# Variables of bird fly
bird_movement = 0
gravity = 0.25


def draw_floor():
    screen.blit(ground_surface, (floor_x1_pos, 650))
    screen.blit(ground_surface, (floor_x1_pos + 567, 650))


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bird_movement = -12
    screen.blit(bg_surface, (0, 0))
    draw_floor()
    screen.blit(main_bird,main_bird_r)
    floor_x1_pos -= 1
    bird_movement += gravity
    main_bird_r.centery += bird_movement
    if floor_x1_pos <= -567:
        floor_x1_pos = 0
    pygame.display.update()
    clock.tick(120)