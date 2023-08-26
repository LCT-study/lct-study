def dfs(depth, n, m):
    if depth == m:
        print(''.join(map(str, result)))
        count[0] += 1
        return
    for i in range(1, n+1):
        if not visited[i]:
            visited[i] = True
            result.append(i)
            dfs(depth + 1, n, m)
            visited[i] = False
            result.pop()

n, m = map(int, input().split())
count = [0]
visited = [False] * (n+1)
result = []
dfs(0, n, m)
print(count)