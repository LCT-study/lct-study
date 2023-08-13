# DFS 예제
def dfs(graph, v, visited):
    # 현재 노드 방문 처리
    visited[v] = True
    print(v, end="")
    
    # 현재 노드와 연결된 다른 노드 재귀적으로 방문
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited) 


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

dfs(graph, 1, visited)