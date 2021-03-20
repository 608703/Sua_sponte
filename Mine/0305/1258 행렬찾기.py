for tc in range(1, int(input())+1):
    n = int(input())
    mapp = [list(map(int, input().split())) for _ in range(n)]

    warning = []
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    for i in range(n):
        for j in range(n):
            if mapp[i][j] > 0:
                r = i
                c = j
                big_r = 0
                big_c = 0
                while 0 <= c < n and mapp[r][c] != 0:
                    c = c + dc[3]
                big_c = c - 1

                while 0 <= r < n and mapp[r][c-1] != 0:
                    r = r + dr[1]
                big_r = r - 1

                for l in range(i, big_r+1):
                    for m in range(j, big_c+1):
                        mapp[l][m] = 0
                warning.append((big_r-i+1, big_c-j+1))
    result = []
    for a, b in warning:
        result.append([a*b, a, b])
    result.sort()

    print('#{} {}'.format(tc, len(result)), end = ' ')
    for i in range(len(result)):
        print(result[i][1], result[i][2], end = ' ')
    print()