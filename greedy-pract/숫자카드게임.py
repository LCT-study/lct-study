import sys
input = sys.stdin.readline

n,m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
answer = 0

for i in arr:
    if answer<min(i):
        answer = min(i)
print(answer)