for tc in range(1, int(input())+1):
    n = int(input())

    mapp = [[0] * 10 for _ in range(10)]
    cnt = 0
    for i in range(n):
        x1, y1, x2, y2, c = map(int, input().split())

        for x in range(x1, x2+1):
            for y in range(y1, y2+1):
                mapp[x][y] += c

    for i in range(10):
        for j in range(10):
            if mapp[i][j] == 3:
                cnt += 1
    print('#{} {}'.format(tc, cnt))