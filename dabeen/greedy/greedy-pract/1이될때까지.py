#1이 될때까지
#goal: 최소 수행횟수 출력

n,k = map(int,input().split())
num = 0

while n!=1:
    if n%k==0:
        n=n//k
        num+=1
        continue
    n-=1
    num += 1

print(num)