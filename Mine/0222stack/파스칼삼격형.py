for tc in range(1, int(input()) + 1):
    n = int(input())

    mapp = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(i+1):
            if j == 0 or i == j:
                mapp[i][j] = 1
            else:
                if i > 0 and j > 0:
                    mapp[i][j] = mapp[i-1][j-1] + mapp[i-1][j]

    print('#{}'.format(tc))
    for i in range(n):
        for j in range(i+1):
            print(mapp[i][j], end = ' ')
        print()