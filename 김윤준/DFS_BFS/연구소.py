import itertools
import copy

n,m = map(int,input().split())
current_lab = []
for i in range(n):
    current_lab.append(list(map(int,input().split())))

dx = [-1,0,1,0]
dy = [0,1,0,-1]

data = []

for i in range(n):
    for j in range(m):
        if current_lab[i][j] == 0:
            data.append([i,j])

iter_data = list(itertools.combinations(data,3))


def virus(x,y):
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]

        # 퍼질 수 있음
        if nx>-1 and ny>-1 and nx < n and ny < m :
            if after_lab[nx][ny] == 0:
                after_lab[nx][ny] = 2
                virus(nx,ny)



def count_safe(now):
    safe_count = 0
    for i in range(n):
        safe_count += now[i].count(0)

    return safe_count


result = 0
for new_wall in iter_data:
    after_lab = copy.deepcopy(current_lab)
    for new in new_wall :
        after_lab[new[0]][new[1]] = 1

    for i in range(n):
        for j in range(m):
            if after_lab[i][j] == 2:
                virus(i,j)

    result = max(result,count_safe(after_lab))


print(result)
