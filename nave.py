import pygame


class Nave():

    def __init__(self, pantalla):
        """Inicializa la nave y establece su posición inicial."""
        self.pantalla = pantalla

        #Cargue la imagen de la nave y obtenga su corrección.
        self.imagen = pygame.image.load('imagenes/alien.bmp')
        self.rect = self.imagen.get_rect()
        self.rect_pantalla = pantalla.get_rect()

        #Inicie cada nave nueva en la parte inferior central de la pantalla.
        self.rect.centerx = self.rect_pantalla.centerx
        self.rect.bottom = self.rect_pantalla.bottom

    def blitme(self):
        """Dibuja la nave en su ubicación actual"""
        self.pantalla.blit(self.imagen, self.rect)