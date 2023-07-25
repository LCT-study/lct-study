import sys
input = sys.stdin.readline

n = list(map(int, input().strip()))
answer = n.pop(0)

for i in n:
    #print(i,n)
    if answer*i>answer+i:
        answer*=i
    else:
        answer+=i

print(answer)