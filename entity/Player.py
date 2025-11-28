# game.py — starter roguelite top-down con arcade
import arcade
import random
import math
from typing import List
from constants import (WINDOW_WIDTH, WINDOW_HEIGHT,
                       SPRITE_SHEET, 
                       FRAME_COUNT, 
                       FRAME_WIDTH, 
                       FRAME_HEIGHT
                       )


MOVEMENT_SPEED = 5 # px/s
ZOMBIE_SPEED = 100.0
BULLET_SPEED = 600.0
SPRITE_SCALING = 0.5


class Player(arcade.Sprite):

    def __init__(self):
        super().__init__()
        
        # Cargar lista de texturas
        self.textures = []

        for i in range(FRAME_COUNT):
            frame = arcade.load_texture(
                SPRITE_SHEET,
                x = i * FRAME_WIDTH,
                y = 0,
                width = FRAME_WIDTH,
                height = FRAME_HEIGHT,
            )
            self.textures.append(frame)

        # textura inicial
        self.texture = self.textures[0]

        # Frame actual
        self.current_frame = 0


    def update(self):
        """ Move the player """
        # Move player.
        # Remove these lines if physics engine is moving player.
        self.center_x += self.change_x
        self.center_y += self.change_y

        # Check for out-of-bounds
        if self.left < 0:
            self.left = 0
        elif self.right > WINDOW_WIDTH - 1:
            self.right = WINDOW_WIDTH - 1

        if self.bottom < 0:
            self.bottom = 0
        elif self.top > WINDOW_HEIGHT - 1:
            self.top = WINDOW_HEIGHT - 1



    def update_animation(self, delta_time: float = 1/60):
        self.current_frame = (self.current_frame + 1) % FRAME_COUNT
        self.texture = self.textures[self.current_frame]