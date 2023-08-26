import sys
from collections import deque
#바이러스는 낮은 번호부터 증식하므로, 초기 큐에, 번호가 낮은 바이러스부터 삽입
# 시험관 크기 및 바이러스 종류 저장
n, k = map(int, sys.stdin.readline().split())

# 바이러스 정보 저장
graph = []
# 바이러스의 추가 정보 저장
data = []

for i in range(n):
    graph.append(list(map(int, sys.stdin.readline().split())))
    # 바이러스의 추가 정보 저장 
    for j in range(n):
        # 해당 위치에 바이러스가 존재하는 경우
        if (graph[i][j] != 0):
            # 바이러스 종류, 확산 시간, x축 위치, y축 위치
            data.append((graph[i][j], 0, i, j))

# 바이러스를 번호가 낮은 순서대로 정렬
data.sort()
# 바이러스 추가 정보를 큐로 변환
q = deque(data)

# 결과를 위한 입력 [S초와 (X,Y)에 존재하는 바이러스의 종류]
s, x, y = map(int, sys.stdin.readline().split())

# 상하좌우 이동을 위한 좌표
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

while (q):

    # 현재 위치
    virus, time, i, j = q.popleft()

    # 현재 위치의 바이러스가 S초까지 확산된 바이러스라면 종료
    if (time == s):
        break

    # 상하좌우로 바이러스 확산
    for l in range(4):
        nx = i + dx[l]
        ny = j + dy[l]
        # 해당 위치로 확산될 수 있을 경우
        if (0<= nx and nx < n and 0 <= ny and ny < n and graph[nx][ny] == 0):
            # 그래프에 바이러스 확산 표시
            graph[nx][ny] = virus
            # 큐에 삽입
            q.append((virus, time+1, nx, ny))

print(graph[x-1][y-1])