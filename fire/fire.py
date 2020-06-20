import pygame
import os
from players import player

class Fire(pygame.sprite.Sprite):
    def __init__(self, explode_group, id=None, rotate:bool=False, x: int=0, y: int=0,
                                     scalex=150, scaley=50, path='fires'):
        pygame.sprite.Sprite.__init__(self)
        self.rotate = rotate
        self.id = id
        if not self.rotate: 
            self.play = pygame.mixer.Sound(os.path.join('sounds', 'cannon.wav'))
            self.play.set_volume(0.1)
            self.play.play()
        self.x = x
        self.y = y
        self.scale_x = scalex
        self.scale_y = scaley
        self.path = path
        self.list_dir = []
        self.person_ani = {}
        self.dir_ani = os.listdir(f'assets/{self.path}')
        self.add_to_list_dir()
        self.add_to_person_ani()
        self.image = self.person_ani[self.list_dir[0]][0]
        #self.select_bomb = pygame.sprite.Group()
        self.frame = 0
        self.last_update = pygame.time.get_ticks()
        self.frame_rate = 80
        self.var = 0
        self.explode_group = explode_group


    def add_to_list_dir(self):
        for i in range(len(self.dir_ani)):
            self.list_dir.append(self.dir_ani[i])
           
    # Função responsável por adquirir imagens do personagem e  
    # transforma-las em formato surface do pygame, redimensionando-as e
    # armazenando-as no dictionary person_ani.  
    def add_to_person_ani(self):            
        for i in self.list_dir:
            liss = []
            folder = os.listdir(f'assets/{self.path}/{i}')
            for img in folder:
                fig = pygame.image.load(os.path.join(\
                    f'assets/{self.path}/{i}', img)).convert()
                fig = pygame.transform.scale(fig,(self.scale_x ,
                                                    self.scale_y ))
                if self.rotate:
                    fig = pygame.transform.rotate(fig, 90)   
                self.rect = fig.get_rect(center=(self.x, self.y))
                fig.set_colorkey((0,0,0))
                liss.append(fig)
            self.person_ani[i] = liss

    # Função update é interna, construída pela pygame.
    # Tem chamada na tela de execution.
    def update(self):
        self.animation()
        #self.boundary()
        #self.control()
       
    def validation(self, id):
        print(player.mem_2)
        if id == 0:
            player.mem_1.pop(-1)
        elif id == 1:
            player.mem_2.pop(-1)
        
    # Animação de sprites.
    def animation(self, fr: int=0):
        now = pygame.time.get_ticks()
        if now - self.last_update > self.frame_rate:
            self.last_update = now
            if True:
                if self.frame == len(self.person_ani[self.dir_ani[fr]]):
                    self.frame = 0
                    self.var += 1 
                self.image = self.person_ani[self.dir_ani[fr]][self.frame]
                self.frame += 1
                if self.var == 1:
                    self.validation(self.id)
                    self.explode_group.remove(self)
                    