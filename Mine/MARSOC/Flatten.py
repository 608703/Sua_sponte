for tc in range(1, 11):
    n = int(input())
    nums = list(map(int, input().split()))

    while n >= 0:
        big = nums[0]
        small = nums[0]
        indexb = 0
        indexs = 0
        for i in range(len(nums)):
            if big < nums[i]:
                big = nums[i]
                indexb = i
            if small > nums[i]:
                small = nums[i]
                indexs = i
        nums[indexb] -= 1
        nums[indexs] += 1
        n -= 1

    print('#{} {}'.format(tc, big - small))