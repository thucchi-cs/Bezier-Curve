import pygame

class Circle:
    def __init__(self, x, y):
        super().__init__()
        self.x = x
        self.y = y
        self.rad = 5
        self.drag = False
    
    def draw(self, screen):
        pygame.draw.circle(screen, (255,0,0), (self.x, self.y), self.rad)

    def collide(self, pos):
        self.drag = ((((pos[0] - self.x) ** 2) + ((pos[1] - self.y) ** 2)) **0.5) <= self.rad
        return self.drag

    def update(self, pressed, mouse):
        if self.drag:
            if not mouse.get_pressed()[0]:
                self.drag = False
                return
            self.x, self.y = mouse.get_pos()


def draw_Bezier(screen, circles_group):
    t = 0
    path = []
    while t <= 1:
        x = [i.x for i in circles_group]
        y = [i.y for i in circles_group]
        posX = calc_Bezier(x, t, 1, len(x)-1)
        posY = calc_Bezier(y, t, 1, len(y)-1)
        pygame.draw.circle(screen, (255,255,255), (posX, posY), 2.5)
        path.append((posX, posY))
        t += 0.025
    return path

def calc_Bezier(circles_group, t, k, count):
    power = len(circles_group)-1 - count
    if count <= 0:
        return ((1-t)**power)*circles_group[0]
    else:
        return calc_Bezier(circles_group, t, len(circles_group) -1 , count-1) + ((k*(1-t)**power)*(t**count)*circles_group[count])

