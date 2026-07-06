import pygame
import random

pygame.init()
WIDTH, HEIGHT = 1000, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))

bg = pygame.transform.scale(pygame.image.load('background.png'), (WIDTH, HEIGHT))

player_img = pygame.transform.scale(pygame.image.load('player_icon.png'), (60, 60))
img_safe = pygame.transform.scale(pygame.image.load('safe_icon.png'), (40, 40))
img_virus = pygame.transform.scale(pygame.image.load('virus_icon.png'), (40, 40))
img_unknown = pygame.transform.scale(pygame.image.load('unknown_icon.png'), (40, 40))
packet_choices = [img_safe, img_virus, img_unknown]


player_x = WIDTH // 2
player_y = HEIGHT - 80
packets = []  # Packet list

running = True
clock = pygame.time.Clock()

while running:
    screen.blit(bg, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]: player_x -= 5
    if keys[pygame.K_RIGHT]: player_x += 5
    screen.blit(player_img, (player_x, player_y))
    if random.randint(1, 30) == 1:
        x_pos = random.randint(0, WIDTH - 40)
        chosen_img = random.choice(packet_choices)
        packets.append([pygame.Rect(x_pos, -40, 40, 40), chosen_img])
    for pkt in packets:
        pkt[0].y += 4
        screen.blit(pkt[1], pkt[0])
    pygame.display.flip()
    clock.tick(60)
pygame.quit()