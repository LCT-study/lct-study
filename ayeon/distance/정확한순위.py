import sys
input = sys.stdin.readline

INF = int(1e9)
n,m = map(int, input().split())
graph = [[INF]*(n+1) for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, n+1):
        if i == j:
            graph[i][j]=0
            
for _ in range(m):
    start, end = map(int, input().split())
    graph[start][end]=1
    

for mid in range(1,n+1):
    for start in range(1,n+1):
        for end in range(1,n+1):
            graph[start][end] = min(graph[start][end], graph[start][mid]+graph[mid][end])
#print(graph)      
result = 0
for i in range(1, n+1):
    count = 0
    for j in range(1, n+1):
        if graph[i][j]!=INF or graph[j][i]!=INF:
            count+=1 # 해당 노드 도달 가능
    #print(count)
    # 모든 노드 간 비교 가능하단 소리 = 순위 정확히 알 수 있음          
    if count==n:
        result+=1
        
print(result)

"""
6 6
1 5
3 4
4 2
4 6
5 2
5 4
ans: 1
"""