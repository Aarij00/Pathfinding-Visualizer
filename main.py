from cell import Cell
import constants
from bfs import BFS
from dfs import DFS
from a_star import AStar


class Maze:
    def __init__(self) -> None:
        self.grid = [[Cell(r, c, constants.CYAN) for c in range(constants.COLS)] for r in range(constants.ROWS)]

        self.grid[constants.DEFAULT_START_X][constants.DEFAULT_START_Y].setStart()
        self.grid[constants.DEFAULT_GOAL_X][constants.DEFAULT_GOAL_Y].setGoal()

        self.start = (constants.DEFAULT_START_X, constants.DEFAULT_START_Y)
        self.goal = (constants.DEFAULT_GOAL_X, constants.DEFAULT_GOAL_Y)

        self.height = len(self.grid) # rows
        self.width = len(self.grid[0]) # columns
        self.solution = None
        self.algorithm = -1
        self.running = True
        self.searching = False

    def getStartState(self):
        return tuple(reversed(self.start))

    def setStartState(self, newStart):
        self.start = newStart

    def getGoalState(self):
        return tuple(reversed(self.goal))

    def setGoalState(self, newGoal):
        self.goal = newGoal
    
    def neighbors(self, state):
        row, col = state
        candidates = [
            ("up", (row - 1, col)),
            ("down", (row + 1, col)),
            ("left", (row, col - 1)),
            ("right", (row, col + 1))
        ]

        result = []
        for action, (r, c) in candidates:
            if 0 <= r < self.height and 0 <= c < self.width and self.grid[r][c].value != constants.WALL:
                result.append((action, (r, c)))
        return result

    def solve(self, draw, clock ,menu):
        self.algorithm = {constants.DFS: 0, constants.BFS: 1, constants.A: 2}[menu.current_item]
        if self.algorithm == 1:
            DFS().solve(self, draw, clock, menu)
        elif self.algorithm == 0:
            BFS().solve(self, draw, clock, menu)
        elif self.algorithm == 2:
            AStar().solve(self, draw, clock, menu)
