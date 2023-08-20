#특정 거리의 도시 찾기 (다시풀기)

from collections import deque

n,m,k,x = map(int,input().split())
graph = [[] for _ in range((n+1))]

for i in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)

#모든 도시 최단 거리를 초기화
distance = [-1]*(n+1)
distance[x] = 0 #출발 도시까지 거리 0

q = deque([x])
while q:
    now = q.popleft()
    print("now가 뭔가 " + now)
    #현 시점에서 이동할 수 있는 모든 도시
    for next_n in graph[now]:
        #방문 ㄴ
        if distance[next_n] == -1:
            #최단 거리 갱신
            distance[next_n] = distance[now] + 1
            q.append(next_n)

#최단 거리가 k인 모든 도시의 번호를 오름차순으로
check = False
for i in range(1,n+1):
    if distance[i] == k:
        print(i)
        check = True

#만약 최단 거리가 k인 도시가 없다면, -1
if check == False:
    print(-1)