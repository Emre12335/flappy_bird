# Scoreboard ekleme
# Oyun ekranı ekleme
# Score tutmak için 2 tane de variable oluştrduk score ve high_score
# score u pipe ların bir tanesinin şimdiki hali kuşun x indenksinden küçükse ve gelecekteki hali kuşunkinden büyük ise
# score a 1 ekliyoruz. pipeların x ekseni konumları için b,r set oluşturuyoruz öncesinde
# ardından üstteki durumu kontrol ediyoruz.
# eğer score high_score dan büyükse high score u score yapıyoruz.
# diğerleri klasik menü ekranı ve  animated bird u bastırdık ayrıca animated bird u if else,game active den çıkarıp
# ortak alana soktuk oyun active olsa da olmasa da ÇALIŞACAK BİÇİMDE FOR LOOP DA
# while loop un içini de 3 kısma böldük if if not ve diğer bu üç kısım if game_active ise if not game active değil ise
# diğer ise game_active e bağlı olmaksızın çalışıyor
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

# Main bird ekleniyor /1
main_bird = pygame.image.load("assets/bluebird-midflap.png").convert()
main_bird3 = pygame.image.load("assets/bluebird-upflap.png").convert()
main_bird2 = pygame.image.load("assets/bluebird-downflap.png").convert()

main_bird = pygame.transform.scale(main_bird, (50, 40)).convert()
main_bird3 = pygame.transform.scale(main_bird3, (50, 40)).convert()
main_bird2 = pygame.transform.scale(main_bird2, (50, 40)).convert()

main_bird_r = main_bird.get_rect(center=(100, 200))
# Variable of animation /2
animation_list = [main_bird, main_bird2, main_bird3]
animation_index = 0
animation_event = pygame.USEREVENT + 2
pygame.time.set_timer(animation_event, 200)
animated_bird = animation_list[animation_index]
animated_bird_r = animated_bird.get_rect(center=(100, 200))
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

# Score board
game_score_font = pygame.font.Font("04B_19.TTF", 40)  # score board şekli
score = 0
highscore = 0


def menu_screen():
    menu = pygame.image.load("assets/message.png").convert_alpha()
    menu = pygame.transform.scale(menu, (menu.get_width() + 130, 500))
    menu_r = menu.get_rect(center=(283, 330))
    non_movement_bird = animated_bird
    non_movement_bird_r = main_bird.get_rect(center=(100, 215))
    screen.blit(menu, menu_r)
    screen.blit(non_movement_bird, non_movement_bird_r)


def update_score():
    global score
    new_centerx_list = {pipe.centerx for pipe in pipe_list}
    for value in new_centerx_list:
        old = value
        new = value - 5
        if new < animated_bird_r.centerx <= old:
            score += 1


def display_score():
    if game_active:
        score_surface = game_score_font.render(f"{int(score)}", True, (255, 255, 255))
        score_surface_r = score_surface.get_rect(center=(288, 100))
    else:
        score_surface = game_score_font.render(f"score: {int(score)}", True, (255, 255, 255))
        score_surface_r = score_surface.get_rect(center=(288, 40))
    screen.blit(score_surface, score_surface_r)


def display_high_score():
    highscore_surface = game_score_font.render(f"High Score: {int(highscore)}", True, (255, 255, 255))
    highscore_surface_r = highscore_surface.get_rect(center=(288, 710))
    screen.blit(highscore_surface, highscore_surface_r)


def update_high_score():
    global highscore
    if score > highscore:
        highscore = score


def bird_animation():
    new_bird = animation_list[animation_index]
    new_bird_r = new_bird.get_rect(center=(100, animated_bird_r.centery))
    return new_bird, new_bird_r


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


def check_collisions(pipes: list):  # 1 game active check
    for pipe in pipes:
        if animated_bird_r.colliderect(pipe):
            return False
    if animated_bird_r.top <= 0:
        return False
    if animated_bird_r.bottom >= 650:
        return False
    return True


def rotate_bird(surface1):  # /1
    return pygame.transform.rotate(surface1, -3 * bird_movement)  # /2 #bird movement kadar flip ediyor.


def draw_floor():
    screen.blit(ground_surface, (floor_x1_pos, 650))
    screen.blit(ground_surface, (floor_x1_pos + 567, 650))


game_active = False
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == animation_event:
            if animation_index < 2:
                animation_index += 1
            else:
                animation_index = 0
            animated_bird, animated_bird_r = bird_animation()
        if game_active:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    bird_movement = -7
            if event.type == spawnpipe:
                pipe_list.extend(create_pipe())

        else:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    animated_bird_r.center = (100, 200)
                    pipe_list.clear()
                    bird_movement = 0
                    score = 0
                    game_active = True
    screen.blit(bg_surface, (0, 0))
    if game_active:
        draw_pipes(pipe_list)
        bird_movement += gravity
        animated_bird_r.centery += bird_movement
        rotated_new_bird = rotate_bird(animated_bird)  # /3
        screen.blit(rotated_new_bird, animated_bird_r)  # /4
        pipe_list = move_pipes(pipe_list)
        update_score()
        update_high_score()
        game_active = check_collisions(pipe_list)
    draw_floor()
    display_score()
    if not game_active:
        display_high_score()
        menu_screen()
    floor_x1_pos -= 1
    if floor_x1_pos <= -567:
        floor_x1_pos = 0
    pygame.display.update()
    clock.tick(120)
