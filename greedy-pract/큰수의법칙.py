#특정 인덱스 수가 k번을 초과하여 연속적으로 더해질 수 없음
#큰 수의 법칙

N,M,K = map(int,input().split())
arr = list(map(int,input().split()))
arr.sort(reverse=True)

MAX = arr[0]
sec = arr[1]
res = 0

while M != 0:
    for i in range(K):
        res+= MAX
        M-=1
    #1번만 다음 큰 수 넣기
    res += sec
    M -= 1
print(res)


