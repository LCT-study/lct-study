import sys
from copy import deepcopy
from collections import deque
input = sys.stdin.readline

row, col = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(row)]

# 0은 빈 칸, 1은 벽, 2는 바이러스
dr = [-1,1,0,0]
dc = [0,0,-1,1]
answer = 0

# virusList
virusList = []

# 깊이 우선 탐색으로 각 바이러스 사방에 퍼지게
def spread(r,c, temp):
    for idx in range(4):
        nr = r + dr[idx]
        nc = c + dc[idx]
        
        if 0<=nr<row and 0<=nc<col:
            if temp[nr][nc] == 0: # 빈칸인 경우
                temp[nr][nc] = 2
                spread(nr,nc, temp)
                
                
# 현재 맵에서 안전 영역 크기 계산
def get_size(temp):
    size = 0
    for i in range(row):
        for j in range(col):
            if temp[i][j] == 0:
                size+=1
    #print(size)
    return size
    
def dfs(start,count):
    global answer
    
    if count==3:
        # 그래프 복사
        temp  = deepcopy(graph)
        
        # 바이러스 퍼트리기 
        for i in range(len(virusList)):
            r,c = virusList[i]
            spread(r,c, temp)

        answer = max(answer, get_size(temp))
        return
    
    for i in range(start, row*col):
        x = int(i/col)
        y = int(i%col)
        if graph[x][y] == 0:
            graph[x][y] = 1
            dfs(i+1,count+1)
            graph[x][y] = 0
            
for i in range(row):
    for j in range(col):
        if graph[i][j] == 2:
            virusList.append([i,j])

dfs(0,0)
print(answer)