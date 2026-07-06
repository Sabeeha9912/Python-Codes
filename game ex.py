import pygame
import random

# Initialize pygame
pygame.init()

# Screen setup
WIDTH,HEIGHT = 1200,600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Fireall defender: Catch the Falling Packets")

# Colors
WHITE =(255,255,255)
GREEN = (0, 255, 0)   # Safe packet
RED = (255, 0, 0)     # Malicious packet 
BLUE = (0, 0, 255)    # Player

# Player
player_width, player_height = 80, 20
player_x = WIDTH // 2 - player_width // 2
player_y = HEIGHT - player_height - 10
player_speed = 5

# Packets
packet_width, packet_height = 30, 30
packets = []
packet_speed = 3
spawn_rate = 25  # frames

# Score
score = 0
font = pygame.font.SysFont(None, 30)

# Game loop
running = True
frame_count = 0
clock = pygame.time.Clock()

while running:
    clock.tick(60)
    screen.fill(WHITE)
    
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Player movement
    keys = pygame.key.get_pressed() 
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < WIDTH - player_width:
        player_x += player_speed
    
    # Spawn packets
    frame_count += 1
    if frame_count % spawn_rate == 0:
        packet_x = random.randint(0, WIDTH - packet_width)
        color = random.choice([GREEN, RED])
        packets.append([packet_x, 0, color])
    
    # Move packets
    for packet in packets[:]:
        packet[1] += packet_speed
        pygame.draw.rect(screen, packet[2], (packet[0], packet[1], packet_width, packet_height))
        
        # Collision with player
        if (packet[1] + packet_height >= player_y) and (player_x < packet[0] + packet_width and player_x + player_width > packet[0]):
            if packet[2] == GREEN:
                score += 1
            else:
                score -= 1
            packets.remove(packet)
        # Remove if off-screen
        elif packet[1] > HEIGHT:
            packets.remove(packet)
    
    # Draw player
    pygame.draw.rect(screen, BLUE, (player_x, player_y, player_width, player_height))
    
    # Draw score
    score_text = font.render(f"Score: {score}", True, (0,0,0))
    screen.blit(score_text, (10, 10))
    
    pygame.display.flip()

pygame.quit()
