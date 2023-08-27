import sys
import pygame
from pygame.locals import QUIT

# ゲーム画面を初期化
pygame.init()
screen = pygame.display.set_mode((800, 600))
back = (255, 200, 255)
Green = (0, 255, 0)
white = (255, 255, 255)
black = (0, 0, 0)

# ボードの初期設定 0:空白 1:○ 2:×
board_status = [[0, 0, 0],
                [0, 0, 0],
                [0, 0, 0]]

# プレイヤーの初期設定
player = 1  # 1:○ 2:×
px = 0  # プレイヤーの位置
py = 0


# マスの移動
def move(key):
    global px, py
    if key == K_UP:
        py = max(0, py - 1)
    elif key == K_DOWN:
        py = min(2, py + 1)
    elif key == K_RIGHT:
        px = min(2, px + 1)
    elif key == K_LEFT:
        px = max(0, px - 1)


# 終了フラグ
end_flag = False


# ボードの初期化
def reset_board():
    global board_status
    board_status = [[0, 0, 0],
                    [0, 0, 0],
                    [0, 0, 0]]


# メインループ
def main():
    global end_flag
    while True:
        # イベントを処理
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        # 画面を背景色でクリア
        screen.fill(back)

        # ボードの描画
        pygame.draw.rect(screen, Green, (175, 75, 450, 450))
        pygame.draw.line(screen, black, (325, 75), (325, 525), 5)
        pygame.draw.line(screen, black, (475, 75), (475, 525), 5)
        pygame.draw.line(screen, black, (175, 225), (625, 225), 5)
        pygame.draw.line(screen, black, (175, 375), (625, 375), 5)

        # 画面を更新
        pygame.display.update()


if __name__ == '__main__':
    main()
