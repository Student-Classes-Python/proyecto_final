# -*- coding: utf-8 -*-
import pgzrun
import pygame

import injector
from example import Servicio, ServicioConcreto, Cliente
from startup.service_collection_extensions import ModuloDeAplicacion

from pgzero.actor import Actor
from pgzero.keyboard import keyboard
from pgzero.screen import Screen


# Crear un injector y utilizarlo para obtener una instancia de Cliente
injector_obj = injector.Injector(ModuloDeAplicacion())
cliente = injector_obj.get(Cliente)

# Ejecutar el método para verlo en acción
print(cliente.ejecutar_servicio())


# Crear una ventana con Pygame Zero
# Configuración de la ventana del juego
WIDTH = 1280
HEIGHT = 720
TITLE = "Aventura en el Parque de Atracciones"

# Load background image
background = Actor('fondo') # type: ignore
background.pos = WIDTH // 2, HEIGHT // 2  # Center position
background.width = WIDTH
background.height = HEIGHT

scale_factor = 0.025

player = Actor('player', center=(WIDTH // 2, HEIGHT - 60)) # type: ignore
new_width = int(player.width * scale_factor)
new_height = int(player.height * scale_factor)
player._surf = pygame.transform.scale(player._surf, (new_width, new_height))
player._update_pos()

# Lista de las atracciones con sus respectivos nombres de archivo
attractions = [
    Actor('attractions/enchanted_castle', center=(200, HEIGHT - 300)), # type: ignore
    Actor('attractions/grand_ferris_wheel', center=(400, HEIGHT - 300)), # type: ignore
    Actor('attractions/pirate_ship_swings', center=(600, HEIGHT - 300)), # type: ignore
    Actor('attractions/thunder_loops', center=(800, HEIGHT - 300)), # type: ignore
    Actor('attractions/viking_ship', center=(1000, HEIGHT - 300)), # type: ignore
]

def update():
    # Actualizar la posición del jugador con las teclas de dirección
    if keyboard.left and player.left > 0: # type: ignore
        player.x -= 2
    elif keyboard.right and player.right < WIDTH: # type: ignore
        player.x += 2
    if keyboard.up and player.top > 0: # type: ignore
        player.y -= 2
    elif keyboard.down and player.bottom < HEIGHT: # type: ignore
        player.y += 2

    # Interacciones con las atracciones aquí
    # for attraction in attractions:
    #     if player.colliderect(attraction):
    #         print(f"Interacting with {attraction}")
    pass

def draw():
    # Dibujar el fondo, jugador y atracciones
    screen.clear() # type: ignore
    background.draw()
    # for attraction in attractions:
    #     attraction.draw()
    player.draw()
    pass

pgzrun.go()  # Iniciar el bucle del juego
