row, col = map(int, input().split())
now_x, now_y, d = map(int, input().split())

dir = [0, 3, 2, 1]  # 북서남동
dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]

board = []
cnt = 1
for i in range(row):
    board.append(list(map(int, input().split())))

idx = dir.index(d)+1
while(1):
    board[now_y][now_x] = 1
    wx = now_x + dx[idx]
    wy = now_y + dy[idx]

    if board[wy][wx] == 0:
        now_x = wx
        now_y = wy
        board[wy][wx] = 1
        cnt += 1

    if idx < 3:
        idx += 1
    else:
        idx = 0
    
    count_n = 0
    for i in board:
        if 0 not in i:
            count_n += 1
    if count_n == row:
        break

print(cnt)
