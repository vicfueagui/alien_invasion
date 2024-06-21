# alien_invasion.py

import pygame
from pygame.sprite import Group

from configuraciones import Configuraciones
from juego_estadisticas import JuegoEstadisticas
from nube import Nube
import funciones_juego as fg


def ejecutar_juego():
    # Inicializa pygame, configuración y objeto de pantalla
    pygame.init()
    ai_configuraciones = Configuraciones()
    pantalla = pygame.display.set_mode((ai_configuraciones.ancho_pantalla, ai_configuraciones.altura_pantalla))
    pygame.display.set_caption("Alien Invasion")

    # Crear una instancia para almacenar las estadísticas del juego.
    estadisticas = JuegoEstadisticas(ai_configuraciones)

    # Haz una nube, un grupo de balas y un grupo de extraterrestres.
    # Crea tu nube.
    nube = Nube(ai_configuraciones, pantalla)
    # Crea un grupo para almacenar balas
    balas = Group()
    # Crea un grupo para almacenar extraterrestres.
    aliens = Group()

    estrellas = Group()

    gotas = Group()

    # Crea una flota de extraterrestres.
    fg.crear_flota(ai_configuraciones, pantalla, nube, aliens)
    fg.crear_cuadricula_estrellas(ai_configuraciones, pantalla, estrellas)
    fg.crear_cuadricula_gotas(ai_configuraciones, pantalla, gotas)

    # Inicia el bucle principal del juego
    while True:
        # Este atento a los eventos del teclado y mouse.
        fg.verificar_eventos(ai_configuraciones, pantalla, nube, balas)
        # Actualiza la posición de la nube
        nube.actualizacion()
        # Actualiza la posición de las balas
        fg.actualizar_balas(ai_configuraciones, pantalla, nube, aliens, balas)

        fg.update_aliens(ai_configuraciones, estadisticas, pantalla, nube, aliens, balas)

        fg.actualizar_gotas(ai_configuraciones, pantalla, gotas)

        fg.update_aliens(ai_configuraciones, estadisticas, pantalla, nube, aliens, balas)
        # Redibuja la pantalla y los elementos en ella.
        fg.actualizar_pantalla(ai_configuraciones, pantalla, nube, aliens, balas, estrellas, gotas)


ejecutar_juego()