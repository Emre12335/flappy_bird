# Zemin kayma efekti verme
# Zemin kayma efekti vermek için 2 tane zemin bastırdık.Yanyana şekilde
# 1.zemin -567 yi geçtiği zaman 2 zemini de eski yerine kaydırarak
# bunu sürekli tekrarladığımızda kayan zemin görüntüsü oluşuyor

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

# zemin hareketi için variable kullanacağız ama rectangle kullanmak daha mantıklı normalde
floor_x1_pos = 0


def draw_floor():
    screen.blit(ground_surface, (floor_x1_pos, 650))
    screen.blit(ground_surface, (floor_x1_pos + 567, 650))


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    screen.blit(bg_surface, (0, 0))
    draw_floor()
    floor_x1_pos -= 1
    if floor_x1_pos <= -567:
        floor_x1_pos = 0
    pygame.display.update()
    clock.tick(120)
