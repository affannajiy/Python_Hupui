import pygame
import math
pygame.init()
screen = pygame.display.set_mode((1500, 800))
pygame.display.set_caption("Differential Drive Robot")
clock = pygame.time.Clock()
x, y = 300, 300
angle = 0
speed = 0
angular_speed = 0
running = True
while running:
    screen.fill((255, 255, 255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        speed = 50
    elif keys[pygame.K_DOWN]:
        speed = -50
    else:
        speed = 0
    if keys[pygame.K_LEFT]:
        angular_speed = -0.05
    elif keys[pygame.K_RIGHT]:
        angular_speed = 0.05
    else:
        angular_speed = 0
    angle += angular_speed
    x += speed * math.cos(angle)
    y += speed * math.sin(angle)
    pygame.draw.circle(screen, (0, 0, 255), (int(x), int(y)), 10)
    pygame.draw.line(screen, (255, 0, 0), (x, y), (x + 20 * math.cos(angle), y + 20 * math.sin(angle)), 2)
    pygame.display.flip()
    clock.tick(30)

    # Add inside Pygame loop
    pygame.draw.line(screen, (0, 0, 0), (0, 300), (600, 300), 5)
    sensor_x = int(x + 10 * math.cos(angle))
    sensor_y = int(y + 10 * math.sin(angle))
    try:
        color = screen.get_at((sensor_x, sensor_y))
        if color == (0, 0, 0, 255):
            speed = 2
        else:
            angular_speed = 0.05
    except:
      pass
pygame.quit()