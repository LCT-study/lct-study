import sys
input  = sys.stdin.readline

n, k = map(int, input().split())

count = 0
temp =  a = n

while(a!=1):
    count+=1
    if a%k==0:
        temp = a//k
    else:
        temp = a-1
    a = temp
    print(a, end = " ")
        
    