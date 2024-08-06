import pygame
import circles

pygame.init()
pygame.display.set_caption("Bezier Curves")
screen = pygame.display.set_mode((500,500))
screen.fill((0,0,0))
running = True

circles_group = []

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            for c in circles_group:
                if c.collide(pos):
                    break
            else:
                circles_group.append(circles.Circle(pos[0], pos[1]))
    
    screen.fill((0,0,0))
    for c in circles_group:
        c.update(False, pygame.mouse)
        c.draw(screen)

    if len(circles_group) > 1:
        circles.draw_Bezier(screen, circles_group)

    pygame.display.update()