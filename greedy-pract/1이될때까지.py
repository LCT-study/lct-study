# 아래 2과정중 하나를 반복적으로 선택해 수행. 
#   1. N에서 1빼기
#   2. N을 K로 나누기 (단, N이 K로 나누어 떨어질때에만)
# 두 과정을 사용해 최소 횟수로 N을 1로 만들기

n, k = map(int, input().split())
count = 0
while(n >= k):
    remain = n % k
    if remain:
        n -= remain
        count += remain
    else:
        n //= k
        count += 1

if n > 1:
    n -= n-1
    count += n - 1
print(count)