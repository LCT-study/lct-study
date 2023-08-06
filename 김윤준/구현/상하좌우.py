N = int(input())

fear = list(map(str, input().split()))
move = {'L' : -1, 'R' : 1, 'U' : -1, 'D' : 1}

X = 0
Y = 0

for f in fear:
    if(f == 'L' or f == 'R'):
        X = X + move[f]
    elif(f == 'U' or f == 'D'):
        Y = Y + move[f]
    if(X < 0):
        X = 0
        continue
    elif(X == N):
        X = X - 1
        continue
    if(Y < 0):
        Y = 0
        continue
    elif(Y == N):
        Y = Y - 1
        continue

print(Y+1, X+1)


