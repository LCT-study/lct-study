import sys
input = sys.stdin.readline

n,m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
answer = 0

for row in arr:
    min_v = min(row)
    answer = max(answer, min_v)
    
print(answer)