from heapq import heappop, heappush
import sys
input = sys.stdin.readline

INF = int(1e9)
# 헛간 갯수, 통로 갯수(양방향)
n,m=map(int, input().split())
graph = [[]*(n+1) for _ in range(n+1)]
distance = [INF]*(n+1)

startNode=1
distance[startNode]=0

for _ in range(m):
    start, end = map(int, input().split())
    graph[start].append([end, 1])
    graph[end].append([start,1])
# cost, 노드번호
heap=[[distance[startNode],startNode]]

while heap:
    dist, now = heappop(heap)
    if distance[now]<dist:
        continue
    for node, cost in graph[now]:
        if distance[node]>cost+dist:
            distance[node]=cost+dist
            heappush(heap,[distance[node],node])
            

minDistance = min(distance[start+1:])
minNode = distance.index(minDistance)
minCount = distance.count(minDistance)
# 헛간번호, 헛간거리, 동일한 헛간 거리 가진거 갯수
print( minNode, minDistance,minCount)

"""
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