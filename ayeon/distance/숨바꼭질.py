import sys
from heapq import heappush, heappop
input = sys.stdin.readline

INF = int(1e9)
# 헛간 갯수, 양방향 통로 갯수
n,m = map(int, input().split())
graph = [[] for _ in range(n+1)]
distance=[INF]*(n+1)
for _ in range(m):
    start, end = map(int, input().split())
    graph[start].append([end,1])
    graph[end].append([start,1])
    
start=1
distance[start]=0
heap=[]
heappush(heap,[distance[start],start])

while heap:
    dist, node = heappop(heap)
    if distance[node]<dist:
        continue
    for next_, cost in graph[node]:
        if distance[next_]>cost+distance[node]:
            distance[next_]=cost+distance[node]
            heappush(heap,[distance[next_],next_])

print(distance)

maxDistance = max(distance[1:])
count = distance.count(maxDistance)
node = distance.index(maxDistance)

# 헛간번호, 헛간거리, 동일한 헛간 거리 가진거 갯수
print(node, maxDistance, count)

"""숨바꼭질
6 7
3 6
4 3
3 2
1 3
1 2
2 4
5 2
ans: 
4 2 3
"""