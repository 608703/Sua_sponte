for tc in range(1, int(input())+1):
    n = int(input())
    nums = list(map(int, input()))

    counting = [0] * 10
    result = 0
    number = 0
    cnt = 0
    for i in nums:
        counting[i] += 1

    for l in range(len(counting)):
        if result <= counting[l]:
            result = counting[l]
            number = l

    for k in nums:
        if k == number:
            cnt += 1

    print('#{} {} {}'.format(tc, number, cnt))