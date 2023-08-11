from collections import deque   #deque라이브러리 호출

#도시의 개수, 도로의 개수, 거리 정보, 출발 도시 번호
n, m, k, x = map(int, input().split())
# 2차원 리스트의 맵 정보 입력 받기
graph = [[] for _ in range(n+1)] #city[0]부터 city[n]까지 총 n+1개의 빈 리스트가 생성
#모든 도로 정보 입력 받기
for i in range(n):
    a, b = map(int, input().split())
    graph[a].append(b)

#최단 거리를 저장하기 위한 1차원 배열 생성
distance = [-1]*(n+1)
distance[x] = 0 # 출발 도시(x)까지의 거리는 0으로 지정

q = deque([x])
while q:
    now = q.popleft()
    #현재 도시에서 이동할 수 있는 모든 도시를 확인
    for neighbor in graph[now]:
        #아직 방문x 도시라면
        if distance[neighbor] == -1:
            #최단 거리 갱신
            #방문한 도시는 무조건 최단 거리이므로, 방문하지 않은 도시에 대해서만 업데이트하면 됨
            distance[neighbor] = distance[now] + 1
            q.append(neighbor)

#최단 거리가 k인 모든 도시를 오름차순 출력
find = False
for i in range(1, n+1):
    if distance[i] == k:
        print(i)
        find = True
#만약 최단 거리가 k인 도시가 없다면, -1 출력
if find == False:
    print(-1)        

