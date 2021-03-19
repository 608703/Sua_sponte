for tc in range(1, 11):
    n = int(input())
    mapp = [list(map(int, input().split())) for _ in range(100)]

    dr = [1, 0, 0]
    dc = [0, -1, 1]
    result = 0

    for i in range(100):
        if mapp[0][i] == 1:
            r = 0
            c = i
            dir = 0
            while r < 100:
                if dir == 0:
                    if c - 1 >= 0 and mapp[r][c-1] == 1:
                        dir = 1
                    elif c + 1 < 100 and mapp[r][c+1] == 1:
                        dir = 2
                elif dir == 1 or dir == 2:
                    if r + 1 < 100 and mapp[r+1][c] == 1:
                        dir = 0
                r += dr[dir]
                c += dc[dir]

                if r == 99 and mapp[r][c] == 2:
                    result = i
                    break

    print('#{} {}'.format(tc, result))