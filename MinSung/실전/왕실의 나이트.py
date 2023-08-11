position = input()

x = ord(position[0]) - 96   #첫번째 원소를 아스키코드로 반환
y = int(position[1])
cnt = 0

dx = [-2, -2, -1, -1, 1, 1, 2, 2]
dy = [-1, 1, -2, 2, -2, 2, -1, 1]

for i in range(len(dx)):
    nx = x + dx[i]
    ny = y + dy[i]
    if nx <= 8 and nx >= 1 and ny <= 8 and ny >= 1:
        cnt = cnt + 1

print(cnt)    