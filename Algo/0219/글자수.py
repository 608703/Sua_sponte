for tc in range(1, int(input())+1):
    n = input()
    m = input()

    result = 0
    for i in n:
        cnt = 0
        for j in m:
            if i == j:
                cnt += 1
            if result <= cnt:
                result = cnt

    print('#{} {}'.format(tc, result))