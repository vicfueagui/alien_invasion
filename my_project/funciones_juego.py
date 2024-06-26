#funciones_juego.py

import sys
from time import sleep

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


def verificar_eventos(ai_configuraciones, pantalla, estadisticas, boton_reproducir, nube, aliens, balas):
    """Responder a pulsaciones de teclas y eventos del mouse."""
    for event in pygame.event.get():
        # print(event)  # Agregar esta línea para imprimir cada evento
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            verificar_eventos_keydown(event, ai_configuraciones, pantalla, nube, balas)
        elif event.type == pygame.KEYUP:
            verificar_eventos_keyup(event, nube)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            verificar_boton_reproducir(ai_configuraciones, pantalla, estadisticas, boton_reproducir, nube, aliens,
                                       balas, mouse_x, mouse_y)


def verificar_boton_reproducir(ai_configuraciones, pantalla, estadisticas, boton_reproducir, nube, aliens, balas,
                               mouse_x, mouse_y):
    """Comienza un nuevo juego cuando el jugador hace clic en jugar."""
    boton_clic = boton_reproducir.rect.collidepoint(mouse_x, mouse_y)
    if boton_clic and not estadisticas.juego_activo:
        #   Ocultar el cursor del mouse.
        pygame.mouse.set_visible(False)
        #   Restablecer las estadisticas del juego.
        estadisticas.reiniciar_estadisticas()
        estadisticas.juego_activo = True

        # Vaciar la lista de extraterrestres y balas.
        aliens.empty()
        balas.empty()

        # Crea una nueva flota y centra la nube.
        crear_flota(ai_configuraciones, pantalla, nube, aliens)
        nube.centro_nube()


def actualizar_pantalla(ai_configuraciones, pantalla, estadisticas, nube, aliens, balas, boton_reproducir):
    """Actualiza imágenes en la pantalla y cambia a la nueva pantalla."""
    #Vuelva a dibujar la pantalla durante cada paso por el bucle.
    pantalla.fill(ai_configuraciones.fondo_color)
    # Redibujar todas las balas detrás de la nube y los extraterrestres.
    for bala in balas.sprites():
        bala.dibujar_bala()
    nube.blitme()
    aliens.draw(pantalla)

    # Dibuja el botón de reproducción si el juego está inactivo.
    if not estadisticas.juego_activo:
        boton_reproducir.draw_boton()

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


def golpear_nube(ai_configuraciones, estadisticas, pantalla, nube, aliens, balas):
    """Responder a la nube que es golpeada por un extraterrestre."""
    if estadisticas.nubes_izquierda > 0:
        # Decremento nubes_izquierda.
        estadisticas.nubes_izquierda -= 1

        # Vaciar la lista de extraterrestres y balas.
        aliens.empty()
        balas.empty()

        # Crear una nueva flota y centrar la nube.
        crear_flota(ai_configuraciones, pantalla, nube, aliens)
        nube.centro_nube()

        # Pausa.
        sleep(0.5)

    else:
        estadisticas.juego_activo = False
        pygame.mouse.set_visible(True)


def verificar_fondo_aliens(ai_configuraciones, estadisticas, pantalla, nube, aliens, balas):
    """Comprueba si algún extraterrestre ha llegado al final de la pantalla."""
    rect_pantalla = pantalla.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= rect_pantalla.bottom:
            # Trate esto igual que si la nube hubiera sido alcanzada.
            golpear_nube(ai_configuraciones, estadisticas, pantalla, nube, aliens, balas)
            break


def update_aliens(ai_configuraciones, estadisticas, pantalla, nube, aliens, balas):
    """
    Compruebe si la flota está en los bordes y luego actualizar las posiciones de todos los
    extraterrestres de la flota.
    """
    verificar_bordes_flota(ai_configuraciones, aliens)
    aliens.update()

    # Busque colisiones de nubes alienígenas.
    if pygame.sprite.spritecollideany(nube, aliens):
        golpear_nube(ai_configuraciones, estadisticas, pantalla, nube, aliens, balas)

    # Busca extraterrestres que lleguen a la parte inferior de la pantalla.
    verificar_fondo_aliens(ai_configuraciones, estadisticas, pantalla, nube, aliens, balas)












