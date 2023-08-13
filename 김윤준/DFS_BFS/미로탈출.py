# from collections import deque

# n,m = map(int, input().split())

# graph = []
# for i in range(n):
#     graph.append(list(map(int,input())))


# move = []

# def bfs(x, y ,move):
#     if x < n and y < m:
#         if graph[x][y] == 1:
#             print(x, y, move)
#             if x == n-1 and y == m-1:
#                 return move
#             move.append(1)
#             bfs(x+1, y, move)
#             bfs(x, y+1, move)
#     return move


# moveSum = bfs(0, 0, move)
# print(len(moveSum))

from collections import deque

n, m = map(int, input().split())

graph = []
for i in range(n):
    graph.append(list(map(int, input())))

# 이동할 네 가지 방향 정의 (상, 하, 좌, 우)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    queue = deque()
    queue.append((x, y))

    while queue:
        x, y = queue.popleft()

        # 현재 위치에서 네 방향으로의 위치 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 미로 찾기 공간을 벗어난 경우 무시
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue

            # 벽인 경우 무시
            if graph[nx][ny] == 0:
                continue

            # 해당 노드를 처음 방문하는 경우에만 최단 거리 기록
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                print(graph)
                queue.append((nx, ny))

    return graph[n - 1][m - 1]

print(bfs(0, 0))
