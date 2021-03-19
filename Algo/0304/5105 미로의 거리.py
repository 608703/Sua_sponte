import sys
sys.stdin = open('5105.txt')

def bfs(r, c):
    # queue랑 방문 여부 찍을 준비

    queue = []
    visited = [[0] * n for _ in range(n)]

    # 더 해주고 방문 찍고
    queue.append((r, c, 0))
    visited[r][c] = 1

    # 동서남북 준비
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    # 수색 시작
    while queue:
        cr, cc, cd = queue.pop(0)
        if mapp[cr][cc] == 3:
            # 그냥 cd를 하면 도착지까지의 이동거리므로 -1
            return cd-1
        for d in range(4):
            nr = cr + dr[d]
            nc = cc + dc[d]
            # 항상 조건 잘 확인하고 빠진거 없나 확인
            if 0 <= nr < n and 0 <= nc < n and mapp[nr][nc] != 1 and visited[nr][nc] == 0:
                queue.append((nr, nc, cd+1))
                visited[nr][nc] = 1
    return 0

for tc in range(1, int(input())+1):
    n = int(input())
    mapp = [list(map(int,input())) for _ in range(n)]

    # 출발지가 될 2 좌표 찾아주고 그걸 수색대로 bfs에 투입
    for i in range(n):
        for j in range(n):
            if mapp[i][j] == 2:
                r = i
                c = j
    print('#{} {}'.format(tc, bfs(r, c)))

