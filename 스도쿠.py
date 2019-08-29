# import sys
# sys.stdin = open("input.txt", "r")
import sys
I = sys.stdin.readline
def back(x, y):
    for i in range(9):
        if board[x][i] != 0 and visit[board[x][i]] == 0:
            visit[board[x][i]] = 1
    for i in range(9):
        if board[i][y] != 0 and visit[board[i][y]] == 0:
            visit[board[i][y]] = 1
    for i in range(3):
        for j in range(3):
            if board[x//3*3 + i][y//3*3 + j] != 0 and visit[board[x//3*3 + i][y//3*3 + j]] == 0:
                visit[board[x // 3 * 3 + i][y // 3 * 3 + j]] = 1
    for i in range(1, 10):
        if visit[i] == 0:
            board[x][y] = i


board = []
for _ in range(9):
    board.append(list(map(int, I().split())))

for i in range(9):
    for j in range(9):
        if board[i][j] == 0:
            back(i, j)

visit = [0] * 10
for i in board:
    print(*i)