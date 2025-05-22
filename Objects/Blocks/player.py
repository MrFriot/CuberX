# Import
from time import time
import pygame as pg
from Scripts.load_assets import Assets
from Scripts.game_data import Data, BlockId


# Fraction of player object
class Fraction:
    def __init__(self, fraction_name: str, fraction_img) -> None:
        self.Name: str = fraction_name
        self.Img = fraction_img
        self.Score: int = 0


# Player object
class Player:
    def __init__(self, position: list[int], fraction: Fraction, bind: dict[str]) -> None:
        Data.Matrix[position[1]][position[0]]["Id"] = BlockId.IdPlayer
        self.Fraction: Fraction = fraction
        self.Img = fraction.Img
        self.Position: list[int] = position
        self.Bind: dict[str] = bind
        self.StepTimer = time()

    def moving(self, pressed_keys, apples: list) -> None:
        if time() - self.StepTimer >= Data.PlayerSpeed:
            step_flag = False

            if pressed_keys[eval(f"pg.constants.{self.Bind['1']}")] and not step_flag:
                if Data.CellInScreenHeight_Y > self.Position[1] - 1 >= 0:
                    if Data.Matrix[self.Position[1] - 1][self.Position[0]]["Id"] == BlockId.IdGrass:
                        Data.Matrix[self.Position[1]][self.Position[0]]["Id"] = BlockId.IdGrass
                        self.Position[1] -= 1
                        Assets.Sound.SoundPlayerStep.play()
                        self.StepTimer = time()
                    elif Data.Matrix[self.Position[1] - 1][self.Position[0]]["Id"] == BlockId.IdApple:
                        if Data.IsAppleRespawn:
                            for apple in apples:
                                if apple.Position == [self.Position[0], self.Position[1] - 1]:
                                    apple.respawn()
                        Data.Matrix[self.Position[1]][self.Position[0]]["Id"] = BlockId.IdGrass
                        self.Position[1] -= 1
                        self.Fraction.Score += 1
                        Assets.Sound.SoundPlayerStep.play()
                        Assets.Sound.SoundPickupApple.play()
                        self.StepTimer = time()

            elif pressed_keys[eval(f"pg.constants.{self.Bind['2']}")] and not step_flag:
                if Data.CellInScreenHeight_Y > self.Position[1] + 1 >= 0:
                    if Data.Matrix[self.Position[1] + 1][self.Position[0]]["Id"] == BlockId.IdGrass:
                        Data.Matrix[self.Position[1]][self.Position[0]]["Id"] = BlockId.IdGrass
                        self.Position[1] += 1
                        Assets.Sound.SoundPlayerStep.play()
                        self.StepTimer = time()
                    elif Data.Matrix[self.Position[1] + 1][self.Position[0]]["Id"] == BlockId.IdApple:
                        if Data.IsAppleRespawn:
                            for apple in apples:
                                if apple.Position == [self.Position[0], self.Position[1] + 1]:
                                    apple.respawn()
                        Data.Matrix[self.Position[1]][self.Position[0]]["Id"] = BlockId.IdGrass
                        self.Position[1] += 1
                        self.Fraction.Score += 1
                        Assets.Sound.SoundPlayerStep.play()
                        Assets.Sound.SoundPickupApple.play()
                        self.StepTimer = time()
            elif pressed_keys[eval(f"pg.constants.{self.Bind['3']}")] and not step_flag:
                if Data.CellInScreenWidth_X > self.Position[0] - 1 >= 0:
                    if Data.Matrix[self.Position[1]][self.Position[0] - 1]["Id"] == BlockId.IdGrass:
                        Data.Matrix[self.Position[1]][self.Position[0]]["Id"] = BlockId.IdGrass
                        self.Position[0] -= 1
                        Assets.Sound.SoundPlayerStep.play()
                        self.StepTimer = time()
                    elif Data.Matrix[self.Position[1]][self.Position[0] - 1]["Id"] == BlockId.IdApple:
                        if Data.IsAppleRespawn:
                            for apple in apples:
                                if apple.Position == [self.Position[0] - 1, self.Position[1]]:
                                    apple.respawn()
                        Data.Matrix[self.Position[1]][self.Position[0]]["Id"] = BlockId.IdGrass
                        self.Position[0] -= 1
                        self.Fraction.Score += 1
                        Assets.Sound.SoundPlayerStep.play()
                        Assets.Sound.SoundPickupApple.play()
                        self.StepTimer = time()
            elif pressed_keys[eval(f"pg.constants.{self.Bind['4']}")] and not step_flag:
                if Data.CellInScreenWidth_X > self.Position[0] + 1 >= 0:
                    if Data.Matrix[self.Position[1]][self.Position[0] + 1]["Id"] == BlockId.IdGrass:
                        Data.Matrix[self.Position[1]][self.Position[0]]["Id"] = BlockId.IdGrass
                        self.Position[0] += 1
                        Assets.Sound.SoundPlayerStep.play()
                        self.StepTimer = time()
                    elif Data.Matrix[self.Position[1]][self.Position[0] + 1]["Id"] == BlockId.IdApple:
                        if Data.IsAppleRespawn:
                            for apple in apples:
                                if apple.Position == [self.Position[0] + 1, self.Position[1]]:
                                    apple.respawn()
                        Data.Matrix[self.Position[1]][self.Position[0]]["Id"] = BlockId.IdGrass
                        self.Position[0] += 1
                        self.Fraction.Score += 1
                        Assets.Sound.SoundPlayerStep.play()
                        Assets.Sound.SoundPickupApple.play()
                        self.StepTimer = time()
            Data.Matrix[self.Position[1]][self.Position[0]]["Id"] = BlockId.IdPlayer
