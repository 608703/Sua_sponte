for tc in range(1, int(input())+1):
    n = int(input())

    arr = [[0] * n for _ in range(n)]

    for i in range(n):
        for j in range(i+1):
            if j == 0 or i == 0:
                arr[i][j] = 1
            else:
                if i > 0 and j > 0:
                    arr[i][j] = arr[i - 1][j] + arr[i - 1][j - 1]
    print('#{}'.format(tc))
    for i in range(n):
        for j in range(i + 1):
            print(arr[i][j], end=' ')
        print()