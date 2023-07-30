N, M = list(map(int, input().split()))

count = 0

while(1) :
    if(N == 1): 
        break
    elif(N % M != 0):
        N -= 1
        count += 1
    else:
        N //= M
        count += 1

print(count)
