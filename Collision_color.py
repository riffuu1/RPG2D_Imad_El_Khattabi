# Author : El Khattabi Imad
# Date: 28.04.2026
# Version : 1.0

import pygame

obstacle_colors = [(0, 0, 0),(255,255,255),(255,216,0)]

def check_collision_with_color(surface, x, y):
    # --- Checks if a pixel on the surface matches a collision color.Returns True if a collision is detected. ---

    # --- Check if the pixel is within the screen ---
    if x < 0 or y < 0 or x >= surface.get_width() or y >= surface.get_height():
        return True  # outside map → considered collision

    color = surface.get_at((x, y))[:3]  # --- Ignore alpha channel ---

    # --- Compare with all forbidden colors ---
    return color in obstacle_colors