for tc in range(1, int(input())+1):
    n, m = map(int, input().split())
    mapp = [input() for _ in range(n)]

    result = []

    for r in range(n):
        for c in range(n-m+1):
            if mapp[r][c:c+m] == mapp[r][c:c+m][::-1]:
                result.append(mapp[r][c:c+m])

    for r in range(n-m+1):
        for c in range(n):
            sero = []
            for i in range(m):
                sero.append(mapp[r+i][c])
            if sero == sero[::-1]:
                result.append(''.join(sero))

    print('#{} {}'.format(tc, result[0]))
