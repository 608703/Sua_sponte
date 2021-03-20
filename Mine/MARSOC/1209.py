for tc in range(1, 11):
    n = int(input())
    mapp = [list(map(int, input().split())) for _ in range(100)]

    xsum = 0
    ysum = 0
    csum = 0
    for i in range(100):
        sum = 0
        sum2 = 0
        for j in range(100):
            sum += mapp[i][j]
            if xsum < sum:
                xsum = sum
            sum2 += mapp[j][i]
            if ysum < sum2:
                ysum = sum2
        sumr = 0
        suml = 0
        sumr += mapp[i][i]
        suml += mapp[i][99-i]
        if sumr > suml:
            csum = sumr
        else:
            csum = suml

    print('#{} {}'.format(tc, max(xsum, ysum, csum)))