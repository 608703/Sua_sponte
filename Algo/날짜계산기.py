for tc in range(1, int(input())+1):
    m1, d1, m2, d2 = map(int, input().split())
    day = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    result = 0

    result += d2 - d1 +1

    if m1 != m2:
        for i in range(m1, m2):
            result += day[i]

    print('#{} {}'.format(tc, result))