# chapter4 구현 실전[4-1]
# input : 5\n R R R U D D
# output : 3 4

n = int(input())
moves = input().split()
cur = (1, 1)
directions = {'L' : (0, -1), 'R' : (0, 1), 'U' : (-1, 0), 'D' : (1, 0)}

for move in moves:
    d = directions[move]
    next = (cur[0] + d[0],cur[1] + d[1])
    if next[0] < 1 or next[0] > n or next[1] < 1 or next[1] > n:
        continue
    cur = next

print(*cur, sep=' ')
