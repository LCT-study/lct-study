P = int(input())

fear = [P]
fear = list(map(int, input().split()))

fear.sort()

sum = 1
# 1 2 2 2 3
while(sum):
    team = [] # 팀 별로 표시하기 위해 선언
    if(len(fear) == 0):
        break
    fear_cloan = fear.copy() # for 에서 배열 삭제시 기존 배열에 영향이 가니
    for j in range(max(fear_cloan)):
        team.append(fear[len(fear_cloan)-(j+1)]) # 팀 출력
        del fear[len(fear_cloan)-(j+1)] # 뒤에서부터 삭제 : 공포도 가장 높은 사람 기준만큼 팀 구성
    print(sum, "팀 : ", team)
    sum += 1

print("총 팀 수 : ", sum-1)