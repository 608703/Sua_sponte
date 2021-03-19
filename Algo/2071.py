T = int(input())


for i in range(1, T + 1):
    list1 = list(map(int, input().split()))

    result = 0
    for num in list1:
        result += num

    print('#{} {}'.format(i, round(result/10)))