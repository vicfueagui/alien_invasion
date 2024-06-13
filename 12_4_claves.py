import sys

import pygame


def ejecutar_juego():
    # Inicializa pygame, configuración y objeto de pantalla
    pygame.init()
    pantalla = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Eventos clave")

    # Iniciar el bucle principal del juego
    while True:
        #Este atento a los eventos del teclado y mouse
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                print(f"Tecla presionada: {event.key}")

            # Vuelva a dibujar la pantalla durante cada paso por el bucle
            pantalla.fill((0, 0, 0))    # Llena la pantalla de negro

            # Hacer visible la pantalla dibujada más recientemente
            pygame.display.flip()


ejecutar_juego()
