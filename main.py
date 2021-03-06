# -*- coding: utf-8 -*-

import sys
import pygame
from pygame.locals import QUIT

# pygame モジュールの初期化
pygame.init()

# ウィンドウの作成し、 SURFACE に格納する
SURFACE = pygame.display.set_mode((400,300))
pygame.display.set_caption("Just Window")

def main():

    """ main routine """
    while True:

        # RGBを指定して色を塗る
        SURFACE.fill((255,255,255))

        # イベントキューからイベントを取得
        for event in pygame.event.get():

            # 終了ボタン待ち
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()

if __name__ == "__main__":
    main()
