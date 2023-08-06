# https://www.acmicpc.net/problem/18406

import sys
input = sys.stdin.readline

arr = list(map(int, input().strip()))
idx = len(arr)//2

r = arr[:idx]
l = arr[idx:]

if sum(r) == sum(l):
    print("LUCKY")
else:
    print("READY")
