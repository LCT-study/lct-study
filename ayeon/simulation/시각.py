import sys
input = sys.stdin.readline
n=int(input())

def contain_num(n, time):
    
    for i in time:
        if int(i)==n:
            return True
    return False
answer = 0
for h in range(n+1):
    for m in range(60):
        for s in range(60):
            time = str(h)+str(m)+str(s)
            if contain_num(n,list(time)):
                answer+=1
print(answer)

"""
5
11475
"""