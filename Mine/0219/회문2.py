for tc in range(1, 11):
    N = int(input())
    arr = [input() for _ in range(100)]
    result = 1

    for i in range(100):
        for f in range(100):
            for l in range(99, f, -1):
                k = l-f+1
                if k <= result:
                    break
                for j in range(k//2):
                    if arr[i][f+j] != arr[i][l-j]:
                        break
                else:
                    result = k
                if k <= result:
                    break
                for j in range(k//2):
                    if arr[f+j][i] != arr[l-j][i]:
                        break
                else:
                    result = k
    print('#{} {}'.format(tc, result))