import pygame
import os
from fire.fire import Fire


class Bomb(pygame.sprite.Sprite):
    def __init__(self, gp_player, explode_group, id, memory, 
                                x: int = 0, y: int = 0, path='bombs'):
        pygame.sprite.Sprite.__init__(self)
        self.play = pygame.mixer.Sound(os.path.join('sounds', 'SHIBIRE.wav'))
        self.play.set_volume(0.05)
        self.play.play()
        self.id = id
        self.memory = memory
        self.memory.append(self)
        self.x = x
        self.y = y
        self.path = path
        self.list_dir = []
        self.person_ani = {}
        self.dir_ani = os.listdir(f'assets/{self.path}')
        self.add_to_list_dir()
        self.add_to_person_ani()
        self.image = self.person_ani[self.list_dir[0]][0]
        self.select_bomb = pygame.sprite.Group()
        self.frame = 0
        self.last_update = pygame.time.get_ticks()
        self.frame_rate = 180
        self.rx = self.rect.x
        self.have = False
        self.var = 0
        self.gp_player = gp_player
        self.gp_player.add(self)
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
                fig = pygame.transform.scale(fig,(50,50))
                self.rect = fig.get_rect(center=(self.x, self.y))
                fig.set_colorkey((255,255,255))
                liss.append(fig)
            self.person_ani[i] = liss

    # Função update é interna, construída pela pygame.
    # Tem chamada na tela de execution.
    def update(self):
        self.animation()
        self.drift()
        #self.boundary()
        #self.control()
       


    # Animação de sprites.
    def animation(self, fr: int=0):
        now = pygame.time.get_ticks()
        if now - self.last_update > self.frame_rate:
            self.last_update = now
            if True:
                if self.frame == len(self.person_ani[self.dir_ani[fr]]):
                    self.var += 1
                    self.frame = 0        
                self.image = self.person_ani[self.dir_ani[fr]][self.frame]
                self.frame += 1
            if self.var == 5:
                self.gp_player.remove(self)
                self.memory.pop(-1)
                self.explode_group.add(Fire(self.explode_group, self.id, False,
                                            self.rect.x + 20,self.rect.y + 30))
                self.explode_group.add(Fire(self.explode_group, None, True,
                                           self.rect.x + 20, self.rect.y + 30))
    
    # Adiciona e remove sprites de um grupo.        
    #def bomb_sprite(self, window):
    #    self.select_bomb.add(self)
    #    self.select_bomb.update()
    #    self.select_bomb.draw(window)
    #    self.select_bomb.remove(self) 
        
    def drift(self):
        if self.have:
            self.rect.x += 5
        
    