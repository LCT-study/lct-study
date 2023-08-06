import sys
input = sys.stdin.readline
n = list(input().strip())
arr = 8

# 오른(0,1), 왼쪽(0,-1), 위(-1, 0), 아래(1,0)
#dx = [0,0,-1,1]
#dy = [1,-1,0,0]

# 모든 이동 방향
#(우우하),(우우상)
#(좌좌하),(좌좌상)
#(우하하),(우상상)
#(좌하하),(좌상상)

dir = [
    [1,2],[-1,2],
    [1,-2],[-1,2],
    [2,1],[-2,1],
    [2,-1],[-2,-1]
]
answer = 0
def get_xy(n):
    col = ord(n[0]) - ord("a")
    row = int(n[1]) - 1
    return row, col

row, col = get_xy(n)
for dr, dc in dir:
   
    nr, nc = row + dr, col+dc
    if 0<=nr<arr and 0<=nc<arr:
        #print(x,y,dx, dy, nx, ny)
        answer+=1
    
print(answer)

"""
a1
2
"""

"""
c2
6
"""