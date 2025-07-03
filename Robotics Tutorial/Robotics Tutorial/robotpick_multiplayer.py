import pygame
import random

# Initialize
pygame.init()
WIDTH, HEIGHT = 600, 600
GRID_SIZE = 60
ROWS, COLS = HEIGHT // GRID_SIZE, WIDTH // GRID_SIZE

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Advanced Robot Picking Game")
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 28)

# Colors
WHITE, BLACK, RED, GREEN, BLUE, YELLOW, GRAY = (255,255,255), (0,0,0), (255,0,0), (0,255,0), (0,0,255), (255,255,0), (100,100,100)

# Game objects
robot1 = [0, 0]
robot2 = [COLS - 1, ROWS - 1]
parts = []
obstacles = []

# Generate parts
for _ in range(8):
    x, y = random.randint(0, COLS - 1), random.randint(0, ROWS - 1)
    if [x, y] not in [robot1, robot2]:
        parts.append([x, y])

# Generate obstacles
for _ in range(10):
    x, y = random.randint(0, COLS - 1), random.randint(0, ROWS - 1)
    if [x, y] not in parts + [robot1, robot2]:
        obstacles.append([x, y])

# Game state
score1 = 0
score2 = 0
start_time = pygame.time.get_ticks()
time_limit = 60000  # 60 seconds

# Drawing functions
def draw_grid():
    for x in range(0, WIDTH, GRID_SIZE):
        pygame.draw.line(screen, BLACK, (x, 0), (x, HEIGHT))
    for y in range(0, HEIGHT, GRID_SIZE):
        pygame.draw.line(screen, BLACK, (0, y), (WIDTH, y))

def draw_robot(pos, color):
    pygame.draw.rect(screen, color, (pos[0] * GRID_SIZE, pos[1] * GRID_SIZE, GRID_SIZE, GRID_SIZE))

def draw_parts():
    for p in parts:
        pygame.draw.circle(screen, RED, (p[0] * GRID_SIZE + GRID_SIZE // 2, p[1] * GRID_SIZE + GRID_SIZE // 2), 15)

def draw_obstacles():
    for obs in obstacles:
        pygame.draw.rect(screen, GRAY, (obs[0] * GRID_SIZE, obs[1] * GRID_SIZE, GRID_SIZE, GRID_SIZE))

def draw_score_and_timer():
    time_left = max(0, (time_limit - (pygame.time.get_ticks() - start_time)) // 1000)
    screen.blit(font.render(f"Robot 1: {score1}", True, BLUE), (10, 10))
    screen.blit(font.render(f"Robot 2: {score2}", True, GREEN), (10, 40))
    screen.blit(font.render(f"Time Left: {time_left}s", True, BLACK), (400, 10))

# Movement and part picking
def move_robot(pos, dx, dy):
    new_pos = [pos[0] + dx, pos[1] + dy]
    if 0 <= new_pos[0] < COLS and 0 <= new_pos[1] < ROWS and new_pos not in obstacles:
        return new_pos
    return pos

def pick_part(robot, score):
    if robot in parts:
        parts.remove(robot)
        return score + 1
    return score

def game_over():
    screen.fill(WHITE)
    msg = f"Time's up! R1: {score1}  R2: {score2}"
    over_text = font.render(msg, True, RED)
    screen.blit(over_text, (WIDTH // 2 - 120, HEIGHT // 2))
    pygame.display.flip()
    pygame.time.wait(4000)
    pygame.quit()
    exit()

# Main loop
def main():
    global robot1, robot2, score1, score2
    running = True
    while running:
        screen.fill(WHITE)
        draw_grid()
        draw_obstacles()
        draw_parts()
        draw_robot(robot1, BLUE)
        draw_robot(robot2, GREEN)
        draw_score_and_timer()

        pygame.display.flip()
        clock.tick(10)

        if pygame.time.get_ticks() - start_time > time_limit:
            game_over()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()

        # Robot 1 (Arrow keys)
        if keys[pygame.K_LEFT]:
            robot1 = move_robot(robot1, -1, 0)
        if keys[pygame.K_RIGHT]:
            robot1 = move_robot(robot1, 1, 0)
        if keys[pygame.K_UP]:
            robot1 = move_robot(robot1, 0, -1)
        if keys[pygame.K_DOWN]:
            robot1 = move_robot(robot1, 0, 1)

        # Robot 2 (WASD keys)
        if keys[pygame.K_a]:
            robot2 = move_robot(robot2, -1, 0)
        if keys[pygame.K_d]:
            robot2 = move_robot(robot2, 1, 0)
        if keys[pygame.K_w]:
            robot2 = move_robot(robot2, 0, -1)
        if keys[pygame.K_s]:
            robot2 = move_robot(robot2, 0, 1)

        # Part picking
        if keys[pygame.K_SPACE]:
            score1 = pick_part(robot1, score1)
        if keys[pygame.K_RETURN]:
            score2 = pick_part(robot2, score2)

    pygame.quit()

if __name__ == "__main__":
    main()
