N = str(input())

index = 0

i = 1
for n in N:
    sum[index] = sum[index] + int(n)
    if(len(N) / i == 2):
        index = 1
    i += 1

if(sum[0] == sum[1]):
    print("LUCKY")
else:
    print("READY")