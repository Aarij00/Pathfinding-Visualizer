import pygame, sys
from main import Maze
import constants
from menu import Menu


pygame.init()





screen = pygame.display.set_mode((constants.WIDTH, constants.HEIGHT))
pygame.display.set_caption("Path Visualizer")

# toolbar options
start_button_text = constants.SMALL_FONT.render('START', False, constants.CYAN)
start_button_rect = pygame.rect.Rect(210, 75, 100, 30)

clear_button_text = constants.SMALL_FONT.render('CLEAR', False, constants.CYAN)
clear_button_rect = pygame.rect.Rect(890, 75, 100, 30)


def draw_toolbar(win: pygame.surface.Surface, menu) -> None:
    pygame.draw.line(win, constants.CYAN, (0, 0), (constants.WIDTH, 0), 3)                                              # TOP
    pygame.draw.line(win, constants.CYAN, (0, constants.GRID_ORIGIN_Y), (constants.WIDTH, constants.GRID_ORIGIN_Y))     # BOTTOM
    pygame.draw.line(win, constants.CYAN, (0, 0), (0, constants.GRID_ORIGIN_Y))                                         # LEFT
    pygame.draw.line(win, constants.CYAN, (constants.WIDTH, 0), (constants.WIDTH, constants.GRID_ORIGIN_Y), 3)          # RIGHT

    pygame.draw.rect(win, constants.CYAN, start_button_rect, 2)
    win.blit(start_button_text, (((start_button_rect.x + (start_button_rect.w / 2)) - (start_button_text.get_width() / 2)), 
    ((start_button_rect.y + (start_button_rect.h / 2)) - (start_button_text.get_height() / 2))))

    pygame.draw.rect(win, constants.CYAN, clear_button_rect, 2)
    win.blit(clear_button_text, (((clear_button_rect.x + (clear_button_rect.w / 2)) - (clear_button_text.get_width() / 2)), 
    ((clear_button_rect.y + (clear_button_rect.h / 2)) - (clear_button_text.get_height() / 2))))

    menu.draw(win)

def draw_grid(win: pygame.surface.Surface, maze: Maze) -> None:
    for row in range(maze.height):
        for col in range(maze.width):
            maze.grid[row][col].draw(win)
    draw_gridlines(win)
    

def draw_gridlines(win: pygame.surface.Surface) -> None:
    for r in range(constants.ROWS):
        pygame.draw.line(win, constants.CYAN, (0, (constants.GRID_ORIGIN_Y + (r*constants.SIZE))), (constants.WIDTH, (constants.GRID_ORIGIN_Y + (r*constants.SIZE))))
        for c in range(constants.COLS):
            pygame.draw.line(win, constants.CYAN, (c*constants.SIZE, constants.GRID_ORIGIN_Y), (c*constants.SIZE, constants.HEIGHT))
    
    pygame.draw.line(win, constants.CYAN, (0, (constants.GRID_ORIGIN_Y + (constants.ROWS*constants.SIZE))), (constants.WIDTH, (constants.GRID_ORIGIN_Y + (constants.ROWS*constants.SIZE))), 3)
    pygame.draw.line(win, constants.CYAN, (constants.COLS*constants.SIZE, constants.GRID_ORIGIN_Y), (constants.COLS*constants.SIZE, constants.HEIGHT), 3)


def runAlgo(win: pygame.surface.Surface, maze: Maze, menu) -> None:
    for row in range(maze.height):
        for col in range(maze.width):
            cell = maze.grid[row][col]
            if cell.getExplored():
                cell.setEmpty()
    maze.solve(lambda: draw_window(win, maze, menu), clock, menu)


def draw_window(win: pygame.surface.Surface, m: Maze, menu: Menu) -> None:
    win.fill(constants.NAVY_BLUE)
    draw_toolbar(win, menu)
    draw_grid(win, m)


def clearGrid(maze: Maze) -> None:
    for row in range(maze.height):
        for col in range(maze.width):
            cell = maze.grid[row][col]
            if not cell.getStart() and not cell.getGoal():
                cell.setEmpty()


def makeWallDrag(wallDrag, maze):
    if wallDrag:
        x, y = get_clicked_cell(pygame.mouse.get_pos())
        if 0 <= x <= (constants.COLS - 1) and 0 <= y <= (constants.ROWS - 1): 
            cell = maze.grid[y][x]
            if cell.getEmpty():
                cell.setWall()


def makeWallClick(maze):
    x, y = get_clicked_cell(pygame.mouse.get_pos())
    if 0 <= x <= (constants.COLS - 1) and 0 <= y <= (constants.ROWS - 1): 
        cell = maze.grid[y][x]
        if cell.getEmpty():
            cell.setWall()
        else:
            cell.setEmpty()
    
wallDrag = False
def handle_event(win: pygame.surface.Surface, e: pygame.event.Event, maze: Maze, menu: Menu) -> None:
    global wallDrag
    if e.type == pygame.MOUSEBUTTONDOWN:
        if e.button == 1:
            menu.checkCollision(e.pos)
            if start_button_rect.collidepoint(e.pos):
                runAlgo(win, maze, menu)
            elif clear_button_rect.collidepoint(e.pos):
                clearGrid(maze)
            elif menu.arrow_rect.collidepoint(e.pos):
                menu.setExpand(not menu.getExpand())
                # maze.algorithm = menu.checkCollision(e.pos)
                # print(maze.algorithm)
            else:
                wallDrag = True
                makeWallClick(maze)
    elif e.type == pygame.MOUSEBUTTONUP:
        wallDrag = False
    elif e.type == pygame.MOUSEMOTION:
        makeWallDrag(wallDrag, maze)
    

def get_clicked_cell(pos: tuple[int, int]) -> tuple[int, int]:
    x, y = pos
    new_x = x // constants.SIZE
    new_y = (y - constants.GRID_ORIGIN_Y) // constants.SIZE
    return new_x, new_y


myMaze = Maze()
menu = Menu()
running = True
clock = pygame.time.Clock()
while running:
    if myMaze.running == False and myMaze.solution is None:
        print("*** NO SOLUTION ***")
        running = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        handle_event(screen, event, myMaze, menu)
    draw_window(screen, myMaze, menu)

    pygame.display.update()

sys.exit()