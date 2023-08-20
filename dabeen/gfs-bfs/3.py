#음료수 얼려먹기
n,m = map(int,input().split())

arr = [list(map(int,input().split())) for _ in range(n)]

def dfs(x,y):
    #범위를 벗어나는지 체크(그 즉시 종료)
    if x<=-1 or x>=n or y<=-1 or y>=m:
        return False
    #현재 노드를 방문하지 않았다?
    if arr[x][y] == 0:
        arr[x][y] = 1 #방문처리
        #이어지는 상하좌우도 다 검사 재귀처리 (방문처리만 함 , return x)
        dfs(x-1, y)
        dfs(x, y-1)
        dfs(x+1, y)
        dfs(x, y+1)
        #그 주변의 재귀함수들도 다 체크하고 최종적으로 return
        return True
    return False


#함수 실행
cnt = 0
for i in range(n):
    for j in range(m):
        #배열을 하나씩 돌리면서 방문여부 확인(DFS)
        if dfs(i,j) == True:
            cnt+=1 #최초 dfs 한 번 된 경우에만 cnt

print(cnt)
