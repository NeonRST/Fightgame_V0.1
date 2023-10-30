import pygame


class Choose:
    def __init__(self, font, text, x, y):
        self.text = text
        self.font = pygame.font.Font(f"{font}", 30)
        self.surface = self.font.render(f"{text}", True, "Black")
        self.surface_rect = self.surface.get_rect(midbottom=(x, y))

    def __getitem__(self, item):
        return self.surface_rect

    def draw_menu(self, surface):
        surface.blit(self.surface, self.surface_rect)
