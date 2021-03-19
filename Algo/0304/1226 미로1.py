def DMZ(r, c):
    # queue랑 방문 여부 찍을 준비
    queue = []
    visited = [[0] * 16 for _ in range(16)]

    # 더 해주고 방문 찍고
    queue.append((r, c))
    visited[r][c] = 1

    # 동서남북 준비
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    # 수색 시작
    while queue:
        cr, cc = queue.pop(0)
        if mapp[cr][cc] == '3': # 도착지 3이니 도착하면 1
            return 1
        for d in range(4):
            nr = cr + dr[d]
            nc = cc + dc[d]
            # 항상 조건 잘 확인하고 빠진거 없나 확인
            if 0 <= nr < 16 and 0 <= nc < 16 and mapp[nr][nc] != '1' and visited[nr][nc] == 0:
                queue.append((nr, nc))
                visited[nr][nc] = 1
    return 0

for tc in range(1, 11):
    n = int(input())
    mapp = [input() for _ in range(16)]
    # print(mapp)
    # 2 좌표 찾아주고 수색대로 배정해서 DMZ투입
    for i in range(16):
        for j in range(16):
            if mapp[i][j] == '2':
                r = i
                c = j
    print('#{} {}'.format(tc, DMZ(r, c)))