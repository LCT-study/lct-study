import sys
from collections import deque
input = sys.stdin.readline

row, col = map(int, input().split())
r, c, d = map(int,input().split())

# 0: 육지, 1: 바다
LAND = 0
SEA = 1
graph = [list(map(int, input().split())) for _ in range(row)]
que = deque()
visited = [[False]*col for _ in range(row)]

# 최초로 있는 곳 육지임
visited[r][c] = True
que.append([r,c])
count = 1 # 방문 육지 갯수
turn = 0 # 방향 전환 횟수

# 북, 동, 남, 서
dr = [-1, 0, +1, 0]
dc = [0,+1,0,-1]
# 반시계 방향 전환 : d = (d+3)%4 
# 북(0) -> 서(3) -> 남(2) -> 동(1)
# 후진 : d = (d+2)%4
# 북(0) -> 남(2), 서(3) -> 동(1) 


def isAble(r,c,row, col):
    if 0<=r<row and 0<=c<col:
        return True
    else:
        return False

while que:
    r, c = que.popleft()
    for _ in range(4):
        d = (d+3)%4 # 왼쪽 회전
        turn+=1
        nx, ny = r + dr[d], c+dc[d]
        # 유효한 범위 아닌 경우
        if not(isAble(nx,ny,row, col)):
            continue
        # 방문한 적 없고 바다 아님 
        if not(visited[nx][ny]) and graph[nx][ny]==LAND:
            turn = 0
            count+=1
            visited[nx][ny]=True
            que.append([nx,ny])
            break
    if turn ==4:
        d = (d+2)%4 # 후진
        nx, ny = r + dr[d], c + dc[d]
        # 바다인 경우
        if graph[nx][ny] == SEA: 
            break
        # 범위를 벗어난 경우
        if not(isAble(nx,ny,row, col)):
            break
        # 육지이면서 아직 방문 안한 경우
        if not(visited[nx][ny]):
            turn =0
            que.append([nx, ny])
        
print(count)   


#for i in visited:
#    print(i)
"""
4 4 
1 1 0
1 1 1 1
1 0 0 1
1 1 0 1
1 1 1 1
"""