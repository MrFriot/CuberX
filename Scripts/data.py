from glob import glob

GameName: str = "Cuber-X"
DataFilenameList: list = glob("Level/*.json")
GameLevelPath: str = DataFilenameList[0]
FPS: int = 60
