import sys
input = sys.stdin.readline

# n개 원소
# k 번 바뀌치기 가능
# 배열 a, 배열 b
# 배열 a의 합이 최대

n,k = map(int, input().split())
arrA = list(map(int, input().split()))
arrA.sort()
arrB = list(map(int, input().split()))
arrB.sort(reverse=True)

for i in range(k):
    if arrA[i]<arrB[i]:
        arrA[i],arrB[i] = arrB[i],arrA[i]
    else:
        break
    
print(sum(arrA))
        
"""
5 3
1 2 5 4 3
5 5 6 6 5
"""