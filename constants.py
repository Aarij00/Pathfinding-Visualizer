import pygame

pygame.init()
# COLORS
NAVY_BLUE = (15, 35, 55)
CYAN = (101, 255, 220)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
SLATE = (136, 146, 176)
LIGHT_SLATE = (204, 214, 246)
YELLOW = (255, 245, 0)

# SIZE
SIZE = 20


START = 'A'
GOAL = 'B'
EMPTY = '.'
WALL = '#'
ROWS = 30
COLS = 60


WIDTH = 1200
HEIGHT = 800
GRID_ORIGIN_Y = 200

DEFAULT_START_X = 15
DEFAULT_START_Y = 20

DEFAULT_GOAL_X = 15
DEFAULT_GOAL_Y = 40

# FONTS
SMALL_FONT = pygame.font.Font(None, 22)
MEDIUM_FONT = pygame.font.Font(None, 8)
LARGE_FONT = pygame.font.Font(None, 60)

# ALGORITHMS
DFS = 'Depth-First Search (DFS)'
BFS = 'Breadth-First Search (BFS)'
A = 'A* Search'