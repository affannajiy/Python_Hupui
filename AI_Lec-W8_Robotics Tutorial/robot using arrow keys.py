import pygame
import math

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Robot with Obstacle and Line Following")
clock = pygame.time.Clock()

# Robot initial state
x, y = 300, 300
angle = 0
speed = 0
angular_speed = 0
manual_mode = True  # Start in manual mode

# Main loop
running = True
while running:
    screen.fill((255, 255, 255))  # Clear screen

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Toggle between manual and line-follow mode (press spacebar)
    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
        manual_mode = not manual_mode
        pygame.time.wait(300)  # debounce

    # Controls
    if manual_mode:
        if keys[pygame.K_UP]:
            speed = 2
        elif keys[pygame.K_DOWN]:
            speed = -2
        else:
            speed = 0

        if keys[pygame.K_LEFT]:
            angular_speed = -0.05
        elif keys[pygame.K_RIGHT]:
            angular_speed = 0.05
        else:
            angular_speed = 0
    else:
        # Line following mode
        sensor_x = int(x + 10 * math.cos(angle))
        sensor_y = int(y + 10 * math.sin(angle))
        if 0 <= sensor_x < 600 and 0 <= sensor_y < 600:
            color = screen.get_at((sensor_x, sensor_y))
            if color[:3] == (0, 0, 0):  # Black line
                speed = 2
                angular_speed = 0
            else:
                speed = 0
                angular_speed = 0.05

    # Update robot pose
    angle += angular_speed
    x += speed * math.cos(angle)
    y += speed * math.sin(angle)

    # Obstacle
    obstacle = pygame.Rect(200, 200, 50, 50)
    pygame.draw.rect(screen, (0, 0, 0), obstacle)

    # Line to follow
    pygame.draw.line(screen, (0, 0, 0), (100, 400), (500, 400), 5)

    # Collision detection
    robot_rect = pygame.Rect(x - 10, y - 10, 20, 20)
    if robot_rect.colliderect(obstacle):
        print("Collision Detected!")
        speed = 0

    # Draw robot
    pygame.draw.circle(screen, (0, 0, 255), (int(x), int(y)), 10)
    pygame.draw.line(
        screen, (255, 0, 0),
        (x, y),
        (x + 20 * math.cos(angle), y + 20 * math.sin(angle)), 2
    )

    pygame.display.flip()
    clock.tick(30)

pygame.quit()

