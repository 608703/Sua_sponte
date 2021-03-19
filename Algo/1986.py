for tc in range(1, int(input())+1):
    nums = int(input())

    result = 0
    for i in range(1, nums+1):
        if i % 2:
            result += i
        else:
            result -= i
    print('#{} {}'.format(tc, result))