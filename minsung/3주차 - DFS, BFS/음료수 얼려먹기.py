n, m = map(int, input().split()) # n(세로), m(가로)길이 입력

# 2차원 리스트의 맵 정보 입력 받기
graph = []
for i in range(n):
    graph.append(list(map(int, input()))) #문자열을 입력받아 int형 리스트로 만듦

#모든 노드(위치)에 대하여 음료수 채우기
def dfs(x, y):
    #종료 조건 1(범위 벗어날 때 종료):
    if x < 0 or x >= n or y < 0 or y >= m:
        return False
    # 현재 노드를 아직 방문 안했을 때
    if graph[x][y] == 0:
        #해당 노드 방문처리
        graph[x][y] = 1
        dfs(x, y-1) #좌
        dfs(x, y+1) #우
        dfs(x-1, y) #상
        dfs(x+1, y) #하
        return True
    # 종료 조건 2
    return False

cnt = 0
for i in range(n):
    for j in range(m):
        #현재 위치에서 DFS 수행
        if dfs(i, j):   #현재 위치에서 방문처리가 됐으면 카운트 수행
            cnt = cnt + 1
print(cnt)            
