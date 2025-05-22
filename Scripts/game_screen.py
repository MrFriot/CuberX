import pygame as pg

from Scripts.data import GameName, FPS
from Scripts.game_setup import Setup
from Scripts.load_assets import Assets
from Scripts.game_data import Data, BlockId


def game() -> None:
    # add screen
    screen = pg.display.set_mode((Data.ScreenWidth_X, Data.ScreenHeight_Y), 0, 32, 0)
    pg.display.set_icon(Assets.Img.ImgIcon)

    # some code
    font = pg.font.SysFont("Linux Biolinum G", Data.ScreenHeight_Y // 10)
    is_final = False

    # main loop
    run_flag: bool = True
    while run_flag:
        pg.time.Clock().tick(FPS)
        pg.display.flip()

        # is final?
        if Data.FinalScore != -1:
            for fraction in Setup.Fractions:
                if fraction.Score >= Data.FinalScore:
                    is_final = True
                    msg = font.render(f"{fraction.Name} teem win!", False, (0, 0, 0))
                    screen.fill((255, 255, 255))
                    screen.blit(pg.transform.scale(fraction.Img, (Data.ScreenWidth_X // 4, Data.ScreenWidth_X // 4)),
                                (Data.ScreenWidth_X // 2 - Data.ScreenWidth_X // 8, Data.ScreenHeight_Y // 10))
                    screen.blit(msg, (Data.ScreenWidth_X // 2 - msg.get_width() // 2, Data.ScreenHeight_Y // 2))

        # draw
        if not is_final:
            __PlayerNum: int = -1
            for PLAYER in Setup.Players:
                __PlayerNum += 1
                screen.blit(PLAYER.Img, (PLAYER.Position[0] * Data.CellSize, PLAYER.Position[1] * Data.CellSize))
            for pos_y in range(Data.CellInScreenHeight_Y):
                for pos_x in range(Data.CellInScreenWidth_X):
                    match Data.Matrix[pos_y][pos_x]["Id"]:
                        case BlockId.IdGrass:
                            screen.blit(Assets.Img.ImgGrass, (pos_x * Data.CellSize, pos_y * Data.CellSize))
                        case BlockId.IdWall:
                            for wall in Setup.Walls:
                                if wall.Position == [pos_x, pos_y]:
                                    screen.blit(wall.Img, (pos_x * Data.CellSize, pos_y * Data.CellSize))
                        case BlockId.IdApple:
                            screen.blit(Assets.Img.ImgApple, (pos_x * Data.CellSize, pos_y * Data.CellSize))
                            for apple in Setup.Apples:
                                if apple.Position == [pos_x, pos_y]:
                                    screen.blit(apple.Img, (pos_x * Data.CellSize, pos_y * Data.CellSize))

        text: str = ''
        for i in Setup.Fractions:
            text += f" {i.Name}-{i.Score}"
        pg.display.set_caption(f"{GameName}     {text}", "Icon")

        # updates
        keys: pg.key.ScancodeWrapper = pg.key.get_pressed()
        if not is_final:
            for player in Setup.Players:
                player.moving(keys, Setup.Apples)
        for Event in pg.event.get():
            if Event.type == pg.QUIT or keys[pg.K_ESCAPE]:
                run_flag: bool = False
