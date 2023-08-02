import sys
input = sys.stdin.readline

# 5
# 2 3 1 2 2 
# 2

n = int(input())

# 오름차순으로 배열
# 공포가 낮은 사람부터 빠르게 순회하며 그만큼 적은 사람을 써서 그룹을 생성
# 최대 갯수의 그룹 생성 
arr = sorted(list(map(int, input().split())))

curr = [] # 현재 그룹 내 탐험가
answer = [] # 현재 그룹 결성된 그룹 

# 공포도가 x인 모험가는 반드시 x명 이상으로 구성된 그룹에 있어야만 참여 가능 
# 현재 그룹에 포함된 모험가의 수가 
# 현재 확인하고 있는 공포도보다 크거나 같으면 그룹 결성 
for i in arr:
    curr.append(i)
    if len(curr)>=i: # 그룹 결성 완료됨 
        answer.append(curr) 
        curr = [] # 다음 그룹 담기 위해 초기화 
        
print(len(answer))