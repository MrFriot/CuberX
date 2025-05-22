# Import
import pygame as pg

from Scripts.game_data import Data

# Pygame initialise
pg.init()


class Assets:
    # Load images
    class Img:
        ImgFractionRed: pg.Surface = pg.transform.scale(
            pg.image.load("Assets/Img/Player/fraction_red.png"), (Data.CellSize, Data.CellSize)
        )
        ImgFractionBlue: pg.Surface = pg.transform.scale(
            pg.image.load("Assets/Img/Player/fraction_blue.png"), (Data.CellSize, Data.CellSize)
        )
        ImgFractionGreen: pg.Surface = pg.transform.scale(
            pg.image.load("Assets/Img/Player/fraction_green.png"), (Data.CellSize, Data.CellSize)
        )
        ImgFractionYellow: pg.Surface = pg.transform.scale(
            pg.image.load("Assets/Img/Player/fraction_yellow.png"), (Data.CellSize, Data.CellSize)
        )
        ImgWall: pg.Surface = pg.transform.scale(
            pg.image.load("Assets/Img/Wall/wall.png"), (Data.CellSize, Data.CellSize)
        )
        ImgWallSide_in_Up: pg.Surface = pg.transform.scale(
            pg.image.load("Assets/Img/Wall/wall_circuit_up.png"), (Data.CellSize, Data.CellSize)
        )
        ImgWallSide_in_Down: pg.Surface = pg.transform.scale(
            pg.image.load("Assets/Img/Wall/wall_circuit_down.png"), (Data.CellSize, Data.CellSize)
        )
        ImgWallSide_in_Right: pg.Surface = pg.transform.scale(
            pg.image.load("Assets/Img/Wall/wall_circuit_right.png"), (Data.CellSize, Data.CellSize)
        )
        ImgWallSide_in_Left: pg.Surface = pg.transform.scale(
            pg.image.load("Assets/Img/Wall/wall_circuit_left.png"), (Data.CellSize, Data.CellSize)
        )
        ImgWallAngle_in_UpLeft: pg.Surface = pg.transform.scale(
            pg.image.load("Assets/Img/Wall/wall_angle_in_UpLeft.png"), (Data.CellSize, Data.CellSize)
        )
        ImgWallAngle_in_UpRight: pg.Surface = pg.transform.scale(
            pg.image.load("Assets/Img/Wall/wall_angle_in_UpRight.png"), (Data.CellSize, Data.CellSize)
        )
        ImgWallAngle_in_DownLeft: pg.Surface = pg.transform.scale(
            pg.image.load("Assets/Img/Wall/wall_angle_in_DownLeft.png"), (Data.CellSize, Data.CellSize)
        )
        ImgWallAngle_in_DownRight: pg.Surface = pg.transform.scale(
            pg.image.load("Assets/Img/Wall/wall_angle_in_DownRight.png"), (Data.CellSize, Data.CellSize)
        )
        ImgWallAngle_out_UpLeft: pg.Surface = pg.transform.scale(
            pg.image.load("Assets/Img/Wall/wall_angle_out_UpLeft.png"), (Data.CellSize, Data.CellSize)
        )
        ImgWallAngle_out_UpRight: pg.Surface = pg.transform.scale(
            pg.image.load("Assets/Img/Wall/wall_angle_out_UpRight.png"), (Data.CellSize, Data.CellSize)
        )
        ImgWallAngle_out_DownLeft: pg.Surface = pg.transform.scale(
            pg.image.load("Assets/Img/Wall/wall_angle_out_DownLeft.png"), (Data.CellSize, Data.CellSize)
        )
        ImgWallAngle_out_DownRight: pg.Surface = pg.transform.scale(
            pg.image.load("Assets/Img/Wall/wall_angle_out_DownRight.png"), (Data.CellSize, Data.CellSize)
        )
        ImgGrass: pg.Surface = pg.transform.scale(
            pg.image.load("Assets/Img/grass.png"), (Data.CellSize, Data.CellSize)
        )
        ImgApple: pg.Surface = pg.transform.scale(
            pg.image.load("Assets/Img/apple.png"), (Data.CellSize, Data.CellSize)
        )
        ImgIcon: pg.Surface = pg.transform.scale(
            pg.image.load("Assets/Img/icon.ico"), (Data.CellSize, Data.CellSize)
        )

    # Load sounds
    class Sound:
        SoundPlayerStep: pg.mixer.Sound = pg.mixer.Sound("Assets/Sound/step.mp3")
        SoundPickupApple: pg.mixer.Sound = pg.mixer.Sound("Assets/Sound/pickup.mp3")
        Sounds: list = [
            SoundPlayerStep,
            SoundPickupApple
        ]


# Pygame quit
pg.quit()
