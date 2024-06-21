import pygame
from pygame.sprite import Sprite


class Estrella(Sprite):
    """Una lase para representar una estrella en la pantalla."""

    def __init__(self, ai_configuraciones, pantalla):
        """Inicializa la estrella y establece su posición inicial."""
        super().__init__()
        self.pantalla = pantalla
        self.ai_configuraciones = ai_configuraciones

        # Cargar la imagen de la estrella y establecer su atributo rect.
        self.image = pygame.image.load('imagenes/estrella.bmp')
        self.rect = self.image.get_rect()

        # Iniciar cada nueva estrella cerca de la parte superior izquierda de la pantalla.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Almacenar la posición exacta de la estrella.
        self.x = float(self.rect.x)

    def blitme(self):
        """Dibujar la estrella en su ubicación actual."""
        self.pantalla.blit(self.image, self.rect)

