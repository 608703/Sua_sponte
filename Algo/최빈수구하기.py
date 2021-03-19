T = int(input())

for tc in range(1, T+1):
    N = int(input())
    scores = list(map(int, input().split()))
    ans = 0

    result = {}
    for score in scores:
        if score in result:
            result[score] += 1
        else:
            result[score] = 1
    max1 = 0
    for key, value in result.items():
        if max1 < value:
            max1 = value
            ans = key
        elif max1 == value:
            if ans < key:
                ans = key
    print('#{} {}'.format(N, ans))