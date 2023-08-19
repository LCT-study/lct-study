#특정한 도시 X로부터 출발하여 도달할 수 있는 모든 도시 중에서, 
# 최단 거리가 정확히 K인 모든 도시들의 번호

import sys
from collections import deque
input = sys.stdin.readline

# 도시 갯수, 도로 갯수, 거리 정보, 출발 도시 번호
n,m,k,x = map(int, input().split())
# start -> end : 이동가능한 단방향 도로 존재
graph = [[] for _ in range(n+1)]
distance=[0]*(n+1)
visited =  [False]*(n+1)
que = deque()
flag = False

for _ in range(m):
    start, end = map(int, input().split())
    graph[start].append(end)
    
    

def bfs(start):
    que.append(start)
    visited[start] = True
    while que:
        x = que.popleft()
        for nx in graph[x]:
            #print(nx, distance)
            if not(visited[nx]):
                visited[nx] = True
                distance[nx] = distance[x]+1
                que.append(nx)
            
        
bfs(x)
for idx, dist in enumerate(distance):
    if dist == k:
        flag = True
        print(idx)
        
if not(flag):
    print(-1)