import pygame
import circles
import character

pygame.init()
pygame.display.set_caption("Bezier Curves")
screen = pygame.display.set_mode((500,500))
screen.fill((0,0,0))
running = True

thing = character.Character()

circles_group = []
path = []
clock = pygame.time.Clock()

while running:
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                thing.following = True
            if event.key == pygame.K_q:
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
        path = circles.draw_Bezier(screen, circles_group)
    
    thing.follow(path)
    thing.draw(screen)

    pygame.display.update()
    
print(path)