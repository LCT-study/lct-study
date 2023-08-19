import sys

n = int(input())

arr = [int(input()) for _ in range(n)]
arr.sort(reverse=True)
print(* arr)