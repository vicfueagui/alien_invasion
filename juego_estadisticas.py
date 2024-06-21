# juego_estadisticas.py

class JuegoEstadisticas():
    """Seguimiento de las estadísticas del juego Alien Invasión."""
    def __init__(self, ai_configuraciones):
        """Inicializa estadísticas."""
        self.ai_configuraciones = ai_configuraciones
        self.reiniciar_estadisticas()

        # Inicia Alien Invasion en un estado inactivo.
        self.juego_activo = False

    def reiniciar_estadisticas(self):
        """Inicializa estadísticas que pueden cambiar durante el juego."""
        self.nubes_izquierda = self.ai_configuraciones.nube_limite



