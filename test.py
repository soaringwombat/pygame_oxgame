import sys
import pygame
from pygame.locals import (QUIT, KEYDOWN,
                           K_UP, K_DOWN, K_RIGHT, K_LEFT,
                           K_SPACE, K_ESCAPE, K_1)

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


# ○の表示
def draw_circle(x, y):
    pygame.draw.circle(screen, black, (x * 150 + 250, y * 150 + 150), 50, 5)


# ×の表示
def draw_x(x, y):
    pygame.draw.line(screen, black, (x * 150 + 200, y * 150 + 100),
                     (x * 150 + 300, y * 150 + 200), 5)
    pygame.draw.line(screen, black, (x * 150 + 200, y * 150 + 200),
                     (x * 150 + 300, y * 150 + 100), 5)


# 列ができているか判定
def check_column():
    if board_status[0][0] == board_status[1][0] == board_status[2][0] != 0:
        return True
    elif board_status[0][1] == board_status[1][1] == board_status[2][1] != 0:
        return True
    elif board_status[0][2] == board_status[1][2] == board_status[2][2] != 0:
        return True
    elif board_status[0][0] == board_status[1][1] == board_status[2][2] != 0:
        return True
    elif board_status[0][2] == board_status[1][1] == board_status[2][0] != 0:
        return True
    elif board_status[0][0] == board_status[0][1] == board_status[0][2] != 0:
        return True
    elif board_status[1][0] == board_status[1][1] == board_status[1][2] != 0:
        return True
    elif board_status[2][0] == board_status[2][1] == board_status[2][2] != 0:
        return True
    else:
        return False


# 引き分けの判定
def check_draw():
    for x in range(3):
        for y in range(3):
            if board_status[y][x] == 0:
                return False
    return True


# キー入力を処理
def push_key(key):
    global px, py, player
    if key == K_UP:
        py = max(0, py - 1)
    elif key == K_DOWN:
        py = min(2, py + 1)
    elif key == K_RIGHT:
        px = min(2, px + 1)
    elif key == K_LEFT:
        px = max(0, px - 1)
    elif key == K_SPACE:
        if board_status[py][px] == 0:
            board_status[py][px] = player
            if player == 1:
                player = 2
            else:
                player = 1
    elif key == K_1:
        reset_board()
    elif key == K_ESCAPE:
        pygame.quit()
        sys.exit()


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
    global px, py
    global end_flag
    while True:
        # 画面を背景色でクリア
        screen.fill(back)
        # ボード背景の描画
        pygame.draw.rect(screen, Green, (175, 75, 450, 450))
        pygame.draw.line(screen, black, (325, 75), (325, 525), 5)
        pygame.draw.line(screen, black, (475, 75), (475, 525), 5)
        pygame.draw.line(screen, black, (175, 225), (625, 225), 5)
        pygame.draw.line(screen, black, (175, 375), (625, 375), 5)
        # ボードの描画
        for x in range(3):
            for y in range(3):
                if board_status[y][x] == 1:
                    draw_circle(x, y)
                elif board_status[y][x] == 2:
                    draw_x(x, y)
        # 選択中のマスを描画
        pygame.draw.rect(screen, white,
                         (175 + px * 150, 75 + py * 150, 150, 150), 5)
        # 列判定
        if check_column():
            end_flag = True
        # 引き分け判定
        if check_draw():
            end_flag = True

        # # 終了を判定して表示
        # if end_flag:
        #     pygame.draw.rect(screen, white, (175, 0, 450, 75))
        #     if check_column():
        #         if player == 1:
        #             font = pygame.font.SysFont(None, 100)
        #             text = font.render("○の勝ち", True, black)
        #             screen.blit(text, (200, 10))
        #         else:
        #             font = pygame.font.SysFont(None, 100)
        #             text = font.render("×の勝ち", True, black)
        #             screen.blit(text, (200, 10))
        #     else:
        #         font = pygame.font.SysFont(None, 100)
        #         text = font.render("引き分け", True, black)
        #         screen.blit(text, (200, 10))

        # 画面を更新
        pygame.display.update()
        # イベントを処理
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                push_key(event.key)


if __name__ == '__main__':
    main()
