# -*- coding: utf-8 -*-

import sys
import pygame
from pygame.locals import QUIT

# pygame モジュールの初期化
pygame.init()
SURFACE = pygame.display.set_mode((400,300))
# クロックオブジェクト
FPSCLOCK = pygame.time.Clock()

def main():

    """ main routine """
    sysfont = pygame.font.SysFont(None,36)
    counter = 0

    while True:

        # イベントキューからイベントを取得
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        counter += 1
        SURFACE.fill((0,0,0))
        count_image = sysfont.render("count is {}".format(counter), True, (255,255,255))
        SURFACE.blit(count_image, (50,50))
        pygame.display.update()

        # 10 FPS（1秒間に何回実行するかの調整）
        FPSCLOCK.tick(10)

if __name__ == "__main__":
    main()
