import pygame
from pygame.sprite import Sprite


class Gota(Sprite):
    """Una clase para representar una sola gota de lluvia."""
    def __init__(self, ai_configuraciones, pantalla):
        """Inicializa la gota y establece su posición inicial."""
        super().__init__()
        self.pantalla = pantalla
        self.ai_configuraciones = ai_configuraciones

        # Cargar la imagen de la gota y establecer su atributo rect.
        self.image = pygame.image.load('imagenes/gota.bmp')
        self.rect = self.image.get_rect()

        # Iniciar cada nueva gota cerca de la parte superior izquierda de la pantalla.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Almacenar la posición exacta de la gota.
        self.y = float(self.rect.y)


    def update(self):
        """Mueva la gota hacia abajo."""
        self.y *= self.ai_configuraciones.velocidad_gota
        self.rect.y = self.y

    def blitme(self):
        """Dibuja la gota en su ubicación actual."""
        self.pantalla.blit(self.image, self.rect)
