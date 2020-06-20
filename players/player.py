import pygame
import os
import time
from bomb.bomb import Bomb
from settings import Settings
#from fire.fire import Fire

mem_1 = []
mem_2 = []

set_bomb = Settings()


class Player(pygame.sprite.Sprite):
    def __init__(self, group, gp_player, explode_group, memory, 
                                            id: int, path: str):
        pygame.sprite.Sprite.__init__(self)
        self.gp_player = gp_player
        self.explode_group = explode_group
        self.memory = memory
        self.scale_x = 64
        self.scale_y = 64
        self.bomb_scale_x = 50
        self.bomb_scale_y = 50
        self.vel = 2
        self.id = id
        self.path = path
        self.list_dir = []
        self.person_ani = {}
        self.dir_ani = os.listdir(f'assets/{self.path}')
        self.add_to_list_dir()
        self.add_to_person_ani()
        self.image = self.person_ani[self.list_dir[0]][0]
        self.group = group
        self.group.add(self)
        self.frame = 0
        self.last_update = pygame.time.get_ticks()
        self.frame_rate = 110
        self.posx = 0
        self.posy = 0
        self.get_kick_bomb = False
        self.mem_bomb = []
        self.bomb_quantity = 1


        if self.id == 0:
            self.rect.x = 70

        if self.id == 0:
            self.rect.y = 20

        if self.id == 1:
            self.rect.x = 670

        if self.id == 1:
            self.rect.y = 485

    # Aplia a escala da imagem/explosão.
    def scale(self):
        self.posx = self.rect.x
        self.posy = self.rect.y
        self.scale_y = 100
        self.add_to_person_ani()
        self.rect.x = self.posx
        self.rect.y = self.posy 
        

    # Adiciana as pastas que contem figuras à list_dir.
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
                fig = pygame.transform.scale(fig,(self.scale_x,self.scale_y))
                self.rect = fig.get_rect()
                fig.set_colorkey((255,255,255))
                liss.append(fig)
            self.person_ani[i] = liss    
         

    # Função update é interna, construída pela pygame.
    # Tem chamada na tela de execution.
    def update(self):
        self.boundary()
        self.control()
        self.animation(fr = 4)
        self.explode_check()
        
                    

    # Animação de sprites.
    def animation(self, fr: int):
        now = pygame.time.get_ticks()
        if now - self.last_update > self.frame_rate:
            self.last_update = now
            if True:
                if self.frame == len(self.person_ani[self.dir_ani[fr]]):
                    self.frame = 0
                try:
                    self.image = self.person_ani[self.dir_ani[fr]][self.frame]
                    self.frame += 1
                except IndexError:
                    self.frame = 0

    # Adiciona e remove sprites de um grupo.        
    #def player_sprite(self, window):
        #self.group.clear(window, (255,255,255))
        #self.group.draw(window)
        #self.group.update()
        #self.group.remove(self)
        
        
    
    # Função que checa se há contanto entre a bomba e o segundo player.
    # Deve ser utilizada como item chutar bomba.
    def check_hit(self):
        hit_list = pygame.sprite.spritecollide(self, self.gp_player, False)
        for hit in hit_list:
            for i in self.memory:
                if self.get_kick_bomb == True:
                    if i == hit:
                        i.have = True
                        i.rect.x += 5

    # Função que capacita o player a chutar bomba.
    def check_item_kick_bomb(self, kick_item):
        contact = pygame.sprite.spritecollide(self, kick_item, True)
        for cont in contact:
            self.get_kick_bomb = True 

    def explode_check(self):
        contact = pygame.sprite.groupcollide(self.group, self.explode_group,
                                                                True, False)

    # Controla o personagem.    
    def control(self):
        key = pygame.key.get_pressed()
        #Controle do player1
        # Mover-se para direita
        if key[pygame.K_d] and self.id == 0: 
            self.rect.x += self.vel
            self.animation(fr = 3)
        # Mover-se para baixo
        if key[pygame.K_a] and self.id == 0:
            self.rect.x -= self.vel
            self.animation(fr = 2)
        # Mover-se para cima
        if key[pygame.K_w] and self.id == 0:
            self.rect.y -= self.vel
            self.animation(fr = 1)
        # Mover-se para esquerda.
        if key[pygame.K_s] and self.id == 0: 
            self.rect.y += self.vel
            self.animation(fr = 0)
        # Plantar bomba.
        if len(mem_1) < self.bomb_quantity:
            if key[pygame.K_v] and self.id == 0:
                b = Bomb(self.gp_player, self.explode_group, self.id, self.memory,
                                            self.rect.x + 35, self.rect.y + 40)
                mem_1.append(0)
            #gp_player.add(b)
            #memory.append(b)
            #print(self.track)
          
        
        # Controle do player2
        # Mover-se para direita.
        if key[pygame.K_l] and self.id == 1:
            self.rect.x += self.vel
            self.animation(fr = 3)
        # Mover-se para esquerda.
        if key[pygame.K_j] and self.id == 1:
            self.rect.x -= self.vel
            self.animation(fr = 2)
        # Mover-se para cima.
        if key[pygame.K_i] and self.id == 1:
            self.rect.y -= self.vel
            self.animation(fr = 1)
        # Mover-se para baixo.
        if key[pygame.K_k] and self.id == 1:
            self.rect.y += self.vel
            self.animation(fr = 0)
        # Plantar bomba.
        if len(mem_2) < self.bomb_quantity:
            if key[pygame.K_m] and self.id == 1:
                b = Bomb(self.gp_player, self.explode_group, self.id, self.memory, 
                                        self.rect.x + 35, self.rect.y + 40)
                mem_2.append(0)
            #gp_player.add(b)
            #memory.append(b)


    # Verifica se o player está nas delimitações do mapa.
    def boundary(self):
        if self.rect.x == 674:
            self.rect.x -= self.vel

        if self.rect.x == 64:
            self.rect.x += self.vel

        if self.rect.y == 490:
            self.rect.y -= self.vel

        if self.rect.y == 14:
            self.rect.y += self.vel

#p1 = Player(0,'pilantra')