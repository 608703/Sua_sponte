for tc in range(1, int(input())+1):
    time = list(map(int, input().split()))

    result1 = 0
    result2 = 0
    result1 = time[0] + time[2]
    if result1 >= 13:
        result1 -= 12
    result2 = time[1] + time[3]
    if result2 >= 61:
        result1 += 1
        result2 -= 60

    print('#{} {} {}'.format(tc, result1, result2))
