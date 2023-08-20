#실전 미로탈출(다시)

from collections import deque

n,m = map(int, input().split())
graph = []
for i in range(n):
    graph.append(list(map(int,input())))

#[상,하,좌,우]
dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(x,y):
    queue = deque()
    queue.append((x,y))
    #큐가 다 비여질 때까지
    while queue:
        print("queue 상태 : ", queue)
        x,y = queue.popleft()
        print("x,y는 ", x,y)
        #현 위치에서 네가지 방향으로 위치 탐색
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            #미로 찾기 공간을 벗어난 경우 무시
            if nx<0 or ny<0 or nx>=n or ny >= m:
                continue
            #벽인 경우엔 무시
            if graph[nx][ny] == 0:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))
    return graph[n-1][m-1]

print(bfs(0,0))