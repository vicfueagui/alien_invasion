#funciones_juego.py

import sys

import pygame
from bala import Bala
from alien import Alien
from estrella import Estrella
from gota import Gota
import random


def verificar_eventos_keydown(event, ai_configuraciones, pantalla, nube, balas):
    """Responder a las pulsaciones de teclas."""
    # print(f"KEYDOWN: {event.key}")  # Imprimir la tecla presionada
    if event.key == pygame.K_RIGHT:
        nube.moviendose_derecha = True
        # print("Moviéndose a la derecha activado")
    elif event.key == pygame.K_SPACE:
        disparar_bala(ai_configuraciones, pantalla, nube, balas)
    elif event.key == pygame.K_LEFT:
        nube.moviendose_izquierda = True
        # print("Moviéndose a la izquierda activado")
    elif event.key == pygame.K_UP:
        nube.moviendose_arriba = True
        # print("Moviéndose hacia arriba activado")
    elif event.key == pygame.K_DOWN:
        nube.moviendose_abajo = True
        # print("Moviéndose hacia abajo activado")
    elif event.key == pygame.K_q:
        sys.exit()


def disparar_bala(ai_configuraciones, pantalla, nube, balas):
    """Disparar una nueva bala si aun no se ha alcanzado el limite."""
    # Crea una nueva bala y agrégala al grupo de balas.
    if len(balas) < ai_configuraciones.balas_permitidas:
        nueva_bala = Bala(ai_configuraciones, pantalla, nube)
        balas.add(nueva_bala)
        """
        print("Bala disparada. Total de balas:", len(balas))
    else:
        print("Límite de balas alcanzado.")
        """     # Verificar este código, no cumple el límite de balas


def verificar_eventos_keyup(event, nube):
    """Responder cuando se sueltan las teclas."""
    # print(f"KEYUP: {event.key}")  # Imprimir la tecla liberada
    if event.key == pygame.K_RIGHT:
        nube.moviendose_derecha = False
        # print("Moviéndose a la derecha desactivado")
    elif event.key == pygame.K_LEFT:
        nube.moviendose_izquierda = False
        # print("Moviéndose a la izquierda desactivado")
    elif event.key == pygame.K_UP:
        nube.moviendose_arriba = False
        # print("Moviéndose hacia arriba desactivado")
    elif event.key == pygame.K_DOWN:
        nube.moviendose_abajo = False
        # print("Moviéndose hacia abajo desactivado")


def verificar_eventos(ai_configuraciones, pantalla, nube, balas):
    """Responder a pulsaciones de teclas y eventos del mouse."""
    for event in pygame.event.get():
        # print(event)  # Agregar esta línea para imprimir cada evento
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            verificar_eventos_keydown(event, ai_configuraciones, pantalla, nube, balas)
        elif event.type == pygame.KEYUP:
            verificar_eventos_keyup(event, nube)


def actualizar_pantalla(ai_configuraciones, pantalla, nube, aliens, balas, estrellas, gotas):
    """Actualiza imágenes en la pantalla y cambia a la nueva pantalla."""
    #Vuelva a dibujar la pantalla durante cada paso por el bucle.
    pantalla.fill(ai_configuraciones.fondo_color)
    # Redibujar todas las balas detrás de la nube y los extraterrestres.
    for bala in balas.sprites():
        bala.dibujar_bala()
    nube.blitme()
    aliens.draw(pantalla)
    estrellas.draw(pantalla)
    for gota in gotas.sprites():
        gota.blitme()

    # Hacer visible la pantalla dibujada más recientemente.
    pygame.display.flip()


def actualizar_balas(ai_configuraciones, pantalla, nube, aliens, balas):
    """Actualizar la posición de las balas y eliminar las balas antiguas."""
    # Actualizar la posición de las balas.
    balas.update()
    # Eliminar la balas que ya desaparecieron.
    for bala in balas.copy():
        if bala.rect.bottom <= 0:
            balas.remove(bala)
            # print("Bala eliminada. Total de balas:", len(balas))
    verificar_colision_alien_bala(ai_configuraciones, pantalla, nube, aliens, balas)


def verificar_colision_alien_bala(ai_configuraciones, pantalla, nube, aliens, balas):
    """Responder a colisiones bala-extraterrestre."""
    # Elimina las balas y los extraterrestres que hayan chocado.
    colisiones = pygame.sprite.groupcollide(balas, aliens, True, True)
    if len(aliens) == 0:
        # Destruye las balas existentes y crea una nueva flota.
        balas.empty()
        crear_flota(ai_configuraciones, pantalla, nube, aliens)


def actualizar_gotas(ai_configuraciones, pantalla, gotas):
    gotas.update()
    for gota in gotas.copy():
        if gota.rect.top >= ai_configuraciones.altura_pantalla:
            gotas.remove(gota)
            crear_gota(ai_configuraciones, pantalla, gotas)


def recibir_numero_gotas_x(ai_configuraciones, gota_ancho):
    espacio_disponible_x = ai_configuraciones.ancho_pantalla - 2 * gota_ancho
    numero_gotas_x = int(espacio_disponible_x / (2 * gota_ancho))
    return numero_gotas_x


def recibir_numero_filas_gotas(ai_configuraciones, gota_altura):
    """Determina el número de filas de extraterrestres que caben en la pantalla."""
    espacio_disponible_y = ai_configuraciones.altura_pantalla - 2 * gota_altura
    numero_filas = int(espacio_disponible_y / (2 * gota_altura))
    return numero_filas


