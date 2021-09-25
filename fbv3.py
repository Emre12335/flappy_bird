# Pipeları ekleme
# pipeları random olarak eklemek için bir rectangle listesi açacağız.
# bu listenin içine rectangle ları ekleyip ekrana bastıracağız.
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
main_bird_r = main_bird.get_rect(center=(100, 400))
# Variable of floor
floor_x1_pos = 0

# Variables of bird fly
bird_movement = 0
gravity = 0.25

# Pipe surface
p1 = pygame.image.load("assets/pipe-green.png").convert() # 1 image basıldı
p1 = pygame.transform.scale2x(p1).convert() # 1 image ın boyutu ayarlandı
pipe_list = [] # 1 pipeların rectangle larının listesi oluşturuldu
pipe_positions = [300,400,600] # 1 pipeların boyutlarının listesi oluşturuldu
spawnpipe = pygame.USEREVENT # 1 userevent oluşturuldu
pygame.time.set_timer(spawnpipe, 1200) # 1 userevent in timerı 1200 e ayarlandı.


def create_pipe(): # 2 pipe oluşturucu eklenip aşağıdaki timera extend ediliyor.
    random_pos = choice(pipe_positions) # random position seçiliyor
    new_pipe_r = p1.get_rect(midtop=(700,random_pos)) # alttaraftakinin rectangle ı
    new_pipe_r2 = p1.get_rect(midbottom=(700,random_pos - 200)) # üst taraftakinin rectangle ı
    return new_pipe_r,new_pipe_r2 # tuple dönderiyoruz.


def move_pipes(pipes: list) -> list: # 3 pipeları hareket ettiriyoruz ve ekranın dışında kalanları atıyoruz.
    for pipe in pipes: # pipeları hareket ettiriyoruz.
        pipe.centerx -= 5
    pipes = [pipe for pipe in pipes if pipe.right > 0] # dışında kalanları atıyoruz.
    return pipes


def draw_pipes(pipes: list): # 4 pipeları ekrana çiziyoruz.
    for pipe in pipes:
        if pipe.bottom >= 800: # eğer bottom 800 den büyükse düz çiziyoruz.
            screen.blit(p1, pipe)
        else:
            flip_pipe = pygame.transform.flip(p1,False,True) # diğer durumda ters çiziyoruz.
            screen.blit(flip_pipe,pipe)


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
        if event.type == spawnpipe:
            pipe_list.extend(create_pipe()) # 2 pipeları rectangle list e ekliyoruz.
    screen.blit(bg_surface, (0, 0))
    draw_pipes(pipe_list) # 4 ekrana pipeları çizyoruz.
    draw_floor()
    screen.blit(main_bird, main_bird_r)
    floor_x1_pos -= 1
    bird_movement += gravity
    main_bird_r.centery += bird_movement
    pipe_list = move_pipes(pipe_list) # 3 pipeları hareket etitriyoruz ve yeni pipe listesi ekliyoruz.
    if floor_x1_pos <= -567:
        floor_x1_pos = 0
    pygame.display.update()
    clock.tick(120)
