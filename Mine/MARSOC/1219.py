def dfs(v):
    visited[v] = 1
    if v == 99:
        return 1
    for i in range(100):
        if adj[v][i] == 1 and visited[i] == 0:
            if dfs(i) == 1:
                return 1
    return 0


for tc in range(1, 11):
    t, N = map(int, input().split())
    num = list(map(int, input().split()))
    line = []

    for i in range(0, len(num), 2):
        line.append([num[i], num[i + 1]])
    adj = [[0] * 100 for _ in range(100)]

    for j in range(len(line)):
        a = line[j][0]
        b = line[j][1]
        adj[a][b] = 1
    visited = [0] * 100
    result = dfs(0)

    print('#{} {}'.format(t, result))