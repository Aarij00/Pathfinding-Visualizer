import pygame
import constants


class Menu:
    def __init__(self) -> None:
        self.x = 460
        self.y = 75
        self.width = 250
        self.height = 30
        self.default_item = 'Algorithm'
        self.current_item = self.default_item
        self.menu_items = [
                            (constants.SMALL_FONT.render(constants.DFS, False, constants.CYAN), pygame.rect.Rect(self.x, self.y+30, self.width, self.height)),
                            (constants.SMALL_FONT.render(constants.BFS, False, constants.CYAN), pygame.rect.Rect(self.x, self.y+60, self.width, self.height)),
                            (constants.SMALL_FONT.render(constants.A, False, constants.CYAN), pygame.rect.Rect(self.x, self.y+90, self.width, self.height))
                          ]
        self.expand = False
        self.rect = pygame.rect.Rect(self.x, self.y, self.width, self.height)

        self.arrow_x = self.x + self.width
        self.arrow_y = self.y
        self.arrow_width = 30
        self.arrow_height = 31
        self.arrow_rect = pygame.rect.Rect(self.arrow_x, self.arrow_y, self.arrow_width, self.arrow_height)
        self.arrow_points = [[self.arrow_x + 4, self.arrow_y + 6.5], [self.arrow_x + 25, self.arrow_y + 6.5], 
                            [self.arrow_x + 15, self.arrow_y + 23.5]]

    
    def draw(self, win: pygame.surface.Surface) -> None:
        pygame.draw.rect(win, constants.CYAN, self.rect, 2)

        self.text = constants.SMALL_FONT.render(self.current_item, False, constants.CYAN)
        win.blit(self.text, (((self.rect.x + (self.rect.w / 2)) - (self.text.get_width() / 2)), 
        ((self.rect.y + (self.rect.h / 2)) - (self.text.get_height() / 2))))

        # drawing arrow
        pygame.draw.rect(win, constants.CYAN, self.arrow_rect)
        pygame.draw.polygon(win, constants.NAVY_BLUE, self.arrow_points)

        if self.expand:
            for item in self.menu_items:
                pygame.draw.rect(win, constants.CYAN, item[1], 2)

                win.blit(item[0], (((item[1].x + (item[1].w / 2)) - (item[0].get_width() / 2)), 
                ((item[1].y + (item[1].h / 2)) - (item[0].get_height() / 2))))
    

    def setExpand(self, x: bool) -> None:
        self.expand = x
    
    def getExpand(self) -> bool:
        return self.expand
    
    def checkCollision(self, pos: tuple) -> int:
        if self.expand:
            for idx,item in enumerate(self.menu_items):
                if item[1].collidepoint(pos):
                    self.expand = False
                    if idx == 0:
                        self.current_item = constants.DFS
                    elif idx == 1:
                        self.current_item = constants.BFS
                    elif idx == 2:
                        self.current_item = constants.A
                    return idx
        return -1