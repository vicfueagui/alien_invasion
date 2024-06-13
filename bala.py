# bala.py

import pygame
from pygame.sprite import Sprite


class Bala(Sprite):
    """Una clase para gestionar las balas de la nube"""


    def __init__(self, ai_configuraciones, pantalla, nube):
        # Crea un objeto bala en la posición actual de la nube
        super(Bala, self).__init__()
        self.pantalla = pantalla

        # Crea una bala recta en (0, 0) y luego establezca la posición correcta.
        self.rect = pygame.Rect(0, 0, ai_configuraciones.ancho_bala, ai_configuraciones.altura_bala)
        self.rect.centerx = nube.rect.centerx
        self.rect.top = nube.rect.top

        # Almacena la posición de la bala como un valor decimal.
        self.y = float(self.rect.y)

        self.color = ai_configuraciones.bala_color
        self.factor_velocidad_bala = ai_configuraciones.factor_velocidad_bala


    def update(self):
        """Mueva la bala hacia arriba de la pantalla."""
        # Actualiza la posición decimal de la viñeta.
        self.y -= self.factor_velocidad_bala
        # Actualiza la posición recta.
        self.rect.y = self.y

    def dibujar_bala(self):
        """Dibujar la bala hacia la pantalla."""
        pygame.draw.rect(self.pantalla, self.color, self.rect)






