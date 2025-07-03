import pygame
import random

# Initialize Pygame
pygame.init()
WIDTH, HEIGHT = 600, 600
GRID_SIZE = 60
ROWS, COLS = HEIGHT // GRID_SIZE, WIDTH // GRID_SIZE

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Robot Picking Parts")
clock = pygame.time.Clock()

# Colors
WHITE, BLACK, RED, GREEN, BLUE = (255, 255, 255), (0, 0, 0), (255, 0, 0), (0, 255, 0), (0, 0, 255)

# Robot initial position
robot_pos = [0, 0]

# Randomly place parts
parts = []
for _ in range(5):
    x = random.randint(0, COLS - 1)
    y = random.randint(0, ROWS - 1)
    if [x, y] != robot_pos:
        parts.append([x, y])

# Score tracking
score = 0
font = pygame.font.SysFont(None, 36)

# Draw the grid lines
def draw_grid():
    for x in range(0, WIDTH, GRID_SIZE):
        pygame.draw.line(screen, BLACK, (x, 0), (x, HEIGHT))
    for y in range(0, HEIGHT, GRID_SIZE):
        pygame.draw.line(screen, BLACK, (0, y), (WIDTH, y))

# Draw robot as a blue square
def draw_robot():
    pygame.draw.rect(screen, BLUE, (robot_pos[0] * GRID_SIZE, robot_pos[1] * GRID_SIZE, GRID_SIZE, GRID_SIZE))

# Draw parts as red circles
def draw_parts():
    for part in parts:
        pygame.draw.circle(screen, RED, (part[0] * GRID_SIZE + GRID_SIZE // 2, part[1] * GRID_SIZE + GRID_SIZE // 2), 15)

# Display picked part count
def draw_score():
    text = font.render(f"Picked: {score}", True, BLACK)
    screen.blit(text, (10, 10))

# Check and pick part
def pick_part():
    global score
    if robot_pos in parts:
        parts.remove(robot_pos)
        score += 1

# Main game loop
def main():
    running = True
    while running:
        screen.fill(WHITE)
        draw_grid()
        draw_robot()
        draw_parts()
        draw_score()

        pygame.display.flip()
        clock.tick(10)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # User control
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and robot_pos[0] > 0:
            robot_pos[0] -= 1
        if keys[pygame.K_RIGHT] and robot_pos[0] < COLS - 1:
            robot_pos[0] += 1
        if keys[pygame.K_UP] and robot_pos[1] > 0:
            robot_pos[1] -= 1
        if keys[pygame.K_DOWN] and robot_pos[1] < ROWS - 1:
            robot_pos[1] += 1
        if keys[pygame.K_SPACE]:
            pick_part()

    pygame.quit()

if __name__ == "__main__":
    main()

