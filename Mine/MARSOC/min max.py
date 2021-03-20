for tc in range(1, int(input())+1):
    n = int(input())
    nums = list(map(int, input().split()))

    big = 0
    small = nums[0]

    for num in nums:
        if num > big:
            big = num
        if num < small:
            small = num

    print('#{} {}'.format(tc, big-small))