# Import
from json import load

from numpy import array

from Scripts.data import GameLevelPath

# Load data
with open(GameLevelPath, 'r') as data_file:
    _Data: dict = load(data_file)


# Game data
class Data:
    TickRate: float = 1 / _Data["TickRate"]
    Matrix = array(_Data["Matrix"], dict)
    CellSize: int = _Data["CellSize"]
    FinalScore: int = _Data["FinalScore"]
    IsAppleRespawn: bool = _Data["IsAppleRespawn"]
    IsSoundsOn: bool = _Data["IsSoundsOn"]
    PlayerSpeed: float = 1 / _Data["PlayerSpeed"]

    # support subjects
    CellInScreenWidth_X: int = Matrix.shape[1]
    CellInScreenHeight_Y: int = Matrix.shape[0]
    ScreenWidth_X: int = CellSize * CellInScreenWidth_X
    ScreenHeight_Y: int = CellSize * CellInScreenHeight_Y


# ID of blocks in game
class BlockId:
    IdGrass: int = 0
    IdPlayer: int = 1
    IdWall: int = 2
    IdApple: int = 3
