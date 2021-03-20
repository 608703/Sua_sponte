for tc in range(1, int(input())+1):
    N, M = map(int, input().split())
    mapp = [[0] * N for _ in range(N)]

    moving = [(1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1)]
    center = N//2
    mapp[center][center] = 2
    mapp[center-1][center-1] = 2
    mapp[center][center-1] = 1
    mapp[center-1][center] = 1

    for i in range(M):
        c, r, col = map(int, input().split())
        c -= 1
        r -= 1

        if not mapp[r][c]:
            mapp[r][c] = col
            for s in range(8):
                dx, dy = moving[s]
                nx, ny = r + dx, c + dy
                reverse = []
                while True:
                    if nx < 0 or N - 1 < nx or ny < 0 or N - 1 < ny:
                        reverse = []
                        break
                    if mapp[nx][ny] == 0:
                        reverse = []
                        break
                    if mapp[nx][ny] == col:
                        break
                    else:
                        reverse.append((nx, ny))
                    nx += dx
                    ny += dy
                for rx, ry in reverse:
                    mapp[rx][ry] = col

        wht, blk = 0, 0
        for i in range(N):
            for j in range(N):
                if mapp[i][j] == 1:
                    wht += 1
                elif mapp[i][j] == 2:
                    blk += 1
    print('#{} {} {}'.format(tc, wht, blk))