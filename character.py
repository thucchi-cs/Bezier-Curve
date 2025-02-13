import pygame

class Character(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("key.png")
        # self.image = pygame.transform.flip(self.image, True, False)
        self.image = pygame.transform.scale(self.image, (25,25))
        self.rect = self.image.get_rect()
        self.rect.x = 200
        self.rect.y = 200
        self.pos = 0
        self.following = False
        
    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))
    
    def follow(self, path):
        if self.following:
            if self.pos < len(path):
                self.rect.centerx = path[self.pos][0]
                self.rect.centery = path[self.pos][1]
                self.pos += 1
            else:
                self.following = False
                self.pos = 0