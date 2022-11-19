import pygame 
import constants, random

class Cell:
    def __init__(self, row, col, color) -> None:
        self.row = row
        self.col = col
        self.value = constants.EMPTY

        self.size = constants.SIZE
        self.x = self.col * self.size
        self.y = (self.row * self.size) + 200
        self.color = color

        self.start_node = False
        self.goal_node = False
        self.wall = False
        self.explored = False
        self.solution = False

        self.rect = pygame.rect.Rect(self.x, self.y, self.size, self.size)


    def getWall(self) -> bool:
        return self.wall

    def setWall(self) -> None:
        if not self.start_node and not self.goal_node:
            self.value = constants.WALL
            self.wall = True
            self.color = constants.SLATE


    def getEmpty(self) -> bool:
        return self.value == constants.EMPTY

    def setEmpty(self) -> None:
        if not self.start_node and not self.goal_node:
            self.value = constants.EMPTY
            self.color = constants.CYAN
            self.wall = False
            self.explored = False
            self.solution = False


    def getStart(self) -> bool:
        return self.start_node

    def setStart(self) -> None:
        self.value = constants.START
        self.wall = False
        self.color = constants.GREEN
        self.start_node = True
        self.goal_node = False


    def getGoal(self) -> bool:
        return self.goal_node

    def setGoal(self) -> None:
        self.value = constants.GOAL
        self.wall = False
        self.color = constants.RED
        self.goal_node = True
        self.start_node = False
    

    def getExplored(self) -> bool:
        return self.explored

    def setExplored(self) -> None:
        if not self.start_node and not self.goal_node:
            self.color = constants.LIGHT_SLATE
        self.explored = True


    def getSolution(self) -> bool:
        return self.solution

    def setSolution(self) -> None:
        if not self.start_node and not self.goal_node:
            self.color = constants.YELLOW
        self.solution = True


    def draw(self, win) -> None:
        if any([self.start_node, self.goal_node, self.wall, self.explored, self.solution]):
            pygame.draw.rect(win, self.color, self.rect)
        else:
            pygame.draw.rect(win, self.color, self.rect, 1)