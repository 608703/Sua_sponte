for tc in range(1, int(input())+1):
    N = int(input())//10

    cnt = [0] * (N+1)
    cnt[0] = 1
    cnt[1] = 1

    for i in range(2, N+1):
        cnt[i] = cnt[i-1] + cnt[i-2] * 2
    print('#{} {}'.format(tc, cnt[N]))