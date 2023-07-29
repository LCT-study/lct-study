#숫자카드게임
#즉 최종적(마지막으로)으로 카드를 선택할 때 높은 수가 나와야함
#이말은 곧 행들을 비교해서 각 행에서 제일 작은 수가 좀 커야
# 마지막에 뽑을 때 뽑히는 수도 높을거 아니냐 이런 것임
# 출력: 룰에 맞게 선택한 맨 처음 뽑는 카드의 숫자

n,m = map(int,input().split())
arr = []
MIN = []

for i in range(n):
    arr2 = list(map(int,input().split()))
    MIN.append(min(arr2))

print(max(MIN))

