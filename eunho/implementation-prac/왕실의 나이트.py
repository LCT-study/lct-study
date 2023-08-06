# chapter4 구현 실전[4-3]
# input : a1, output : 2
#print(ord('a'))
#print(chr(97))

cur_c, cur_r = list(input())
cur_c = ord(cur_c) - 96 # 'a' == 97
cur_r = int(cur_r)
moves = [(1, 2), (1, -2), (-1, 2), (-1, 2),
         (2, 1), (2, -1), (-2, 1), (-2, 1)]
answer = 0

for move in moves:
    next_r = cur_r + move[0]
    next_c = cur_c + move[1]
    if next_r >= 1 and next_r <= 8 and next_c >= 1 and next_c <= 8:
        answer += 1
print(answer)

