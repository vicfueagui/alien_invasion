#nube.py

import pygame


class Nube:

    def __init__(self, ai_configuraciones, pantalla):
        """Inicializa la nave y establece su posición inicial."""
        self.pantalla = pantalla
        self.ai_configuraciones = ai_configuraciones

        #Cargue la imagen de la nave y obtenga su corrección.
        self.imagen = pygame.image.load('imagenes/tormenta.bmp')
        self.rect = self.imagen.get_rect()
        self.rect_pantalla = pantalla.get_rect()

        #Inicie cada nave nueva en la parte inferior central de la pantalla.
        self.rect.centerx = self.rect_pantalla.centerx
        self.rect.bottom = self.rect_pantalla.bottom

        #Almacenar un valor decimal para el centro del barco.
        self.centro_x = float(self.rect.centerx)
        self.centro_y = float(self.rect.centery)

        #Bandera de movimiento.
        self.moviendose_derecha = False
        self.moviendose_izquierda = False
        self.moviendose_arriba = False
        self.moviendose_abajo = False


    def actualizacion(self):
        """Actualiza la posición de la nube según las banderas de movimiento."""
        #Actualiza el valor del centro del barco, no el rect.
        if self.moviendose_derecha and self.rect.right < self.rect_pantalla.right:
            self.centro_x += self.ai_configuraciones.factor_velocidad_nube
            # print("Moviéndose a la derecha:", self.centro_x)
        if self.moviendose_izquierda and self.rect.left > 0:
            self.centro_x -= self.ai_configuraciones.factor_velocidad_nube
            # print("Moviéndose a la izquierda:", self.centro_x)
        if self.moviendose_arriba and self.rect.top > 0:
            self.centro_y -= self.ai_configuraciones.factor_velocidad_nube
            # print("Moviéndose hacia arriba:", self.centro_y)
        if self.moviendose_abajo and self.rect.bottom < self.rect_pantalla.bottom:
            self.centro_y += self.ai_configuraciones.factor_velocidad_nube
            # print("Moviéndose hacia abajo:", self.centro_y)


        #Actualiza el objeto rect desde self.centro
        self.rect.centerx = self.centro_x
        self.rect.centery = self.centro_y

    def blitme(self):
        """Dibuja la nave en su ubicación actual"""
        self.pantalla.blit(self.imagen, self.rect)


    def centro_nube(self):
        # Centrar la nube en la pantalla.
        self.centro = self.rect_pantalla.centerx













