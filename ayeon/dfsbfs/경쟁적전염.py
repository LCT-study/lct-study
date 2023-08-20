from collections import deque

n,k = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
target_s, target_x, target_y = map(int, input().split())

dr = [-1,1,0,0]
dc = [0,0,-1,1]

# 바이러스 최초 위치 - 우선 순위 고려 X
data = []


for i in range(n):
    for j in range(n):
        if graph[i][j]!=0:
            # 바이러스 종류, 현재 시간, r, c
            data.append((graph[i][j],0,i,j))

# 바이러스 종류 기준 오름 차순 정렬 -  우선 순위 맞추기 진행            
data.sort()
que = deque(data)

# bfs
while que:
    v, s, r, c =que.popleft()
    if s == target_s:
        break
    
    for idx in range(4):
        nr, nc = r + dr[idx], c + dc[idx]
        if not(0<=nr<n and 0<=nc<n):
            continue
        if graph[nr][nc]==0:
            graph[nr][nc] = v #graph[r][c]와 동일
            que.append((graph[nr][nc], s+1, nr, nc))
            
            
print(graph[target_x-1][target_y-1])
            