# Import
from Scripts.load_assets import Assets
from Scripts.game_data import Data, BlockId


# Wall object
class Wall:
    def __init__(self, position: list[int]) -> None:
        self.Position: list[int] = position
        Data.Matrix[self.Position[1]][self.Position[0]]["Id"] = BlockId.IdWall
        self.Img = Assets.Img.ImgWall.copy()
        # Overlaying
        # side
        if self.Position[1] != 0:
            if Data.Matrix[self.Position[1] - 1, self.Position[0]]["Id"] != BlockId.IdWall:
                self.Img.blit(Assets.Img.ImgWallSide_in_Up, (0, 0))
        try:
            if Data.Matrix[self.Position[1] + 1, self.Position[0]]["Id"] != BlockId.IdWall:
                self.Img.blit(Assets.Img.ImgWallSide_in_Down, (0, 0))
        except Exception:
            pass
        if self.Position[0] != 0:
            if Data.Matrix[self.Position[1], self.Position[0] - 1]["Id"] != BlockId.IdWall:
                self.Img.blit(Assets.Img.ImgWallSide_in_Left, (0, 0))
        try:
            if Data.Matrix[self.Position[1], self.Position[0] + 1]["Id"] != BlockId.IdWall:
                self.Img.blit(Assets.Img.ImgWallSide_in_Right, (0, 0))
        except Exception:
            pass
        # angle in
        try:
            if Data.Matrix[self.Position[1] - 1, self.Position[0] - 1]["Id"] != BlockId.IdWall and \
                    Data.Matrix[self.Position[1], self.Position[0] - 1]["Id"] != BlockId.IdWall and \
                    Data.Matrix[self.Position[1] - 1, self.Position[0]]["Id"] != BlockId.IdWall:
                self.Img.blit(Assets.Img.ImgWallAngle_in_UpLeft, (0, 0))
        except Exception:
            pass
        try:
            if Data.Matrix[self.Position[1] + 1, self.Position[0] - 1]["Id"] != BlockId.IdWall and \
                    Data.Matrix[self.Position[1], self.Position[0] - 1]["Id"] != BlockId.IdWall and \
                    Data.Matrix[self.Position[1] + 1, self.Position[0]]["Id"] != BlockId.IdWall:
                self.Img.blit(Assets.Img.ImgWallAngle_in_DownLeft, (0, 0))
        except Exception:
            pass
        try:
            if Data.Matrix[self.Position[1] - 1, self.Position[0] + 1]["Id"] != BlockId.IdWall and \
                    Data.Matrix[self.Position[1], self.Position[0] + 1]["Id"] != BlockId.IdWall and \
                    Data.Matrix[self.Position[1] - 1, self.Position[0]]["Id"] != BlockId.IdWall:
                self.Img.blit(Assets.Img.ImgWallAngle_in_UpRight, (0, 0))
        except Exception:
            pass
        try:
            if Data.Matrix[self.Position[1] + 1, self.Position[0] + 1]["Id"] != BlockId.IdWall and \
                    Data.Matrix[self.Position[1], self.Position[0] + 1]["Id"] != BlockId.IdWall and \
                    Data.Matrix[self.Position[1] + 1, self.Position[0]]["Id"] != BlockId.IdWall:
                self.Img.blit(Assets.Img.ImgWallAngle_in_DownRight, (0, 0))
        except Exception:
            pass
        # Angle out
        try:
            if Data.Matrix[self.Position[1] - 1, self.Position[0] - 1]["Id"] != BlockId.IdWall and \
                    Data.Matrix[self.Position[1], self.Position[0] - 1]["Id"] == BlockId.IdWall and \
                    Data.Matrix[self.Position[1] - 1, self.Position[0]]["Id"] == BlockId.IdWall:
                self.Img.blit(Assets.Img.ImgWallAngle_out_UpLeft, (0, 0))
        except Exception:
            pass
        try:
            if Data.Matrix[self.Position[1] + 1, self.Position[0] - 1]["Id"] != BlockId.IdWall and \
                    Data.Matrix[self.Position[1], self.Position[0] - 1]["Id"] == BlockId.IdWall and \
                    Data.Matrix[self.Position[1] + 1, self.Position[0]]["Id"] == BlockId.IdWall:
                self.Img.blit(Assets.Img.ImgWallAngle_out_DownLeft, (0, 0))
        except Exception:
            pass
        try:
            if Data.Matrix[self.Position[1] - 1, self.Position[0] + 1]["Id"] != BlockId.IdWall and \
                    Data.Matrix[self.Position[1], self.Position[0] + 1]["Id"] == BlockId.IdWall and \
                    Data.Matrix[self.Position[1] - 1, self.Position[0]]["Id"] == BlockId.IdWall:
                self.Img.blit(Assets.Img.ImgWallAngle_out_UpRight, (0, 0))
        except Exception:
            pass
        try:
            if Data.Matrix[self.Position[1] + 1, self.Position[0] + 1]["Id"] != BlockId.IdWall and \
                    Data.Matrix[self.Position[1], self.Position[0] + 1]["Id"] == BlockId.IdWall and \
                    Data.Matrix[self.Position[1] + 1, self.Position[0]]["Id"] == BlockId.IdWall:
                self.Img.blit(Assets.Img.ImgWallAngle_out_DownRight, (0, 0))
        except Exception:
            pass

    def __eq__(self, other):
        return BlockId.IdWall == other

    def __ne__(self, other):
        return BlockId.IdWall != other
