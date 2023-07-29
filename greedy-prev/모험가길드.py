#모험가 길드(A)

n=int(input())
arr = list(map(int, input().split()))

arr.sort()
cnt=0 #현 그룹 모험가 수
res = 0

for v in arr:
    cnt+=1
    if cnt>=v:
        res += 1 #그룹 형성
        cnt = 0 # 초기화ㅏ
print(res)