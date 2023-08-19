import sys

n = int(input())

arr = [list(input().split()) for _ in range(n)]
arr.sort(key=lambda x : int(x[1]))
print(arr)

for name, score in arr:
    print(name, end=" ")