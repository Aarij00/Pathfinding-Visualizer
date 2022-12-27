from bfs import Stack, Node
import pygame

class AStarNode(Node):
    def __init__(self, state, parent, action, g, h) -> None:
        super().__init__(state, parent, action)
        self.g = g
        self.h = h
        self.f = self.g + self.h

class AStarStack(Stack):
    def __init__(self):
        super().__init__()

class AStar:
    def __init__(self) -> None:
        pass

    def getH(self, cur, maze):
        x1,y1 = cur
        x2,y2 = maze.goal
        return abs(x1 - x2) + abs(y1 - y2)

    def solve(self, maze, draw, clock, menu):
        maze.searching = True

        self.num_explored = 0

        sh = self.getH(maze.start, maze)
        start = AStarNode(state=maze.start, parent=None, action=None, g=0, h=sh)
        frontier = Stack()
        frontier.add(start)

        self.explored = set()

        running = True
        while running:
            # If nothing left in frontier, then no path
            if frontier.empty():
                running = False

            # Choose a node from the frontier
            node = frontier.remove()
            if not node:
                running = False
                break
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
            scores = []
            for action, state in maze.neighbors(node.state):
                if not frontier.contains_state(state) and state not in self.explored:
                    th = self.getH(state, maze)
                    child = AStarNode(state=state, parent=node, action=action, g=node.g+1, h=th)
                    scores.append(child)
            # get everything that is in stack
            while not frontier.empty():
                scores.append(frontier.remove())

            scores.sort(key=lambda x: x.f, reverse=True)

            # put everything back in stack
            for i in scores:
                frontier.add(i)

            draw()
            pygame.display.flip()
            pygame.event.pump()
            clock.tick(500)
        maze.searching = False
        maze.running = False
