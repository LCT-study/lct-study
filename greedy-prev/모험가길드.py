import sys
input = sys.stdin.readline

n  = int(input())
arr = sorted(list(map(int,input().strip().split())), reverse = True)
answer = []

while(len(arr)>0):
    for i in arr:
        arr.remove(i)
        temp = [i]
        for _ in range(i-1):
            temp.append(arr.pop())
            #print(i,temp)
        answer.append(temp)

print(len(answer))