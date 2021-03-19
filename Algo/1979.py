for tc in range(1, int(input()) + 1):
    n, k = map(int, input().split())

    mapp = []
    for _ in range(n):
        mapp.append(list(map(int, input().split())))
    result = 0

    for i in range(n):
        cnt = 0
        for j in range(n):
            if mapp[i][j] == 0:
                if cnt == k:
                    result += 1
                cnt = 0
            else:
                cnt += 1
        if cnt == k:
            result += 1
    for i in range(n):
        cnt = 0
        for j in range(n):
            if mapp[j][i] == 0:
                if cnt == k:
                    result += 1
                cnt = 0
            else:
                cnt += 1
        if cnt == k:
            result += 1
    print('#{} {}'.format(tc, result))