def crear_gota(ai_configuraciones, pantalla, gotas, numero_gota=0, numero_fila=0):
    gota = Gota(ai_configuraciones, pantalla)
    gota_ancho = gota.rect.width
    gota.x = gota_ancho + 2 * gota_ancho * numero_gota
    gota.rect.x = gota.x
    gota.rect.y = gota.rect.height + 2 * gota.rect.height * numero_fila
    gotas.add(gota)


def crear_cuadricula_gotas(ai_configuraciones, pantalla, gotas):
    gota = Gota(ai_configuraciones, pantalla)
    numero_gotas_x = recibir_numero_gotas_x(ai_configuraciones, gota.rect.width)
    numero_filas = recibir_numero_filas_gotas(ai_configuraciones, gota.rect.height)
    for numero_fila in range(numero_filas):
        for numero_gota in range(numero_gotas_x):
            crear_gota(ai_configuraciones, pantalla, gotas, numero_gota, numero_fila)


def recibir_numero_aliens_x(ai_configuraciones, alien_ancho):
    """Determinar el número de extraterrestres que caben en una fila."""
    espacio_disponible_x = ai_configuraciones.ancho_pantalla - 2 * alien_ancho
    numero_aliens_x = int(espacio_disponible_x / (2 * alien_ancho))
    return numero_aliens_x


def recibir_numero_filas_aliens(ai_configuraciones, nube_altura, alien_altura):
    """Determina el número de filas de extraterrestres que caben en la pantalla."""
    espacio_disponible_y = (ai_configuraciones.altura_pantalla - (3 * alien_altura) - nube_altura)
    numero_filas = int(espacio_disponible_y / (2 * alien_altura))
    return numero_filas


def crear_alien(ai_configuraciones, pantalla, aliens, numero_alien, numero_fila):
    """Crea un extraterrestre y colócalo en la fila."""
    alien = Alien(ai_configuraciones, pantalla)
    alien_ancho = alien.rect.width
    alien.x = alien_ancho + 2 * alien_ancho * numero_alien
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * numero_fila
    aliens.add(alien)


def crear_flota(ai_configuraciones, pantalla, nube, aliens):
    """Crea una flota completa de extraterrestres."""
    # Crea un extraterrestre y encuentra la cantidad de extraterrestres seguidos.
    # El espacio entre cada extraterrestre es igual al ancho de un extraterrestre.
    alien = Alien(ai_configuraciones, pantalla)
    numero_aliens_x = recibir_numero_aliens_x(ai_configuraciones, alien.rect.width)
    numero_filas = recibir_numero_filas_aliens(ai_configuraciones, nube.rect.height, alien.rect.height)

    # Crear la flota de extraterrestres.
    for numero_fila in range(numero_filas):
        for numero_alien in range(numero_aliens_x):
            crear_alien(ai_configuraciones, pantalla, aliens, numero_alien, numero_fila)


def crear_estrella(ai_configuraciones, pantalla, estrellas, numero_estrella, numero_fila):
    """Crea una estrella y la coloca en la fila."""
    estrella = Estrella(ai_configuraciones, pantalla)
    estrella_ancho = estrella.rect.width
    estrella.x = estrella_ancho + 2 * estrella_ancho * numero_estrella
    estrella.rect.x = estrella.x + random.randint(-10, 10)
    estrella.rect.y = estrella.rect.height + 2 * estrella.rect.height * numero_fila + random.randint(-10, 10)
    estrellas.add(estrella)


def crear_cuadricula_estrellas(ai_configuraciones, pantalla, estrellas):
    """Crear una cuadrícula de estrellas."""
    # Crear una estrella y encontrar el número de estrellas en una fila.
    # El espacio entre cada estrella es igual al ancho de una estrella.
    estrella = Estrella(ai_configuraciones, pantalla)
    numero_estrellas_x = recibir_numero_estrellas_x(ai_configuraciones, estrella.rect.width)
    numero_filas = recibir_numero_filas_estrellas(ai_configuraciones, estrella.rect.height)

    # Crear una cuadrícula de estrellas.
    for numero_fila in range(numero_filas):
        for numero_estrella in range(numero_estrellas_x):
            crear_estrella(ai_configuraciones, pantalla, estrellas, numero_estrella, numero_fila)


def recibir_numero_estrellas_x(ai_configuraciones, estrella_ancho):
    """Determinar el número de estrellas que caben en una fila."""
    espacio_disponible_x = ai_configuraciones.ancho_pantalla - 2 * estrella_ancho
    numero_estrellas_x = int(espacio_disponible_x / (2 * estrella_ancho))
    return numero_estrellas_x


def recibir_numero_filas_estrellas(ai_configuraciones, estrella_altura):
    """Determinar el número de filas de estrellas que caben en la pantalla."""
    espacio_disponible_y = ai_configuraciones.altura_pantalla - 2 * estrella_altura
    numero_filas = int(espacio_disponible_y / (2 * estrella_altura))
    return numero_filas


def verificar_bordes_flota(ai_configuraciones, aliens):
    """Responder apropiadamente si un extraterrestre llego a algún borde."""
    for alien in aliens.sprites():
        if alien.verificar_bordes():
            cambiar_direccion_flota(ai_configuraciones, aliens)
            break


def cambiar_direccion_flota(ai_configuraciones, aliens):
    """Soltar toda la flota y cambiar la dirección de la flota."""
    for alien in aliens.sprites():
        alien.rect.y += ai_configuraciones.velocidad_caida_flota
    ai_configuraciones.direccion_flota *= -1


def update_aliens(ai_configuraciones, aliens):
    """
    Compruebe si la flota está en los bordes y luego actualizar las posiciones de todos los
    extraterrestres de la flota.
    """
    verificar_bordes_flota(ai_configuraciones, aliens)
    aliens.update()















