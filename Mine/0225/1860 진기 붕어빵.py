for tc in range(1, int(input())+1):
    n, m, k = map(int, input().split())
    sonnom = list(map(int, input().split()))

    result = 'Possible'
    max1 = 0
    # 오기 전에 만들 수 있는지
    for i in sonnom:
        if i > max1:
            max1 = i
        if i < m:
            result = 'Impossible'
    time = (max1 // m) + 1
    eating = k
    for i in range(2, time + 1):
        for num in sonnom:
            if eating == 0 and n == 0:
                result = 'Possible'
                break
            if eating < 0 and n > 0:
                result = 'Impossible'
            if m * (i - 1) < num < m * i:
                eating -= 1
                n -= 1
        eating += k
    print('#{} {}'.format(tc, result))