#예제 4-1 상하좌우

n=int(input())
arr = input().split()
y,x=1,1 #좌표를 (y,x) 로 잡고 시작

for v in arr:
    print(x, y)
    if v == 'R':
        if x == n:
            continue
        x+=1
    elif v == 'L':
        if x == 1:
            continue
        x-=1
    elif v == 'U':
        if y == 1:
            continue
        y-=1
    else:
        if y == n:
            continue
        y+=1


print(y,x)