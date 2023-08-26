import sys
from collections import deque

# n(땅 크기), L R 입력(인구 차이 최소L 최대R)
n, l, r = map(int, sys.stdin.readline().split())

# 땅 입력
graph = []
for _ in range(n):
    graph.append(list(map(int, sys.stdin.readline().split())))

# 상하좌우 탐색용 인덱스
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 지난 날짜
date = 0

# 현재 나라와 연합할 수 있는 나라 탐색 후, 연합
def process(x, y, union_number):

    # (x, y)의 위치와 연결된 나라들의 정보를 담는 리스트
    countrys = []
    countrys.append((x, y))

    # 현재 나라를 큐에 삽입
    q = deque()
    q.append((x, y))

    # 현재 연합의 번호 할당
    union[x][y] = union_number

    # 현재 연합의 국가 수
    summary = graph[x][y]

    # 현재 연합의 나라 수
    count = 1

    # 현재 나라와 연합할 수 있는 모든 나라 탐색
    while q:
        now = q.popleft()
        # 이웃 나라 탐색
        for k in range(4):
            nx = now[0] + dx[k]
            ny = now[1] + dy[k]
            # 이웃 나라가 지도 내부에 존재하고, 방문한 적이 없고, 인구 차이가 l 이상 r 이하라면
            if (0 <= nx < n and 0 <= ny < n and union[nx][ny] == -1 and  l <= abs(graph[nx][ny] - graph[now[0]][now[1]]) <= r ):
                # 현재 연합 번호 할당
                union[nx][ny] = union_number
                # 큐에 삽입
                q.append((nx, ny))
                # 연합 별 인구 수, 나라 개수, 좌표 추가
                summary += graph[nx][ny]
                count += 1
                countrys.append((nx, ny))

    # 연합 국가끼리 인구를 분배
    for i, j in countrys:
        graph[i][j] = summary // count

# 더 이상 인구 이동을 할 수 없을 때까지 반복
while True:    

    # 연합 정보 저장
    union = [[-1]*n for _ in range(n)]

    # 연합 번호
    union_number = 0

    # 모든 좌표 탐색
    for i in range(n):
        for j in range(n):

            # 현재 나라의 아무런 연합이 없을 경우, 새로운 연합 탐색
            if (union[i][j] == -1):

                # 현재 나라와 연합할 수 있는 나라 탐색 후, 연합
                process(i, j, union_number)

                # 연합 번호 추가
                union_number += 1

    # 모든 인구 이동이 끝난 경우
    if (union_number == n*n):
        break
    # 지난 날짜 추가
    date += 1

print(date)