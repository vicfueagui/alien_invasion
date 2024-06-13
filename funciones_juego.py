#funciones_juego.py

import sys

import pygame
from bala import Bala
from alien import Alien


def verificar_eventos_keydown(event, ai_configuraciones, pantalla, nube, balas):
    """Responder a las pulsaciones de teclas."""
    if event.key == pygame.K_RIGHT:
        nube.moviendose_derecha = True
    elif event.key == pygame.K_SPACE:
        disparar_bala(ai_configuraciones, pantalla, nube, balas)
    elif event.key == pygame.K_LEFT:
        nube.moviendose_izquierda = True
    elif event.key == pygame.K_UP:
        nube.moviendose_arriba = True
    elif event.key == pygame.K_DOWN:
        nube.moviendose_abajo = True
    elif event.key == pygame.K_q:
        sys.exit()


def disparar_bala(ai_configuraciones, pantalla, nube, balas):
    """Disparar una nueva bala si aun no se ha alcanzado el limite."""
    # Crea una nueva bala y agrégala al grupo de balas.
    if len(balas) < ai_configuraciones.balas_permitidas:
        nueva_bala = Bala(ai_configuraciones, pantalla, nube)
        balas.add(nueva_bala)


def verificar_eventos_keyup(event, nube):
    """Responder cuando se sueltan las teclas."""
    if event.key == pygame.K_RIGHT:
        nube.moviendose_derecha = False
    elif event.key == pygame.K_LEFT:
        nube.moviendose_izquierda = False
    elif event.key == pygame.K_UP:
        nube.moviendose_arriba = False
    elif event.key == pygame.K_DOWN:
        nube.moviendose_abajo = False


def verificar_eventos(ai_configuraciones, pantalla, nube, balas):
    """Responder a pulsaciones de teclas y eventos del mouse."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            verificar_eventos_keydown(event, ai_configuraciones, pantalla, nube, balas)
        elif event.type == pygame.KEYUP:
            verificar_eventos_keyup(event, nube)


def actualizar_pantalla(ai_configuraciones, pantalla, nube, aliens, balas):
    """Actualiza imágenes en la pantalla y cambia a la nueva pantalla."""
    #Vuelva a dibujar la pantalla durante cada paso por el bucle.
    pantalla.fill(ai_configuraciones.fondo_color)
    # Redibujar todas las balas detrás de la nube y los extraterrestres.
    for bala in balas.sprites():
        bala.dibujar_bala()
    nube.blitme()
    aliens.draw(pantalla)

    # Hacer visible la pantalla dibujada más recientemente.
    pygame.display.flip()


def actualizar_balas(balas):
    """Actualizar la posición de las balas y eliminar las balas antiguas."""
    # Actualizar la posición de las balas.
    balas.update()
    # Eliminar la balas que ya desaparecieron.
    for bala in balas.copy():
        if bala.rect.bottom <= 0:
            balas.remove(bala)


def recibir_numero_aliens_x(ai_configuraciones, alien_ancho):
    """Determinar el número de extraterrestres que caben en una fila."""
    espacio_disponible_x = ai_configuraciones.ancho_pantalla - 2 * alien_ancho
    numero_aliens_x = int(espacio_disponible_x / (2 * alien_ancho))
    return numero_aliens_x


def recibir_numero_filas(ai_configuraciones, nube_altura, alien_altura):
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
    numero_filas = recibir_numero_filas(ai_configuraciones, nube.rect.height, alien.rect.height)

    # Crear la flota de extraterrestres.
    for numero_fila in range(numero_filas):
        for numero_alien in range(numero_aliens_x):
            crear_alien(ai_configuraciones, pantalla, aliens, numero_alien, numero_fila)

