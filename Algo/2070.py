T = int(input())


for tc in range(1, T + 1):
    # list1 = list(map(int, input().split()))
    a, b = input().split()
    a = int(a)
    b = int(b)

    if a > b:
        print('#{} {}'.format(tc, '>'))
    elif a < b:
        print('#{} {}'.format(tc, '<'))
    else:
        print('#{} {}'.format(tc, '='))