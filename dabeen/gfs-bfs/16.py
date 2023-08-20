#기출 연구소 (다시풀기)
#0: 빈공간, 2 바이러스 , 1: 벽
#만일 0이 유지되면 바이러스가 퍼짐
#goal: 최대한의 안전 영역의 크기를 구해라

n,m = map(int,input().split())
data =[] #초기 맵
after = [[0] * m for _ in range(n)] #벽 설치 후

for _ in range(n):
    data.append(list(map(int,input().split())))

dx = [-1,0,1,0]
dy = [0,1,0,-1]

result = 0

#dfs 바이러스가 사방으로 퍼진경우..
def virus(x,y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        #상하좌우 중 바이러스가 퍼질 수 있는 경우의 수
        if nx>=0 and nx<n and ny>=0 and ny<m:
            if after[nx][ny] == 0:
                #해당 위치에 바이러스를 넣고, 다시 재귀적으로 돌림
                after[nx][ny] = 2
                virus(nx,ny)

def get_score():
    score = 0
    for i in range(n):
        for j in range(m):