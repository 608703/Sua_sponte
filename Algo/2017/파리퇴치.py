for tc in range(1, int(input())+1):
    n, m = map(int, input().split())
    mapp = [list(map(int, input().split())) for _ in range(n)]

    result = 0

    for x in range(n-m+1):
        for y in range(n-m+1):
            hop = 0
            for i in range(m):
                for j in range(m):
                    hop += mapp[x+i][y+j]
            if result < hop:
                result = hop
    print('#{} {}'.format(tc, result))