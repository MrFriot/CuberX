# Import
from random import choice

import pygame as pg

from Scripts.load_assets import Assets
from Scripts.game_data import Data, BlockId


# Apple object
class Apple:
    def __init__(self, position: list[int]) -> None:
        self.Position: list[int] = position
        Data.Matrix[self.Position[1]][self.Position[0]]["Id"] = BlockId.IdApple
        self.Img: pg.Surface = Assets.Img.ImgApple

    def respawn(self) -> None:
        free_positions: list = []
        for pos_y in range(Data.CellInScreenHeight_Y):
            for pos_x in range(Data.CellInScreenWidth_X):
                if Data.Matrix[pos_y][pos_x]["Id"] == BlockId.IdGrass:
                    free_positions.append([pos_x, pos_y])
        if free_positions:
            Data.Matrix[self.Position[1]][self.Position[0]]["Id"] = BlockId.IdGrass
            self.Position: list[int] = choice(free_positions)
            Data.Matrix[self.Position[1]][self.Position[0]]["Id"] = BlockId.IdApple
