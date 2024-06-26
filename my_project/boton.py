# boton.py

import pygame.font


class Boton:

    def __init__(self, ai_configuraciones, pantalla, msg):
        """Inicializar atributos del botón."""
        self.pantalla = pantalla
        self.rect_pantalla = pantalla.get_rect()

        # Establecer las dimensiones y propiedades del botón.
        self.ancho, self.altura = 200, 50
        self.boton_color = (0, 255, 0)
        self.text_color = (255, 255, 255)
        self.fuente = pygame.font.SysFont(None, 48)

        # Construye el objeto rectángulo del botón y céntralo.
        self.rect = pygame.Rect(0, 0, self.ancho, self.altura)
        self.rect.center = self.rect_pantalla.center

        # El mensaje del botón debe prepararse solo una vez.
        self.prep_msg(msg)


    def prep_msg(self, msg):
        """Convierte el mensaje en una imagen renderizada y centra el texto en el botón."""
        self.msg_imagen = self.fuente.render(msg, True, self.text_color, self.boton_color)
        self.msg_imagen_rect = self.msg_imagen.get_rect()
        self.msg_imagen_rect.center = self.rect.center


    def draw_boton(self):
        # Dibujar un botón en blanco y luego dibujar un mensaje.
        self.pantalla.fill(self.boton_color, self.rect)
        self.pantalla.blit(self.msg_imagen, self.msg_imagen_rect)

