n = int(input())
x, y = 1, 1
plans = input().split()

#L, R, U, D에 따른 이동 방향
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_types = ['L', 'R', 'U', 'D']

#이동 계획을 하나씩 확인
for plan in plans:
    for i in range(len(move_types)): #무브타입의 길이만큼 확인
        if plan == move_types[i]:      #계획과 무브타입이 같다면
            nx = x + dx[i]
            ny = y + dy[i]
    # 공간을 벗어나면 무시
    if nx < 1 or ny < 1 or nx > n or ny > n:
        continue
    #공간을 벗어나지 않을 때 이동 수행
    x, y = nx, ny
print(x, y)
