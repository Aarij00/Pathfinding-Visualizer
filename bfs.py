# from main import Maze, Node
import constants
import pygame

class Node:
    def __init__(self, state, parent, action) -> None:
        self.state = state
        self.parent = parent
        self.action = action

class Stack():
    def __init__(self):
        self.frontier = []

    def add(self, node):
        self.frontier.append(node)

    def contains_state(self, state):
        return any(node.state == state for node in self.frontier)

    def empty(self):
        return len(self.frontier) == 0

    def remove(self):
        if self.empty():
            raise Exception("empty frontier")
        else:
            node = self.frontier[-1]
            self.frontier = self.frontier[:-1]
            return node

class BFS:
    def __init__(self) -> None:
        pass

    def solve(self, maze, draw, clock, menu):
        maze.searching = True

        self.num_explored = 0

        start = Node(state=maze.start, parent=None, action=None)
        frontier = Stack()
        frontier.add(start)

        self.explored = set()

        running = True
        while running:

            # If nothing left in frontier, then no path
            if frontier.empty():
                print("*** NO SOLUTION ***")
                running = False

            # Choose a node from the frontier
            node = frontier.remove()
            x,y = node.state
            maze.grid[x][y].setExplored()


            self.num_explored += 1

            # If node is the goal, then we have a solution
            if node.state == maze.goal:
                self.solution = []
                while node.parent is not None:
                    self.solution.append(node.action)
                    node = node.parent
                    x,y = node.state
                    maze.grid[x][y].setSolution()

                self.solution.reverse()
                return

            # Mark node as explored
            self.explored.add(node.state)

            # Add neighbors to frontier
            for action, state in maze.neighbors(node.state):
                if not frontier.contains_state(state) and state not in self.explored:
                    child = Node(state=state, parent=node, action=action)
                    frontier.add(child)
            draw()
            pygame.display.flip()
            pygame.event.pump()
            clock.tick(500)
        maze.searching = False