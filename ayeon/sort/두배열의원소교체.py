import sys
input = sys.stdin.readline

# n개 원소
# k 번 바뀌치기 가능
# 배열 a, 배열 b
# 배열 a의 합이 최대

n,m = map(int, input().split())
arrA = list(map(int, input().split()))
arrA.sort()
arrB = list(map(int, input().split()))
arrB.sort(reverse=True)

idx, count = 0,0
while m-count>0:
    #print(idx, arrB[idx],arrA[idx])
    if arrB[0]>arrA[0]:
        arrB.append(arrA.pop(0))
        arrA.append(arrB.pop(0))
        #print(arrA, arrB)
        count+=1
print(sum(arrA))
        
"""
5 3
1 2 5 4 3
5 5 6 6 5
"""