for tc in range(1, int(input())+1):
    mapp = [list(map(int, input().split())) for _ in range(9)]
    result = 1

    for i in range(9):
        arr = [0] * 10
        for j in range(9):
            num = mapp[i][j]
            arr[num] += 1
        for n in range(1, 10):
            if arr[n] != 1:
                result = 0

        arr = [0] * 10
        for j in range(9):
            num = mapp[j][i]
            arr[num] += 1
        for n in range(1, 10):
            if arr[n] != 1:
                result = 0

    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            arr = [0] * 10
            for x in range(3):
                for y in range(3):
                    num = mapp[i+x][j+y]
                    arr[num] += 1
            for n in range(1, 10):
                if arr[n] != 1:
                    result = 0
    print('#{} {}'.format(tc, result))