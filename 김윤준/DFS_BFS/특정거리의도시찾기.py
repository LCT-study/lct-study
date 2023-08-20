# N, M, K, X = map(int, input().split())

# matrix = []
# 1 
# for i in range(M):
#     while True:
#         row = list(map(int, input().split()))

#         # 입력된 row가 이전에 입력된 row와 중복되지 않는지 확인
#         if any(row == prev_row for prev_row in matrix):
#             print("같은 값이 이미 입력되었습니다. 다시 입력해주세요.")
#         else:
#             matrix.append(row)
#             break

# print("입력된 2x2 행렬:")
# for row in matrix:
#     print(row)

# load = []
# for i in range(2):
#     for j in range(4):
#         if matrix[j][i] == j:
#             load.append((matrix[j][i], matrix[j][i]))

# print(load)

from collections import deque

# 입력 받기
N, M, K, X = map(int, input().split())

# 도시 간 연결 정보 저장
graph = [[] for _ in range(N + 1)]
for _ in range(M):
    A, B = map(int, input().split())
    graph[A].append(B)

# BFS 알고리즘
def bfs(graph, start, K):
    distance = [-1] * (N + 1)
    distance[start] = 0

    queue = deque([start])
    while queue:
        current = queue.popleft()

        for neighbor in graph[current]:
            if distance[neighbor] == -1:
                distance[neighbor] = distance[current] + 1
                queue.append(neighbor)

    return distance

# 결과 출력
distance_list = bfs(graph, X, K)
result = [i for i, dist in enumerate(distance_list) if dist == K]

if not result:
    print(-1)
else:
    for city in result:
        print(city)


