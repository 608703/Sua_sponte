for tc in range(1, int(input())+1):
    n, m = map(int, input().split())
    nums = list(map(int, input().split()))

    big = 0
    small = 1234567890
    for i in range(n-m+1):
        hop = 0
        for j in range(m):
            hop += nums[i+j]

        if big <= hop:
            big = hop

        if small >= hop:
            small = hop

    print('#{} {}'.format(tc, big-small))