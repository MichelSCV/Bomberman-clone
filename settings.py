import pygame
import os


class Settings:
    def __init__(self):
        self.bomb_permission_p1 = 0
        self.bomb_permission_p2 = 0
    
    def permission(self,id):
        if id == 0:
            self.bomb_permission_p1 -= 1
        if id == 1:
            self.bomb_permission_p2 -= 1