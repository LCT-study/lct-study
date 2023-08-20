n, k = map(int, input().split())

count = 0 
while True:
    if n == 1:
        break
    if n % k == 0:  #k로 나누어 떨어지면 나누기 
        n = n / k
        count = count + 1
    else:           #나누어 떨어지지 않으면 n-1 
        n = n - 1
        count = count + 1
print(count)    
    