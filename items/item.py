import pygame
import os

class Item(pygame.sprite.Sprite):
    def __init__(self, item:str='item_kick_bomb.png', posx=400, posy=300):
        pygame.sprite.Sprite.__init__(self)
        self.item = item
        self.posx = posx
        self.posy = posy
        self.image = pygame.image.load(os.path.join('assets/items', self.item))
        self.image = pygame.transform.scale(self.image, (50,50))
        self.rect = self.image.get_rect(center=(self.posx,self.posy))


    def item_detection(self, bomb_item):
        bomb_item.add(self)
     #   hit_list = pygame.sprite.spritecollide(self, gp_player, True)
      #  for hit in hit_list:
            
                    


#item = Item()
