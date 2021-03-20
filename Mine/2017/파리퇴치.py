for tc in range(1, int(input()) + 1):
    n, m = map(int, input().split())
    mapp = [list(map(int, input().split())) for _ in range(n)]

    result = 0
    for i in range(n-m+1):
        for j in range(n-m+1):
            hop = 0
            for a in range(m):
                for b in range(m):
                    hop += mapp[i+a][j+b]
            if result < hop:
                result = hop
    print('#{} {}'.format(tc, result))