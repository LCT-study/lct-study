from collections import deque

n, k = map(int, input().split())

graph = [] # 전체 보드 정보를 담는 리스트
data = [] # 바이러스에 대한 정보를 담은 리스트

for i in range(n):
    # 보드 정보를 한 줄 단위로 입력
    graph.append(list(map(int, input().split())))
    for j in range(n):
        if graph[i][j] != 0:
            data.append((graph[i][j], 0, i, j))

# 정렬 이후 큐로 옮기기(낮은 번호부터 증식하므로)
data.sort()
q = deque(data)

# 바이러스 퍼지는 4방향 위치
dx = [-1,0,1,0]
dy = [0,1,0,-1]

target_s, target_x, target_y = map(int, input().split()) 

# BFS 진행
while q:
    virus, s, x, y = q.popleft() # 처음에는 기존 오름차순 바이러스 정보를 받고 그 위치 상하좌우로 0인 경우 해당 바이러스로 변환 후 해당 위치 큐에 추가  
    if s == target_s:            # 그 후 계속 큐에 추가되는 바이러스 정보를 받는다. (정렬된 바이러스 순으로 추가되어 자동으로 정렬이 되어진다.)                                      
        break                    # 정한 초만큼 s가 증가했거나 큐가 사라지면  breack
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]    
        if nx >= 0 and nx < n and ny >= 0 and ny < n:
            if graph[nx][ny] == 0:
                graph[nx][ny] = virus
                q.append((virus, s+1, nx, ny))

print(graph[target_x-1][target_y-1])