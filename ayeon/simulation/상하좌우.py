import sys
input = sys.stdin.readline

n = int(input())
cmd = list(input().strip().split())

# 왼, 아래, 오른, 위
dx= [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

#print(n, cmd)

def change_direction(command, x,y):
    if command=="U": # 3
        nx = x + dx[3]
        ny = y + dy[3]
    elif command=="D": # 1
        nx = x + dx[1]
        ny = y + dy[1]
    elif command == "L": # 0
        nx = x + dx[0]
        ny = y + dy[0]
    elif command == "R": # 2
        nx = x + dx[2]
        ny = y + dy[2]
    return nx, ny
    
def isAble(n, nx, ny):
    if 0<nx<=n and 0<ny<=n:
        return True
    return False
    
x = y = 1
for c in cmd:
    nx, ny = change_direction(c, x, y)
    #print(nx, ny)
    if isAble(n, nx, ny):
        x = nx
        y = ny
    
print(x, y)

"""
5
R R R U D D
"""