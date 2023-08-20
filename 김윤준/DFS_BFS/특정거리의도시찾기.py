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
# 받는게 중요하다.
# [1, 2] [1, 3] 으로 받으면 1번 노드는 2, 3과 이어져 있으므로
# [n개의 배열] [[] ,[2, 3], [n..+1배열 개수]] 이렇게 "인덱스 = 노드 번호" 로 저장해 주고 풀어야 함.

# 도시 간 연결 정보 저장
graph = [[] for _ in range(N + 1)]
for _ in range(M):
    A, B = map(int, input().split())
    graph[A].append(B)

# BFS 알고리즘
def bfs(graph, start, K):
    distance = [0] * (N + 1) #인덱스 번호 : 노드, 값 : 거치는 비용 
    distance[start] = 0 # [1]번 배열부터 시작 
                        # (자기 자신이므로 거리비용은 0. 안해도 되는데 일단 시작임을 선언.)
    queue = deque([start])
    while queue:
        current = queue.popleft() #BFS 특 popleft() 
        print("큐에서 pop ", current)
        for neighbor in graph[current]:
            if distance[neighbor] == 0: # graph(노드간 거리정보) distance(노드간(인덱스) 거치는 비용) 
                                        # 이 두 리스트를 접목시켜 주는게 중요함.
                                        # graph = [[], [2,3], [3, 4], [], []]  => (1번) 노드는 (2번), (3번)과 연결 / (2번) 노드는 (3번), (4번)과 연결 / (3번) (4번) 은 아무것도 연결 X
                                        # distance = [0, 0, 0, 0, 0] => 초기 셋팅, 인덱스 별로 거리 비용이 들어감
                                        # 처음시작 [1번노드] = 0, graph[current] => current(시작노드) 와 연결된 노드들을 for 문으로 돌린다.
                                        # 그리고 BFS, DFS 는 노드를 순회하는 것이므로 조건을 두어 "distance[(2번 노드)/(3번 노드)] 처음 순회하는 노드일 경우 = 0" 와 같은 조건을 둔다. 
                                        # 순회하는 노드는 = 시작노드 거리 비용 + 1(기본거리). 따라서 이 60번 코드는 "distance 배열로 처음 순회할 때마다, 그동안 순회한 비용 + 1" 이 된다. 
                distance[neighbor] = distance[current] + 1
                print(distance)
                queue.append(neighbor) # 처음 순회하는 인접한 노드를 큐에 추가(2, 3) 따라서 popleft로 빼내면서 BFS 수행.
                                       # 이놈이 중요한데 앞으로 문제 풀때 BFS 로 풀릴것 같으면
                                       # 큐 구조를 생각하며, 그래프를 BFS로 돌면서 큐에 값을 넣었다 빼는 과정을 생각하며 조건문(while ... for)를 짠다 
        print("큐에 노드 추가 ", queue)
    return distance

# 결과 출력
distance_list = bfs(graph, X, K)
result = [i for i, dist in enumerate(distance_list) if dist == K]
# distance_list = [0]

if not result:
    print(-1)
else:
    for city in result:
        print(city)


