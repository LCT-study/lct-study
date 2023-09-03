import sys
input = sys.stdin.readline
from heapq import heappush, heappop

# 도시 갯수, 통로 갯수, 시작 도시
n, m, start = map(int, input().split())
graph = [[] for _ in range(n+1)]
INF = int(1e9)
for _ in range(m):
    start, end, cost = map(int, input().split())
    graph[start].append([end, cost])
    
distance =[INF for _ in range(n+1)] 
heap = []

def dijsktra(start):
    distance[start] = 0
    heappush(heap, [0, start])
    
    while heap:
        dist, curr = heappop(heap)
        if distance[curr]<dist:
            continue
        for next_, cost in graph[curr]:
            cost_ = dist+cost
            if distance[next_]>cost_:
                distance[next_]=cost_
                heappush(heap,[cost_,next_])

dijsktra(1)

count=0
min_distance = -INF
for i in distance[1:]:
    if i!=0:
        count+=1
        min_distance = max(min_distance, i)
        
print(count, min_distance)
        
"""
3 2 1
1 2 4
1 3 2
ans: 2 4
"""