import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """Una clase para representar a un único alienígena en la flota."""

    def __init__(self, ai_configuraciones, pantalla):
        """Inicializa el extraterrestre y establece su posición inicial."""
        super(Alien, self).__init__()
        self.pantalla = pantalla
        self.ai_configuraciones = ai_configuraciones

        # Cargue la imagen alienígena y establezca su atributo rect.
        self.image = pygame.image.load('imagenes/alien.bmp')
        self.rect = self.image.get_rect()

        # Inicie cada nuevo alienígena cerca de la parte superior izquierda de la pantalla.

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Almacena la posición exacta del alienígena.
        self.x = float(self.rect.x)

    def blitme(self):
        """Dibuja el extraterrestre en su ubicación actual."""
        self.pantalla.blit(self.image, self.rect)


    def verificar_bordes(self):
        """Devuelve True si el extraterrestre esta en el borde de la pantalla."""
        pantalla_rect = self.pantalla.get_rect()
        if self.rect.right >= pantalla_rect.right:
            return True
        elif self.rect.left <= 0:
            return True


    def update(self):
        """Mueve al extraterrestre hacia la derecha o a la izquierda."""
        self.x += (self.ai_configuraciones.factor_velocidad_alien * self.ai_configuraciones.direccion_flota)
        self.rect.x = self.x

