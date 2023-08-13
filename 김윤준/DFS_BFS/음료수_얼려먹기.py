n,m = map(int, input().split())

graph = []
for i in range(n):
    graph.append(list(map(int,input())))


def dfs(x,y):
    if x<= -1 or x>= n or y <= -1 or y >= m :
        return False
    if graph[x][y] == 0: #자신이 0일 경우 과 주변 상하좌우 0인 요소들을 1로 바꾼다. 다 바꾸면 True
        graph[x][y] = 1  #그림으로 이해하면 편함
        dfs(x-1,y) 
        dfs(x,y-1)
        dfs(x+1,y)
        dfs(x,y+1)
        return True
    return False



result = 0 
for i in range(n):
    for j in range(m):
        if dfs(i,j) == True: # 0인 자신 외 주변을 1로 바꾸거나 1일 시 True가 나는 경우 : 상하좌우가 0으로 연결이 전부 완료된 경우. result + 1
            result += 1

print(result)