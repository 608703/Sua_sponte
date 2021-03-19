import sys
sys.stdin = open('123.txt')

for tc in range(1, 10):
    N = int(input())

    arr = [list(map(int, input().split())) for _ in range(100)]

    sum_c = 0
    for i in range(100):
        sum = 0
        for j in range(100):
            sum += arr[i][j]
        if sum_c < sum:
            sum_c = sum

    sum_r = 0
    for i in range(100):
        sum = 0
        for j in range(100):
            sum += arr[j][i]
        if sum_r < sum:
            sum_r = sum

    sum_x = 0
    for i in range(100):
        sum_left = 0
        sum_right = 0
        sum_left += arr[i][i]
        sum_right += arr[i][99-i]
    if sum_left > sum_right:
        sum_x = sum_left
    else:
        sum_x = sum_right

    print('#{} {}'.format(N, max(sum_c, sum_r, sum_x)))