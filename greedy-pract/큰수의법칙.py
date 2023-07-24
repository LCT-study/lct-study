import sys
input = sys.stdin.readline

n,m,k = map(int, input().split())
arr = sorted(list(map(int, input().split())), reverse=True)
i = arr[0]
j = arr[1]
res = 0
count = 1
flag = False

while(m>0):
    while(count%(k+1)!=0) and (m>1):
        count+=1
        m-=1 
        res+=i
    res+=j
    m-=1
    count+=1

print(res)