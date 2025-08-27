import pygame
import noise
import random

# -----------------------------
# Initialize Pygame
# -----------------------------
pygame.init()

WIDTH, HEIGHT = 500, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("2D Sandbox Game Prototype")

# -----------------------------
# World / Tile Parameters
# -----------------------------
CHUNK_SIZE = 100      # pixels per chunk
TILE_SIZE = 10        # pixels per tile
TILES_PER_CHUNK = CHUNK_SIZE // TILE_SIZE

SCALE = 100.0
OCTAVES = 6
PERSISTENCE = 0.5
LACUNARITY = 2.0
TREE_CHANCE = 0.02

# Rare crimson rectangles
RARE_RED_CHANCE = 0.002
RARE_RED_MIN_SIZE = 10
RARE_RED_MAX_SIZE = 50
CRIMSON = (220, 20, 60)

# Player
player_x, player_y = 250, 250  # world coordinates
player_speed = 5
PLAYER_COLOR = (255, 0, 255)
PLAYER_SIZE = TILE_SIZE

# Camera
camera_x, camera_y = 0, 0

# -----------------------------
# Biome Color Function
# -----------------------------
def get_biome_color(height_val, river_val, desert_val):
    if abs(river_val - 0.5) < 0.05:
        return (0, 0, 255)  # river
    if desert_val > 0.7 and height_val > 0.35:
        return (238, 214, 175)  # desert
    if height_val < 0.2: return (0,0,150)  # deep ocean
    elif height_val < 0.3: return (0,0,255)  # shallow ocean
    elif height_val < 0.35: return (238,214,175)  # beach
    elif height_val < 0.5: return (124,252,0)  # plains
    elif height_val < 0.6: return (34,139,34)  # forest
    elif height_val < 0.65: return (0,100,0)  # jungle
    elif height_val < 0.75: return (139,69,19)  # hills
    elif height_val < 0.85: return (139,137,137)  # mountains
    else: return (255,250,250)  # snow

# -----------------------------
# Add Rare Crimson Rectangle
# -----------------------------
def add_rare_crimson(surface):
    if random.random() < RARE_RED_CHANCE:
        max_w = min(RARE_RED_MAX_SIZE, CHUNK_SIZE)
        max_h = min(RARE_RED_MAX_SIZE, CHUNK_SIZE)
        rect_w = random.randint(RARE_RED_MIN_SIZE, max_w)
        rect_h = random.randint(RARE_RED_MIN_SIZE, max_h)
        start_x = random.randint(0, CHUNK_SIZE - rect_w)
        start_y = random.randint(0, CHUNK_SIZE - rect_h)
        pygame.draw.rect(surface, CRIMSON, (start_x, start_y, rect_w, rect_h))

# -----------------------------
# Generate Chunk
# -----------------------------
def generate_chunk(chunk_x, chunk_y):
    surface = pygame.Surface((CHUNK_SIZE, CHUNK_SIZE))
    for x in range(CHUNK_SIZE):
        for y in range(CHUNK_SIZE):
            world_x = chunk_x * CHUNK_SIZE + x
            world_y = chunk_y * CHUNK_SIZE + y

            nx, ny = world_x / SCALE, world_y / SCALE

            # Terrain height
            height_val = noise.pnoise2(nx, ny, octaves=OCTAVES, persistence=PERSISTENCE,
                                       lacunarity=LACUNARITY, repeatx=999999, repeaty=999999, base=0)
            height_val = height_val / 2 + 0.5

            # River
            river_val = noise.pnoise2(nx*0.01, ny*0.01, octaves=4, persistence=0.5, lacunarity=2.0,
                                      repeatx=999999, repeaty=999999, base=1)
            river_val = river_val / 2 + 0.5

            # Desert
            desert_val = noise.pnoise2(nx*0.05, ny*0.05, octaves=3, persistence=0.5, lacunarity=2.0,
                                       repeatx=999999, repeaty=999999, base=2)
            desert_val = desert_val / 2 + 0.5

            color = get_biome_color(height_val, river_val, desert_val)
            surface.set_at((x, y), color)

            # Trees
            if color in [(34,139,34),(0,100,0)] and random.random() < TREE_CHANCE:
                surface.set_at((x, y-1 if y>0 else y), (0,50,0))
                surface.set_at((x, y), (139,69,19))

    add_rare_crimson(surface)
    return surface

# -----------------------------
# Chunk Dictionary
# -----------------------------
chunks = {}

# -----------------------------
# Main Game Loop
# -----------------------------
running = True
clock = pygame.time.Clock()

while running:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Player movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]: player_x -= player_speed
    if keys[pygame.K_RIGHT]: player_x += player_speed
    if keys[pygame.K_UP]: player_y -= player_speed
    if keys[pygame.K_DOWN]: player_y += player_speed

    # Camera follows player
    camera_x = player_x - WIDTH // 2
    camera_y = player_y - HEIGHT // 2

    # Determine visible chunks
    start_chunk_x = camera_x // CHUNK_SIZE
    start_chunk_y = camera_y // CHUNK_SIZE
    end_chunk_x = (camera_x + WIDTH) // CHUNK_SIZE + 1
    end_chunk_y = (camera_y + HEIGHT) // CHUNK_SIZE + 1

    screen.fill((0,0,0))

    # Draw visible chunks
    for cx in range(start_chunk_x, end_chunk_x):
        for cy in range(start_chunk_y, end_chunk_y):
            if (cx, cy) not in chunks:
                chunks[(cx, cy)] = generate_chunk(cx, cy)
            screen.blit(chunks[(cx, cy)], (cx*CHUNK_SIZE - camera_x, cy*CHUNK_SIZE - camera_y))

    # Draw player on top
    pygame.draw.rect(screen, PLAYER_COLOR, (player_x - camera_x, player_y - camera_y, PLAYER_SIZE, PLAYER_SIZE))

    pygame.display.flip()

pygame.quit()
