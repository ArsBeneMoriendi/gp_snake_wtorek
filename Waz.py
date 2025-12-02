import pygame
from Kierunek import Kierunek

class Waz(pygame.sprite.Sprite):
    # stwórz konstruktor (nie przyjmuje żadnych parametrów)
    # w konstruktorze stwórz zmienne:
    # oryginalny_obraz - załaduj obrazek ze ścieżki
    # obraz - obrazek skierowany początkowo do góry:
    #       pygame.transform.rotate(self.oryginalny_obraz, 0)
    # rect - współrzędne środka ekranu 

    def __init__(self):
        self.oryginalny_obraz = pygame.image.load("images/head.png")
        self.obraz = pygame.transform.rotate(self.oryginalny_obraz, 0)
        self.rect = self.obraz.get_rect(center = (12*32+16, 9*32+16))