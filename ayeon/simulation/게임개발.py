import sys
input = sys.stdin.readline

row, col = map(int, input().split())
x,y,dir = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(row)]
#print(row, col, x, y, dir)
#print(graph)

LAND = 0 # 육지
SEA = 1 # 바다

# 방문 여부 확인
visited = [[False]*col for _ in range(row)]
visited[x][y] = True # 최초 위치 방문 처리

# 방향 전환 : (d+3)%4
# 북, 동, 남, 서
dx = [-1,0,1,0]
dy = [0, 1,0,-1]

answer = 1 # 처음 캐릭터가 있는 곳은 육지
turn = 0

while True:
    dir = (dir+3)%4
    nx, ny = x + dx[dir], y + dy[dir]
    # 회전한 방향에서 안 가본 곳 있음
    if graph[nx][ny] == LAND and not(visited[nx][ny]):
        visited[nx][ny]=True
        answer+=1
        turn = 0
        x, y = nx, ny
        continue # 뒤로 나오는 4방향 모두 방문한 경우에 대한 처리 필요 없음
    else: # 회전 : 해당 방향 이미 방문한 곳임 OR 바다임
        turn+=1
    
    # 4칸 모두 방문했거나 바다인 경우
    if turn==4:
        # 바라보는 방향 유지하고 뒤로 한칸
        nx = x - dx[dir]
        ny = y - dy[dir]
        if graph[nx][ny]==LAND:
            x, y = nx, ny
        else:
            break
        turn = 0 # 회전 횟수 초기화
print(answer)

"""
4 4
1 1 0 // (1, 1)에 북쪽(0)을 바라보고 서 있는 캐릭터
1 1 1 1
1 0 0 1
1 1 0 1
1 1 1 1

3
"""