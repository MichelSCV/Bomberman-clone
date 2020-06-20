import pygame
import os


class Mapa(pygame.sprite.Sprite):


    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join(\
            'assets/fase', 'mapa1.png')).convert()
        self.image = pygame.transform.scale(self.image,(800, 600))
        self.rect = self.image.get_rect()


    # Adiciona e remove sprites de um grupo.        
    def mapa_sprite(self, window):
        select_mapa = pygame.sprite.Group()
        select_mapa.add(self)
        select_mapa.update()
        select_mapa.draw(window)
        select_mapa.empty()
