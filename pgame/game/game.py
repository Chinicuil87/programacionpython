import sys
import pygame

from .config import *
from .platform import Platform

# Creamos la clase principal


class Game:

    def __init__(self):
        # pintamos nuestra pantalla
        pygame.init()

        # generar ventana
        self.surface = pygame.display.set_mode((WIDTH, HEIGHT))
        # titulo de la vventana
        pygame.display.set_caption(TITLE)

        # Definimos un atributo que permite saber si se encuentra ejecutandose o no la aplicacion
        self.running = True

    # Metodo que permite iniciar el juego

    def start(self):
        self.new()

    # Metodo que permite generar nuevo juego
    def new(self):
        self.generate_elements()
        self.run()

    # Genera elementos
    def generate_elements(self):
        self.platform = Platform()

        self.sprites = pygame.sprite.Group()

        self.sprites.add(self.platform)

    # Metodo que ejecuta el juego
    def run(self):
        while self.running:
            self.event()
            self.draw()
            self.update()

    # Metodo event que escucha todos los eventos que se sucitan
    def event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                pygame.quit()
                sys.exit()

    # Metodo que pinta todos los elementos.
    def draw(self):
        self.surface.fill(BLACK)

        self.sprites.draw(self.surface)

    # Metodo de actualizar la pantalla
    def update(self):
        pygame.display.flip()

    # Metodo que detiene el juego
    def stop(self):
        pass
