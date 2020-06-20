import pygame
import os
import threading
from players.player import Player
from mapas.mapa import Mapa
from bomb.bomb import Bomb
from items.item import Item


FPS = 60   
WIDTH = 800
HEIGHT = 600
BLACK = (0,0,0)
NOFRAME = pygame.NOFRAME
FULLSCREEN = pygame.FULLSCREEN
MEM_BOMB = []


pygame.init()
pygame.display.init()
pygame.mixer.init()
window = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

pygame.mixer.music.load(os.path.join('sounds','music.mp3'))
pygame.mixer.music.set_volume(0.1)

# Instanciação de mapas
m1 = Mapa()
# Instanciaçâo de items.
item = Item()
kick_item = pygame.sprite.Group()
item.item_detection(kick_item)


group = pygame.sprite.Group()
# adiciona ao grupo sprite da instaciação de player para usar collide sprite.
gp_player = pygame.sprite.Group()

#gp_player.add()
explode_group = pygame.sprite.Group()

#gp_bomb = pygame.sprite.Group()
#gp_bomb.add(p1, p1.bomb())

# Instanciação de players.
p1 = Player(group, gp_player, explode_group, MEM_BOMB, 0, 'malandro')
p2 = Player(group, gp_player, explode_group, MEM_BOMB, 1, 'pilantra')

update_list = [m1]



def update_gp_player():
    if len(gp_player) > 0:
        gp_player.update()
        gp_player.draw(window)


 
   
#dis_inf = DisplayInfo()
#font = pygame.font.Font()
def init():
    pygame.mixer.music.play(-1)
        
    execution = True
    while execution:
        dt = clock.tick(FPS)
        #font(clock.get_fps(),color=(255,255,255))   
    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                execution = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                print(pygame.mouse.get_pos())
                #p1.btn()
        # Simula o item chutar bomba.
        # Função que detecta contato entre player e item.
        p1.check_item_kick_bomb(kick_item)
        p2.check_item_kick_bomb(kick_item)
        # Função que checa se há contanto entre a bomba e os players. 
        p1.check_hit()
        p2.check_hit()
        #if hit:
            #execution = False
        m1.mapa_sprite(window)
        #gp_player.draw(window)
        #explode_group.draw(window)
        update_gp_player()
        kick_item.draw(window)
        #p1.player_sprite(window)
        #p2.player_sprite(window)
        group.update()
        group.draw(window)
        kick_item.update()
        explode_group.update()
        explode_group.draw(window)
        #gp_player.update()
        #explode_group.update()
        #collide = pygame.sprite.collide_mask(p1,p2)
        #if collide:
        #    print(collide)
        pygame.display.update(update_list)
        #pygame.display.update(p1)
        #pygame.display.flip()

    pygame.quit()

init()