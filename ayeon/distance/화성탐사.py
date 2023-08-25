from heapq import heappop, heappush
import sys
input = sys.stdin.readline

INF = int(1e9)
T = int(input())

for _ in range(T):
    n = int(input())   
    graph = [list(map(int, input().split())) for _ in range(n)]
    distance = [[INF]*n for _ in range(n)]
    
    start_r, start_c = 0, 0 
    heap = [[graph[start_r][start_c], start_r, start_c]]
    distance[start_r][start_c] = graph[start_r][start_c]
    
    dr=[-1,1,0,0]
    dc= [0,0,-1,1]
    while heap:
        dist, r, c = heappop(heap)
        if distance[r][c]<dist:
            continue
        for idx in range(4):
            nr = r + dr[idx]
            nc = c + dc[idx]
            if not(0<=nr<n and 0<=nc<n):
                continue
            cost = dist+graph[nr][nc]
            if distance[nr][nc]>cost:
                distance[nr][nc]=cost
                heappush(heap,[cost, nr, nc])
    
    print(distance[n-1][n-1])


"""
3
3
5 5 4
3 9 1
3 2 7
5
3 7 2 0 1
2 8 0 9 1
1 2 1 8 1
9 8 9 2 0
3 6 5 1 5
7
9 0 5 1 1 5 3
4 1 2 1 6 5 3
0 7 6 1 6 8 5
1 1 7 8 3 2 3
9 4 0 7 6 4 1
5 8 3 2 4 8 3
7 4 8 4 8 3 4
answ: 
20
19
36
"""