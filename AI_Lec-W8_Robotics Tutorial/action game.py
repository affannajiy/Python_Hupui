import pygame
import random

'''
Game Controls

Move: WASD
Shoot: Space
'''

# Initialize
pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Advanced Shooting Game")
clock = pygame.time.Clock()

# Colors
WHITE, BLACK, RED, GREEN, BLUE, YELLOW = (255,255,255), (0,0,0), (255,0,0), (0,255,0), (0,0,255), (255,255,0)

# Load sounds (place these .wav files in your game folder)
#shoot_sound = pygame.mixer.Sound("shoot.wav.wav")
#hit_sound = pygame.mixer.Sound("hit.wav.wav")

# Player setup
player_width, player_height = 60, 20
player_x = WIDTH // 2 - player_width // 2
player_y = HEIGHT - 40
player_speed = 7
player_health = 3

# Bullet setup
bullets = []
bullet_speed = 10
multi_shot = False
multi_shot_timer = 0

# Enemy setup
enemies = []
enemy_width, enemy_height = 50, 20
enemy_speed = 3
enemy_spawn_delay = 40
spawn_timer = 0

# Power-ups
powerups = []
powerup_types = ["health", "multi"]
powerup_spawn_timer = 0

# Game state
score = 0
level = 1
font = pygame.font.SysFont(None, 36)

# Drawing functions
def draw_player():
    pygame.draw.rect(screen, GREEN, (player_x, player_y, player_width, player_height))

def draw_bullets():
    for bullet in bullets:
        pygame.draw.rect(screen, RED, (bullet[0], bullet[1], 5, 10))

def draw_enemies():
    for enemy in enemies:
        pygame.draw.rect(screen, BLACK, (enemy[0], enemy[1], enemy_width, enemy_height))

def draw_powerups():
    for p in powerups:
        color = BLUE if p[2] == "multi" else YELLOW
        pygame.draw.rect(screen, color, (p[0], p[1], 20, 20))

def draw_ui():
    screen.blit(font.render(f"Health: {player_health}", True, RED), (10, 10))
    screen.blit(font.render(f"Score: {score}", True, BLACK), (10, 40))
    screen.blit(font.render(f"Level: {level}", True, BLACK), (WIDTH - 150, 10))

# Movement and game logic
def move_bullets():
    for bullet in bullets[:]:
        bullet[1] -= bullet_speed
        if bullet[1] < 0:
            bullets.remove(bullet)

def move_enemies():
    global player_health
    for enemy in enemies[:]:
        enemy[1] += enemy_speed
        if enemy[1] > HEIGHT:
            game_over()
        for bullet in bullets[:]:
            if (enemy[0] < bullet[0] < enemy[0] + enemy_width) and (enemy[1] < bullet[1] < enemy[1] + enemy_height):
                enemies.remove(enemy)
                bullets.remove(bullet)
                #hit_sound.play()
                update_score()
                break

def move_powerups():
    global player_health, multi_shot, multi_shot_timer
    for p in powerups[:]:
        p[1] += 2
        if player_x < p[0] < player_x + player_width and player_y < p[1] < player_y + player_height:
            if p[2] == "health":
                player_health += 1
            elif p[2] == "multi":
                multi_shot = True
                multi_shot_timer = 300
            powerups.remove(p)
        elif p[1] > HEIGHT:
            powerups.remove(p)

def update_score():
    global score, level, enemy_speed, enemy_spawn_delay
    score += 1
    if score % 10 == 0:
        level += 1
        enemy_speed += 1
        enemy_spawn_delay = max(10, enemy_spawn_delay - 5)

def spawn_enemy():
    x = random.randint(0, WIDTH - enemy_width)
    enemies.append([x, 0])

def spawn_powerup():
    x = random.randint(20, WIDTH - 40)
    ptype = random.choice(powerup_types)
    powerups.append([x, 0, ptype])

def game_over():
    screen.fill(WHITE)
    over_text = font.render("GAME OVER", True, RED)
    screen.blit(over_text, (WIDTH // 2 - 100, HEIGHT // 2))
    pygame.display.flip()
    pygame.time.wait(3000)
    pygame.quit()
    exit()

# Main loop
def main():
    global player_x, spawn_timer, powerup_spawn_timer, multi_shot, multi_shot_timer
    running = True

    while running:
        screen.fill(WHITE)
        draw_player()
        draw_bullets()
        draw_enemies()
        draw_powerups()
        draw_ui()

        move_bullets()
        move_enemies()
        move_powerups()

        # Spawn enemies
        spawn_timer += 1
        if spawn_timer >= enemy_spawn_delay:
            spawn_enemy()
            spawn_timer = 0

        # Spawn powerups
        powerup_spawn_timer += 1
        if powerup_spawn_timer >= 300:
            spawn_powerup()
            powerup_spawn_timer = 0

        # Multi-shot timing
        if multi_shot:
            multi_shot_timer -= 1
            if multi_shot_timer <= 0:
                multi_shot = False

        pygame.display.flip()
        clock.tick(60)

        # Input
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player_x > 0:
            player_x -= player_speed
        if keys[pygame.K_RIGHT] and player_x < WIDTH - player_width:
            player_x += player_speed
        if keys[pygame.K_SPACE]:
            if not bullets or bullets[-1][1] < player_y - 20:
                bullets.append([player_x + player_width // 2, player_y])
                if multi_shot:
                    bullets.append([player_x + 10, player_y])
                    bullets.append([player_x + player_width - 10, player_y])
                #shoot_sound.play()

    pygame.quit()

if __name__ == "__main__":
    main()