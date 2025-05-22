"""
Hope this is readable :/
Player binds(so as not to forget): 1 - up, 2 - down, 3 - left, 4 - right.
"""
import pygame as pg

from Scripts.game_screen import game

if __name__ == "__main__":
    # pygame initialise
    pg.init()

    game()

    # Pygame quit
    pg.quit()
