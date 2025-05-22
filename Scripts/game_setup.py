# Import
import pygame as pg

from Objects.Blocks.apple import Apple
from Scripts.load_assets import Assets
from Scripts.game_data import Data, BlockId
from Objects.Blocks.player import Fraction, Player
from Objects.Blocks.wall import Wall

# Pygame initialise
pg.mixer.init()


class Setup:
    # Sound settings
    Assets.Sound.SoundPlayerStep.set_volume(0.25)
    if not Data.IsSoundsOn:
        sound: pg.mixer.Sound
        for sound in Assets.Sound.Sounds:
            sound.set_volume(0)

    # Object's lists
    Walls: list = []
    Fractions = []
    Players: list = []
    Apples: list = []

    # Insert objects
    for pos_y in range(Data.CellInScreenHeight_Y):
        for pos_x in range(Data.CellInScreenWidth_X):
            Block: dict = Data.Matrix[pos_y][pos_x]
            match Block["Id"]:
                case BlockId.IdWall:
                    Walls.append(Wall([pos_x, pos_y]))
                case BlockId.IdApple:
                    Apples.append(Apple([pos_x, pos_y]))
                case BlockId.IdPlayer:
                    match Block["Fraction"]:
                        case "red":
                            Fractions.append(Fraction(Block["Fraction"], Assets.Img.ImgFractionRed))
                        case "blue":
                            Fractions.append(Fraction(Block["Fraction"], Assets.Img.ImgFractionBlue))
                        case "green":
                            Fractions.append(Fraction(Block["Fraction"], Assets.Img.ImgFractionGreen))
                        case "yellow":
                            Fractions.append(Fraction(Block["Fraction"], Assets.Img.ImgFractionYellow))
                    for fraction in Fractions:
                        if fraction.Name == Block["Fraction"]:
                            Players.append(Player([pos_x, pos_y], fraction, Block["Binds"]))


# Pygame quit
pg.quit()
