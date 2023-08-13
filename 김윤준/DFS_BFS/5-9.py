#BFS 예제
from collections import deque

def bfs(graph, start, visited):
    visited[start] = True
    quere = deque([start])

    while quere:
        v = quere.popleft()
        print(v, end="")
        for i in graph[v]:
            if not visited[i]:
                quere.append(i)
                visited[i] = True


# !! 노드 처음 시작이 1이므로 리스트 0번째는 비워둔다.
graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

# !! 노드가 1부터 시작하니까 0번째가 비워진거까지 노드개수+1 개인 9개로 방문된 정보 리스트 생성
visited = [False] * 9

bfs(graph, 1, visited)