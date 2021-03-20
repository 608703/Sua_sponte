for tc in range(1, 11):
    n = int(input())
    result = 0
    list1 = list(map(int, input().split()))
    for i in range(2, n-2):
        max = 0
        for j in [-2, -1, 1, 2]:
            if max < list1[i+j]:
                max = list1[i+j]

        if max < list1[i]:
            result += list1[i] - max

    print('#{} {}'.format(tc, result))