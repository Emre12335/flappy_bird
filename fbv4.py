# collisionları check etme
from random import choice
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
main_bird = pygame.transform.scale(main_bird, (50, 40))
main_bird_r = main_bird.get_rect(center=(100, 200))
# Variable of floor
floor_x1_pos = 0

# Variables of bird fly
bird_movement = 0
gravity = 0.25

# Pipe surface
p1 = pygame.image.load("assets/pipe-green.png").convert()
p1 = pygame.transform.scale2x(p1).convert()
pipe_list = []
pipe_positions = [300, 400, 600]
spawnpipe = pygame.USEREVENT
pygame.time.set_timer(spawnpipe, 1200)


def create_pipe():
    random_pos = choice(pipe_positions)
    new_pipe_r = p1.get_rect(midtop=(700, random_pos))
    new_pipe_r2 = p1.get_rect(midbottom=(700, random_pos - 200))
    return new_pipe_r, new_pipe_r2


def move_pipes(pipes: list) -> list:
    for pipe in pipes:
        pipe.centerx -= 5
    pipes = [pipe for pipe in pipes if pipe.right > 0]
    return pipes


def draw_pipes(pipes: list):
    for pipe in pipes:
        if pipe.bottom >= 800:
            screen.blit(p1, pipe)
        else:
            flip_pipe = pygame.transform.flip(p1, False, True)
            screen.blit(flip_pipe, pipe)


def check_collisions(pipes: list): # 1 game active check
    for pipe in pipes:
        if main_bird_r.colliderect(pipe):
            return False
    if main_bird_r.top <= 0:
        return False
    if main_bird_r.bottom >= 650:
        return False
    return True


def draw_floor():
    screen.blit(ground_surface, (floor_x1_pos, 650))
    screen.blit(ground_surface, (floor_x1_pos + 567, 650))


game_active = True # 1 game active loopumuz
while True:
    for event in pygame.event.get(): # for loopu da ikiye böldük.
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if game_active:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    bird_movement = -7
            if event.type == spawnpipe:
                pipe_list.extend(create_pipe())
        else:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    main_bird_r.center =(100, 200)
                    pipe_list.clear()
                    bird_movement = 0
                    game_active = True
    screen.blit(bg_surface, (0, 0))
    if game_active: # 2 eğer game activse bunlar oynatılacak değilse sadece yüzey oynatılacak.
        draw_pipes(pipe_list)
        screen.blit(main_bird, main_bird_r)
        bird_movement += gravity
        main_bird_r.centery += bird_movement
        pipe_list = move_pipes(pipe_list)
        game_active = check_collisions(pipe_list)
    draw_floor()
    floor_x1_pos -= 1
    if floor_x1_pos <= -567:
        floor_x1_pos = 0
    pygame.display.update()
    clock.tick(120)
