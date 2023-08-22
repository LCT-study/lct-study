import sys
from heapq import heappop, heappush
input = sys.stdin.readline

INF = int(1e9)
n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    start, end = map(int, input().split())
    graph[start].append([end, 1])
    graph[end].append([start, 1])
# 1 -> k -> x
x, k = map(int, input().split())

def dijsktra(start, end):
    heap = []
    distance = [INF for _ in range(n+1)]
    distance[start] = 0
    heappush(heap,[start, 0])
    
    while heap:
        curr, dist = heappop(heap)
        if distance[curr]<dist:
            continue
        for next_, cost in graph[curr]:
            #print("next: ",next_)
            cost_ = dist+cost
            if distance[next_]>cost_:
                distance[next_] = cost_
                heappush(heap, [next_,cost_ ])
        #print(distance)
    
    
    return distance[end]
    
answer = dijsktra(1, k)+dijsktra(k,x)
if answer>=INF:
    print(-1)
else:
    print(answer)

"""
5 7
1 2
1 3
1 4
2 4
3 4
3 5
4 5
4 5
ans: 3
"""

"""
4 2
1 3
2 4
3 4
ans: -1
"""

"""
5 7
1 2
1 3
1 4
2 4
3 4
3 5
4 5
4 5
ans: 3
"""

"""
4 2
1 3
2 4
3 4
ans: -1
"""