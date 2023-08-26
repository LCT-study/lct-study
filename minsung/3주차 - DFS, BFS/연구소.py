import sys
from itertools import combinations
from collections import deque
from copy import deepcopy

# 지도의 크기
n, m = map(int, sys.stdin.readline().split())

# 지도 정보 저장
lab = []
for _ in range(n): 
    lab.append(list(map(int, sys.stdin.readline().split())))

# 빈 공간의 좌표를 모두 저장
empty = []
for i in range(n):
    for j in range(m):
        if (lab[i][j] == 0):
            empty.append((i,j))

# 가능한 울타리 조합을 모두 계산
total_empty_combi = list(combinations(empty, 3))

# 상하좌우 이동용 좌표
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# BFS를 사용해 바이러스 확산시킨 뒤, 남은 안전 영역을 계산
def bfs():

    # 울타리가 설치된 지도를 깊은 복사
    lab_copy = deepcopy(lab)

    for x in range(n):
        for y in range(m):

            # 바이러스 확산용 큐
            q = deque()     

            # 현재 위치에 바이러스가 있다면
            if (lab_copy[x][y] == 2):

                # 현재 위치를 큐에 추가
                q.append((x, y))
                while(q):    

                    # 현재 위치를 큐에서 추출
                    now = q.popleft()

                    # 상하좌우의 빈 공간에 바이러스를 학산
                    for i in range(4):
                        new_x = now[0] + dx[i]
                        new_y = now[1] + dy[i]

                        # 이웃 영역이 지도 내에 존재하고, 빈 공간인지 확인
                        if (0 <= new_x and new_x < n and 0 <= new_y and new_y < m and lab_copy[new_x][new_y] == 0):
                            # 주변 위치에 바이러스를 확산
                            lab_copy[new_x][new_y] = 2

                            # 이웃 공간을 큐에 추가
                            q.append((new_x, new_y))

    return safe_area(lab_copy)

# 남은 안전 영역을 계산
def safe_area(lab_copy):

    count = 0
    for i in range(n):
        for j in range(m):
            if (lab_copy[i][j] == 0):
                count += 1

    return count

def solution():

    # 울타리 설치 전 원본
    global lab

    # 울타리 조합 별 안전 영역의 개수 저장
    result = -1

    # 울타리를 세운 뒤, BFS를 사용해 바이러스를 확산시키고, 남은 안전 영역을 계산
    for empty_combi in total_empty_combi:

        # 울타리 설치
        for x, y in empty_combi:
            lab[x][y] = 1

        # BFS를 사용해 바이러스 확산시킨 뒤, 남은 안전 영역을 계산하고, 최대값과 비교
        result = max(result, bfs())

        # 울타리 제거
        for x, y in empty_combi:
            lab[x][y] = 0

    return result

print(solution())