#예제 4-2 시각 (다시풀기)
# 시간 복잡도 계산 공부 필요

n = int(input())
cnt = 0

for i in range(n+1): #0-23시 기준
    for j in range(60):
        for k in range(60):
            if '3' in (str(i)+str(j)+str(k)):
                cnt+=1
print(cnt)
