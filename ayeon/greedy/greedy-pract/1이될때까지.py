import sys
input  = sys.stdin.readline

n, k = map(int, input().split())

arr = [n] # n에서 1로 가기까지 과정
count = 0 # 계산 횟수

while(n!=1):
    count+=1
    if n%k==0:
        n = n//k
    else:
        n = n-1
    arr.append(n)
    #print(a, end = " ")
    
# 계산 과정
#print(arr)

# 계산 횟수
print(count)