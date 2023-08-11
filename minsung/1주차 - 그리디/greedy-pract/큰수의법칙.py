# 배열의 크기: n
# 숫자가 더해지는 횟수: m
# 같은 숫자를 연속해서 더할 수 있는 최대 수: k

n, m, k = map(int, input().split())
data = list(map(int, input().split()))

data.sort() #작은 수부터 차례대로 정렬
first = data[n - 1]     #첫번째 큰 수
second = data[n - 2]    #두번째 큰 수
sum = 0
while True:
    if m == 0:
        break
    for i in range(k):  #첫번째 큰 수를 k번까지 더하기
        sum = sum + first
        m = m - 1
    sum = sum + second    #두번째 큰 수 한번 더하기 
    m = m - 1
print(sum)
    