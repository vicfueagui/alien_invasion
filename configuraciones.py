#configuraciones.py

class Configuraciones():
    """Una clase para almacenar todas las configuraciones de Alien Invasion."""
    def __init__(self):
        """Inicializa la configuración del juego"""
        # Ajustes de pantalla
        self.ancho_pantalla = 1200
        self.altura_pantalla = 800
        self.fondo_color = (173, 216, 230)  # Azul claro

        # Nube configuraciones.
        self.factor_velocidad_nube = 1.5

        # Bala configuraciones.
        self.factor_velocidad_bala = 1
        self.ancho_bala = 3
        self.altura_bala = 15
        self.bala_color = (60, 60, 60)
        self.balas_permitidas = 3

        # Configuración extraterrestre.
        self.factor_velocidad_alien = 1
        self.velocidad_caida_flota = 10
        # Dirección_flota de 1 representa la derecha; -1 representa la izquierda.
        self.direccion_flota = 1


