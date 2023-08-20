from collections import deque   #deque라이브러리 호출

n, m = map(int, input().split())

# 2차원 리스트의 맵 정보 입력 받기
graph = []
for i in range(n):
    graph.append(list(map(int, input()))) #문자열을 입력받아 int형 리스트로 만듦

#이동방향 (상하좌우)
dx = [-1, 1, 0, 0] 
dy = [0, 0, -1, 1]

def bfs(x, y):
    # 큐(Queue) 구현을 위해 deque 라이브러리 사용
    q = deque()
    q.append((x, y))
    #큐가 빌 때까지 반복
    while q:
        x, y = q.popleft()  # q에서 현재노드 꺼냄
        #현재 위치에서 4가지 방향으로 위치 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 맵 밖으로 나가면 false
            if nx<0 or nx>=n or ny<0 or ny>=m:
                continue
            # 괴물(0)인 경우 false
            if graph[nx][ny] == 0:
                continue
            # 첫번째 방문하는 경우만 최단 거리 기록:
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                q.append((nx, ny))
    # 가장 오른쪽 아래까지 최단 거리 반환
    return graph[n-1][m-1]

print(bfs(0, 0))              

