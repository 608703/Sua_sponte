def bfs(r, c):
    # queue랑 방문 여부 찍을 준비

    queue = []
    visited = [[0] * n for _ in range(n)]

    queue.append((r, c, 0))
    visited[r][c] = 1

    # 동서남북
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    while queue:
        cr, cc, cd = queue.pop(0)
        if mapp[cr][cc] == 3:
            return cd-1
        for d in range(4):
            nr = cr + dr[d]
            nc = cc + dc[d]
            if 0 <= nr < n and 0 <= nc < n and mapp[nr][nc] != 1 and visited[nr][nc] == 0:
                queue.append((nr, nc, cd+1))
                visited[nr][nc] = 1
    return 0

for tc in range(1, int(input())+1):
    n = int(input())
    mapp = [list(map(int,input())) for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if mapp[i][j] == 2:
                r = i
                c = j
    print('#{} {}'.format(tc, bfs(r, c)))
